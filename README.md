Student Roster Diff
===================

Naive work-around code for automating student rosters.

File Setup
----------
For each course, store the original rosters along with the updated rosters
together in a common directory named after the course (e.g. PHY114), allowing
Windows to alter the filenames automatically. For example, for a course with
a course ID of `98765`, the original roster's file name would be `1234-98765.csv`,
and the _newer_ roster would be saved as `1234-98765(1).csv`.

This will compare these 2 `.csv` files and return a `.csv` highlighting
the differences between the two rosters.


Running the Executable
----------------------
Simply save the executable anywhere and run it. A dialog box will open.
Click the "Browse" button and locate the directory containing the student
roster .csv files to compare. Click "Select Folder" and the script will
generate a .csv file containing the student names to add/remove, along
with all of their relevant info.


Generating the Executable
-------------------------
With `pyinstaller` installed, run:

```
  pyinstaller student_roster_diff.py -F
```
