import zipfile,os
class what():
    xfuck = 0

def newfilename():
    whatt = what.xfuck
    whatt+=1
    what.xfuck+=1
    whatt = str(whatt)
    whatt+=".zip"
    return (whatt)

def fuck():
    files = os.listdir(os.getcwd())
    x = 0
    for file in files:
        if os.path.isdir(file):
            print (file + "is a directory")
            break
            pass
        else:
            try:
                zipfile.ZipFile(newfilename(),mode='w').write(file)
                print (file)
                os.remove(file)
                x+=1
            except:
                print ("error " + file)
                pass
    fuck()
fuck()
