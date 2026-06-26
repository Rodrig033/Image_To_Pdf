from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QListWidget,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QFormLayout,
    QComboBox,
    QSpinBox,
    QGroupBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from models.image_model import ImageModel
from services.image_service import ImageService
from services.pdf_service import PDFService
from ui.image_viewer import ImageViewer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PDF Image Generator")
        self.resize(1200, 700)


        self.images = []  # lista de ImageModel
        self.current_image = None

        self.setup_ui()
        self.connect_signals()
        self.crop_mode = True
        self.preview.crop_mode = True

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        #
        # PANEL IZQUIERDO
        #
        self.image_list = QListWidget()
        self.image_list.setMinimumWidth(250)

        #
        # PANEL CENTRAL
        #
        preview_layout = QVBoxLayout()

        self.preview_label = QLabel("Vista previa")
        self.preview = ImageViewer()
        self.preview.setMinimumSize(700, 500)

        self.load_button = QPushButton(
            "Cargar imágenes"
        )

        self.edit_buttons_layout = QHBoxLayout()

        self.rotate_left_btn = QPushButton("⟲ Rotar -90°")
        self.rotate_right_btn = QPushButton("⟳ Rotar +90°")
        self.zoom_in_btn = QPushButton("Zoom +")
        self.zoom_out_btn = QPushButton("Zoom -")
        self.reset_btn = QPushButton("Reset")
        self.export_pdf_btn = QPushButton("Generar PDF")
        self.crop_mode_btn = QPushButton("Modo recorte")
        self.pdf_group = QGroupBox("Configuración PDF")
        self.crop_mode_btn.setCheckable(True)

        pdf_layout = QFormLayout()
        
        # Tamaño
        self.page_size_combo = QComboBox()
        self.page_size_combo.addItems([
            "A4",
            "LETTER"
        ])

        # Orientación
        self.orientation_combo = QComboBox()
        self.orientation_combo.addItems([
            "Vertical",
            "Horizontal"
        ])

        # Margenes 
        self.margin_top = QSpinBox()
        self.margin_bottom = QSpinBox()
        self.margin_left = QSpinBox()
        self.margin_right = QSpinBox()

        # Valores iniciales para los margenes:
        for spin in [
            self.margin_top,
            self.margin_bottom,
            self.margin_left,
            self.margin_right
        ]:
            spin.setRange(0, 100)
            spin.setValue(20)

        self.edit_buttons_layout.addWidget(self.rotate_left_btn)
        self.edit_buttons_layout.addWidget(self.rotate_right_btn)
        self.edit_buttons_layout.addWidget(self.zoom_in_btn)
        self.edit_buttons_layout.addWidget(self.zoom_out_btn)
        self.edit_buttons_layout.addWidget(self.reset_btn)
        self.edit_buttons_layout.addWidget(self.export_pdf_btn)
        
        pdf_layout.addRow(
            "Tamaño",
            self.page_size_combo
        )

        pdf_layout.addRow(
            "Orientación",
            self.orientation_combo
        )

        pdf_layout.addRow(
            "Margen superior",
            self.margin_top
        )

        pdf_layout.addRow(
            "Margen inferior",
            self.margin_bottom
        )

        pdf_layout.addRow(
            "Margen izquierdo",
            self.margin_left
        )

        pdf_layout.addRow(
            "Margen derecho",
            self.margin_right
        )

        preview_layout.addLayout(self.edit_buttons_layout)

        preview_layout.addWidget(
            self.preview
        )

        preview_layout.addWidget(
            self.load_button
        )

        self.pdf_group.setLayout(pdf_layout)

        preview_layout.addWidget(
            self.pdf_group
        )

        #
        # ENSAMBLADO
        #
        main_layout.addWidget(
            self.image_list
        )

        main_layout.addLayout(
            preview_layout
        )

    def load_images(self):
        file_dialog = QFileDialog()
        file_paths, _ = file_dialog.getOpenFileNames(
            self,
            "Selecciona imágenes",
            "",
            "Images (*.png *.jpg *.jpeg *.webp)"
        )

        if not file_paths:
            return

        self.image_list.clear()
        self.images.clear()

        for path in file_paths:
            model = ImageModel(path)
            self.images.append(model)

            self.image_list.addItem(path)

        # mostrar primera imagen
        self.set_current_image(self.images[0])    

    # Sistema de selección real
    def on_image_selected(self, item):
        for img in self.images:
            if img.path == item.text():
                self.set_current_image(img)
                break

    def set_current_image(self, image_model):
        self.current_image = image_model
        self.update_preview()

    def update_preview(self):
        if not self.current_image:
            return

        original = self.current_image.original_image
        transformed = ImageService.apply_transformations(
            original,
            self.current_image
        )

        # Convertir PIL → Qt
        from PySide6.QtGui import QImage, QPixmap

        img_data = transformed.convert("RGB")
        data = img_data.tobytes("raw", "RGB")

        qimg = QImage(
            data,
            img_data.width,
            img_data.height,
            QImage.Format_RGB888
        )

        pixmap = QPixmap.fromImage(qimg)
        self.preview.set_image(pixmap)

    def rotate_left(self):
        if not self.current_image:
            return

        self.current_image.rotate_left()
        self.update_preview() 

    def rotate_right(self):
        if not self.current_image:
            return

        self.current_image.rotate_right()
        self.update_preview()   

    def zoom_in(self):
        if not self.current_image:
            return

        self.current_image.zoom_in()
        self.update_preview()

    def zoom_out(self):
        if not self.current_image:
            return

        self.current_image.zoom_out()
        self.update_preview() 

    def reset_image(self):
        if not self.current_image:
            return

        self.current_image.reset()
        self.update_preview()

    def toggle_crop_mode(self):
        self.crop_mode = self.crop_mode_btn.isChecked()
        self.preview.crop_mode = self.crop_mode
        if self.crop_mode:
            self.crop_mode_btn.setText("Recorte ACTIVADO")
            self.preview.start_crop()
        else:
            self.crop_mode_btn.setText("Recorte desactivado")
            self.preview.crop_rect_item = None

    def generate_pdf(self):
        if not self.images:
            return

        output_path, _ = QFileDialog.getSaveFileName(
            self, 
            "Guardar PDF",
            "",
            "PDF (*.pdf)"
        )      

        if not output_path:
            return

        PDFService.generate_pdf(
            self.images,
            output_path,

            self.page_size_combo.currentText(),

            self.orientation_combo.currentText(),

            self.margin_top.value(),
            self.margin_bottom.value(),
            self.margin_left.value(),
            self.margin_right.value()
    )
    
    # Convertir crop a imagen real
    def scene_to_image_rect(self, rect):

        img = self.current_image.original_image.size
        pix = self.preview.current_pixmap.size()

        scale_x = img[0] / pix.width()
        scale_y = img[1] / pix.height()

        return (
            int(rect.left() * scale_x),
            int(rect.top() * scale_y),
            int(rect.right() * scale_x),
            int(rect.bottom() * scale_y)
        )

    def on_crop_selected(self, rect):

        if not self.current_image:
            return

        crop_box = self.scene_to_image_rect(rect)
        self.current_image.crop_box = crop_box
        self.update_preview()

    def connect_signals(self):
        self.load_button.clicked.connect(self.load_images)

        self.image_list.itemClicked.connect(self.on_image_selected)

        self.rotate_left_btn.clicked.connect(self.rotate_left)
        self.rotate_right_btn.clicked.connect(self.rotate_right)
        self.zoom_in_btn.clicked.connect(self.zoom_in)
        self.zoom_out_btn.clicked.connect(self.zoom_out)
        self.reset_btn.clicked.connect(self.reset_image)    
        self.export_pdf_btn.clicked.connect(self.generate_pdf)
        self.crop_mode_btn.clicked.connect(self.toggle_crop_mode)
        self.preview.crop_selected.connect(self.on_crop_selected)