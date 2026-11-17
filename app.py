import streamlit as st
import pandas as pd
from datetime import datetime

st.title("📋 Mi App de Registros")

if "registros" not in st.session_state:
    st.session_state.registros = []

nombre = st.text_input("Nombre")
detalle = st.text_input("Detalle")
cantidad = st.number_input("Cantidad", min_value=1, value=1, step=1)

if st.button("Guardar Registro"):
    fecha = datetime.now().strftime("%d/%m/%Y")
    nuevo = {"Fecha": fecha, "Nombre": nombre, "Detalle": detalle, "Cantidad": cantidad}
    st.session_state.registros.append(nuevo)
    st.success("Guardado!")

st.subheader("Registros guardados")

if len(st.session_state.registros) == 0:
    st.write("Aún no hay registros")
else:
    df = pd.DataFrame(st.session_state.registros)
    st.dataframe(df)

    st.subheader("📈 Curvas - Cantidad por día")
    df["Fecha"] = pd.to_datetime(df["Fecha"], format="%d/%m/%Y")
    por_dia = df.groupby("Fecha")["Cantidad"].sum()
    st.line_chart(por_dia)

    st.subheader("📊 Total acumulado")
    por_dia_acum = por_dia.cumsum()
    st.line_chart(por_dia_acum)

    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Descargar Excel", csv, "registros.csv", "text/csv")
