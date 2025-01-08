import os
import filecmp
import shutil


def compare_directories(dir1, dir2):
    """
    Compare two directories and list the differing filenames.
    :param dir1: First directory path
    :param dir2: Second directory path
    """
#    comparison = filecmp.dircmp(dir1, dir2, shallow=False)
# Playing with this stuff
    compare_directories(dir1, dir2)

    # List differing files
    for filename in comparison.diff_files:
        print(f"Difference found: {filename}")

    # Provide option to copy differing files
    copy_differences = input("Do you want to copy the differing files? (yes/no): ").lower()
    if copy_differences == "yes":
        for filename in comparison.diff_files:
            src_path = os.path.join(dir1, filename)
            dest_path = os.path.join(dir2, filename)
            shutil.copy2(src_path, dest_path)
            print(f"File '{filename}' copied from '{dir1}' to '{dir2}'.")


if __name__ == "__main__":
#    path1 = "path/to/first/directory"
#    path2 = "path/to/second/directory"
    path1 = r"C:\Users\twbas\OneDrive\Documents\Test\Obsidian Vault-1"
    path2 = r"C:\Users\twbas\OneDrive\Documents\Test\Obsidian Vault-2"
    compare_directories(path1, path2)

#Replace "path/to/first/directory" and "path/to/second/directory" with the actual paths of the directories
#you want to compare. When you run this script, it will display the differing filenames and
#prompt you to copy them if desired. Remember to adjust the paths and customize the behavior as needed for
#your specific use case.