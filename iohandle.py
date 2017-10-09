import os


def regularizeData(ratio):
    recoard = str(ratio[0]) + '|' + str(ratio[1])
    return recoard


def readFile():
    cupath = os.getcwd()
    fpath = cupath + '/recoard.txt'
    if os.path.exists(fpath):
        f = open(fpath)
        content = f.read()
        f.close()

        return content
    else:
        f = open(fpath, 'w')
        f.close()
        return 0


def writeFile(content):
    cupath = os.getcwd()
    fpath = cupath + '/recoard.txt'
    f = open(fpath, 'w')
    f.write(content)
    f.close()
