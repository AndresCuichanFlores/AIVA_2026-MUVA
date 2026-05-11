## Introducción

Este proyecto desarrolla un sistema de **Detección y Reconocimiento Automático de Matrículas (ALPR)** orientado a su uso desde un **vehículo policial**. El sistema utiliza **técnicas de visión artificial y aprendizaje profundo** para identificar matrículas de vehículos de cuatro ruedas capturadas mediante una cámara instalada en el coche patrulla. El procesamiento se ejecuta sobre una **Raspberry Pi**, que actúa como unidad de captura y análisis de imágenes.

Una vez detectada y reconocida la matrícula, el sistema realiza **consultas en diferentes bases de datos** con el objetivo de comprobar posibles incidencias asociadas al vehículo, como por ejemplo que esté **reportado como robado, tenga multas pendientes o no disponga de la ITV vigente**. De esta forma, los agentes de policía pueden obtener **información rápida y automática durante las labores de patrullaje**.

El proyecto contempla el desarrollo de un **prototipo funcional** capaz de detectar y reconocer matrículas de vehículos estacionados en parkings de la vía pública. Además del sistema implementado, el proyecto incluye la **documentación de requisitos, el repositorio del código y los elementos necesarios para la evaluación del sistema**.


![img_main.png](img_main.png)


## Mockup del sistema principal

El siguiente mockup muestra una posible interfaz del sistema de detección y reconocimiento automático de matrículas utilizado desde un vehículo policial.

```text
+------------------------------------------------------+
| SISTEMA DE DETECCIÓN DE MATRÍCULAS - VEHÍCULO POLICIAL |
+------------------------------------------------------+

INTERFAZ
--------------------------------------------------------
|                                                      |
|                                                      |
|                                                      |
|            [ Imagen capturada del vehículo ]         |
|                                                      |
|                                                      |
|                                                      |
|                                                      |
|           Matrícula detectada: 1234 ABC              |
|                                                      |
--------------------------------------------------------

Información del vehículo
--------------------------------------------------------
Marca del Vehículo:     TESLA
Vehículo robado:        ❌ No
Multas pendientes:      2
ITV vigente hasta:      04-06-2028      
--------------------------------------------------------

Estado del sistema
--------------------------------------------------------
Dispositivo: Raspberry Pi
Modelo de detección: YOLO / OCR
Base de datos: Vehículos e incidencias
--------------------------------------------------------
```

## Requisitos previos

Para ejecutar este proyecto es necesario disponer de Python 3.12 instalado en el sistema, así como de pip para la gestión
de dependencias. Además, se recomienda trabajar dentro de un entorno virtual para evitar conflictos con otras librerías 
instaladas en el equipo.

Las principales bibliotecas utilizadas en el proyecto son ultralytics, para la detección de matrículas mediante YOLO; 
easyocr, para el reconocimiento de caracteres; opencv-python, para la captura y procesamiento de imágenes y vídeo; numpy, 
para la manipulación de arrays y datos numéricos; torch y torchvision, como base para la ejecución de los modelos de deep learning; 
y pytest, para la ejecución de pruebas automáticas.

Estas dependencias pueden instalarse automáticamente ejecutando el siguiente comando en la raíz del proyecto:

```
pip install -r requirements.txt
```

## Cómo clonar el repositorio

El código fuente del proyecto se encuentra alojado en GitHub. Para descargarlo en local, primero se debe clonar el 
repositorio con el siguiente comando:
```
git clone https://github.com/AndresCuichanFlores/AIVA_2026-MUVA.git
```
Una vez descargado, se accede a la carpeta principal del proyecto mediante:
```
cd AIVA_2026-MUVA
```
La rama main contiene la versión más actualizada y estable del proyecto, por lo que se recomienda trabajar sobre ella:
```
git checkout main
```

## Ejecución del proyecto

Una vez clonado el repositorio y situados en la carpeta del proyecto, se debe acceder al directorio system/src, donde 
se encuentra el archivo principal de ejecución. Desde ahí, el sistema puede iniciarse mediante el siguiente comando:

```
python main.py
```

Este script lanza el sistema completo de reconocimiento automático de matrículas (ALPR). El vídeo a procesar se especifica
directamente en el código, modificando manualmente la variable correspondiente a la ruta del vídeo (video_path) dentro del
archivo main.py.

Una vez configurada la ruta, el sistema procesa el vídeo frame a frame, detectando matrículas, reconociendo el texto 
mediante OCR y mostrando la información asociada a cada vehículo detectado en el terminal.

## Ejecución de tests

El proyecto incluye pruebas unitarias que permiten verificar el correcto funcionamiento de los principales componentes 
del sistema ALPR, como el flujo completo de detección y reconocimiento de matrículas.

Para ejecutar los tests, es necesario situarse en el directorio system/tests y lanzar el siguiente comando:

```
python -m pytest test_detection_and_recognition.py
```

Este archivo de test incluye varias pruebas: una centrada en la detección de matrículas mediante YOLO, otra en el 
reconocimiento de texto mediante OCR, y una última que valida el flujo completo del sistema, desde la detección hasta 
el reconocimiento final de la matrícula. De este modo, se asegura que tanto los módulos individuales como la integración 
entre ellos funcionan correctamente.

# Sistema funcional de Raspberry Pi 5

## Autores

- TAREF BILEL SEIFEDDINE
- FLAVIO ANDRES CUICHAN FLORES

---

# Introducción

Este proyecto desarrolla un sistema de Detección y Reconocimiento Automático de Matrículas (ALPR) orientado a su uso desde un vehículo policial. El sistema utiliza técnicas de visión artificial y aprendizaje profundo para identificar matrículas de vehículos capturadas mediante una cámara instalada en el coche patrulla.

El procesamiento se ejecuta sobre una Raspberry Pi 5, que actúa como unidad principal de captura y análisis de imágenes. Una vez detectada y reconocida la matrícula, el sistema puede mostrar información asociada al vehículo procesado.

El objetivo principal del proyecto es demostrar el despliegue de un sistema funcional de visión artificial utilizando Raspberry Pi y Python.

---

# Mockup del sistema principal

El siguiente mockup muestra una posible interfaz simplificada del sistema:

```text
+------------------------------------------------+
| SISTEMA DE DETECCIÓN DE MATRÍCULAS - POLICÍA  |
+------------------------------------------------+

[ Imagen capturada del vehículo ]

Matrícula detectada: 1234 ABC

Información del vehículo:
- Marca: TESLA
- Vehículo robado: No
- ITV vigente: Sí

Estado del sistema:
- Dispositivo: Raspberry Pi 5
- Modelo IA: YOLO + OCR
```

---

# Requisitos previos

## Hardware necesario

- Raspberry Pi 5
- Tarjeta microSD con Raspberry Pi OS
- TV o monitor
- Cable HDMI
- Ratón USB
- Cargador USB-C
- Memoria USB
- Portátil Linux/Ubuntu

---

# Librerías utilizadas

El proyecto utiliza principalmente:

- ultralytics (YOLO)
- easyocr
- opencv-python
- numpy
- torch
- torchvision
- pytest

---

# Instalación de dependencias

Instalar las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

---

# Cómo clonar el repositorio

```bash
git clone https://github.com/AndresCuichanFlores/AIVA_2026-MUVA.git
```

Entrar al proyecto:

```bash
cd AIVA_2026-MUVA
```

---

# Despliegue estándar en Raspberry Pi 5

## 1. Conexión del hardware

Conectar:

- Raspberry Pi 5
- HDMI a TV/monitor
- Ratón USB
- Alimentación USB-C

---

## 2. Inicio del sistema

Al conectar la alimentación, Raspberry Pi OS arrancará automáticamente.

---

## 3. Configuración WiFi

Desde el escritorio:

- seleccionar la red WiFi
- introducir contraseña
- confirmar conexión

En caso de no disponer de teclado físico, se puede utilizar el teclado virtual:

```text
Squeekboard
```

---

## 4. Transferencia del proyecto

El proyecto puede copiarse desde un portátil Linux mediante una memoria USB.

Ejemplo de ruta del proyecto:

```bash
/home/alumno/Bilel_Andres/AIVA_2026-MUVA
```

---

# Creación del entorno virtual

Entrar al proyecto:

```bash
cd ~/Bilel_Andres/AIVA_2026-MUVA
```

Crear entorno virtual:

```bash
python3 -m venv venv
```

Activar entorno virtual:

```bash
source venv/bin/activate
```

Si funciona correctamente aparecerá:

```bash
(venv)
```

---

# Instalación de dependencias en Raspberry Pi

```bash
pip install -r requirements.txt
```

---

# Ejecución del proyecto

Acceder al directorio principal:

```bash
cd system
```

Ejecutar aplicación:

```bash
python3 main.py
```

---

# Ejecución de tests

Para ejecutar las pruebas:

```bash
python -m pytest
```

o:

```bash
python -m pytest test_detection_and_recognition.py
```

---

# Estructura del proyecto

```text
AIVA_2026-MUVA/
│
├── system/
├── tests/
├── requirements.txt
├── README.md
└── venv/
```

---

# Diagrama UML del despliegue estándar

El sistema sigue el siguiente despliegue:

```text
+-------------------+
| Portátil Linux    |
| Proyecto Python   |
+-------------------+
          |
          | USB
          v
+------------------------+
| Raspberry Pi 5         |
| Raspberry Pi OS        |
| Python + venv          |
| Aplicación principal   |
+------------------------+
          |
          | HDMI
          v
+-------------------+
| TV / Monitor      |
+-------------------+
```

---

# Posibles errores comunes

## Dependencias faltantes

Ejecutar nuevamente:

```bash
pip install -r requirements.txt
```

---

## Error del entorno virtual

Recrear entorno virtual:

```bash
python3 -m venv venv
```

---

## Error de ruta

Comprobar que el proyecto fue extraído correctamente.

---

# Finalización de la aplicación

Para detener la ejecución:

```bash
Ctrl + C
```

---

# Tecnologías utilizadas

- Raspberry Pi OS
- Python 3
- Raspberry Pi 5
- OpenCV
- YOLO
- OCR
- Linux/Ubuntu
- Entornos virtuales Python
