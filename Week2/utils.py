import os

def first(path, output_file):
    files = os.listdir(path)
    with open(output_file) as file_object:
        for line in files:
            file_object.write(line + "\n")


def second(path):
    lst = []
    files = os.listdir(path)
    for file in files:
		low_path = os.path.join(path, file)
	    if(os.path.isdir(low_path)):
		    lst.append(file)
            sup_files = os.listdir(low_path)
            for subfile in sub_files
                lst.append(subfile)
        else:
            lst.append(file)

    put = open(inputFile, 'r')
    for file in lst:
        put.write(file + '\n')
    f.close()
    print()


def third(lst):
    for file in lst:
        with open(file) as file_object:
            print(file_object.readlines()[0])

def fourth(lst):
    for file in lst:
        with open(file) as file_object:
            for line in file_object.readlines():
                if '@' in line:
                    print(line)

def fifth(lst, output_file):
    lines = []
    for file in lst:
        with open(file) as file_object:
            for line in file_object.readlines():
                if line[0] == "#":
                    lines_to_output.append(line);
        with open(output_file) as file_object:
            for line in lines_to_output:
                file_object.write(line)