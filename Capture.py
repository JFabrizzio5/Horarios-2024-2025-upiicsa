import fitz  # PyMuPDF
from PIL import Image, ImageDraw

def buscar_texto_y_capturar(pdf_path, texto, margen=10, output_pdf="output.pdf"):
    # Abre el archivo PDF
    doc = fitz.open(pdf_path)
    paginas_a_capturar = []

    for pagina_num in range(len(doc)):
        pagina = doc.load_page(pagina_num)
        texto_rects = pagina.search_for(texto)

        if texto_rects:
            # Definir el factor de escala para mejorar la resolución
            factor_escala = 2.0

            for rect in texto_rects:
                # Ajustar el margen fijo para capturar menos área arriba y abajo
                y0 = rect.y0 - margen
                y1 = rect.y1 + margen
                
                # Asegurarse de que el margen no se salga de los límites de la página
                y0 = max(0, y0)
                y1 = min(pagina.rect.height, y1)

                # Definir el recorte con el ancho completo de la página
                x0 = 0
                x1 = pagina.rect.width

                # Tomar la imagen del área específica con mayor resolución
                pix = pagina.get_pixmap(matrix=fitz.Matrix(factor_escala, factor_escala), clip=fitz.Rect(x0, y0, x1, y1))

                # Convertir a imagen PIL
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                draw = ImageDraw.Draw(img)

                # Dibujar rectángulos amarillos alrededor del texto encontrado
                for rect in texto_rects:
                    x0 = (rect.x0 - x0) * factor_escala
                    y0 = (rect.y0 - y0) * factor_escala
                    x1 = (rect.x1 - x0) * factor_escala
                    y1 = (rect.y1 - y0) * factor_escala

                    # Asegurarse de que x1 >= x0 y y1 >= y0
                    if x1 > x0 and y1 > y0:
                        draw.rectangle([x0, y0, x1, y1], outline="yellow", width=3)

                # Guardar la imagen como temporal
                img.save(f"pagina_{pagina_num + 1}_recorte.png")

                # Añadir la página a la lista
                paginas_a_capturar.append(f"pagina_{pagina_num + 1}_recorte.png")

    # Crear un nuevo PDF con las imágenes capturadas
    if paginas_a_capturar:
        images = [Image.open(png) for png in paginas_a_capturar]
        images[0].save(output_pdf, save_all=True, append_images=images[1:], resolution=300.0, quality=95)
        print(f"Nuevo PDF guardado en: {output_pdf}")

# Ejemplo de uso
buscar_texto_y_capturar("horarios_periodo_2025_1.pdf", "2CV22")
