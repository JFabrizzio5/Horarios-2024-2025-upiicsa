import PyPDF2
import re
from flask import Flask, render_template, request

app = Flask(__name__)

def extraer_datos_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        texto = ''
        for page in reader.pages:
            texto += page.extract_text()
        
        print(texto)  # Agregar esta línea para imprimir el texto extraído
        
        # Aquí sigue tu código de procesamiento...


        # Patrones para las dos estructuras diferentes
        pattern_1 = re.compile(r'(\b\w+\b(?: \b\w+\b){7,})')
        pattern_2 = re.compile(r'(\b\w+\b(?: \b\w+\b){8,})')
        
        datos = []

        # Procesar las coincidencias del primer patrón
        matches_1 = pattern_1.findall(texto)
        for match in matches_1:
            elementos = match.split()
            if len(elementos) >= 18:  # Verificar si tiene la longitud mínima
                fila = {
                    'programa_academico': elementos[0],
                    'plan': elementos[1],
                    'estd_turno': elementos[2],
                    'secuencia': elementos[3],
                    'unidad_de_aprendizaje': elementos[4],
                    'academia': elementos[5],
                    'docente': elementos[6],
                    'lunes': elementos[7],
                    'lunes_salon': elementos[8],
                    'martes': elementos[9],
                    'martes_salon': elementos[10],
                    'miercoles': elementos[11],
                    'miercoles_salon': elementos[12],
                    'jueves': elementos[13],
                    'jueves_salon': elementos[14],
                    'viernes': elementos[15],
                    'viernes_salon': elementos[16],
                    'edificio': elementos[17],
                }
                datos.append(fila)

        # Procesar las coincidencias del segundo patrón
        matches_2 = pattern_2.findall(texto)
        for match in matches_2:
            elementos = match.split()
            if len(elementos) >= 19:  # Verificar si tiene la longitud mínima
                fila = {
                    'programa_academico': elementos[0],
                    'plan': elementos[1],
                    'estd_turno': elementos[2],
                    'secuencia': elementos[3],
                    'unidad_de_aprendizaje': elementos[4],
                    'academia': elementos[5],
                    'profesor': elementos[6],
                    'lunes': elementos[7],
                    'lunes_salon': elementos[8],
                    'martes': elementos[9],
                    'martes_salon': elementos[10],
                    'miercoles': elementos[11],
                    'miercoles_salon': elementos[12],
                    'jueves': elementos[13],
                    'jueves_salon': elementos[14],
                    'viernes': elementos[15],
                    'viernes_salon': elementos[16],
                    'edificio': elementos[17],
                    'salon': elementos[18],
                }
                datos.append(fila)

    return datos

@app.route('/', methods=['GET', 'POST'])
def index():
    datos = extraer_datos_pdf('horarios_periodo_2025_1.pdf')
    secuencia_filtrada = request.form.get('secuencia')
    
    if secuencia_filtrada:
        datos = [d for d in datos if d.get('secuencia') == secuencia_filtrada]
    
    return render_template('index.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)
