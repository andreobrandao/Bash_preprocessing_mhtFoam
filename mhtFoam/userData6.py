import re
import json

# Print the data
# print(data)

def changeFileDict(dataDict):
    for file in dataDict.keys():
        with open(file,"r") as f:
            entrie=f.read()
        f.close()
        dfile = dataDict[file]
        for prop in dfile:
            for key in prop.keys():
                entrie=re.sub(rf'{key}{prop[key]["exp"]}',f'{key}\t\t{prop[key]["value"]}',entrie)
        with open(file,"w") as f:
            f.write(entrie)
        f.close()

def generate_dictionary(data,dir="."):        
    ## Dict modifications
    dict1 = {f"{dir}/system/controlDict":
            [{"endTime":{"exp":'\s+[0-9]+',"value":data["tf"]}}],
            f"{dir}/constant/blockMeshdict":
            [
                {"xmax":{"exp":r'\s+[0-9]+\.*[0-9]*',"value":data["chi0"]}},
                {"ymax":{"exp":r'\s+[0-9]+\.*[0-9]*e*[+-]*[0-9]*',"value":data["betam"]}},
                {"zmax":{"exp":r'\s+[0-9]+\.*[0-9]*e*[+-]*[0-9]*',"value":data["Hmax"]}},
                {"xnode":{"exp":r'\s+[0-9]+\.*[0-9]*e*[+-]*[0-9]*',"value":data["Hmax"]}},
                {"ynode":{"exp":r'\s+[0-9]+\.*[0-9]*e*[+-]*[0-9]*',"value":data["Hmax"]}},
                {"znode":{"exp":r'\s+[0-9]+\.*[0-9]*e*[+-]*[0-9]*',"value":data["mag_height"]}}
            ]
    }

    return dict1
    
def main(file,dir="."):
    """
    Função principal. Inicializa a aplicação e constrói a interface
    """

    # Open and read the JSON file
    with open(file, 'r') as f:
        data = json.load(f)
    inputDict = generate_dictionary(data,dir=dir)
    changeFileDict(inputDict)

if __name__ == "__main__":
    import argparse
    import os

    parser = argparse.ArgumentParser(description="Python script to modify the setup of fhdFoam")
    parser.add_argument("--file", required=False, type=str, help='Json file with parameters', dest='file', default="./input.json")
    parser.add_argument("--new-case", required=False, type=str, help='Path for the new case', dest='new_case', default=None)
    args = parser.parse_args()
    
    if args.new_case:
        cwd = os.getcwd()
        os.system(f"cp -r {cwd} {args.new_case}")
        os.system(f"cd {args.new_case}")

        main(args.file,dir=args.new_case)
    else:
        main(args.file)

