import json
import cv2
import os
from ..app.models.alumni_face import AlumniFace
from .user_search import UserSearch
from .load_from_json import transliterate


class ImageUploader:

    def __init__(self,
                 upload_dir: str = r"C:\Users\Alexander\PycharmProjects\newera4\linkedin\web\media\faces",
                 photos_dir: str = r"C:\Users\Alexander\PycharmProjects\newera4\linkedin\web\photos",
                 json_path: str = r"C:\Users\Alexander\PycharmProjects\newera4\linkedin\web\faces.json",
                 ):
        self.upload_dir = upload_dir
        self.photos_dir = photos_dir
        self.json_path = json_path


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
        image = cv2.imread(image_path)

        base_name = os.path.splitext(os.path.basename(image_path))[0]

        for name, (top_left, bottom_right) in rectangles:
            img_copy = image.copy()
            user = UserSearch.user_search(self, query=name).first()
            cv2.rectangle(img_copy, top_left, bottom_right, color=(0, 255, 0), thickness=2)
            english_username = transliterate(user.username)

            output_filename = f"{base_name}_{english_username}.jpg"
            output_path = os.path.join(self.upload_dir,  output_filename)
            cv2.imwrite(output_path, img_copy)

            AlumniFace.objects.create(
                user=user,
                image_path=os.path.basename(image_path)
            )

    def process_all_photos(self, json_path: str):

        image_paths = self.image_from_json(json_path)

        for image_path in image_paths:
            self.face_contouring(image_path)
