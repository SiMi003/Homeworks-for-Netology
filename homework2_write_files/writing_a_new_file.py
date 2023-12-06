# function for calculate numbers of lines in a file 
def calculate_lines(file_name):
    count = 0
    line = 0
    with open(file_name, 'r', encoding='UTF-8') as file:
        while line != '':
            line = file.readline()
            count += 1
    return count-1

# The function returns a list of line numbers in each file from imput list of files           
def all_lines_list(files_list):
    line_numbers = []
    for file in files_list:
         line_numbers.append(calculate_lines(file))
    print(line_numbers)
    return line_numbers

def writing_new_file(files_list):
    lines = all_lines_list(files_list)
    while lines != []:
        ind = lines.index(min(lines))
        file_name = files_list[ind]
        print(file_name)
        with open(file_name, 'r', encoding='UTF-8') as f:
            reading = f.read()
            with open('new file.txt', 'a', encoding='UTF-8') as ff:
                ff.write(file_name + '\n' + str(lines[ind]) + '\n' + reading)
        lines.pop(ind)
        files_list.pop(ind)

# The list of input files
files_list = ['the first file.txt', 'the second file.txt', 
              'the third file.txt', 'the fourth file.txt']    

writing_new_file(files_list)   
        
    
    
