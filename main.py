import os

paths_folder = []
apps_folder = {}

def add_to_path_folder(path):
    if os.path.exists(path): paths_folder.append(path)

def change_path_folder(path, path_to_remove):
    if os.path.exists(path) and path_to_remove in paths_folder: 
        paths_folder.append(path) 
        paths_folder.remove(path_to_remove)

def remove_from_path_folder(path):
    if path in paths_folder: paths_folder.remove(path)

def add_apps():
    choice = {}
    choiceFolder = ""
    choiceApps = {}
    apps = []

    for i in range(len(paths_folder)):
        print(f"{i}: {paths_folder[i]}")
        choice[i] = paths_folder[i]

    prompt = ""
    try:
        choiceFolder = input("Folder > ") 
        if int(choiceFolder) in choice:
            subfolders = [i for i in os.listdir(paths_folder[int(choiceFolder)])]
            while True:
                for i in range(len(subfolders)):
                    print(f"{i}: {subfolders[i]}")
                    choiceApps[i] = subfolders[i]
                prompt = input("> ")
                if prompt.casefold() == "cancel": 
                    apps_folder[choice.get(int(choiceFolder))] = apps
                    break
                if int(prompt) in choiceApps:
                    apps.append(choiceApps[int(prompt)])
    
    except NameError:
        print(NameError)

    

