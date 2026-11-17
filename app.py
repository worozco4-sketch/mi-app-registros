import streamlit as st
import pandas as pd
from datetime import datetime

st.title("📋 Mi App de Registros")

if "registros" not in st.session_state:
    st.session_state.registros = []

nombre = st.text_input("Nombre")
detalle = st.text_input("Detalle")
cantidad = st.number_input("Cantidad", min_value=1, value=1)

if st.button("Guardar Registro"):
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M")
    nuevo = {"Fecha": fecha, "Nombre": nombre, "Detalle": detalle, "Cantidad": cantidad}
    st.session_state.registros.append(nuevo)
    st.success(f"Guardado: {nombre} - {detalle} - {cantidad}")

st.subheader("Registros guardados")
if st.session_state.registros:
    df = pd.DataFrame(st.session_state.registros)
    st.dataframe(df)
    st.write(f"Total registros: {len(df)}")
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(label="📥 Descargar Excel", data=csv, file_name="mis_registros.csv", mime="text/csv")
else:
    st.write("Aún no hay registros")
