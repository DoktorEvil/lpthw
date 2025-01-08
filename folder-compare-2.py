#Here is a Python script that compares two directories and their subdirectories

import os
import filecmp


def compare_dirs(dir1, dir2):
    dcmp = filecmp.dircmp(dir1, dir2)
    report_diff(dcmp)


def report_diff(dcmp, indent=''):
    for name in dcmp.left_only:
        print(f"{indent}Only in {dcmp.left}: {name}")
    for name in dcmp.right_only:
        print(f"{indent}Only in {dcmp.right}: {name}")
    for name in dcmp.diff_files:
        print(f"{indent}Differing files: {name}")
    for sub_dcmp in dcmp.subdirs.values():
        report_diff(sub_dcmp, indent + '  ')


if __name__ == "__main__":
    dir1 = '/path/to/first/folder'
    dir2 = '/path/to/second/folder'
    compare_dirs(dir1, dir2)

#Replace /path/to/first/folder and /path/to/second/folder with the paths to the directories you want to compare.
#This script will recursively compare the contents of the two directories and print the differences.
