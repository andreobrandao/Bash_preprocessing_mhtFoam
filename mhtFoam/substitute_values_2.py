import re
import json

def changeFileDict(dict1):
    for file in dict1.keys():
        with open(file,"r") as f:
            entrie=f.read()
        f.close()
        #print(entrie)
        dfile = dict1[file]
        for entrie_line in dfile:
            #print(entrie_line)
            for key in entrie_line:
                    exp = entrie_line[key]["exp"]
                    value = entrie_line[key]["value"]
                    #print(entrie_line)
                    #print(key)
                    #print(entrie_line[key]["exp"])
                    #print(entrie_line[key]["value"])
                    entrie = re.sub(rf'{exp}', str(value), entrie)
        with open(file,"w") as f:
            f.write(entrie)
        f.close()

def changeFileDict_2(tumor_dict):
    input_file = "./0/ID"
    i=0
    with open(input_file, "r") as file:
        lines = file.readlines()
    tumor_data_lines = []
    tumor_data_lines_2=[]
    for tumor_data in tumor_dict.values():
        print(tumor_data)
        i=i+1
        tumor_data_lines.append(f"        //Tumor_{i}\n")
        for param in tumor_data["./0/ID"]:
            for key, value in param.items():
                scalar_name = key
                scalar_value = value["value"]
                #file.write(f"scalar {scalar_name} = {scalar_value};\n")
                tumor_data_lines.append(f"        scalar {scalar_name} = {scalar_value};\n")
       #file.write("\n")  # Linha em branco entre tumores
       
        tumor_data_lines.append(f"        scalar inclination_rad_{i} = inclination_{i} * pi / 180.0;\n")
        tumor_data_lines.append(f"        scalar be_{i} = radius_{i}*pow((1-pow(eccen_{i},2)),0.25);\n")
        tumor_data_lines.append(f"        scalar ae_{i} = pow(pow(be_{i},2)*(pow(1-pow(eccen_{i},2),-1)),0.5);\n")
        tumor_data_lines.append("\n")
            
        tumor_data_lines_2.append(f"        scalar y_rot_{i} = (y-posy_{i})*cos(inclination_rad_{i})-(x-posx_{i})* sin(inclination_rad_{i});\n")
        tumor_data_lines_2.append(f"        scalar x_rot_{i} = (y-posy_{i})*sin(inclination_rad_{i})+(x-posx_{i})* cos(inclination_rad_{i});\n")
        tumor_data_lines_2.append(f"                if (pow(y-posy_{i},2) <= pow(radius_{i},2)-pow(x-posx_{i},2))\n")
        tumor_data_lines_2.append("                {\n")
        tumor_data_lines_2.append("                        ID[i] = 1.;\n")
        tumor_data_lines_2.append("                }\n")
        tumor_data_lines_2.append("\n")
        
    insertion_line = 47
    insertion_line_2=insertion_line+(i*10+8)
    lines[insertion_line:insertion_line] = tumor_data_lines
    lines[insertion_line_2:insertion_line_2] = tumor_data_lines_2
    
    
    with open(input_file, "w") as file:
        file.writelines(lines)

def generate_dictionary_1(data,dir="."): 
    #print(data["endtime"])
    dict1 = {
        f"{dir}/system/controlDict":
         [
            {"endtime":{"exp":"{endtime}","value":data["endtime"]}},
            #{"endTime":{"exp":"\s+[0-9]+","value":tf}}
            {"timestep":{"exp":"{timestep}","value":data["timestep"]}}
         ]
         
    } 
    return dict1
    
def generate_dictionary_2(data,dir="."):
    dict1 = {
        f"{dir}/system/blockMeshDict":
         [
             {"xmax":{"exp":"{xmax}","value":data["xmax"]}},
             {"ymax":{"exp":"{ymax}","value":data["ymax"]}},
             {"zmax":{"exp":"{zmax}","value":data["zmax"]}},
             {"xnode":{"exp":"{xnode}","value":data["xnode"]}},
             {"ynode":{"exp":"{ynode}","value":data["ynode"]}},
             {"znode":{"exp":"{znode}","value":data["znode"]}}
        ]
    }
    return dict1

def generate_dictionary_3(data,indexx,dir="."):
    #print(index)
    tumor_dict = {}
    for i in range(1, indexx+1):  # Certifique-se de iterar até indexx inclusive
        tumor_dict[f"dict{i}"] = {
            f"{dir}/0/ID": [
                {f"radius_{i}": {"exp": "{radius}", "value": data["tumors"][i-1][f"radius_{i}"]}},
                {f"eccen_{i}": {"exp": "{eccen}", "value": data["tumors"][i-1][f"eccen_{i}"]}},
                {f"posx_{i}": {"exp": "{posx}", "value": data["tumors"][i-1][f"posx_{i}"]}},
                {f"posy_{i}": {"exp": "{posy}", "value": data["tumors"][i-1][f"posy_{i}"]}},
                {f"inclination_{i}": {"exp": "{inclination}", "value": data["tumors"][i-1][f"inclination_{i}"]}},
            ]
        }
    #print(tumor_dict)
    return tumor_dict
    #print(data)
    #dict1 = {
     #   f"{dir}/0/ID":
      #  [
       #      {"radius":{"exp":"{radius}","value":data["tumors"][index][f"radius_{indexx}"]}},
        #     {"eccen":{"exp":"{eccen}","value":data["tumors"][index][f"eccen_{indexx}"]}},
         #    {"posx":{"exp":"{posx}","value":data["tumors"][index][f"posx_{indexx}"]}},
         #    {"posy":{"exp":"{posy}","value":data["tumors"][index][f"posy_{indexx}"]}},
         #    {"inclination":{"exp":"{inclination}","value":data["tumors"][index][f"inclination_{indexx}"]}}
        #]
    #}
    print(tumor_dict)
    
    
#changeFileDict(dict1)
