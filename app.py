import streamlit as st

# -------------------------------
# CONFIGURACIÓN GENERAL
# -------------------------------

st.set_page_config(page_title="Proyecto Módulo 1", layout="wide")

# Inicializar lista en session_state
if "actividades" not in st.session_state:
    st.session_state.actividades = []

# -------------------------------
# MENÚ LATERAL
# -------------------------------

st.sidebar.image("image.png", width="stretch")

menu = st.sidebar.selectbox(
    "Menú de Navegación",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# -------------------------------
# HOME
# -------------------------------

if menu == "Home":
    st.title("Proyecto Aplicado - Fundamentos de Programación")

    st.write("**Estudiante:** Leonardo Luis Díaz Vargas")
    st.write("**Curso:** Especialización en Python for Analytics")
    st.write("**Módulo:** Módulo 1 - Python Fundamentals")
    st.write("**Año:** 2026")

    st.write("""
    ### Descripción del Proyecto
    Esta aplicación interactiva desarrollada en Streamlit integra los conceptos
    fundamentales de programación aprendidos en el Módulo 1:
    - Variables
    - Condicionales
    - Listas y diccionarios
    - Funciones
    - Programación funcional
    - Programación orientada a objetos (POO)
    """)

    st.write("### Tecnologías utilizadas")
    st.write("- Python")
    st.write("- Streamlit")

# -------------------------------
# EJERCICIO 1
# -------------------------------

elif menu == "Ejercicio 1":
    st.title("Ejercicio 1 - Variables y Condicionales")

    presupuesto = st.number_input("Ingrese el presupuesto", min_value=0.0)
    gasto = st.number_input("Ingrese el gasto", min_value=0.0)

    if st.button("Evaluar presupuesto"):
        diferencia = presupuesto - gasto

        if gasto <= presupuesto:
            st.success("El gasto está dentro del presupuesto")
        else:
            st.warning("El presupuesto fue excedido")

        st.write(f"Diferencia: {diferencia}")

# -------------------------------
# EJERCICIO 2
# -------------------------------

elif menu == "Ejercicio 2":
    st.title("Ejercicio 2 - Listas y Diccionarios")

    nombre = st.text_input("Nombre de la actividad")
    tipo = st.selectbox("Tipo de actividad", ["Marketing", "Operaciones", "Finanzas", "Otro"])
    presupuesto = st.number_input("Presupuesto", min_value=0.0)
    gasto_real = st.number_input("Gasto real", min_value=0.0)

    if st.button("Agregar actividad"):
        actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presupuesto,
            "gasto_real": gasto_real
        }
        st.session_state.actividades.append(actividad)
        st.success("Actividad agregada correctamente")

    if st.session_state.actividades:
        st.subheader("Lista de actividades")
        st.dataframe(st.session_state.actividades)

        st.subheader("Estado de cada actividad")

        for act in st.session_state.actividades:
            if act["gasto_real"] <= act["presupuesto"]:
                estado = "Dentro del presupuesto"
            else:
                estado = "Presupuesto excedido"

            st.write(f"{act['nombre']} → {estado}")

# -------------------------------
# EJERCICIO 3
# -------------------------------

elif menu == "Ejercicio 3":
    st.title("Ejercicio 3 - Funciones y Programación Funcional")

    tasa = st.slider("Seleccione la tasa", 0.0, 1.0, 0.1)
    meses = st.number_input("Número de meses", min_value=1)

    def calcular_retorno(actividad, tasa, meses):
        return actividad["presupuesto"] * tasa * meses

    if st.button("Calcular retorno esperado"):
        if st.session_state.actividades:

            retornos = list(
                map(lambda act: calcular_retorno(act, tasa, meses),
                    st.session_state.actividades)
            )

            for i, act in enumerate(st.session_state.actividades):
                st.write(f"{act['nombre']} → Retorno esperado: {retornos[i]}")

        else:
            st.warning("No hay actividades registradas")

# -------------------------------
# EJERCICIO 4
# -------------------------------

elif menu == "Ejercicio 4":
    st.title("Ejercicio 4 - Programación Orientada a Objetos")

    class Actividad:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real

        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto

        def mostrar_info(self):
            return f"Actividad: {self.nombre} | Tipo: {self.tipo} | Presupuesto: {self.presupuesto} | Gasto Real: {self.gasto_real}"

    if st.session_state.actividades:

        objetos = [
            Actividad(act["nombre"], act["tipo"], act["presupuesto"], act["gasto_real"])
            for act in st.session_state.actividades
        ]

        for obj in objetos:
            st.write(obj.mostrar_info())

            if obj.esta_en_presupuesto():
                st.success("Cumple el presupuesto")
            else:
                st.warning("No cumple el presupuesto")

    else:
        st.warning("No hay actividades registradas")