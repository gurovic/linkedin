import json
import os

from app.models.alumni_face import AlumniFace
from scripts.user_search import UserSearch


class ImageUploader:
    def __init__(
        self,
        json_path: str = None,
    ):
        self.json_path = json_path or os.environ.get(
            "JSON_PATH",
            r"C:\Users\bushi\Downloads\data (5).json",
        )

    def image_from_json(self, json_path: str):
        with open(json_path, encoding="utf-8") as f:
            data = json.load(f)

        image_paths = []
        for image_path in data.keys():
            if os.path.exists(image_path):
                image_paths.append(image_path)

        return image_paths

    def get_rectangles_from_json(self, json_path: str):
        with open(json_path, encoding="utf-8") as f:
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

        for name, _ in rectangles:
            user = UserSearch.user_search(self, query=name).first()
            AlumniFace.objects.create(
                user=user,
                image_path=os.path.basename(image_path),
            )

    def process_all_photos(self, json_path: str):
        image_paths = self.image_from_json(json_path)

        for image_path in image_paths:
            self.face_contouring(image_path)
