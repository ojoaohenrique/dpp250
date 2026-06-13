# Sistema de Impressão de Guias de Remoção – Guarda Municipal 2026

## 📋 Descrição

Sistema simples desenvolvido em **Python, HTML e CSS** para emissão e impressão de **Guias de Remoção de Veículos** utilizadas pela Guarda Municipal.

O sistema permite cadastrar os dados da remoção, gerar um registro em **JSON**, criar uma cópia em **TXT** para arquivamento e imprimir diretamente em impressoras térmicas, como a **Datecs DPP-250**.

---

## 🚀 Funcionalidades

* Cadastro de Guia de Remoção
* Geração automática do número da guia
* Impressão em impressora térmica DPP-250
* Salvamento dos dados em JSON
* Geração de arquivo TXT para arquivamento
* Interface simples e rápida
* Layout otimizado para papel térmico 58mm

---

## 🛠️ Tecnologias Utilizadas

### Backend

* Python 3
* Flask

### Frontend

* HTML5
* CSS3
* JavaScript

### Armazenamento

* Arquivos JSON
* Arquivos TXT

---

## 📂 Estrutura do Projeto

```text
guia-remocao/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── imprimir.html
│
├── static/
│   └── style.css
│
├── dados/
│   ├── json/
│   └── txt/
│
└── README.md
```

---

## ⚙️ Instalação

### 1. Clonar o projeto

```bash
git clone https://github.com/seuusuario/guia-remocao.git
```

### 2. Entrar na pasta

```bash
cd guia-remocao
```

### 3. Criar ambiente virtual

```bash
python -m venv venv
```

### 4. Ativar ambiente virtual

Windows:

```bash
venv\Scripts\activate
```

Linux:

```bash
source venv/bin/activate
```

### 5. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Executando o Sistema

```bash
python app.py
```

Acesse:

```text
http://127.0.0.1:5000
```

---

## 🖨️ Impressão

O sistema foi projetado para funcionar com a impressora térmica:

```text
Datecs DPP-250
```

Largura recomendada:

```text
58 mm
```

Para imprimir:

1. Preencha os dados da guia.
2. Clique em "Gerar Guia".
3. Clique em "Imprimir".
4. Selecione a impressora DPP-250.

---

## 📄 Exemplo de Guia

```text
================================
GUARDA MUNICIPAL DE LAGUNA
GUIA DE REMOÇÃO DE VEÍCULO
================================

Nº Guia: GM-2026-0001

Data: 13/06/2026
Hora: 14:30

Placa: ABC1D23
Marca: Volkswagen
Modelo: Gol

Motivo:
Estacionamento em local proibido.

Agente:
João Henrique

================================
```

---

## 📁 Arquivo TXT Gerado

```text
GM-2026-0001.txt
```

Conteúdo:

```text
Nº Guia: GM-2026-0001
Placa: ABC1D23
Marca: Volkswagen
Modelo: Gol
Motivo: Estacionamento irregular
```

---

## 📁 Arquivo JSON Gerado

```json
{
  "numero": "GM-2026-0001",
  "data": "13/06/2026",
  "hora": "14:30",
  "placa": "ABC1D23",
  "marca": "Volkswagen",
  "modelo": "Gol",
  "motivo": "Estacionamento irregular",
  "agente": "João Henrique"
}
```

---

## 🔒 Objetivo

Facilitar a emissão, impressão e arquivamento das Guias de Remoção da Guarda Municipal, reduzindo o preenchimento manual e organizando os registros de forma digital.

---

## 👨‍💻 Desenvolvido por

**João Henrique Fanfa**
Guarda Municipal de Laguna - SC

**Versão:** 1.0.0
**Ano:** 2026

```text
Sistema simples para impressão de guias de remoção.
Compatível com impressora Datecs DPP-250.
```
