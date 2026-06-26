from PySide6.QtWidgets import QGraphicsView, QGraphicsScene
from PySide6.QtGui import QPixmap, QPen, QBrush, QColor
from PySide6.QtCore import Qt, QRectF, Signal


class ImageViewer(QGraphicsView):

    crop_selected = Signal(QRectF)

    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene()
        self.setScene(self.scene)

        self.pixmap_item = None

        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)

        self.zoom_factor = 1.15
        self.current_pixmap = None

        # --- crop state ---
        self.crop_mode = False
        self.start_pos = None
        self.crop_rect_item = None

    # -------------------------
    # IMAGE SETTER
    # -------------------------
    def set_image(self, pixmap):

        self.scene.clear()
        self.crop_rect_item = None
        self.current_pixmap = pixmap
        self.pixmap_item = self.scene.addPixmap(pixmap)
        self.setSceneRect(self.pixmap_item.boundingRect())
        self.fitInView(self.pixmap_item, Qt.KeepAspectRatio)
        self.image_original_size = pixmap.size()  # tamaño mostrado
        self.image_raw_size = None

    # -------------------------
    # ZOOM
    # -------------------------
    def wheelEvent(self, event):

        if event.angleDelta().y() > 0:
            self.scale(self.zoom_factor, self.zoom_factor)
        else:
            self.scale(1 / self.zoom_factor, 1 / self.zoom_factor)

    # -------------------------
    # MOUSE EVENTS (CROP)
    # -------------------------
    def mousePressEvent(self, event):

        if not self.crop_mode:
            super().mousePressEvent(event)
            return

        if event.button() == Qt.LeftButton:
            self.start_pos = self.mapToScene(event.position().toPoint())

            if self.crop_rect_item:
                self.scene.removeItem(self.crop_rect_item)
                self.crop_rect_item = None

        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):

        if self.crop_mode and self.start_pos:

            current_pos = self.mapToScene(event.position().toPoint())

            rect = QRectF(self.start_pos, current_pos).normalized()

            pen = QPen(QColor(255, 0, 0))
            pen.setWidth(2)

            brush = QBrush(QColor(255, 0, 0, 40))

            if not self.crop_rect_item:
                self.crop_rect_item = self.scene.addRect(rect, pen, brush)
            else:
                self.crop_rect_item.setRect(rect)

        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):

        if self.crop_mode and self.start_pos and self.crop_rect_item:

            rect = self.crop_rect_item.rect()

            # emitir resultado hacia MainWindow si quieres luego
            self.crop_selected.emit(rect)

        self.start_pos = None

        super().mouseReleaseEvent(event)