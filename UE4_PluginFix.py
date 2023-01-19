import os
import re
import sys

directory = os.getcwd()
print("NetSlayer's Mordhau plugin fixer v1.2 (19/01/23)")
print("Please ensure this file is run from \"mordhau\Plugins\" folder!")
print("Where this folder contains plugins that are compatible with UE4.26")
print("**********************")

input("Press Enter to continue...")
print("Script is in " + directory)
checkpath = r"mordhau\Plugins"

# Are we in the correct folder
if directory.endswith(checkpath):
    print("Script is in correct location!\n")
else:
    print(
        "incorrect location for this script, please move to MORDHAUEditor\mordhau\Plugins")
    input("Press Enter to exit!")
    sys.exit()


# Does the engine file exist
enginePath = directory.replace(
    checkpath, r"InstalledBuild\Windows\Engine\Binaries\Win64\UE4Editor.modules")
if os.path.isfile(enginePath):
    print("Engine file found at :\n" + enginePath + "\n")
else:
    print("Engine modules path invalid \n File not found at : " + enginePath)
    input("Press Enter to exit!")
    sys.exit()

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
    print(
        "BuildId could not be found in engine path")
    input("Press Enter to exit!")
    sys.exit()
subfolders = [name for name in os.listdir(".") if os.path.isdir(name)]
print("**********************")
print("Beginning fix operations")
print("**********************")
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
        print("Invalid file path, this plugin will not be processed")

print("**********************")
print("Process Complete! Files processed: " + str(flagCounter))
print("**********************")
input("Press Enter to exit!")
