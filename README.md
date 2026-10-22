# Sistema de Gestión Vehicular - Documentación de Evaluaciones 1 y 2

Este repositorio contiene el desarrollo del proyecto backend para el **Sistema de Gestión de Vehículos y Mantenciones**, correspondiente al proceso formativo que abarca las **Unidades 1 y 2** de la asignatura de Desarrollo Back-End.

---

## 📑 Tabla de Contenidos
1. [Resumen General del Proyecto](#1-resumen-general-del-proyecto)
2. [Estructura del Proyecto](#2-estructura-del-proyecto)
3. [Unidad 1: Tecnologías del Lado del Servidor (Evaluación 1)](#3-unidad-1-tecnologías-del-lado-del-servidor-evaluación-1)
    * [Aprendizajes Esperados y Criterios de Evaluación](#aprendizajes-esperados-y-criterios-de-evaluación---unidad-1)
    * [Contenidos Abordados](#contenidos-abordados---unidad-1)
    * [Desarrollo de la Actividad (ABP / PLT)](#desarrollo-de-la-actividad---unidad-1)
4. [Unidad 2: Framework Back-End (Evaluación 2)](#4-unidad-2-framework-back-end-evaluación-2)
    * [Aprendizajes Esperados y Criterios de Evaluación](#aprendizajes-esperados-y-criterios-de-evaluación---unidad-2)
    * [Contenidos Abordados](#contenidos-abordados---unidad-2)
    * [Desarrollo de la Actividad (ABP / PLT)](#desarrollo-de-la-actividad---unidad-2)
5. [Uso e Integración de Inteligencia Artificial (IA)](#5-uso-e-integración-de-inteligencia-artificial-ia)
6. [Instrucciones de Instalación y Despliegue Local](#6-instrucciones-de-instalación-y-despliegue-local)
7. [Endpoints y Funcionalidades Principales](#7-endpoints-y-funcionalidades-principales)
8. [Autor e Información Académica](#8-autor-e-información-académica)

---

## 1. Resumen General del Proyecto
El proyecto consiste en una aplicación web desarrollada con el framework **Django** y **Django REST Framework (DRF)** orientada a la resolución de problemáticas frecuentes en la gestión vehicular, control de flota y seguimiento de mantenciones en talleres.

A lo largo del proceso formativo, la solución evolucionó desde un prototipo básico basado en arquitectura MVC/MVT con consumo de datos estáticos en JSON (Unidad 1), hacia una aplicación robusta integrada con base de datos relacional (MySQL/SQLite), ORM de Django, interfaz Django Admin, autenticación y endpoints para operaciones CRUD completas (Unidad 2).

---

## 2. Estructura del Proyecto

```text
Back-End-Vehiculos-IEI-N4-C3--main/
│
├── drf/                        # Configuración principal del proyecto Django
│   ├── settings.py             # Configuración de base de datos, apps y middleware
│   ├── urls.py                 # Enrutador principal de URLs
│   ├── wsgi.py                 # Interfaz WSGI para servidores web
│   └── asgi.py                 # Interfaz ASGI para servidores asíncronos
│
├── vehiculos/                  # Aplicación de gestión vehicular
│   ├── migrations/             # Migraciones del ORM
│   ├── static/                 # Archivos estáticos e imágenes (Bootstrap, diagramas, INACAP.png)
│   ├── templates/              # Vistas/Plantillas HTML (Interfaz de usuario)
│   ├── admin.py                # Configuración de Django Admin
│   ├── apps.py                 # Configuración del módulo vehiculos
│   ├── models.py               # Modelos relacionales de datos (ORM)
│   ├── serializer.py           # Serializadores de DRF para API REST
│   ├── views.py                # Vistas y controladores de lógica de negocio
│   └── tests.py                # Pruebas unitarias
│
├── manage.py                   # Script de gestión principal de Django
├── requirements.txt            # Dependencias del entorno virtual
└── README.md                   # Documentación técnica del repositorio
```

---

## 3. Unidad 1: Tecnologías del Lado del Servidor (Evaluación 1)

### Aprendizajes Esperados - Unidad 1
* **1.1** Utiliza tecnologías del lado del servidor para resolver problemáticas planteadas, de acuerdo con la sintaxis del lenguaje y el uso de herramientas de inteligencia artificial como apoyo para mejorar la eficiencia del desarrollo.

### Criterios de Evaluación - Unidad 1
* **1.1.1** Identifica variables y operaciones del lenguaje, según requerimiento.
* **1.1.2** Codifica instrucciones, estructuras y operadores, según requerimientos.
* **1.1.3** Codifica instrucciones utilizando paquetes externos, según requerimientos.
* **1.1.4** Implementa una aplicación sencilla en Django, según los requerimientos establecidos y las recomendaciones generadas por herramientas de inteligencia artificial.

### Contenidos Abordados - Unidad 1
* Tecnologías del lado del servidor, protocolos (HTTP/HTTPS), servicios de hosting y dominios.
* Patrón de arquitectura **Modelo-Vista-Controlador (MVC)** / **Modelo-Vista-Template (MVT)**.
* Django Framework: Instalación, entorno virtual `venv` y estructura básica de proyectos.
* Implementación inicial de Vistas (`views.py`), Plantillas (`templates/`) y Modelos sintácticos (`models.py`).
* Integración de agentes de Inteligencia Artificial como apoyo al diseño de interfaces de usuario y generación de datos de prueba en formato JSON.

### Desarrollo de la Actividad - Unidad 1
* **Estrategia Didáctica:** Aprendizaje Basado en Problemas (ABP) y Prácticas de Laboratorio/Taller (PLT).
* **Entregable:** Construcción de un sitio básico en Django sin conexión inicial a base de datos relacional. Los datos de prueba (lista de vehículos, talleres, estados) se cargaron mediante archivos/estructuras de datos en formato **JSON** procesados directamente desde las vistas para renderizarse en las plantillas HTML.

---

## 4. Unidad 2: Framework Back-End (Evaluación 2)

### Aprendizajes Esperados - Unidad 2
* **2.1** Codifica aplicaciones web para proponer soluciones tentativas a una problemática, utilizando un framework del lado del servidor y herramientas de inteligencia artificial como apoyo al desarrollo.

### Criterios de Evaluación - Unidad 2
* **2.1.1** Configura la conexión a una base de datos, según requerimiento.
* **2.1.2** Utiliza el administrador de Django (`Django Admin`), de acuerdo a los requerimientos.
* **2.1.3** Codifica funciones que realicen operaciones CRUD (Create, Read, Update, Delete) sobre una base de datos, según requerimiento.
* **2.1.4** Codifica una aplicación back-end con acceso a base de datos y seguridad, según los requerimientos del problema planteado y orientaciones generadas por herramientas de inteligencia artificial.

### Contenidos Abordados - Unidad 2
* Conexión y configuración de motores de Base de Datos relacionales (MySQL / SQLite) mediante `settings.py`.
* **Django ORM (Object-Relational Mapping):** Creación y ejecución de migraciones (`makemigrations` y `migrate`).
* Panel de administración avanzado **Django Admin** (`admin.py`) para la gestión administrativa de registros.
* Implementación de operaciones **CRUD** completas a través de Vistas basadas en clases/funciones y Django REST Framework (`serializers.py` y ViewSets).
* Estructuración del código back-end asistida por herramientas de Inteligencia Artificial para optimización y legibilidad.

### Desarrollo de la Actividad - Unidad 2
* **Estrategia Didáctica:** Aprendizaje Basado en Problemas (ABP) y Prácticas de Laboratorio/Taller (PLT).
* **Entregable:** Aplicación web back-end completa con persistencia de datos relacional. Se implementaron los modelos `Vehiculo` y `Mantencion` con campos tipados, migraciones a base de datos, permisos de acceso por roles (Administrador, Supervisor, Cliente) y seguridad en los endpoints.

---

## 5. Uso e Integración de Inteligencia Artificial (IA)

En cumplimiento con los requerimientos de ambas unidades, el desarrollo contó con el apoyo de la IA Gemini Google:
1. **Diseño de Interfaz:** Generación de estructuras HTML5 integradas en 404, base e index con archivos estáticos en la Unidad 1.
2. **Generación de Datos de Prueba:** Creación de conjuntos de datos ficticios en formato JSON para los modelos de base de datos en la Unidad 2.
3. **Estructuración y Refactorización de Código:** Apoyo en la optimización de sintaxis en `models.py`, `views.py` y `serializers.py` de Django REST Framework.
4. **Documentación Técnica:** Apoyo en la organización y redacción de la estructura del archivo `README.md`.

---

## 6. Instrucciones de Instalación y Despliegue Local

Para ejecutar el proyecto localmente, siga los pasos descritos a continuación:

### 1. Clonar el repositorio
```bash
git clone https://github.com/Lientur03/Back-End-Vehiculos-IEI-N4-C3-
cd Back-End-Vehiculos-IEI-N4-C3-
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv

# En Windows (PowerShell):
.\venv\Scripts\Activate

# En Linux/macOS:
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar la Base de Datos y aplicar migraciones
Verifique la configuración en `drf/settings.py` y ejecute:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario para acceso a Django Admin
```bash
python manage.py createsuperuser
```

### 6. Iniciar el servidor de desarrollo con el enlace del proyecto autónomo
```bash
python manage.py runserver
```
El proyecto estará disponible en `http://127.0.0.1:8000/vehiculos/`.

---

## 7. Endpoints y Funcionalidades Principales

* `/admin/` - Panel administrativo de Django para gestión interna de la base de datos.
* `/api/vehiculos/` - Endpoints REST (GET, POST, PUT, DELETE) para el control de la flota vehicular.
* `/api/mantenciones/` - Endpoints REST para el registro y seguimiento de órdenes de servicio y mantención.

---

## 8. Autor e Información Académica
* **Estudiante:** Andrés Lientur Hormazábal Fuentes
* **Institución:** INACAP Sede Temuco - Instituto Profesional (IP)
* **Carrera:** Ingeniería en Informática
* **Asignatura:** Programación Back End
* **Docente:** Erick Bailey Rebolledo
* **Sección:** IEI-N4-C3
* **Evaluaciones:** Sumativa 1 (Unidad 1) y Sumativa 2 (Unidad 2)