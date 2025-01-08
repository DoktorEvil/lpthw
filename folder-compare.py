import filecmp
import os


def compare_folders(first, second):
    comparison = filecmp.dircmp(first, second)

    # Print folders in both directories
    print("Common folders:")
    for common_folder in comparison.common_dirs:
        print(common_folder)

    # Print files in both directories
    print("\nCommon files:")
    for common_file in comparison.common_files:
        print(common_file)

    # Print files only in the first directory
    print("\nFiles only in", first)
    for only_in_folder1 in comparison.left_only:
        print(only_in_folder1)

    # Print files only in the second directory
    print("\nFiles only in", second)
    for only_in_folder2 in comparison.right_only:
        print(only_in_folder2)


if __name__ == "__main__":

    folder1 = input("Enter path to first folder: ")
    folder2 = input("Enter path to second folder: ")

    if not os.path.isdir(folder1) or not os.path.isdir(folder2):
        print("Error: One or both of the paths provided are not directories.")
    else:
        compare_folders(folder1, folder2)
# This script takes two folder paths as input and compares them. It prints out the common folders and files,
# as well as files that exist only in one of the directories. Note that this script does not compare the contents of
# the files, only their names and existence.
