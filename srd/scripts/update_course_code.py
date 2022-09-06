import os
import glob
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="Path to the .csv files to update.")
    parser.add_argument("course_code", type=int, help="The course code.")
    args = parser.parse_args()

    course_code = str(args.course_code)
    path = str(args.path)
    path = os.path.abspath(path)

    for fname in glob.glob(f"{path}/*.csv"):
       keep = fname.split("-")[1]
       fname = os.path.join(path, fname)
       new_fname = os.path.join(path, f"{course_code}-{keep}")
       os.rename(fname, new_fname)
