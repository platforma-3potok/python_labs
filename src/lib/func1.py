import os
def is_file_empty(file_path: str) -> bool:
	return os.path.getsize(file_path) == 0