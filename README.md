# 🧩 Concatenador de Conversas

Este projeto é uma aplicação interativa construída com [Streamlit](https://streamlit.io/) para **processar e concatenar conversas extraídas de um CSV**, normalmente derivadas de sistemas de atendimento automatizado. Ele organiza as mensagens, extrai informações como **feedback do cliente** e **produto citado**, e permite a exportação dos dados enriquecidos em formato Excel.

---

## 🚀 Funcionalidades

- 📁 Upload de arquivos CSV com dados de conversas.
- 🔄 Ordenação e concatenação das mensagens por `conversation_sid`.
- 🧠 Extração automática:
  - **Feedback do cliente** (quem deu a nota e qual foi a avaliação).
  - **Produto mencionado** (detecta se é "Consignado INSS").
- 🧹 Remoção de conversas duplicadas.
- 👀 Pré-visualização dos dados processados.
- 💾 Exportação do resultado em planilha Excel.

---

## 📊 Exemplo de uso

1. Faça upload do arquivo CSV com as conversas.
2. O sistema irá:
   - Concatenar mensagens por conversa.
   - Identificar feedbacks e produtos mencionados.
   - Remover duplicatas.
3. Visualize os primeiros resultados.
4. Baixe a planilha Excel final processada.

---

## 📂 Formato esperado do CSV de entrada

O arquivo deve conter pelo menos as seguintes colunas:

- `conversation_sid`: identificador da conversa.
- `indice_message`: ordem cronológica da mensagem.
- `author`: remetente da mensagem.
- `conversation`: conteúdo da mensagem.

---

## 🛠️ Tecnologias utilizadas

- Python
- [Streamlit](https://streamlit.io/)
- Pandas
- Matplotlib & Seaborn *(opcionais no código atual)*
- Regex (para extração de informações textuais)
- OpenPyXL (para exportação em Excel)

---


