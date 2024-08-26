# Horarios-2024-2025-upiicsa

Repositorio para encontrar mas facil tu horario salon y secuencia

<div class="container mt-4">
    <h1>Proyecto de Búsqueda y Captura de Texto en PDF</h1>
    <p>Este proyecto permite buscar texto en un archivo PDF, tomar capturas de las páginas que contienen el texto buscado y generar un archivo PDF con los resultados.</p>
    
    <h2>Requisitos</h2>
    <p>Antes de ejecutar el proyecto, necesitas configurar un entorno virtual e instalar las dependencias. A continuación se indican los pasos para hacerlo.</p>

    <h3>1. Crear un Entorno Virtual</h3>
    <p>Para crear un entorno virtual en Python, sigue estos pasos:</p>
    <ol>
        <li>Abre una terminal o línea de comandos.</li>
        <li>Navega a la carpeta del proyecto.</li>
        <li>Crea un entorno virtual con el siguiente comando:</li>
    </ol>
    <pre><code>python -m venv nombre_del_entorno</code></pre>
    <p>Reemplaza <code>nombre_del_entorno</code> con el nombre que prefieras para tu entorno virtual, como <code>venv</code>.</p>

    <h3>2. Activar el Entorno Virtual</h3>
    <p>Después de crear el entorno virtual, debes activarlo:</p>
    <ul>
        <li><strong>En Windows:</strong></li>
    </ul>
    <pre><code>nombre_del_entorno\Scripts\activate</code></pre>
    <ul>
        <li><strong>En macOS y Linux:</strong></li>
    </ul>
    <pre><code>source nombre_del_entorno/bin/activate</code></pre>
    <p>Una vez activado, tu terminal debería mostrar el nombre del entorno virtual en el prompt.</p>

    <h3>3. Instalar las Dependencias</h3>
    <p>Con el entorno virtual activado, instala las dependencias del proyecto utilizando el archivo <code>requirements.txt</code>:</p>
    <ol>
        <li>Asegúrate de que el archivo <code>requirements.txt</code> esté en la raíz de tu proyecto.</li>
        <li>Ejecuta el siguiente comando para instalar las dependencias:</li>
    </ol>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h3>4. Ejecutar la Aplicación</h3>
    <p>Para ejecutar la aplicación, sigue estos pasos:</p>
    <ol>
        <li>Asegúrate de que el entorno virtual esté activado.</li>
        <li>Ejecuta el archivo principal de la aplicación (por ejemplo, <code>Api.py</code>) con el siguiente comando:</li>
    </ol>
    <pre><code>python Api.py</code></pre>
    <p>La aplicación se iniciará y estará disponible en <a href="http://127.0.0.1:5000/">http://127.0.0.1:5000/</a>.</p>

    <h3>5. Desactivar el Entorno Virtual</h3>
    <p>Cuando termines de trabajar en el entorno virtual, puedes desactivarlo con el siguiente comando:</p>
    <pre><code>deactivate</code></pre>
    <p>Esto te devolverá a tu entorno de Python global.</p>

    <h2>Notas</h2>
    <p>Asegúrate de que todas las dependencias necesarias estén listadas en el archivo <code>requirements.txt</code>.</p>
    <p>Consulta la documentación de Flask y las bibliotecas utilizadas para más detalles sobre su configuración y uso.</p>

</div>
