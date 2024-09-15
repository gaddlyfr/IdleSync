import os, json
from datetime import datetime, timedelta

paths_folder = []
apps_folder = {}

path_to_sync = []


def add_to_path_folder():
    path = input("atpf> ")
    while True:
        if os.path.exists(path): 
            paths_folder.append(path)
            os.system('cls')
            print("Succesfully added")
            break
        elif path.casefold() == "cancel":
            break
        else:
            error()
            path = input("atpf> ")
def change_path_folder():
    path = input("cpfn> ")
    path_to_remove = input("cpfr> ")
    while True:
        if os.path.exists(path) and path_to_remove in paths_folder: 
            paths_folder.append(path) 
            paths_folder.remove(path_to_remove)
            if path_to_remove in apps_folder:
                apps_folder.pop(path)
            os.system('cls')
            print("Succesfully changed")
            break
        elif path.casefold() == "cancel" or path_to_remove.casefold() == "cancel":
            break
        else:
            error()
            path = input("cpfn> ")
            path_to_remove = input("cpfr> ")
def remove_from_path_folder():
    path = input("rfpf> ")
    while True:
        if path in paths_folder: 
            paths_folder.remove(path)
            if path in apps_folder:
                apps_folder.pop(path)
            os.system('cls')
            print("Succesfully deleted")
            break
        elif path.casefold() == "cancel":
            break
        else:
            error()
            path = input("rfpf> ")
def add_apps():
    choice = {}
    choiceFolder = ""
    choiceApps = {}
    apps = []

    for i in range(len(paths_folder)):
        print(f"{i}: {paths_folder[i]}")
        choice[i] = paths_folder[i]

    prompt = ""
    choiceFolder = input("Folder > ") 
    if int(choiceFolder) in choice:
        subfolders = [i for i in os.listdir(paths_folder[int(choiceFolder)])]
        while True:
            try:
                for i in range(len(subfolders)):
                    print(f"{i}: {subfolders[i]}")
                    choiceApps[i] = subfolders[i]
                prompt = input("> ")
                if prompt.casefold() == "cancel": 
                    apps_folder[choice.get(int(choiceFolder))] = apps
                    break
                if int(prompt) in choiceApps:
                    apps.append(choiceApps[int(prompt)])
                    os.system('cls')
                    print("Succesfully added")
            except:
                error()
def remove_apps():
    prompt = ""
    choiceApps = {}
    choiceFolder = {}

    for i in range(len(paths_folder)):
        print(f"{i}: {paths_folder[i]}" )
        choiceFolder[i] = paths_folder[i]
    

    path = int(input("> ")) # 0 -> c:/
    
    if path in choiceFolder:
        path = choiceFolder[path]
        while True:
            try:
                for i in range(len(apps_folder[path])):
                    print(f"{i}: {apps_folder[path][i]}")
                    choiceApps[i] = apps_folder[path][i]
                prompt = input("> ")
                if prompt.casefold() == "cancel": break
                if int(prompt) in choiceApps:
                    apps_folder[path].pop(int(prompt))
                    os.system('cls')
                    print(f"Succesfully deleted")
            except:
                error()
def print_apps():
    for i in apps_folder:
        for j in apps_folder.get(i):
            print(f"{i} : {j}")
def error(): 
    os.system('cls')
    print("error unknown")

def save_to_file():
    try:
        with open("data.dat", "w") as file:
            json.dump({"paths_folder": paths_folder, "apps_folder": apps_folder}, file)
    except:
        error()
def read_file():
    global paths_folder
    global apps_folder
    try:
        with open("data.dat", "r") as file:
            data = json.load(file)

            paths_folder = data["paths_folder"]
            apps_folder = data["apps_folder"]
    except:
        os.system("cls")
        print("Error with loading data from file")

def get_a_time():
    for i in apps_folder:
        for j in apps_folder[i]:
            # construct path
            if "/" in i:
                path = f"{i}{j}"
                data = os.path.getmtime(path)
            else:
                path = f"{i}/{j}"
                data = os.path.getmtime(path)

            data = datetime.fromtimestamp(data)
            time = datetime.now()

            if (time - data) >= timedelta(days=1):
                path_to_sync.append(path)
    print(path_to_sync)
            


read_file()
get_a_time()
while True:
    try:
        prompt = input("> ").casefold().split()
        if prompt[0] == "atpf": add_to_path_folder()
        elif prompt[0] == "cpf": change_path_folder()
        elif prompt[0] == "rfpf": remove_from_path_folder()
        elif prompt[0] == "aap": add_apps()
        elif prompt[0] == "rap": remove_apps()
        elif prompt[0] == "pap": print_apps()
        elif prompt[0] == "cls" or prompt[0] == "clear": os.system('cls')
        else:
            print("Unknown Command")
        save_to_file()
    except:
        error()