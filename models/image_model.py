from PIL import Image

class ImageModel:
    def __init__(self, path: str):
        self.path = path
        self.original_image = Image.open(path)

        # Estado de edición
        self.rotation = 0
        self.zoom = 1.0
        self.crop_box = None  # (x1, y1, x2, y2)

    def rotate_left(self):
        self.rotation -= 90

    def rotate_right(self):
        self.rotation += 90

    def zoom_in(self):
        self.zoom += 0.1

    def zoom_out(self):
        self.zoom = max(0.1, self.zoom - 0.1)

    def reset(self):
        self.rotation = 0
        self.zoom = 1.0
        self.crop_box = None