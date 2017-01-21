import os, re


def getfiles(dirpath):
    a = [os.path.join(dirpath, s) for s in os.listdir(dirpath)
         if os.path.isfile(os.path.join(dirpath, s))]
    a.sort()
    return a

def main():
        rootdir = 'pictures/chilling'
        for f in getfiles(rootdir):
            print (f)

if __name__ == '__main__':
        main()
