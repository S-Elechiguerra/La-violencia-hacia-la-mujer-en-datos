<img width="7446" height="794" alt="perfiles_la violencia hacia la mujer (197 x 21 cm)" src="https://github.com/user-attachments/assets/10f05fa4-0443-41aa-90fa-d25d3b481777" />

# La-violencia-hacia-la-mujer-en-datos
Plataforma analítica e interactiva que integra datos estadísticos (2021-2024) para visibilizar patrones de violencia feminicida en México, detectar riesgos tempranos y cerrar la brecha de opacidad institucional mediante el uso de estándares CIE-10 y visualización avanzada.

# Descripción del proyecto
La violencia hacia la mujer en datos es una plataforma analítica e interactiva que integra información estadística oficial para visibilizar patrones, riesgos y desigualdades estructurales de la violencia feminicida en México entre 2021 y 2024.
El proyecto combina análisis estadístico, perspectiva de género, codificación estandarizada mediante CIE10 y una plataforma funcional en Streamlit para ofrecer una lectura integral del fenómeno y una herramienta de acción temprana. Su objetivo es transformar datos complejos en información clara, accesible y accionable para instituciones, organizaciones y ciudadanía.

# Motivación
México presenta una prevalencia estimada de violencia contra las mujeres del 31.4%, por encima del promedio mundial (27%) y regional (25%).
A pesar del marco legal, la violencia persiste y se manifiesta en formas visibles y silenciosas.
Durante el análisis descubrimos un punto ciego crítico:

La violencia no empieza en el golpe; empieza mucho antes.
Y esa violencia temprana casi nunca queda registrada.
No aparece en denuncias.
No aparece en estadísticas oficiales.
No aparece en expedientes institucionales.
Este proyecto surge para cerrar esa brecha y para no quedarnos calladas.

# Objetivos del Proyecto 
•  Integrar y depurar datos oficiales sobre violencia contra las mujeres.
•	Construir indicadores avanzados de riesgo, vulnerabilidad y concentración territorial.
•	Visibilizar la violencia silenciosa que antecede al feminicidio.
•	Desarrollar un prototipo funcional en Streamlit para registro, evaluación y canalización.
•	Crear un sistema de continuidad mediante un Código Único de Caso (CUC).
•	Proponer una herramienta de prevención temprana basada en evidencia.

# Datos utilizados
•	ENDIREH (INEGI)
•	Estadísticas de Defunciones Registradas (EDR)
•	Incidencia delictiva y llamadas 911 (SESNSP)
•	Censos y encuestas sociodemográficas
•	API del Banco Mundial
•	Indicadores de ONU Mujeres y CEPAL
•	CIE10 (OPS/OMS)
•	Marco jurídico Mexicano

# Hallazgos principales:

1. Contexto global, regional y nacional
•	Mundo: 27%
•	América Latina y el Caribe: 25%
•	México: 31.4%
 <img width="358" height="257" alt="image" src="https://github.com/user-attachments/assets/a6d80ff7-834a-4b5f-b403-64cec0467c3e" />

2. Perfil sociodemográfico
•	45% adultas jóvenes (26–45 años)
•	22% jóvenes (15–25 años)
•	42% dedicadas al hogar
•	18.5% docentes/profesionales
•	48.2% con educación básica
<img width="975" height="634" alt="image" src="https://github.com/user-attachments/assets/c1885c89-564d-45f4-809a-febe524bf2b8" />
 
4. Anatomía de la agresión
La mayoría de las víctimas vivió violencia silenciosa antes de la agresión física.
•	42.1% en vía pública
•	13.47% en vivienda
•	54.2% con arma de fuego
•	Arma blanca: segundo mecanismo más frecuente
•	12.3% por asfixia/ahorcamiento
•	94.2% vivió violencia psicológica previa
•	68.5% vivió violencia financiera previa
•	98.6% sin antecedentes en salud
 <img width="560" height="448" alt="image" src="https://github.com/user-attachments/assets/129402b3-726f-46d8-8e51-b6420ee3a531" />


5. Impacto en los hogares
•	62% eran proveedoras económicas
•	2.4 dependientes por caso
El feminicidio genera un shock económico inmediato

6. Geografía de la incidencia
El 46.25% de los casos se concentra en ocho estados:
Estado de México, Guanajuato, Jalisco, Chihuahua, Baja California, Michoacán, Morelos y Veracruz.
<img width="427" height="301" alt="image" src="https://github.com/user-attachments/assets/a08d11d7-f36a-433e-bc18-ce19497d25ba" />


7. Indicadores avanzados:
   
Índice de Riesgo Invisible (IRI)
•	Media: 0.143
•	25% de los casos con riesgo acumulado significativo
Índice de Vulnerabilidad Económica del Hogar (IVEH)
•	Media: 0.048
•	Vulnerabilidad severa en un subgrupo crítico
Costo Económico del Feminicidio (CEF)
•	Media: 355,702 pesos
•	Mediana: 375,000 pesos
•	75%: 600,000 pesos
•	Máximo: 960,000 pesos
Índice de Densidad Letal (IDL)
Estados críticos: Edomex, Guanajuato, Jalisco, Chihuahua, CDMX.
<img width="591" height="458" alt="image" src="https://github.com/user-attachments/assets/62af59f5-4140-4ecf-b479-04e922f28e23" />


Durante el análisis identificamos un patrón transversal:
La víctima suele pasar por varias instituciones sin que exista un hilo conductor.
Cada institución genera su propio expediente.
La información se pierde.
La violencia escala.
<img width="365" height="292" alt="image" src="https://github.com/user-attachments/assets/014b25e9-a83b-4ac7-b0c6-4db08c05ab99" />

Para romper ese ciclo creamos:
•	Un sistema de registro inicial y registro canalizado
•	Un Código Único de Caso (CUC)
•	Un Termómetro de Riesgo reproducible
•	Un mapa territorial de opacidad

# Descripcion del prototipo: 
El Termómetro de Riesgo es un modelo analítico diseñado para:
•	detectar señales tempranas de violencia,
•	ponderarlas según su gravedad,
•	generar un nivel de riesgo objetivo,
•	y permitir intervenciones oportunas y comparables.

# Principios rectores
•	Neutralidad absoluta
•	Datos observables o reportados
•	Reglas claras para la incertidumbre
o	“Se desconoce” = riesgo
•	Reproducibilidad
•	No revictimización

# Registro inicial y canalizado
•	La primera institución genera el CUC.
•	Las siguientes instituciones continúan el registro.
•	El termómetro se recalcula.
•	La red se fortalece.

# Regla especial: menores de 15 años
•	Se activa automáticamente violencia vicaria.
•	Se ajusta la ponderación.
•	Se omiten variables no aplicables.

# Uso institucional
El instrumento está diseñado para:
•	escuelas,
•	hospitales,
•	centros comunitarios,
•	instituciones públicas,
•	organizaciones civiles.

Cada institución registra datos, el modelo calcula el riesgo y se genera un resultado objetivo y comparable.

# Principios rectores del modelo
•	Neutralidad absoluta: No se registran percepciones, opiniones, interpretaciones ni valoraciones subjetivas.
•	Datos observables o reportados: Cada variable del formulario corresponde a:
•	un hecho observable,
•	un reporte directo de la víctima,
•	un antecedente institucional verificable,
•	o una condición documentada.
Reglas claras para la incertidumbre
El modelo distingue entre:
•	Información accesible directamente por la institución
→ Solo admite Sí / No
→ No existe “Se desconoce”
•	Información a la que la institución NO tiene acceso directo
→ Admite Sí / No / Se desconoce

# Reproducibilidad
Cualquier institución, con el mismo formulario, debe obtener el mismo resultado.

# No revictimización
El formulario evita preguntas intrusivas, repetitivas o innecesarias.

# Registro inicial
La institución que detecta el primer signo de violencia llena el formulario inicial.
La plataforma genera un CUC, que acompaña a la víctima en todo el proceso.

# Registro canalizado
Cuando otra institución recibe a la víctima, no inicia un caso nuevo.
Ingresa el CUC y continúa el registro.
La información se acumula.
El termómetro se recalcula.
La red se fortalece.

Este modelo permite que colegios, hospitales, centros comunitarios, empresas, DIF, Secretarías de las Mujeres y otras instancias trabajen juntas, sin duplicar esfuerzos y sin revictimizar.
Termómetro de Riesgo (escala cromática)

El termómetro utiliza un gradiente cromático continuo, no saltos discretos.
Esto permite:
•	ver la progresión del riesgo,
•	identificar incrementos sutiles,
•	y comunicar la gravedad sin subjetividad.

La escala aumenta en intensidad conforme se acumulan señales de violencia, igual que un termómetro que sube cuando la situación se vuelve más tensa, más grave o más peligrosa.
Nivel Verde — Riesgo Bajo
Nivel Amarillo — Riesgo Medio
Nivel Naranja — Riesgo Alto
Nivel Rojo — Riesgo Crítico

# Canalización y sugerencias para la institución
Cada registro, inicial o canalizado, activa recomendaciones específicas según:
•	nivel de riesgo,
•	tipo de institución,
•	tipo de violencia,
•	presencia de menores,
•	violencia vicaria,
•	lesiones visibles,
•	acceso a armas por parte del posible agresor,
•	consumo de drogas o sustancias por parte del posible agresor,
•	escalamiento reciente.

# Marco institucional y jurídico para la canalización
La plataforma no sustituye al sistema judicial, lo complementa desde donde el sistema no suele llegar.

# Instituciones clave:
•	Secretarías de las Mujeres (estatales y municipales)
•	AVGM
•	Contraloría Social E015
•	SIDEC (denuncias ciudadanas por omisiones institucionales)
•	CNDH – PAMIMH
•	DIF Nacional (SNDIF)
•	CONAVIM
•	INMUJERES
•	SIPINNA
•	CEAV
Estas instituciones pueden recibir casos canalizados mediante el CUC, fortaleciendo la continuidad y evitando que la víctima quede sola.

# Tecnologías utilizadas
•	Python (pandas, numpy, seaborn, plotly)
•	Jupyter Notebook
•	Streamlit
•	API del Banco Mundial

<img width="6912" height="3456" alt="perfiles_la violencia hacia la mujer" src="https://github.com/user-attachments/assets/c509e215-b69a-412e-959e-a6e9940a1b69" />

# Equipo
•	Saraluz Elechiguerra Cázares
•	Lucero Almanza Escalante
•	Sara Luz Cázares Santibañez
•	Karla Josefina Hernández Gómez

# Licencia
Este proyecto se publica exclusivamente con fines de participación en DAT4CCIÓN: Datatón Regional para la Igualdad 2026, organizado por ONU Mujeres – Oficina Regional para las Américas y el Caribe, en el marco del proyecto Las Mujeres Cuentan, en colaboración con el CEEG, GPSDD y la Secretaría de las Mujeres, México.
El uso del contenido analítico, metodológico y visual está permitido únicamente para fines académicos, de investigación o divulgación no comercial, con el debido crédito.
El uso de los datos está sujeto a las licencias de las fuentes oficiales (INEGI, SESNSP, Banco Mundial, ONU Mujeres, CEPAL, entre otras).

