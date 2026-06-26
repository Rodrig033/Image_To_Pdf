<div align="center">

# 🖼️ Image to PDF

**Convierte múltiples imágenes en un único archivo PDF de forma rápida, sencilla e intuitiva.**

Aplicación de escritorio desarrollada en **Python** y **PySide6** con una interfaz gráfica moderna que permite organizar, recortar y convertir imágenes en un documento PDF de alta calidad.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PySide6](https://img.shields.io/badge/PySide6-Qt-41CD52?style=for-the-badge&logo=qt&logoColor=white)
![ReportLab](https://img.shields.io/badge/ReportLab-PDF-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-Educational-blue?style=for-the-badge)

</div>

---

# ✨ Características

- 🖼️ Carga múltiples imágenes.
- 👀 Vista previa de las imágenes seleccionadas.
- ↕️ Reordena las imágenes antes de generar el PDF.
- ✂️ Recorta imágenes mediante selección con el mouse.
- 🗑️ Elimina imágenes de la lista.
- 📄 Genera un único archivo PDF.
- 🏗️ Arquitectura modular basada en el patrón **MVC**.
- 🎨 Interfaz gráfica intuitiva desarrollada con **PySide6**.

---

# 📂 Estructura del proyecto

```text
Image_To_Pdf/
│
├── controllers/
├── models/
├── services/
├── ui/
├── main.py
├── README.md
└── .gitignore
```

---

# 🛠️ Requisitos

| Software | Versión |
|----------|----------|
| Python | 3.11 o superior |
| pip | Última versión recomendada |

---

# 🚀 Instalación

## 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/Rodrig033/Image_To_Pdf.git
```

## 2️⃣ Entrar al proyecto

```bash
cd Image_To_Pdf
```

## 3️⃣ Crear un entorno virtual

### Windows

```bash
python -m venv .venv
```

### macOS / Linux

```bash
python3 -m venv .venv
```

---

## 4️⃣ Activar el entorno virtual

### Windows

```bash
.venv\Scripts\activate
```

### macOS / Linux

```bash
source .venv/bin/activate
```

---

## 5️⃣ Instalar las dependencias

```bash
pip install PySide6 Pillow reportlab
```

---

# ▶️ Ejecutar la aplicación

```bash
python main.py
```

---

# 📖 Cómo utilizar la aplicación

1. 📂 Abre la aplicación.
2. ➕ Agrega una o varias imágenes.
3. ↕️ Reordénalas según el orden deseado.
4. ✂️ Recorta las imágenes si es necesario.
5. 🗑️ Elimina las imágenes que no quieras incluir.
6. 📄 Genera el archivo PDF.
7. 💾 Selecciona la ubicación donde guardar el documento.

---

# 🧱 Tecnologías utilizadas

| Tecnología | Descripción |
|------------|-------------|
| 🐍 Python | Lenguaje principal del proyecto |
| 🖥️ PySide6 | Interfaz gráfica basada en Qt |
| 🖼️ Pillow | Procesamiento y manipulación de imágenes |
| 📄 ReportLab | Generación de archivos PDF |

---

# 🏗️ Arquitectura

El proyecto sigue el patrón **Modelo-Vista-Controlador (MVC)** para mantener una estructura organizada y escalable.

| Carpeta | Responsabilidad |
|----------|-----------------|
| **models** | Manejo de datos y entidades |
| **ui** | Interfaz gráfica de usuario |
| **controllers** | Comunicación entre la vista y la lógica |
| **services** | Procesamiento de imágenes y generación del PDF |

Esta separación facilita el mantenimiento, las pruebas y la incorporación de nuevas funcionalidades.

---

# 🤝 Contribuciones

¡Las contribuciones son bienvenidas!

1. Haz un **Fork** del proyecto.

2. Crea una nueva rama.

```bash
git checkout -b mi-nueva-funcionalidad
```

3. Realiza tus cambios.

4. Haz un commit.

```bash
git commit -m "Agregar nueva funcionalidad"
```

5. Envía los cambios.

```bash
git push origin mi-nueva-funcionalidad
```

6. Abre un **Pull Request**.

---

# 👨‍💻 Autor

**Rodrigo Farid López Córdoba**

Proyecto desarrollado como una aplicación de escritorio para la conversión de imágenes a PDF utilizando **Python**, **PySide6** y **ReportLab**.

---

# 📄 Licencia

Este proyecto se distribuye con fines educativos y de aprendizaje.

Puedes utilizarlo, modificarlo y adaptarlo libremente, respetando siempre la autoría del proyecto.
