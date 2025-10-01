#!/usr/bin/env python3
import os

def rename_files(directory: str):
    for filename in os.listdir(directory):
        if filename.startswith("invoker"):
            old_path = os.path.join(directory, filename)
            new_filename = "receiver" + filename[len("invoker"):]
            new_path = os.path.join(directory, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    target_dir = "./"  # Change to your directory path
    rename_files(target_dir)
