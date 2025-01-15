from pathlib import Path
def copy_in_new_file(filename_source, filename_copy) -> None:
    PATH_ROOT_DIR = Path(__file__).parent.parent
    SOURCE_PATH_FILE = PATH_ROOT_DIR / f"files/{filename_source}"
    TARGET_PATH_FILE = PATH_ROOT_DIR / f"files/{filename_copy}"
    try:
        with open(SOURCE_PATH_FILE, "r") as file:
            lines = file.readlines()
        with open(TARGET_PATH_FILE, "a") as file:
            file.writelines(lines)
    except IOError:
        print("File not found.")

if __name__ == "__main__":
    copy_in_new_file("copy_file_source.txt", "copy_file_target.txt")