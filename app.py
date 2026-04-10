import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import uuid

st.set_page_config(layout="wide")

# Mostrar banner centrado
st.image("banner.png", width="stretch")


st.set_page_config(page_title="Termómetro de Riesgo", layout="wide")
st.title("Termómetro de Riesgo — Evaluación Institucional")

# ---------------------------------------------------------
# CONTROL DE FLUJO
# ---------------------------------------------------------
if "mostrar_fase2" not in st.session_state:
    st.session_state.mostrar_fase2 = False

if "mostrar_fase3" not in st.session_state:
    st.session_state.mostrar_fase3 = False

if "mostrar_resultado" not in st.session_state:
    st.session_state.mostrar_resultado = False


# ---------------------------------------------------------
# FASE 1 — REGISTRO DE LA INSTITUCIÓN
# ---------------------------------------------------------

st.header("Fase 1 — Registro de la institución")

institucion = st.text_input("Institución:", placeholder="Nombre de la institución")
responsable = st.text_input("Responsable:", placeholder="Nombre completo")
ubicacion = st.text_input("Ubicación:", placeholder="Ciudad / Estado")

cuc_input = st.text_input("CUC previo:", placeholder="Ingresa CUC si ya existe (opcional)")

if st.button("Generar CUC"):
    if cuc_input.strip():
        st.session_state.cuc_actual = cuc_input.strip().upper()
        st.success(f"CUC ingresado utilizado: {st.session_state.cuc_actual}")
    else:
        st.session_state.cuc_actual = str(uuid.uuid4())[:8].upper()
        st.success(f"Código Único de Caso generado: {st.session_state.cuc_actual}")

    st.session_state.mostrar_fase2 = True


# ---------------------------------------------------------
# FASE 2 — DATOS GENERALES
# ---------------------------------------------------------

if st.session_state.mostrar_fase2:

    st.header("Fase 2 — Datos generales")

    edad = st.selectbox("Edad:", [
        "Menor de 15 años", "15–19", "20–24", "25–29", "30–34", "35–39",
        "40–44", "45–49", "50–54", "55–59", "60–64", "65 o más"
    ])

    ocupacion = st.selectbox("Ocupación:", [
        "Trabajadora por cuenta propia", "Trabajadora asalariada",
        "Empleadora o patrona", "Trabajadora del hogar remunerada",
        "Estudiante", "Persona dedicada al hogar", "Jubilada o pensionada",
        "Desempleada", "No especificado"
    ])

    escolaridad = st.selectbox("Escolaridad:", [
        "Sin instrucción", "Primaria incompleta", "Primaria completa",
        "Secundaria incompleta", "Secundaria completa", "Preparatoria",
        "Técnica", "Licenciatura", "Posgrado", "No especificado"
    ])

    relacion = st.selectbox("Relación con la persona agresora:", [
        "Pareja", "Expareja", "Familiar", "Conocido",
        "Compañero de trabajo", "Sin relación previa", "Otro"
    ])

    conviven = st.selectbox("¿Conviven?", ["Sí", "No", "Se desconoce"])
    menores_involucrados = st.selectbox("¿Hay personas menores involucradas?", ["Sí", "No", "Se desconoce"])

    if st.button("Continuar a Reactivos del Termómetro"):
        st.session_state.mostrar_fase3 = True


# ---------------------------------------------------------
# FASE 3 — REACTIVOS DEL TERMÓMETRO
# ---------------------------------------------------------

if st.session_state.mostrar_fase3:

    st.header("Reactivos del Termómetro")

    preguntas = [
        "¿Se ha observado agresión física?",
        "¿Se han escuchado comentarios intimidantes?",
        "¿Se ha observado que la persona agresora manipule objetos de manera intimidante?",
        "¿Se ha identificado presión relacionada con la intimidad?",
        "¿Se han observado episodios repetidos de tensión o control?",
        "¿Se ha identificado un aumento en la frecuencia de los episodios?",
        "¿Se ha identificado un aumento en la intensidad de los episodios?",
        "¿Se ha identificado que ambas personas convivan en el mismo espacio?",
        "¿Se ha observado aislamiento social?",
        "¿Se ha identificado consumo de sustancias por parte de la persona agresora?",
        "¿Se ha observado dependencia económica?",
        "¿Se ha identificado la presencia de hijas o hijos en el entorno?",
        "¿Se ha observado que la persona agresora limite la independencia o el acceso a la salud?",
        "¿Se ha identificado el uso de hijas o hijos como forma de control?",
        "¿Se ha observado interferencia en la crianza?",
        "¿Se ha identificado violencia hacia animales de compañía?",
        "¿Se ha observado que la persona agresora interrumpa o minimice en público?",
        "¿Se ha identificado control sobre gastos o recursos económicos?",
        "¿Se ha observado un ambiente tenso o el uso de objetos para intimidar?",
        "¿Se han identificado factores críticos que aumenten el riesgo?",
        "¿Se ha identificado posesión o uso de armas por parte de la persona agresora?",
        "¿Se han observado lesiones físicas?"
    ]

    reactivos = {}
    for i, p in enumerate(preguntas):
        reactivos[p] = st.selectbox(p, ["Sí", "No", "Se desconoce"], key=f"r{i}")

    # Ponderaciones
    ponderaciones = {
        preguntas[0]: 5, preguntas[1]: 4, preguntas[2]: 4, preguntas[3]: 4,
        preguntas[4]: 3, preguntas[5]: 3, preguntas[6]: 4, preguntas[7]: 3,
        preguntas[8]: 3, preguntas[9]: 4, preguntas[10]: 3, preguntas[11]: 3,
        preguntas[12]: 3, preguntas[13]: 5, preguntas[14]: 4, preguntas[15]: 4,
        preguntas[16]: 3, preguntas[17]: 3, preguntas[18]: 4, preguntas[19]: 6,
        preguntas[20]: 6,  # armas
        preguntas[21]: 5   # lesiones
    }

    def normalizar(v):
        v = v.lower()
        if v in ["sí", "si"]:
            return 1
        if v == "no":
            return 0
        return 1

    def calcular_puntaje(respuestas):
        total = 0
        for clave, peso in ponderaciones.items():
            total += normalizar(respuestas[clave]) * peso
        return total

    # Indicador siempre dentro de la barra (0–86)
    def mostrar_barra_riesgo(p):
        try:
            p = float(p)
        except:
            p = 0

        p = max(0, min(86, p))

        fig, ax = plt.subplots(figsize=(10, 1.2))
        gradient = np.linspace(0, 1, 500).reshape(1, -1)

        ax.imshow(
            gradient,
            aspect='auto',
            cmap=plt.cm.get_cmap('RdYlGn_r'),
            extent=[0, 86, 0, 1]
        )

        ax.set_axis_off()
        ax.plot([p, p], [0, 1], color='black', linewidth=3)

        st.pyplot(fig)

    if st.button("Evaluar riesgo"):
        st.session_state.mostrar_resultado = True
        st.session_state.puntaje = calcular_puntaje(reactivos)


# ---------------------------------------------------------
# RESULTADO FINAL
# ---------------------------------------------------------

if st.session_state.mostrar_resultado:

    st.subheader("Resultado del Termómetro")

    # ✔ Solo mostramos el termómetro
    mostrar_barra_riesgo(st.session_state.puntaje)

    st.subheader("Recomendación y canalización")

    recomendaciones = []

    # Secretaría de la Mujer → solo si puntaje ≥ 43 (50% de 86)
    if st.session_state.puntaje >= 43:
        recomendaciones.append("• Canalización a la Secretaría de la Mujer para acompañamiento especializado.")

    # Violencia vicaria automática
    if edad == "Menor de 15 años":
        recomendaciones.append("• Canalización al DIF por posible violencia vicaria.")

    # Armas
    if reactivos[preguntas[20]] == "Sí":
        recomendaciones.append("• Canalización inmediata al Ministerio Público por presencia de armas.")

    # Lesiones físicas
    if reactivos[preguntas[21]] == "Sí":
        recomendaciones.append("• Canalización a servicios de salud para valoración médica.")

    # Seguimiento institucional
    recomendaciones.append("• Seguimiento institucional y fortalecimiento de redes de apoyo.")

    for r in recomendaciones:
        st.write(r)