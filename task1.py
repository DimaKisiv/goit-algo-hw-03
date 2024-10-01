import sys
from pathlib import Path
import shutil


def parse_arguments():
    if (len(sys.argv) < 2):
        print("Будьласка вкажіть директорію в аргументах")
        sys.exit()
    if (len(sys.argv) < 3):
        return sys.argv[1], sys.argv[1] + "dist"
    if (len(sys.argv) >= 3):
        return sys.argv[1] , sys.argv[2]

def collect_files_recursively(source_dir, files = None):
    if files is None:
        files = []
    source_path = Path(source_dir)
    files_and_folders = list(source_path.iterdir())
    for item in files_and_folders:
        if (item.is_file):
            files.append(item)
        if (item.is_dir()):
            collect_files_recursively(item, files)
    return files

def copy_files(files, dest_dir):
    extensions = set([f.suffix[1:] for f in files])
    extension_folders = create_extensions_folders(extensions, dest_dir)
    for f in files:
        file_ext = f.suffix[1:]
        if (file_ext == ''):
            continue
        file_path_dest = extension_folders[file_ext] / f.name
        if (not file_path_dest.exists()):
            shutil.copy2(f, file_path_dest)


def create_extensions_folders(extensions, dest_dir):
    extension_folders = {}
    dest_path = Path(dest_dir)
    for ext in [e for e in extensions if e != '']:
        folder_path = dest_path / ext 
        folder_path.mkdir(parents=True, exist_ok=True)
        extension_folders[ext] = folder_path
    return extension_folders

def main():
    source_dir, dest_dir = parse_arguments()
    if (not Path(source_dir).is_dir()):
        print(f"Папки {source_dir} не існує")
        sys.exit()
    files = collect_files_recursively(source_dir)
    copy_files(files, dest_dir)
    print(f"Файли скопійовано з {source_dir} в {dest_dir}")


if __name__ == "__main__":
    main()






