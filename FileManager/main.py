import os, shutil

#Move functions
path = "/Users/nikitamozharovskii/Desktop/FINKA/CodePract/FileManager/Wdir"
def cr_dir():
    print("Type in way to directory:")
    folder_name = input()
    os.mkdir(path + folder_name)
def del_df():
    print("Remove dir/file?")
    choice = input()
    if choice == "dir":
        print("Type in way to directory:")
        folder_name = input()
        if len(os.listdir(path + folder_name)) == 0:
            os.rmdir(path + folder_name)
        else:
            shutil.rmtree(path + folder_name)
    else:
        print("Type in way to file:")
        file_name = input()
        os.remove(path + file_name)
def cr_file():
    print("Type in way to file:")
    file_name = input()
    open(path + file_name, "a+")
def wr_file():
    print("Type in way to file:")
    file_name = path + input()
    print("Type your text:")
    txt = input()
    file = open(file_name, "a+")
    file.write(txt)
    file.close()
def name_df():
    print("Type in way to file/directory:")
    old_name = path + input()
    print("Type in new way to file/directory:")
    new_name = path + input()
    os.rename(old_name, new_name)
def view():
    print("Type in way to file:")
    file_name = path + input()
    file = open(file_name)
    for line in file.readlines():
        print(line)
def place_df():
    print("Type in way to file/directory:")
    start_way = path + input()
    print("Type in new way to file/directory:")
    end_way = path + input()
    os.replace(start_way, end_way)
def copy_df():
    print("Type in way to file/directory:")
    start_way = path + input()
    #print("If you want to copy file/directory into your working directory,\n "
          #"leave the field EMPTY.")
    print()
    print("Type in new way to file/directory:")
    end_way = path + input()
    shutil.copy(start_way, end_way)

#Users's instructions
print()
print("INSTRUCTIONS:")
print("You are able to work only in your working directory 'FMTest'.")
print("Pleace type in way to file/directory begining from your working directory.")
print("The way should start with '/'.")


#User's menu
while True:

    print()
    print("MENU:")
    print("1 - Create directory\n"
          "2 - Create file\n"
          "3 - Delete directory/file\n"
          "4 - Write into the file\n"
          "5 - Print the file\n"
          "6 - Rename directory/file\n"
          "7 - Replace directory/file\n"
          "8 - Copy directory/file\n"
          "9 - Finish file manager")
    print()
    print("Type in your move:")
    move=int(input())

    if move == 1:
        cr_dir()
    if move == 2:
        cr_file()
    if move == 3:
        del_df()
    if move == 4:
        wr_file()
    if move == 5:
        view()
    if move == 6:
        name_df()
    if move == 7:
        place_df()
    if move == 8:
        copy_df()
    if move ==9:
        break