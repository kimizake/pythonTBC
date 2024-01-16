def fileReader(path: str) -> str:
    with open(path, "r") as fp:
        return fp.read()
