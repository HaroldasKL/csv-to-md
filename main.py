import csv
import os
from datetime import datetime, timedelta
from sys import exit


def search_for_file() -> str:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = None
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(".csv"):
                file_name = file
                return file_name

    if file_name is None:
        print("File was not found!")
        print("Are you sure you put it in the same directory as the program / source code is?")
        exit()


FILE_NAME = search_for_file()


def read_csv_file() -> list[list[str]] | list[str]:
    rows = []
    with open(FILE_NAME, 'r') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            rows.append(row)

    return rows


def get_current_week() -> str:  # Gets current week out of the file name
    week_start_date = list(FILE_NAME)[24:29]
    week_start_date = week_start_date[0] + week_start_date[1] + week_start_date[2] + week_start_date[3] + week_start_date[4]

    week_end_date = list(FILE_NAME)[38:43]
    week_end_date = week_end_date[0] + week_end_date[1] + week_end_date[2] + week_end_date[3] + week_end_date[4]

    week = week_start_date + "  -  " + week_end_date
    return week


def get_week_number() -> str:
    starting_date_of_the_PBL = "2022-09-05"
    list_of_current_date_characters = list(FILE_NAME)[19:29]
    current_date = ""

    for i in range(0, len(list_of_current_date_characters)):
        current_date += (list_of_current_date_characters[i])

    full_starting_date = datetime.strptime(starting_date_of_the_PBL, "%Y-%m-%d")
    full_current_date = datetime.strptime(current_date, "%Y-%m-%d")

    current_week_number = ((full_current_date - full_starting_date).days // 7) + 1

    return str(current_week_number)


def calculate_total_duration() -> str:
    list_of_durations = []

    for i in range(len(read_csv_file())):
        list_of_durations.append(read_csv_file()[i][11])
        total_duration = timedelta()

        for duration in list_of_durations:
            (h, m, s) = duration.split(':')
            time = timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            total_duration += time

    return str(total_duration)


def create_md_file() -> None:
    user_name = read_csv_file()[0][0]
    length_of_file = len(read_csv_file())

    with open("output_data.md", "w") as file:
        file.write("# Activity of:\n" + "> " + user_name + "\n")
        file.write("\n## Week " + get_week_number() + " (" + get_current_week() + ")\n")
        file.write("| **Date**  | **Time**      | **Duration**  | **Activity** |\n")
        file.write("| --------  | ------------- | ------------  | ------------ |\n")

        list_of_j_indexes = []
        for i in range(length_of_file):
            start_date = read_csv_file()[i][7][5:]
            start_time = read_csv_file()[i][8][:5]
            end_time = read_csv_file()[i][10][:5]
            duration = read_csv_file()[i][11]
            description = read_csv_file()[i][5]

            for j in range(i + 1, length_of_file):
                if read_csv_file()[i][7][5:] == read_csv_file()[j][7][5:]:
                    list_of_j_indexes.append(j)
                break

            if i in list_of_j_indexes:
                file.write("| " + " | " + str(read_csv_file()[i][8])[:5] + " - " + str(read_csv_file()[i][10])[:5] + " | " + str(
                    read_csv_file()[i][11]) + " | " + str(read_csv_file()[i][5]) + " |\n")
            else:
                file.write("| " + start_date + " | " + start_time + " - " + end_time + " | " + duration + " | " + description + " |\n")
        file.write("|  | **Total:** | **" + calculate_total_duration() + "** | |")
        print(".md file was created successfully!")


search_for_file()
create_md_file()
