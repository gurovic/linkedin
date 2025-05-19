import json
from PIL import Image
import os
from ..app.models.alumni_face import AlumniFace
from .user_search import UserSearch
from .load_from_json import transliterate

def custom_rectangle(img, pt1, pt2, color, thickness=1, line_type=None):
    """
    Рисует прямоугольник на изображении аналогично cv2.rectangle()

    Параметры:
    - img: numpy.ndarray (изображение, на котором рисуется прямоугольник)
    - pt1: tuple (координаты верхнего левого угла прямоугольника (x1, y1))
    - pt2: tuple (координаты нижнего правого угла прямоугольника (x2, y2))
    - color: tuple (цвет прямоугольника в формате BGR, например (255, 0, 0) для синего)
    - thickness: int (толщина линии, если -1, то прямоугольник заливается цветом)
    - line_type: int (тип линии, необязательный параметр, здесь для совместимости)

    Возвращает:
    - Изображение с нарисованным прямоугольником
    """
    if thickness == -1:
        thickness = 1
        fill = True
    else:
        fill = False

    x1, y1 = pt1
    x2, y2 = pt2

    # Убедимся, что координаты упорядочены
    x1, x2 = min(x1, x2), max(x1, x2)
    y1, y2 = min(y1, y2), max(y1, y2)

    if fill:
        img[y1:y2, x1:x2] = color
    else:
        # Верхняя линия
        img[y1:y1 + thickness, x1:x2] = color
        # Нижняя линия
        img[y2 - thickness:y2, x1:x2] = color
        # Левая линия
        img[y1:y2, x1:x1 + thickness] = color
        # Правая линия
        img[y1:y2, x2 - thickness:x2] = color

    return img

class ImageUploader:

    def __init__(self,
                 upload_dir: str = None,
                 photos_dir: str = None,
                 json_path: str = None
                 ):
        self.upload_dir = upload_dir or os.environ.get('UPLOAD_DIR',
                                                       r"C:\Users\bushi\Downloads\ооо")
        self.photos_dir = photos_dir or os.environ.get('PHOTOS_DIR',
                                                       r"C:\Users\bushi\Downloads\photos")
        self.json_path = json_path or os.environ.get('JSON_PATH',
                                                     r"C:\Users\bushi\Downloads\data (5).json")


    def image_from_json(self, json_path: str):

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        image_paths = []
        for image_path in data.keys():
            if os.path.exists(image_path):
                image_paths.append(image_path)

        return image_paths


    def get_rectangles_from_json(self, json_path: str):

        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for image_path, people_data in data.items():
            rectangles = []
            for name, coords in people_data.items():
                x, y, w, h = coords
                top_left = x, y
                bottom_right = x + w, y + h
                rectangles.append((name, (top_left, bottom_right)))

        return rectangles


    def face_contouring(self, image_path: str):

        rectangles = self.get_rectangles_from_json(self.json_path)
        image = Image.open(image_path)

        base_name = os.path.splitext(os.path.basename(image_path))[0]

        for name, (top_left, bottom_right) in rectangles:
            img_copy = image.copy()
            user = UserSearch.user_search(self, query=name).first()
            if user:
                custom_rectangle(img_copy, top_left, bottom_right, color=(0, 255, 0), thickness=2)
                english_username = transliterate(user.username)
            else:
                print(f"No user found for name: {name}")
                continue
            output_filename = f"{base_name}_{english_username}.jpg"
            output_path = os.path.join(self.upload_dir,  output_filename)
            img_copy.save(output_path)

            AlumniFace.objects.create(
                user=user,
                image_path=os.path.basename(image_path)
            )

    def process_all_photos(self, json_path: str):

        image_paths = self.image_from_json(json_path)

        for image_path in image_paths:
            self.face_contouring(image_path)
