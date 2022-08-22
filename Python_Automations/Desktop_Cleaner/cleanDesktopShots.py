import os


def deleteUnwantedScreenshots():
    os.chdir("C:\\Users\\058620\\Desktop")

    deletedFiles = []

    for files in os.walk(os.getcwd()):

        for filenames in files:
            for file in filenames:
                if '.png' in file:
                    deletedFiles.append(file)

    print('found ' + str(len(deletedFiles)) + ' file(s)')
    print()
    response = input('Do you want to delete them? [Y/n] ')
    if response.lower() == 'y':
        for file in deletedFiles:
            print('deleted ' + file)
            os.unlink(file)
    else:
        print()
        print('keeping these files')


def main():
    deleteUnwantedScreenshots()


main()
