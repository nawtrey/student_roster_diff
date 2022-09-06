import os
import glob
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to the .csv files to update.")
    args = parser.parse_args()

    path = str(args.path)
    path = os.path.abspath(path)

    for filepath in glob.glob(f"{path}/*.csv"):
       fpath, ext = filepath.split("-")
       course_id = ext.split(".")[0]
       new_filepath = f"{fpath}-{course_id}(1).csv"
       os.rename(filepath, new_filepath)
