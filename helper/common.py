import os

#  How to use:
#  path = "C:/Users/Admin/Desktop"
#  extensions = (".txt")
def write_list_subfolders_files_in_folder(path, extensions=None):
    if(not path or path == None):
        return False

    if(extensions != None):
        if (len(extensions) == 0):
            return False

    file1 = open("output.txt", "w")
    for root, dirs, files in os.walk(path):
        for file in files:
            if (extensions != None):
                if (file.endswith(extensions)):
                    loc = get_the_last_line_of_file(os.path.join(root, file))
                    file1.writelines(os.path.join(root, file) + ":" + str(loc) + "\n")
                    print(os.path.join(root, file)+ ":" + str(loc))
            else:
                loc = get_the_last_line_of_file(os.path.join(root, file))
                file1.writelines(os.path.join(root, file) + ":" + str(loc) + "\n")
                print(os.path.join(root, file) + ":" + str(loc))
    file1.close()


def get_the_last_line_of_file(path):
    fileHandle = open(path, "r", encoding="utf8")
    lineList = fileHandle.readlines()
    fileHandle.close()
    return len(lineList)