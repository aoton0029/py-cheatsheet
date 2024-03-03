import os
import shutil
import json
import csv
from pathlib import Path
import pandas as pd
import glob

class FileUtil:
    @staticmethod
    def read_file(file_path):
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def write_file(file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)

    @staticmethod
    def read_json(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def write_json(file_path, data):
        with open(file_path, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def file_exists(file_path):
        return os.path.isfile(file_path)

    @staticmethod
    def delete_file(file_path):
        if FileUtil.file_exists(file_path):
            os.remove(file_path)

    @staticmethod
    def copy_file(source_path, destination_path):
        shutil.copy2(source_path, destination_path)

    @staticmethod
    def get_file_size(file_path):
        return os.path.getsize(file_path)

    @staticmethod
    def create_directory(directory_path):
        os.makedirs(directory_path, exist_ok=True)

    @staticmethod
    def delete_directory(directory_path):
        shutil.rmtree(directory_path, ignore_errors=True)

    @staticmethod
    def list_files_in_directory(directory_path):
        return os.listdir(directory_path)

    @staticmethod
    def write_dataframe_to_csv(df, file_path):
        df.to_csv(file_path, index=False, sep='\t')
    
    @staticmethod
    def read_csv_to_dataframe(file_path):
        return pd.read_csv(file_path, sep='\t')
    
    @staticmethod
    def get_files_with_extension(directory_path, extension):
        return glob.glob(f"{directory_path}/*.{extension}")

    

