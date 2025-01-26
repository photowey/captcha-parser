import os
import shutil
from pathlib import Path


def main():
    directories_to_clean = ["build", "dist"]

    for directory in directories_to_clean:
        if os.path.exists(directory):
            print(f"Removing {directory}")
            shutil.rmtree(directory)

    for item in Path('.').glob('*/*.egg-info'):
        if item.is_dir():
            print(f"Removing {item}")
            shutil.rmtree(item)

    for file in os.listdir('.'):
        if file.endswith('.spec'):
            spec_file_path = os.path.join('.', file)
            try:
                os.remove(spec_file_path)
                print(f"Successfully removed file: {spec_file_path}")
            except Exception as e:
                print(f"Failed to remove file {spec_file_path}: {e}")

    for file in os.listdir('.'):
        if file.endswith('.log'):
            spec_file_path = os.path.join('.', file)
            try:
                os.remove(spec_file_path)
                print(f"Successfully removed file: {spec_file_path}")
            except Exception as e:
                print(f"Failed to remove file {spec_file_path}: {e}")

    print("Clean operation completed.")


if __name__ == "__main__":
    main()
