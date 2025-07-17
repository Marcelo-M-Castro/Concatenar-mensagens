import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
from io import BytesIO

st.set_page_config(page_title="Concatenador de Conversas", layout="wide")
st.title("🧩 Concatenador de Conversas com Análise de Feedback")

uploaded_file = st.file_uploader("📁 Faça upload do arquivo CSV", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Ordena e concatena mensagens
    df_sorted = df.sort_values(by=['conversation_sid', 'indice_message'])
    df_grouped = df_sorted.groupby('conversation_sid').apply(
        lambda x: '\n'.join([f"[{a}]: {m}" for a, m in zip(x['author'], x['conversation']) if pd.notnull(m)])
    ).reset_index(name='conversation_concatenada')

    df_final = df.merge(df_grouped, on='conversation_sid')

    # Extrair feedback do cliente
    def extract_customer_feedback(conversation):
        pattern = r"Sua opinião faz a diferença\. Como você avalia este atendimento\?\n\[(.*?)\]: (.*)"
        match = re.search(pattern, conversation)
        if match:
            return match.group(1).strip(), match.group(2).strip()
        return None, None

    df_final[['cliente', 'nota']] = df_final['conversation_concatenada'].apply(
        lambda x: pd.Series(extract_customer_feedback(x))
    )

    # Extrair produto
    def extrair_produto(texto):
        frase = "Sobre qual assunto você quer conversar?"
        index = texto.find(frase)
        if index != -1:
            trecho = texto[index + len(frase): index + len(frase) + 150]
            if "Consignado INSS" in trecho:
                return "Consignado INSS"
        return None

    df_final['produto'] = df_final['conversation_concatenada'].apply(extrair_produto)

    # Remover duplicadas
    df_final = df_final.drop_duplicates(subset=['conversation_concatenada'])

    # Exibir prévia dos resultados finais
    st.subheader("📄 Prévia dos resultados processados")
    st.dataframe(
        df_final[['conversation_sid', 'conversation_concatenada', 'cliente', 'nota', 'produto']].head(10),
        use_container_width=True
    )

    # Exportação final
    st.subheader("💾 Exportar Resultado")
    output = BytesIO()
    df_final.to_excel(output, index=False, engine='openpyxl')
    st.download_button(
        label="📥 Baixar Excel com Dados Completos",
        data=output.getvalue(),
        file_name='df_conversas_processado.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
