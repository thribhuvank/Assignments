"""
Create a Multilevel dictionary by reading the provided logfile (PFA) and output the dictionary as 
{"Pattern1":{"line1":"Services","line2":"0001","line3":{"include":"BFE"},"line4":{"Include":"1*1"},
"line5":"0","line7":{"Include":"2*2"},"line8":{"services":["stop","pause","delete","startup"]}},
 "Pattern2":{"line1":"Registry"......}, "Pattern3":{"line1":"Files"......} }
"""

import json
from helper import *

# Reading data from log file
raw_data = read_log_file('./logfile')

# Converting into json string format
json_data = json.dumps(raw_data)

# declaring required data types
pattern1_dict = {}
pattern2_dict = {}
pattern3_dict = {}
dict_output = {}
pattern1_data = []
pattern2_data = []
pattern3_data = []
patterns_list = []

# formating patterns 
json_data = json_data.strip('"')
json_data = json_data.replace('Pattern1 ', 'Pattern1 |')
json_data = json_data.replace('Pattern2 ', ', Pattern2 |')
json_data = json_data.replace('Pattern3 ', ', Pattern3 |').strip('\\n')

# exactrating patterns into separate lists
pattern_split = json_data.split(',')
for pattern in pattern_split:
    new_patterns = pattern.split('|')
    if "Pattern1" in new_patterns[0]:
        patterns_list.append(new_patterns[0].strip(' '))
        pattern1_data = new_patterns
        
    elif "Pattern2" in new_patterns[0]:
        patterns_list.append(new_patterns[0].strip(' '))
        pattern2_data = new_patterns

    elif "Pattern3" in new_patterns[0]:
        patterns_list.append(new_patterns[0].strip(' '))
        pattern3_data = new_patterns
    
    else:
        print("Unknown Patterns")


for pattern in patterns_list:
    # parsing pattern
    if pattern == 'Pattern1':
        pattern1_data_format = pattern1_data[1].replace('\\n', '')
        pattern1_data_format = pattern1_data_format.strip('}')
        pattern1_data_format = pattern1_data_format.strip('{')
        pattern1_data_format = pattern1_data_format.strip(' ')
        pattern1_data_format = pattern1_data_format.replace('Include -e', 'include')
        pattern1_data_format = pattern1_data_format.replace('\"', '')
        pattern1_data_format = pattern1_data_format.replace('\\', '')
        pattern1_data_format = pattern1_data_format.replace('-', '')
        pattern1_data_format = pattern1_data_format.replace('d c ', '')

        pattern1_data_format_split = pattern1_data_format.split('  ')
        # parsing patterns based on lines
        for item in pattern1_data_format_split:
            line_items = item.strip(' ')
            if "line1" in line_items:
                add_single_keypairs(line_items, pattern1_dict)
        
            elif "line2" in line_items:
                add_single_keypairs(line_items, pattern1_dict)
                
            elif "line3" in line_items:
                add_single_dict_3_4(line_items, pattern1_dict)
            
            elif "line4" in line_items:
                add_single_dict_3_4(line_items, pattern1_dict)
            
            elif "line5" in line_items:
                add_single_keypairs(line_items, pattern1_dict)
            
            elif "line6" in line_items:
                add_single_dict(line_items, pattern1_dict)
            
            elif "line7" in line_items:
                add_single_dict(line_items, pattern1_dict)
            
            elif "line8" in line_items:
                patter1_line8 = line_items
                patter1_line8_splitted = patter1_line8.split(' ')
                services_list = []
                services_list_dict = {}
                for i in patter1_line8_splitted:
                    services = i.split(':')
                    if "services" in services:
                        services_list.append(services[1])
                        
                services_list_dict["services]"] = services_list
                pattern1_dict[patter1_line8_splitted[0]] = services_list_dict
            
            else:
                print("Line not available")

    
    elif pattern == 'Pattern2':
        # parsing pattern
        pattern2_data_format = pattern2_data[1].replace('\\n', '')
        pattern2_data_format = pattern2_data_format.strip('}')
        pattern2_data_format = pattern2_data_format.strip('{')
        pattern2_data_format = pattern2_data_format.strip('\\t')
        pattern2_data_format = pattern2_data_format.replace('\\tl', ',l')
        pattern2_data_format = pattern2_data_format.replace('\\"', '')
        pattern2_data_format = pattern2_data_format.replace(' Include -e', 'include ')
        pattern2_data_format_split = pattern2_data_format.split(',')
        
        for item in pattern2_data_format_split:
            # parsing patterns based on lines
            line_items = item.strip(' ')
            if "line1" in line_items:
                add_single_keypairs(line_items, pattern2_dict)
        
            elif "line2" in line_items:
                add_single_keypairs(line_items, pattern2_dict)
            
            elif "line3" in line_items:
                add_single_keypairs(line_items, pattern2_dict)
            
            elif "line4" in line_items:
                patter2_line4 = line_items
                patter2_line2_splitted = patter2_line4.split(' ')
                line4_include = patter2_line2_splitted[2].strip('\\t')
                line4_include = line4_include.replace('\\\\', ' ')
                line4_include = line4_include.replace(' *  I', ' ')
                line4 = line4_include.split(' ')
                line4_list = []
                for i in line4:
                    if i != '':
                        line4_list.append(i)
                pattern2_dict[patter2_line2_splitted[0]] = line4_list


            
            elif "line5" in line_items:
                add_single_dict_5_6(line_items, pattern2_dict)
            
            elif "line6" in line_items:
                add_single_dict_5_6(line_items, pattern2_dict)
            
            elif "line7" in line_items:
                add_single_dict_5_6(line_items, pattern2_dict)
                    
            elif "line8" in line_items:
                patter2_line8 = line_items
                
                patter2_line8 = patter2_line8.replace('{ ','{')
                patter2_line8 = patter2_line8.replace(' }','}')
                patter2_line8 = patter2_line8.replace('-', '')
                patter2_line8 = patter2_line8.replace('c d ', '')
                registry_data = patter2_line8.split(' ')
                registry = []
                line8 = {}
                for i in registry_data:
                    if "registry" in i:
                        reg = i.split(':')
                        registry.append(reg[1])

                line8['registry']=registry
                pattern2_dict[registry_data[0]] = line8
            
            else:
                print("Line not available")

    
    elif pattern == 'Pattern3':
        # parsing pattern
        pattern3_data_format = pattern3_data[1].replace('\\n', '')
        pattern3_data_format = pattern3_data_format.strip('{\\t')
        pattern3_data_format = pattern3_data_format.strip('}')
        pattern3_data_format = pattern3_data_format.replace('\\t', ',')
        pattern3_data_format = pattern3_data_format.replace('$n ', '')
        pattern3_data_format = pattern3_data_format.replace('\\"', '')
        pattern3_data_format = pattern3_data_format.replace('$', '')
        pattern3_data_format = pattern3_data_format.replace('\\\\', '')

        pattern3_data_format_split = pattern3_data_format.split(',')
        for item in pattern3_data_format_split:
            # parsing patterns based on lines
            line_items = item.strip(' ')
            if "line1" in line_items:
                add_single_keypairs(line_items, pattern3_dict)
        
            elif "line2" in line_items:
                add_single_keypairs(line_items, pattern3_dict)

            elif "line3" in line_items:
                add_single_keypairs(line_items, pattern3_dict)
            
            elif "line4" in line_items:
                patter3_line4 = line_items
                patter3_line4 = patter3_line4.replace('{ ', '')
                patter3_line4 = patter3_line4.replace(' }', '')
                patter3_line4_splitted = patter3_line4.split(' ')
                line4 = {}
                line4[patter3_line4_splitted[1]] = patter3_line4_splitted[2]
                pattern3_dict[patter3_line4_splitted[0]] = line4

            elif "line5" in line_items:
                patter3_line5 = line_items
                patter3_line5 = patter3_line5.replace('{ ', '')
                patter3_line5 = patter3_line5.replace('}', '')
                patter3_line5 = patter3_line5.replace('NT ', 'NT-')
                patter3_line5_splitted = patter3_line5.split(' ')
                line_exclude = []
                line_exclude_dict = {}
                for i in range(2, len(patter3_line5_splitted)):
                    line_exclude.append(patter3_line5_splitted[i])

                line_exclude_dict[patter3_line5_splitted[1]] = line_exclude
                pattern3_dict[patter3_line5_splitted[0]] = line_exclude_dict
            
            elif "line6" in line_items:
                add_single_dict_2(line_items, pattern3_dict)

            elif "line7" in line_items:
                add_single_dict_2(line_items, pattern3_dict)
                
            elif "line8" in line_items:
                patter3_line8 = line_items
                patter3_line8_splitted = patter3_line8.split(' ')
                files_list = []
                line_exclude_dict = {}
                for i in patter3_line8_splitted:
                    if i != "line8":
                        files = i.split(':')
                        files_list.append(files[-1])
                
                line_exclude_dict['files'] = files_list
                pattern3_dict[patter3_line8_splitted[0]] = line_exclude_dict
            
            else:
                print("Line not available")
    
    else:
        print("pattern not available")


# adding formatted patterns into output dictionary 
dict_output['Pattern1'] = pattern1_dict
dict_output['Pattern2'] = pattern2_dict
dict_output['Pattern3'] = pattern3_dict

json_dict = json.dumps(dict_output)
print(json_dict)