import os
import shutil

from_dir = "C:/Users/arnav/Downloads"
to_dir = "C:/Users/arnav/Documents"

list_of_files = os.listdir(from_dir)


for file_name in list_of_files:
    root,extension=os.path.splitext(file_name)

    if extension=="":
        continue
    if extension in [".txt",".pdf",".doc",".docx"]:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file_name
        
        if os.path.exists(path2):
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            shutil.move(path1,path3)
