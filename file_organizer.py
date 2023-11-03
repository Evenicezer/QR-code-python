import os
import shutil

#specify the directory to organize
directory=os.getcwd() + '\\...\\...'# or r'copy the path'

#create a dictionary to hold the file extension
file_extensions={'pdf':'PDF','png':'Images','jpg':'Images','doc':'Documents','csv':'Data','zip':'Archives',
                 'avi':'Videos','mp3':'Music','exe':'Executables'}


# Organize files based on their extensions
for filename in os.listdir(source_directory):
    if os.path.isfile(filename):
        file_name, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()  # Convert extension to lowercase
        if file_extension in file_extensions:
            category = file_extensions[file_extension]
            destination_folder = os.path.join(source_directory, category)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            source_file = os.path.join(source_directory, filename)
            destination_file = os.path.join(destination_folder, filename)
            shutil.move(source_file, destination_file)