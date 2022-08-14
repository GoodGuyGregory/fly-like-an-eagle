# this program reads a java hibernate entity and parses it into a typescript DAO Model
#  provide the location of the java entity and the desired location for the corresponding ts model
import os
import pyperclip


def main():
    print('DAO Entity Builder:')
    javaEntityPath = pyperclip.paste()

    JavaClassName = input('Enter the name of the Entity: ')

    startOfClass = javaEntityPath.find(JavaClassName.strip())
    #  strip the tail off of the abs path for directory change and reading of file
    workingDir = javaEntityPath[:startOfClass]
    os.chdir(workingDir)
    # print(os.getcwd())
    filename = javaEntityPath[startOfClass:]
    print("opening: " + filename)
    javafile = open(filename, "r")
    #  gets all of the files contents:
    contents = javafile.readlines()

    javaFields = {}
    for i in range(len(contents)):
        if "private" in contents[i]:
            variableList = contents[i].split()
            # data types are not in the dictionary:
            if variableList[1] not in javaFields.keys():
                #  add them
                javaFields[variableList[1]] = variableList[2]
            else:
                javaFields[variableList[1]] = variableList[2]
    print(javaFields)

    # create the new file with the values from the dictionary
    jsFilename = filename.split(".")

    javaScriptfile = open()


main()
