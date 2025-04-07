import json
import os


class JsonBuilder:
    def __init__(self, alumnus_path, univ_path):
        self.alumnus_path = alumnus_path
        self.univ_path = univ_path
        try:
            with open(alumnus_path, "r", encoding="utf-8") as json_file:
                self.data = json.load(json_file)
        except FileNotFoundError:
            print(f"Error: File {alumnus_path} not found.")
            self.data = [] # setting default value to avoid errors
        except json.JSONDecodeError:
            print(f"Error: File {alumnus_path} is not a valid JSON file.")
            self.data = [] # setting default value to avoid errors

    def delete_replications(self):
        for i in range(len(self.data)):
            self.data[i] = {k: v for k, v in self.data[i].items() if k not in ["lat", "lon", "univ_country"]}

    def build_univ_json(self):
        if not os.path.exists(self.univ_path):
            with open(self.univ_path, "w", encoding="utf-8") as json_file:
                json.dump({}, json_file, indent=4)

        with open(self.univ_path, "r", encoding="utf-8") as json_file:
            univ_data = json.load(json_file)

        univ_info = {}
        for elem in univ_data:
            univ = elem["univ"]
            lat = elem["lat"]
            lon = elem["lon"]
            country = elem["univ_country"]
            if univ not in univ_info.keys():
                univ_info[univ] = (lat, lon, country)

        univ_json = []
        for elem in univ_info.items():
            univ_json.append(
                {"name": elem[0], "description": "", "country": elem[1][2], "lat": elem[1][0], "lon": elem[1][1],
                 "image_path": ""})

        with open(self.univ_path, "w", encoding="utf-8") as json_file:
            json.dump(univ_json, json_file, ensure_ascii=False, indent=4)
