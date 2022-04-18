import os
import random

files_location = input('Type the files path: ')

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
    os.rename(f'./Test/{file_current_name}', f'./Test/{str(random_number)} {file}')
    non_repeated_list.append(random_number)
