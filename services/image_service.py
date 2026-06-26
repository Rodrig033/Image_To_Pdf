from PIL import Image

class ImageService:

    @staticmethod
    def load_image(path: str):
        return Image.open(path)

    @staticmethod
    def apply_transformations(image: Image.Image, model):
        img = image.copy()

        # Rotación
        if model.rotation != 0:
            img = img.rotate(model.rotation, expand=True)

        # Crop (opcional)
        if model.crop_box:
            img = img.crop(model.crop_box)

        # Zoom (escala simple)
        if model.zoom != 1.0:
            w, h = img.size
            new_w = max(1, int(w * model.zoom))
            new_h = max(1, int(h * model.zoom))
            img = img.resize((new_w, new_h))

        return img