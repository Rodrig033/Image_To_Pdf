from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, LETTER, landscape, portrait
from PIL import Image
import tempfile
import os


class PDFService:

    @staticmethod
    def generate_pdf(
        image_models,
        output_path,
        page_size,
        orientation,
        margin_top,
        margin_bottom,
        margin_left,
        margin_right
    ):

        # 1. Tamaño base
        if page_size == "A4":
            pdf_page_size = A4
        else:
            pdf_page_size = LETTER

        # 2. Orientación
        if orientation == "Horizontal":
            pdf_page_size = landscape(pdf_page_size)
        else:
            pdf_page_size = portrait(pdf_page_size)

        pdf = canvas.Canvas(output_path, pagesize=pdf_page_size)

        page_width, page_height = pdf_page_size

        # 3. Área útil
        usable_width = page_width - margin_left - margin_right
        usable_height = page_height - margin_top - margin_bottom

        # 4. Procesar imágenes
        for model in image_models:

            image = model.original_image.copy()

            if model.rotation != 0:
                image = image.rotate(model.rotation, expand=True)

            if model.crop_box:
                image = image.crop(model.crop_box)

            temp_file = tempfile.NamedTemporaryFile(
                suffix=".jpg",
                delete=False
            )

            temp_path = temp_file.name
            temp_file.close()

            image.convert("RGB").save(temp_path, "JPEG")

            img_width, img_height = image.size

            # 5. Escalado
            scale = min(
                usable_width / img_width,
                usable_height / img_height
            )

            draw_width = img_width * scale
            draw_height = img_height * scale

            # 6. Centrado
            x = margin_left + (usable_width - draw_width) / 2
            y = margin_bottom + (usable_height - draw_height) / 2

            pdf.drawImage(
                temp_path,
                x,
                y,
                width=draw_width,
                height=draw_height
            )

            pdf.showPage()

            os.remove(temp_path)

        pdf.save()