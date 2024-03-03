import os
import shutil
from pathlib import Path

class OsUtil:
	@staticmethod
	def get_current_directory():
		return os.getcwd()

	@staticmethod
	def change_directory(path):
		os.chdir(path)

	@staticmethod
	def list_files_in_directory(directory_path):
		return os.listdir(directory_path)

	@staticmethod
	def create_directory(directory_path):
		os.makedirs(directory_path, exist_ok=True)

	@staticmethod
	def delete_directory(directory_path):
		shutil.rmtree(directory_path, ignore_errors=True)

	@staticmethod
	def rename_directory(old_name, new_name):
		os.rename(old_name, new_name)

	@staticmethod
	def get_file_size(file_path):
		return os.path.getsize(file_path)

	@staticmethod
	def get_file_extension(file_path):
		return os.path.splitext(file_path)[1]

	@staticmethod
	def get_file_creation_time(file_path):
		return os.path.getctime(file_path)

	@staticmethod
	def get_file_modification_time(file_path):
		return os.path.getmtime(file_path)

	@staticmethod
	def file_exists(file_path):
		return os.path.isfile(file_path)

	@staticmethod
	def directory_exists(directory_path):
		return os.path.isdir(directory_path)

	@staticmethod
	def copy_file(source_path, destination_path):
		shutil.copy2(source_path, destination_path)

	@staticmethod
	def move_file(source_path, destination_path):
		shutil.move(source_path, destination_path)

	@staticmethod
	def delete_file(file_path):
		if OsUtil.file_exists(file_path):
			os.remove(file_path)

	@staticmethod
	def rename_file(source_path, new_name):
		os.rename(source_path, new_name)

	@staticmethod
	def get_file_path_without_extension(file_path):
		return os.path.splitext(file_path)[0]

	@staticmethod
	def get_parent_directory(file_path):
		return os.path.dirname(file_path)

	@staticmethod
	def get_absolute_path(file_path):
		return os.path.abspath(file_path)

	@staticmethod
	def get_relative_path(file_path, start_path=None):
		return os.path.relpath(file_path, start_path)