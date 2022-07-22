# Generic methods declared here

def read_log_file(file_path):
    file = open(file_path, 'r')
    raw_data = file.read()
    return raw_data 

def add_single_keypairs(line_items, pattern_dict):
    line = line_items
    line_splitted = line.split(' ')
    pattern_dict[line_splitted[0]] = line_splitted[1]



def add_single_dict(line_items, pattern_dict):
    line = line_items
    line_splitted = line.split(' ')
    line_dict = {}
    line6_include = line_splitted[1].strip('{')
    line6_include_value = line_splitted[2].strip('}')
    line_dict[line6_include] = line6_include_value
    pattern_dict[line_splitted[0]] = line_dict


def add_single_dict_2(line_items, pattern_dict):
    line = line_items
    line = line.replace('{', '')
    line = line.replace('}', '')
    line_splitted = line.split(' ')
    line_dict = {}
    line_dict[line_splitted[1]] = line_splitted[2]
    pattern_dict[line_splitted[0]] = line_dict
    

def add_single_dict_3_4(line_items, pattern_dict):
    line = line_items
    line_splitted = line.split(' ')
    line_dict = {}
    line3_include = line_splitted[1].strip('{')
    line3_include_value = line_splitted[2].strip('}')
    line_dict[line3_include] = line3_include_value
    pattern_dict[line_splitted[0]] = line_dict


def add_single_dict_5_6(line_items, pattern_dict):
    line = line_items        
    line = line.replace('{ ','{')
    line = line.replace(' }','}')
    line_splitted = line.split(' ')
    line_dict = {}
    line_include = []
    for i in line_splitted:
        i = i.strip('{')
        i = i.strip('}')
        line_include.append(i)
                
    line_dict[line_include[1]]=line_include[2]
    pattern_dict[line_include[0]] = line_dict