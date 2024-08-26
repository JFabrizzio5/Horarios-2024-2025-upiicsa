import os
import fitz  # PyMuPDF
from flask import Flask, request, jsonify, send_file, send_from_directory
from PIL import Image, ImageDraw

app = Flask(__name__)

PDF_FILE_NAME = 'horarios_periodo_2025_1.pdf'
PDF_DIR = 'pdfs'
CAPTURAS_DIR = 'capturas'

if not os.path.exists(CAPTURAS_DIR):
    os.makedirs(CAPTURAS_DIR)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

def buscar_texto_y_capturar(pdf_path, texto, margen=10):
    archivo_pdf = os.path.join(PDF_DIR, pdf_path)
    if not os.path.exists(archivo_pdf):
        raise FileNotFoundError(f"No se encontró el archivo: {archivo_pdf}")

    doc = fitz.open(archivo_pdf)
    paginas_a_capturar = []
    capturas_subcarpeta = os.path.join(CAPTURAS_DIR, texto)
    if not os.path.exists(capturas_subcarpeta):
        os.makedirs(capturas_subcarpeta)

    for pagina_num in range(len(doc)):
        pagina = doc.load_page(pagina_num)
        texto_rects = pagina.search_for(texto)

        if texto_rects:
            factor_escala = 2.0
            for idx, rect in enumerate(texto_rects):
                y0 = rect.y0 - margen
                y1 = rect.y1 + margen
                y0 = max(0, y0)
                y1 = min(pagina.rect.height, y1)
                x0 = 0
                x1 = pagina.rect.width
                pix = pagina.get_pixmap(matrix=fitz.Matrix(factor_escala, factor_escala), clip=fitz.Rect(x0, y0, x1, y1))
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                draw = ImageDraw.Draw(img)

                for rect in texto_rects:
                    x0 = (rect.x0 - x0) * factor_escala
                    y0 = (rect.y0 - y0) * factor_escala
                    x1 = (rect.x1 - x0) * factor_escala
                    y1 = (rect.y1 - y0) * factor_escala
                    if x1 > x0 and y1 > y0:
                        draw.rectangle([x0, y0, x1, y1], outline="yellow", width=3)

                img_path = f"{capturas_subcarpeta}/{texto}_{pagina_num + 1}_{idx + 1}_recorte.png"
                img.save(img_path)
                paginas_a_capturar.append(f"capturas/{texto}/{texto}_{pagina_num + 1}_{idx + 1}_recorte.png")

    return paginas_a_capturar

@app.route('/buscar', methods=['POST'])
def buscar():
    data = request.json
    texto = data.get('texto')
    if not texto:
        return jsonify({'error': 'Falta el texto de búsqueda'}), 400

    output_pdf = os.path.join(PDF_DIR, f"{texto}.pdf")

    if not os.path.exists(output_pdf):
        # Generar capturas y PDF si no existe
        capturas = buscar_texto_y_capturar(PDF_FILE_NAME, texto)
        images = [Image.open(png) for png in capturas]
        images[0].save(output_pdf, save_all=True, append_images=images[1:], resolution=300.0, quality=95)

    return jsonify({'filename': f"{texto}.pdf"})

@app.route('/images', methods=['GET'])
def images():
    texto = request.args.get('texto')
    if not texto:
        return jsonify({'error': 'Falta el texto de búsqueda'}), 400

    capturas_subcarpeta = os.path.join(CAPTURAS_DIR, texto)
    if not os.path.exists(capturas_subcarpeta):
        return jsonify([])  # No hay capturas para mostrar

    capturas = os.listdir(capturas_subcarpeta)
    return jsonify([f"{texto}/{img}" for img in capturas])

@app.route('/download', methods=['GET'])
def download():
    filename = request.args.get('filename')
    if not filename:
        return jsonify({'error': 'Falta el nombre del archivo'}), 400

    file_path = os.path.join(PDF_DIR, filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'Archivo no encontrado'}), 404

    return send_file(file_path, as_attachment=True)

@app.route('/capturas/<path:filename>')
def serve_image(filename):
    return send_from_directory(CAPTURAS_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
