from django.db import models
import uuid
import qrcode
from io import BytesIO
from django.core.files import File

class Boi(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brinco = models.CharField(max_length=50, verbose_name="Número do Brinco")
    nome = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nome (Opcional)")
    
    RACA_CHOICES = [('NELORE', 'Nelore'), ('ANGUS', 'Angus'), ('BRAHMAN', 'Brahman'), ('GIROLANDO', 'Girolando'), ('HOLANDES', 'Holandês'), ('OUTRA', 'Outra')]
    raca = models.CharField(max_length=20, choices=RACA_CHOICES, default='NELORE')
    
    SEXO_CHOICES = [('M', 'Macho'), ('F', 'Fêmea')]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default='M')
    
    # 1. NOVO: Campo de Status
    STATUS_CHOICES = [('ATIVO', 'Ativo no Pasto'), ('VENDIDO', 'Vendido'), ('MORTO', 'Morto')]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ATIVO')
    
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    peso_kg = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Peso Atual (kg)")
    
    data_cadastro = models.DateTimeField(auto_now_add=True)
    observacoes = models.TextField(blank=True, null=True)
    qrcode_img = models.ImageField(upload_to='qrcodes/', blank=True, null=True)

    def __str__(self):
        return f"{self.brinco} - {self.status}"

    def save(self, *args, **kwargs):
        url_do_animal = f"https://gadocode.com/boi/{self.id}"
        img = qrcode.make(url_do_animal)
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        file_name = f'qrcode_{self.brinco}_{self.id}.png'
        if not self.qrcode_img:
            self.qrcode_img.save(file_name, File(buffer), save=False)
        super().save(*args, **kwargs)

# 3. NOVO: Tabela para o Histórico de Peso
class HistoricoPeso(models.Model):
    boi = models.ForeignKey(Boi, on_delete=models.CASCADE, related_name='historico_peso')
    peso_kg = models.DecimalField(max_digits=6, decimal_places=2)
    data_pesagem = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_pesagem'] # Ordena do mais recente para o mais antigo