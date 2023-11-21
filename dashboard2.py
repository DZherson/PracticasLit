import pandas as pd
import calendar
import plotly.express as px
import streamlit as st


dfCafe = pd.read_excel("datos/limpiezaCafe.xlsx")


anios = list(set(dfCafe['fechaEntrada'].dt.year))
meses = list(set(dfCafe['fechaEntrada'].dt.month_name()))
mesSorted = [calendar.month_name[i] for i in range(1, 13)]

# Título del dashboard
st.title("Dashboard de afluencia de clientes - Café internet")


anioSeleccionado = st.sidebar.selectbox('Selecciona año', anios)
mesSeleccionado = st.sidebar.selectbox('Selecciona mes', mesSorted)


dfFiltradoMesAnio = dfCafe[(dfCafe['fechaEntrada'].dt.month_name() == mesSeleccionado) & (dfCafe['fechaEntrada'].dt.year == anioSeleccionado)]


dfMes = dfFiltradoMesAnio.groupby(pd.Grouper(key="fechaEntrada", freq="1D")).count().reset_index()
dfMes['Dia'] = dfMes['fechaEntrada'].dt.strftime('%A')  # Obtener el nombre del día
dfMes['fechaStr'] = dfMes['fechaEntrada'].dt.strftime('%Y-%m-%d')  # Formato YYYY-MM-DD


fig = px.bar(dfMes, x='fechaStr', y='horaEntrada', labels={'fechaEntrada': 'Día', 'horaEntrada': 'Número de clientes'}, text='horaEntrada', title='Número de clientes por día')
st.plotly_chart(fig, use_container_width=True)


st.title("Tabla del mes")
st.dataframe(dfMes)



