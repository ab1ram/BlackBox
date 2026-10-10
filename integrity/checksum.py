import hashlib


def hash_file(file):
    with open(file,"rb") as opened_file :
        file_hash = hashlib.sha256()
        block_size = 4 * 1024 * 1024
        while block := opened_file.read(block_size):
            file_hash.update(block)
        return file_hash.hexdigest()


def hash_folder(folder):
    folder_hash = hashlib.sha256()
    for item in sorted(folder.rglob("*")):
        if item.is_file():
            item_hash = hash_file(item)
            relative_path = item.relative_to(folder)
            folder_hash.update(str(relative_path).encode())
            folder_hash.update(bytes.fromhex(item_hash))
    return folder_hash.hexdigest()


def calculate_hash(path):
    if not path.exists():
        raise FileNotFoundError(f"File Not Found : {path}")
    if path.is_file():
        return hash_file(path)
    elif path.is_dir():
        return hash_folder(path)


def check_hash(file,exp_hash):
    return calculate_hash(file) == exp_hash

