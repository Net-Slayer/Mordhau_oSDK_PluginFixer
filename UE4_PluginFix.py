import os
import re
import sys

directory = os.getcwd()

print("Script is in " + directory)
checkpath = r"Mordhau_Recap\Plugins"

# Are we in the correct folder
if directory.endswith(checkpath):
    print("Script is in correct location!\n")
else:
    sys.exit(
        "incorrect location for this script, please move to MORDHAUEditor\Mordhau_Recap\Plugins")

# Does the engine file exist
enginePath = directory.replace(
    checkpath, r"InstalledBuild\Windows\Engine\Binaries\Win64\UE4Editor.modules")
if os.path.isfile(enginePath):
    print("Engine file found at :\n" + enginePath + "\n")
else:
    sys.exit(
        "Engine modules path invalid \n File not found at : " + enginePath)

# Grab ID from engine file
EngineBuildID = ""

reID = "\"BuildId\": \"(.*)\""
engineFile = open(enginePath, 'r')
Lines1 = engineFile.readlines()
for line in Lines1:
    out = line.strip()
    x = re.search(reID, out)
    if x:
        EngineBuildID = x.group(1)
        print("Line found:")
        print("Extracted ENGINE build ID: " + EngineBuildID)
engineFile.close()

# Did we grab the ID from the file?
if EngineBuildID == "":
    sys.exit(
        "BuildId could not be found in engine path")
subfolders = [name for name in os.listdir(".") if os.path.isdir(name)]


# for every folder in plugins look for a module file
modulesFile = ""

flagCounter = 0
for folder in subfolders:
    modulesFile = directory + '\\' + folder + \
        "\\Binaries\\Win64\\UE4Editor.modules"
    print("Checking : " + modulesFile)
    # and if the file is there
    if os.path.isfile(modulesFile):
        print("File Path is valid")
        editFile = open(modulesFile)
        modifiedLine = ""
        flagFile = False
        prepNewFile = []
        for line in editFile:
            out = line.strip()
            x = re.search(reID, out)
            if x:
                print("Line found:")
                print(out)
                print("Replacing build ID...")
                modifiedLine = re.sub(
                    reID, "\"BuildId\": \"" + EngineBuildID + "\"", out)
                print(modifiedLine)
                flagFile = True
                flagCounter += 1
                prepNewFile.append(modifiedLine)
            else:
                prepNewFile.append(out)
        if flagFile:
            editFile.close()
            editFile = open(modulesFile, "w")
            for item in prepNewFile:
                editFile.write(item + "\n")
            editFile.close()
    else:
        print("invalid file path")

print("Process Complete! Files processed: " + str(flagCounter))
