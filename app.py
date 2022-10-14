import os
import random

def randomize_file_names_order():
    files_location = input('Type the files path: ')

    files_location = check_back_slash_in_folder_path(files_location)

    files_list = os.listdir(files_location)

    non_repeated_list = list()

    for file in files_list:
        random_number = random.randint(1,len(files_list))
        while random_number in non_repeated_list:
            random_number = random.randint(1,len(files_list))
        file_current_name = file
        while file[0].isdigit():
            file = file[1:]
            file = file.strip()
        os.rename(files_location + file_current_name, files_location + str(random_number) + " " + file)
        non_repeated_list.append(random_number)


def check_back_slash_in_folder_path(folder_path):
    if not folder_path.endswith('\\'):
        folder_path = folder_path + '\\'
        return folder_path
    else:
        return folder_path
        
        
randomize_file_names_order()