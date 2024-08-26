\# Horarios-2024-2025-upiicsa Repositorio para encontrar mas facil tu horario salon y secuencia

Proyecto de Búsqueda y Captura de Texto en PDF
==============================================

Este proyecto permite buscar texto en un archivo PDF, tomar capturas de las páginas que contienen el texto buscado y generar un archivo PDF con los resultados.

Requisitos
----------

Antes de ejecutar el proyecto, necesitas configurar un entorno virtual e instalar las dependencias. A continuación se indican los pasos para hacerlo.

### 1\. Crear un Entorno Virtual

Para crear un entorno virtual en Python, sigue estos pasos:

1.  Abre una terminal o línea de comandos.
2.  Navega a la carpeta del proyecto.
3.  Crea un entorno virtual con el siguiente comando:

    python -m venv nombre_del_entorno

Reemplaza `nombre_del_entorno` con el nombre que prefieras para tu entorno virtual, como `venv`.

### 2\. Activar el Entorno Virtual

Después de crear el entorno virtual, debes activarlo:

*   **En Windows:**

    nombre_del_entorno\Scripts\activate

*   **En macOS y Linux:**

    source nombre_del_entorno/bin/activate

Una vez activado, tu terminal debería mostrar el nombre del entorno virtual en el prompt.

### 3\. Instalar las Dependencias

Con el entorno virtual activado, instala las dependencias del proyecto utilizando el archivo `requirements.txt`:

1.  Asegúrate de que el archivo `requirements.txt` esté en la raíz de tu proyecto.
2.  Ejecuta el siguiente comando para instalar las dependencias:

    pip install -r requirements.txt

1.  Ejecuta algunas si no te dejan este comando.

 pip install --upgrade pip setuptools

### 4\. Ejecutar la Aplicación

Para ejecutar la aplicación, sigue estos pasos:

1.  Asegúrate de que el entorno virtual esté activado.
2.  Ejecuta el archivo principal de la aplicación (por ejemplo, `Api.py`) con el siguiente comando:

    python Api.py

La aplicación se iniciará y estará disponible en [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### 5\. Desactivar el Entorno Virtual

Cuando termines de trabajar en el entorno virtual, puedes desactivarlo con el siguiente comando:

    deactivate

Esto te devolverá a tu entorno de Python global.

Notas
-----

Asegúrate de que todas las dependencias necesarias estén listadas en el archivo `requirements.txt`.

Consulta la documentación de Flask y las bibliotecas utilizadas para más detalles sobre su configuración y uso.
