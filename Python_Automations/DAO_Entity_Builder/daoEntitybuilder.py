# this program reads a java hibernate entity and parses it into a typescript DAO Model
#  provide the location of the java entity and the desired location for the corresponding ts model
import os
import pyperclip


def main():
    print('DAO Entity Builder:')
    javaEntityPath = pyperclip.paste()

    # Strip class name for new Ts file:
    # ==========================================
    #  remove all path params
    filePath = javaEntityPath.split('\\')
    tsfileName = filePath[len(filePath)-1]

    startOfClass = javaEntityPath.find(tsfileName.strip())
    #  strip the tail off of the abs path for directory change and reading of file
    workingDir = javaEntityPath[:startOfClass]
    os.chdir(workingDir)
    # renames new file with typescript extenstion
    tsfileName = tsfileName.strip("java") + "ts"
    # print(os.getcwd())
    javaFilename = javaEntityPath[startOfClass:]
    print("opening: " + javaFilename)
    javafile = open(javaFilename, "r")
    #  gets all of the files contents:
    contents = javafile.readlines()

    javaFields = dict()
    for i in range(len(contents)):
        if "private" in contents[i]:
            variableList = contents[i].split()
            # data types are not in the dictionary:
            if variableList[1] in javaFields.keys():
                #  add them to the running list
                javaFields[variableList[1]].append(variableList[2])
            else:
                javaFields[variableList[1]] = [variableList[2]]

    print(javaFields)

    # create the new file with the values from the dictionary
    # jsFilename = filename.split(".")
    # javaScriptfile = open()


main()
