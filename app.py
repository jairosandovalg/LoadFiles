import streamlit as st

file = st.file_uploader("Sube tu archivo", type = ["csv"])

csv_data = file 

st.download_button(
      label="Descargar archivo modificado",
      data=csv_data,
      file_name="archivo_modificado.csv",
      mime="text/csv",
  )
