import os
import json

class JsonUtil:
    def open_file_in_same_directory(file_name):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_name)
        return open(file_path)

    def save_file_in_same_directory(file_name, data):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, file_name)
        file = open(file_path, "w")
        json.dump(data, file)