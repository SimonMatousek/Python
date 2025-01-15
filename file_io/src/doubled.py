from pathlib import Path
def decrypt_double(file_name):
    PATH_ROOT_DIR = Path(__file__).parent.parent
    SOURCE_PATH = PATH_ROOT_DIR / f"files/{file_name}"
    with open(SOURCE_PATH, "r") as file:
        lines = file.readlines()
    out = []
    line_out = ""
    for line in lines:
        for i in range(0, len(line), 2):
            line_out += line[i]
    out.append(line_out)
    line_out = ""
    with open("files/doubled_output.txt", "w") as file:
        file.writelines(out)

if __name__ == "__main__":
    decrypt_double("doubled.txt")