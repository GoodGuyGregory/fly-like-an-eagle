import pyperclip
import os


def getTab(contents):
    i = 0
    indentedTabs = ""
    tabIndex = contents.rfind("\t")
    while i <= tabIndex:
        indentedTabs += "\t"
        i += 1
    return indentedTabs

def parseValidation():
    # open the html file from the absolute path
    htmlFilePath = pyperclip.paste()
    os.chdir(os.path.dirname(htmlFilePath))
    htmlFile = open(htmlFilePath, "r+")
    newDirectiveFile = open("directiveVersion.html","w")

    # parse all lines for the "matInput" string
    contents = htmlFile.readlines()

    for i in range(len(contents)):
        if "matInput" in contents[i]:
            ngModelIndex = contents[i].find("[(ngModel)]=")
            if (ngModelIndex > 0):
                tabIndex = getTab(contents[i])
                startSlice = contents[i][ngModelIndex+13:]
                # [(ngModel)]=<slice starts here...>"<what we need>"
                endSliceIndex = startSlice.find('"')
                # get the second value of the split command...
                ngModelReference = startSlice[:endSliceIndex].split(".")[1]
                ngModelVariable = ngModelReference + "NgModel";
                ngModelReference = " #" + ngModelVariable + "=\"ngModel\"" + " appInputTextValidator "
                # print(ngModelReference)
                insertionIndex = contents[i].find(">")
                
                contents[i] = contents[i][:insertionIndex] + ngModelReference + contents[i][insertionIndex:] + tabIndex + "<mat-error class=\"error\" *ngIf=" + ngModelVariable + ".errors?.invalidInput\">" + " Input contains EDI characters. Please do not use *,$,',\", or ~ </mat-error>\n"
                
                newDirectiveFile.writelines(contents[i])
                # add the ngModel name from the final part of the items in the "ngModel" section
        else:
            newDirectiveFile.writelines(contents[i])
                # add the class name for css styling
    htmlFile.close()
    newDirectiveFile.close()
        
        
def main():
    parseValidation()
    

main()