def build(string: str) -> str:
    return string + string[::-1]
if __name__ == "__main__":
    print(build("38384949393")) 