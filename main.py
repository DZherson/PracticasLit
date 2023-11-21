# This is a sample Python script.
import streamlit as st
import pandas as pd
import plotly.express as px


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    st.title('David Matu :blue[cool] :sunglasses: ')
    datosVuelos = pd.read_csv('datos/lax_to_jfk.csv')
    st.dataframe(datosVuelos)

    st.title('Gráficas')
    retrasos = datosVuelos.groupby("Month")["ArrDelay"].mean().reset_index()
    st.dataframe(retrasos)
    fig = px.line(retrasos, "Month", "ArrDelay")
    # Luego la mostramos
    st.plotly_chart(fig, use_container_width=True)

    st.title('Mensualmente')

    datosMensuales = datosVuelos['Month'].value_counts().reset_index()
    st.dataframe(datosMensuales)


    fig2 = px.bar(datosMensuales, "Month", "count")
    st.plotly_chart(fig2, use_container_width=True)

    datosAerolinea = datosVuelos['Reporting_Airline'].value_counts().reset_index()
    st.dataframe(datosAerolinea)
    fig3 = px.pie(datosAerolinea, values="count", names="Reporting_Airline",title="Porcentaje vuelos por aerolínea")
    st.plotly_chart(fig3, use_container_width=True)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('David')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
