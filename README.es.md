# 🩺 Consolidado de Pacientes - Automatización con Python & Flet

[**🇬🇧 Read this documentation in English**](README.md)

Aplicación desarrollada en **Python** utilizando el framework **Flet** para automatizar la revisión y visualización de datos de pacientes a partir de archivos Excel (.xlsm, .xlsx) emitidos por el **Ministerio de Salud del Perú (MINSA)**.

El objetivo principal es reducir el tiempo de búsqueda y análisis de registros (más de 10,000 atenciones) mediante una interfaz moderna, rápida y multiplataforma.

Se eligió **Python** por su excelente soporte para análisis de datos mediante el framework **Pandas**, que permite un manejo óptimo de grandes volúmenes de información.  


## ⚙️ Desafíos técnicos

Uno de los principales retos en esta versión fue manejar eficientemente un conjunto de datos grande, lo que inicialmente afectaba el rendimiento.  
Este problema se resolvió implementando **hilos** y el uso de **async/await**, mejorando significativamente la velocidad de carga y respuesta.


## 🚀 Características actuales (v1.0)

- Carga y visualización de las **100 primeras atenciones**.
- Interfaz limpia y moderna construida con **Flet**.
- Manejo asíncrono para mejorar la performance al cargar archivos grandes.

![Vista principal v1](assets/v1/v1_app.png)

## 🧭 Próximas mejoras

- 🔄 **Paginación** de resultados para mostrar todo el archivo Excel.
- 🔍 **Búsqueda y filtrado** por columnas (documento, nombre, fecha, etc.).
- 🧱 **Eliminación dinámica** de columnas desde la interfaz.


## 🛠️ Tecnologías utilizadas

- [Python 3.11+](https://www.python.org)
- [Flet](https://flet.dev)
- [Pandas](https://pandas.pydata.org)
- [OpenPyXL](https://openpyxl.readthedocs.io)
- [Asyncio](https://docs.python.org/3/library/asyncio.html)


## 👨‍💻 Autor

**Jhon Solano C.**  
[GitHub: @dhalcin](https://github.com/dhalcin)


> 🚧 Proyecto en desarrollo activo — versión funcional inicial (**v1.0**)  
> El objetivo es evolucionar esta herramienta hacia una aplicación completa para análisis y gestión de datos clínicos.