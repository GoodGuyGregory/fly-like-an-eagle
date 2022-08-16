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
                javaFields[variableList[1]].append(
                    str(variableList[2]).split(";")[0])
            else:
                javaFields[variableList[1]] = [
                    str(variableList[2].split(";")[0])]

    print(javaFields)

    # create the new file with the values from the dictionary

    javaScriptfile = open(tsfileName, "w")
    classHeader = tsfileName.split(".")
    javaScriptfile.write("export public " + classHeader[0] + "{\n")

    # declare all variables from the dictionary to ts:
    for dataType in javaFields.keys():
        if dataType == 'String':
            for i in javaFields[dataType]:
                tsAttribute = "public" + " " + i + ":" + " " + dataType.lower() + ";\n"
                javaScriptfile.write(tsAttribute)
        if dataType == 'Long' or dataType == 'Integer' or dataType == 'Double':
            for i in javaFields[dataType]:
                tsAttribute = "public" + " " + i + ":" + " " + "number;\n"
                javaScriptfile.write(tsAttribute)
        if dataType == 'Date':
            for i in javaFields[dataType]:
                tsAttribute = "public" + " " + i + ":" + " " + dataType + ";\n"
                javaScriptfile.write(tsAttribute)

    javaScriptfile.write("}")
    javaScriptfile.close()


main()
