import os
def rename_files():
    newName = ""
    # (1) get file names from a folder
    file_list = os.listdir("prank")
    # print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir("prank")

    # (2) for each file, rename filename
    for file_name in file_list:
        newName = file_name.translate(None, "0123456789")
        try:
           print "Trying to rename file "+file_name+" to "+newName+" ...",
           os.rename(file_name, newName)
        except IOError:
           print "Failed"
        else:
           print "Done"

    os.chdir(saved_path)

rename_files()
