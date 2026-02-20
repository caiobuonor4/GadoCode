# 🐮 GadoCode

<div align="center">
  <img src="bovinos/static/img/logo.png" alt="GadoCode Logo" width="200"/>
  
  ### Gestão pecuária na palma da mão. Simples. Offline. Preciso.
  
  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
  ![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
</div>

<br>

## 🌾 O Problema
A pecuária brasileira é gigante, mas a gestão do pequeno e médio produtor ainda é **analógica**. O controle do rebanho é feito em cadernetas de papel que molham, rasgam e perdem o histórico. Softwares tradicionais são complexos, caros e, o pior de tudo: **exigem internet no pasto**.

## 🚀 A Solução
O **GadoCode** é um SaaS (Software as a Service) focado em **usabilidade extrema**. Ele transforma o celular do pecuarista na ferramenta mais poderosa da fazenda. Através da leitura de **QR Codes** (Brincos Inteligentes), o produtor acessa e atualiza a ficha do animal em segundos.

### ✨ Funcionalidades Principais (MVP)
* **📷 Leitor de QR Code Integrado:** Leitura rápida direto do navegador do celular usando a câmera nativa, sem precisar baixar apps de terceiros.
* **📊 Dashboard Inteligente:** Visão em tempo real do tamanho do rebanho, separação por sexo e histórico recente de atividades.
* **📈 Curva de Ganho de Peso (GPD):** Histórico vitalício do peso do animal para o produtor saber exatamente qual boi está dando lucro ou prejuízo.
* **🔄 Gestão de Ciclo de Vida:** Controle de status (Ativo no Pasto, Vendido ou Morto/Baixa) para manter o inventário sempre limpo e real.
* **💳 Modelo Freemium Pronta Entrega:** Plano "Capim" (Grátis até 50 cabeças) e Plano "Nelore" (PRO) com checkout integrado via PayPal e PIX.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python + Django (Padrão MVT)
* **Frontend:** HTML5, Tailwind CSS, JavaScript Vanilla
* **Banco de Dados:** SQLite (Fase de MVP)
* **Bibliotecas Extras:** `qrcode` (Geração de etiquetas), `Pillow` (Processamento de imagens), `html5-qrcode` (Leitura de câmera via JS).

---

## 💻 Como rodar o projeto localmente

Siga os passos abaixo para testar o GadoCode na sua máquina:

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU_USUARIO/GadoCode.git](https://github.com/SEU_USUARIO/GadoCode.git)
   cd GadoCode
