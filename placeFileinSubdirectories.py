

# Generated in response to the following prompt:
# Please write a Python script that copies a file, whose filename is given as a
# command-line argument into each subdirectory of the current directory (the one
# where the Python script is located). Thanks.

import os
import sys
import shutil

def main():
    # Check for correct usage
    if len(sys.argv) < 2:
        print(f"Usage: python3 (or py -3 on Windows) {os.path.basename(__file__)} <source_file>")
        sys.exit(1)

    source_files = sys.argv[1:]
    # print(source_files)

    # Get absolute path of the source file
    source_files_abs = [os.path.abspath(source_file) for source_file in source_files]
    # print(source_files_abs)

    # Check if the source file exists
    for source_file in source_files_abs:
        if not os.path.isfile(source_file):
            print(f"Error: File '{source_file}' does not exist.")
            sys.exit(1)

    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # List all immediate subdirectories in script_dir
    subdirs = [d for d in os.listdir(script_dir)
               if os.path.isdir(os.path.join(script_dir, d))]

    # print(subdirs[0], ':', type(subdirs[0]))
    
    def create_alt_dirname(dir_name):
        items = dir_name.split(" - ")
        d = {'uid' : items[0], 'name': items[1], 'ts' : items[2]}
        name_split = d['name'].split()
        new_fn = name_split[1] + name_split[0] + "-"
        new_fn += d['ts'] + "-" + d['uid']
        return new_fn
    
    alt_filenames = []
    for subdir in subdirs:
        # print(subdir)
        alt_filename = create_alt_dirname(subdir)
        alt_filenames.append(alt_filename)
        items = [i for i in os.listdir(subdir)]
        # print(items)
        # print()
        dest_path = os.path.join(script_dir, alt_filename)
        try:
            os.mkdir(dest_path)
        except Exception as e:
            print(f"Failed to create new directory {dest_path}")
        for f in items:
            f_source_path = os.path.join(script_dir, subdir, f)
            f_dest_path = os.path.join(script_dir, alt_filename, f)
            try:
                shutil.copy2(f_source_path, f_dest_path)
                print(f"Copied from: {f_source_path}, to: {f_dest_path}")
            except Exception as e:
                print(f"Failed to copy from: {f_source_path}, to {f_dest_path}: {e}")

    source_files_base = []
    # Get the filename to copy
    for source_file in source_files_abs:
        source_files_base.append(os.path.basename(source_file))
        
    source_files_ult = list(zip(source_files_abs, source_files_base))
    print("ZIP:", source_files_ult)

    print("ALT:", alt_filenames)
    # Copy the file into each subdirectory
    for subdir in alt_filenames:
        print("SUBDIR:", subdir)
        for source_file, filename in source_files_ult:
            print("FILENAME:", filename)
            dest_path = os.path.join(script_dir, subdir, filename)
            try:
                shutil.copy2(source_file, dest_path)
                print(f"Copied from: {source_file}, to: {dest_path}")
            except Exception as e:
                print(f"Failed to copy from: {source_file}, to {dest_path}: {e}")

if __name__ == "__main__":
    main()
