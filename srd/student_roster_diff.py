import os
import glob
import pathlib

import tkinter
from tkinter import ttk, filedialog

import pandas as pd


def get_filename(path):
    filename = os.path.basename(path)
    filename = os.path.splitext(filename)[0]
    return filename


def get_course_name(path):
    if path[-1] == "/":
        course_name = os.path.dirname(path)
    else:
        course_name = os.path.basename(path)
    return course_name


def get_section_id(filename):
    section_id = filename.split("-")[1][:5]
    return section_id


def get_section_path_dict(dir_path):
    section_dict = {}
    for fpath in glob.glob(dir_path + "/*"):
        fname = get_filename(fpath)
        section_id = get_section_id(filename=fname)
        abspath = os.path.abspath(fpath)
        new_roster = False
        if "(" in fname:
            new_roster = True
        if section_id not in section_dict.keys():
            section_dict[section_id] = [(abspath, new_roster)]
        else:
            section_dict[section_id].append((abspath, new_roster))
    return section_dict


def get_save_path(dir_path):
    course_name = get_course_name(path=dir_path)
    save_path = pathlib.Path(dir_path)
    save_path = save_path.parent.absolute()
    save_path = os.path.join(save_path, f"{course_name}_roster_diff.csv")
    return save_path

def get_student_diff(dir_path):
    section_dict = get_section_path_dict(dir_path=dir_path)
    filter_keys = ["ID", "First Name", "Last Name", "ASURITE", "Zoom Email"]
    final_df_list = []
    for sec_id, section_info in section_dict.items():
        df_list = []
        for path, new_roster in section_info:
            df = pd.read_csv(path)
            df = df.filter(filter_keys)
            if new_roster:
                df["Task"] = "Add"
            else:
                df["Task"] = "Remove"
            df_list.append(df)
        df = pd.concat(df_list, ignore_index=True)
        df = df.drop_duplicates(subset=["ID"], keep=False)
        df["Section ID"] = sec_id
        final_df_list.append(df)
    df = pd.concat(final_df_list, ignore_index=True)

    save_path = get_save_path(dir_path)
    print(f"Saving at location: {save_path}")
    df.to_csv(save_path, index=False)


def collect_usr_dir():
    dir_path = filedialog.askdirectory()
    if dir_path:
        get_student_diff(dir_path)
        window.destroy()



if __name__ == "__main__":

    # Create an instance of tkinter frame
    window = tkinter.Tk()

    # Set the geometry of tkinter frame
    window.geometry("300x200")

    # Add a Label widget
    label = tkinter.Label(window, text="Click to browse files")
    label.pack(pady=10)

    # Create a Button
    ttk.Button(window, text="Browse", command=collect_usr_dir).pack(pady=20)

    window.mainloop()
