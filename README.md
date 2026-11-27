# Sistema de Gestión Vehicular - Documentación de Evaluaciones 1, 2 y 3

Este repositorio contiene el desarrollo acumulativo del proyecto backend para el **Sistema de Gestión de Vehículos y Mantenciones**, correspondiente al proceso formativo que abarca las **Unidades 1, 2 y 3** (Evaluación Sumativa 3 — Ponderación 30%) de la asignatura de Programación Back End.

---

## 📑 Tabla de Contenidos
1. [Resumen General del Proyecto](#1-resumen-general-del-proyecto)
2. [Estructura del Proyecto](#2-estructura-del-proyecto)
3. [Unidad 1: Tecnologías del Lado del Servidor (Evaluación 1)](#3-unidad-1-tecnologías-del-lado-del-servidor-evaluación-1)
    * [Aprendizajes Esperados y Criterios de Evaluación](#aprendizajes-esperados---unidad-1)
    * [Contenidos Abordados](#contenidos-abordados---unidad-1)
    * [Desarrollo de la Actividad (ABP / PLT)](#desarrollo-de-la-actividad---unidad-1)
4. [Unidad 2: Framework Back-End (Evaluación 2)](#4-unidad-2-framework-back-end-evaluación-2)
    * [Aprendizajes Esperados y Criterios de Evaluación](#aprendizajes-esperados---unidad-2)
    * [Contenidos Abordados](#contenidos-abordados---unidad-2)
    * [Desarrollo de la Actividad (ABP / PLT)](#desarrollo-de-la-actividad---unidad-2)
5. [Unidad 3: CRUD Web con CBV y Complemento API REST (Evaluación 3 — Ponderación 30%)](#5-unidad-3-crud-web-con-cbv-y-complemento-api-rest-evaluación-3--ponderación-30)
    * [Objetivo y Alcance](#objetivo-y-alcance)
    * [Aspectos Clave Implementados](#aspectos-clave-implementados)
6. [Uso e Integración de Inteligencia Artificial (IA)](#6-uso-e-integración-de-inteligencia-artificial-ia)
7. [Instrucciones de Instalación y Despliegue Local](#7-instrucciones-de-instalación-y-despliegue-local)
8. [Endpoints y Funcionalidades Principales](#8-endpoints-y-funcionalidades-principales)
9. [Autor e Información Académica](#9-autor-e-información-académica)

---

## 1. Resumen General del Proyecto
El proyecto consiste en una aplicación web desarrollada con el framework **Django** y **Django REST Framework (DRF)** orientada a la resolución de problemáticas frecuentes en la gestión vehicular, control de flota y seguimiento de mantenciones en talleres.

A lo largo del proceso formativo, la solución evolucionó desde un prototipo básico basado en arquitectura MVC/MVT con consumo de datos estáticos en JSON (Unidad 1), hacia una aplicación robusta integrada con base de datos relacional (MySQL/SQLite), ORM de Django, interfaz Django Admin, autenticación, configuración mediante variables de entorno `.env` y endpoints API REST (Unidad 2), culminando con un CRUD web completo mediante Vistas Basadas en Clases (CBV) nativas y formularios `ModelForm` personalizados (Unidad 3).

---

## 2. Estructura del Proyecto

```text
Back-End-Vehiculos-IEI-N4-C3--main/
│
├── drf/                        # Configuración principal del proyecto Django
│   ├── settings.py             # Configuración de base de datos, apps, .env y middleware
│   ├── urls.py                 # Enrutador principal de URLs
│   ├── wsgi.py                 # Interfaz WSGI para servidores web
│   └── asgi.py                 # Interfaz ASGI para servidores asíncronos
│
├── vehiculos/                  # Aplicación de gestión vehicular
│   ├── fixtures/               # Datos de prueba en formato JSON (01 a 06)
│   ├── migrations/             # Migraciones del ORM
│   ├── static/                 # Archivos estáticos locales (Bootstrap, Bootswatch, jQuery, DataTables, imágenes)
│   ├── templates/              # Plantillas HTML (Vistas públicas, CRUD CBV y flujo de autenticación)
│   ├── admin.py                # Configuración de Django Admin
│   ├── apps.py                 # Configuración del módulo vehiculos
│   ├── forms.py                # Formularios ModelForm con widgets y atributos HTML personalizados
│   ├── models.py               # Modelos relacionales de datos (ORM) y extensión de usuario
│   ├── serializer.py           # Serializadores de DRF para API REST
│   ├── urls.py                 # Registro de rutas web (CBV) y rutas de la aplicación
│   ├── views.py                # Vistas basadas en clases (CBV) y controladores de lógica de negocio
│   └── tests.py                # Pruebas unitarias
│
├── .env                        # Variables de entorno para conexión y seguridad
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
* Conexión y configuración de motores de Base de Datos relacionales (MySQL / SQLite) mediante `settings.py` y variables de entorno.
* **Django ORM (Object-Relational Mapping):** Creación y ejecución de migraciones (`makemigrations` y `migrate`).
* Panel de administración avanzado **Django Admin** (`admin.py`) para la gestión administrativa de registros.
* Implementación de operaciones **CRUD** completas a través de Vistas basadas en clases/funciones y Django REST Framework (`serializers.py` y ViewSets).
* Estructuración del código back-end asistida por herramientas de Inteligencia Artificial para optimización y legibilidad.

### Desarrollo de la Actividad - Unidad 2
* **Estrategia Didáctica:** Aprendizaje Basado en Problemas (ABP) y Prácticas de Laboratorio/Taller (PLT).
* **Entregable:** Aplicación web back-end completa con persistencia de datos relacional. Se implementaron los modelos de datos con campos tipados, migraciones a base de datos, permisos de acceso por roles y seguridad en los endpoints.

---

## 5. Unidad 3: CRUD Web con CBV y Complemento API REST (Evaluación 3 — Ponderación 30%)

### Objetivo y Alcance
Complementar el proyecto acumulativo en Django y Django REST Framework (con configuración mediante variables de entorno `.env`, migraciones, serializers y ViewSets) mediante un CRUD web completo con Vistas Basadas en Clases (CBV) nativas (`ListView`, `DetailView`, `CreateView`, `UpdateView` y `DeleteView` con confirmación previa), formularios centralizados en `forms.py` con `ModelForm` y widgets HTML personalizados, navegación funcional y vista pública de bienvenida.

### Aspectos Clave Implementados
* **CRUD Web con CBV y URLs:** Implementación de `ListView`, `DetailView`, `CreateView`, `UpdateView` y `DeleteView` para las entidades principales registradas en `urls.py` (documentando en el `README` cualquier vista omitida con justificación técnica).
* **Formularios (`forms.py`):** Definición explícita de campos mediante `ModelForm`, separación de responsabilidades respecto a vistas y modelos, y personalización de widgets (`TextInput`, `NumberInput`, `EmailInput`, `PasswordInput`, `DateInput`, `Select`, `Textarea`, `CheckboxInput`, etc.) con clases y atributos HTML.
* **Navegación, Interfaz y Vista Pública:** Menús/botones de navegación entre pantallas, página de bienvenida como vista pública obligatoria y carga de datos de prueba mediante fixtures JSON.
* **Entrega y Evidencias:** Repositorio GitHub, scripts SQL de creación de base de datos y de usuario/permisos, archivo `.env`, respuestas a las cinco preguntas individuales y PDF de evidencias con capturas que muestren la URL visible en el navegador junto al registro correspondiente en el terminal.

---

## 6. Uso e Integración de Inteligencia Artificial (IA)

En cumplimiento con los requerimientos de las tres unidades, el desarrollo contó con el apoyo de **Gemini Google**:
1. **Diseño de Interfaz y Plantillas:** Generación y refactorización de estructuras HTML5 integradas en `base.html`, `index.html`, vistas de error y flujo de autenticación/restablecimiento de contraseña con archivos estáticos locales y temas Bootswatch.
2. **Generación de Datos de Prueba (Fixtures):** Creación y ajuste de conjuntos de datos en formato JSON (`01` a `06`) para poblar los modelos relacionales en MySQL sin conflictos de llaves foráneas.
3. **Estructuración y Refactorización de Código:** Apoyo en la optimización de sintaxis en `models.py`, vistas basadas en clases (`views.py`), formularios con widgets personalizados (`forms.py`) y `serializers.py` de Django REST Framework.
4. **Documentación Técnica:** Apoyo en la organización, síntesis y redacción de la estructura del archivo `README.md`.

---

## 7. Instrucciones de Instalación y Despliegue Local

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

### 4. Configurar variables de entorno y Base de Datos
1. Configure el archivo `.env` en la raíz del proyecto con las credenciales de su motor MySQL (`iei_n4_c3`) y `SECRET_KEY`.
2. Ejecute los scripts SQL de creación de base de datos y usuario/permisos entregados junto al proyecto.
3. Aplique las migraciones del ORM:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Crear superusuario y cargar datos de prueba (Fixtures)
```bash
python manage.py createsuperuser
python manage.py loaddata 01_estados_reglas.json 02_clientes_vehiculos.json 03_personal_y_perfiles.json 04_gestion_operacion_datos.json 05_consultas_reportes_indicadores.json 06_actividad_publica_privada.json
```

### 6. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```
El proyecto estará disponible en `http://127.0.0.1:8000/`.

---

## 8. Endpoints y Funcionalidades Principales

* `/` - Vista pública de bienvenida de la aplicación y acceso al sistema.
* `/vehiculos/` - Navegación web y operaciones CRUD mediante Vistas Basadas en Clases (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`).
* `/admin/` - Panel administrativo de Django para gestión interna de la base de datos.
* `/api/vehiculos/` - Endpoints REST (GET, POST, PUT, DELETE) para el control de la flota vehicular.
* `/api/mantenciones/` - Endpoints REST para el registro y seguimiento de órdenes de servicio y mantención.

---

## 9. Autor e Información Académica
* **Estudiante:** Andrés Lientur Hormazábal Fuentes
* **Institución:** INACAP Sede Temuco - Instituto Profesional (IP)
* **Carrera:** Ingeniería en Informática
* **Asignatura:** Programación Back End
* **Docente:** Erick Bailey Rebolledo
* **Sección:** IEI-N4-C3
* **Evaluaciones:** Sumativa 1 (Unidad 1), Sumativa 2 (Unidad 2) y Sumativa 3 (Unidad 3 — Ponderación 30%)