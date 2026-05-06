import os
import zipfile

ZIP_NAME = 'plugin.zip'

EXCLUDE_DIRS = {'__pycache__', '.git', 'build'}

EXCLUDE_EXT = {'.pyc'}


def create_zip():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    zip_path = os.path.join(base_dir, ZIP_NAME)

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, dirs, files in os.walk(base_dir):
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            for file in files:
                if file == os.path.basename(__file__) or file == ZIP_NAME:
                    continue

                if os.path.splitext(file)[1] in EXCLUDE_EXT:
                    continue

                filepath = os.path.join(root, file)

                arcname = os.path.relpath(filepath, base_dir)
                z.write(filepath, arcname)

    print(f'📦 {ZIP_NAME} created at {zip_path}')


if __name__ == '__main__':
    create_zip()
