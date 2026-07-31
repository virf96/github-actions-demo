# Arquitectura Medallion con GitHub Actions

## Descripción

Este proyecto demuestra una implementación práctica de la **Arquitectura Medallion** para el procesamiento de datos, siguiendo buenas prácticas de organización, calidad y automatización del ciclo de desarrollo.

Además, incorpora **GitHub Actions** para automatizar tareas de integración continua (CI), validación del código y despliegue, facilitando un flujo de trabajo reproducible y mantenible.

## Objetivos

* Implementar una arquitectura de datos basada en las capas **Bronze**, **Silver** y **Gold**.
* Mantener una estructura de proyecto clara y escalable.
* Automatizar la validación del proyecto mediante **GitHub Actions**.
* Promover buenas prácticas de desarrollo con control de versiones utilizando Git y GitHub.

## Arquitectura Medallion

La solución se organiza en tres capas principales:

### Bronze

* Ingesta de datos desde las fuentes originales.
* Conservación de los datos en su estado inicial.
* Mínimas transformaciones.

### Silver

* Limpieza y estandarización de los datos.
* Validaciones de calidad.
* Eliminación de duplicados y tratamiento de valores nulos.

### Gold

* Datos listos para consumo.
* Modelos analíticos.
* Agregaciones y métricas para inteligencia de negocio.

## Estructura del proyecto

```text
.
├── bronze/
├── silver/
├── gold/
├── data/
├── notebooks/
├── src/
├── tests/
├── .github/
│   └── workflows/
├── Dockerfile
├── pyproject.toml
├── .gitignore
├── .env.example
└── README.md
```

## Automatización con GitHub Actions

El proyecto incluye un flujo de integración continua que ejecuta automáticamente diversas tareas cuando se realiza un **push** o un **pull request**, tales como:

* Instalación de dependencias.
* Validación del entorno.
* Ejecución de pruebas.
* Verificación del formato del código.
* Análisis estático (si aplica).

Esta automatización ayuda a detectar errores de manera temprana y garantiza que los cambios cumplan con los estándares definidos antes de integrarse al repositorio principal.

## Requisitos

* Python 3.11 o superior
* Git
* Docker (opcional)
* Cuenta de GitHub

## Instalación

1. Clonar el repositorio.

```bash
git clone <URL_DEL_REPOSITORIO>
```

2. Acceder al proyecto.

```bash
cd <NOMBRE_DEL_PROYECTO>
```

3. Crear un entorno virtual.

```bash
python -m venv .venv
```

4. Activar el entorno.

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

5. Instalar las dependencias.

```bash
pip install -e .
```

## Flujo de trabajo

1. Crear una rama para una nueva funcionalidad.
2. Realizar los cambios.
3. Ejecutar pruebas localmente.
4. Crear un Pull Request.
5. GitHub Actions validará automáticamente el proyecto.
6. Una vez aprobados los cambios, realizar el merge a la rama principal.

## Tecnologías utilizadas

* Python
* Git
* GitHub
* GitHub Actions
* Docker
* Arquitectura Medallion

## Licencia

Este proyecto tiene fines educativos y de demostración, mostrando una implementación de la Arquitectura Medallion junto con prácticas modernas de integración continua utilizando GitHub Actions.
