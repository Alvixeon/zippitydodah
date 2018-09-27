#import necessary things
import zipfile,os
#make a class called what to store this value
class what():
    #this one, for infinite file name generation in the form of ascending numbers
    xfuck = 0
#make new zip file name
def newfilename():
    #declare whatt as what.xfuck value
    whatt = what.xfuck
    #add 1 to it
    whatt+=1
    #add one to the class version
    what.xfuck+=1
    #make it a string
    whatt = str(whatt)
    #add .zip
    whatt+=".zip"
    #return that shit
    return (whatt)

#the fuckening
def fuck():
    #for every file in the scripts ran directory
    files = os.listdir(os.getcwd())
    #for every file in my listdir from before
    for file in files:
        if os.path.isdir(file):
            print (file + "is a directory")
            pass
        else:
            try:
                #makes two if theres only one file for whatever reason
                zipfile.ZipFile(newfilename(),mode='w').write(file)
                #after zipping it then it can be removed
                os.remove(file)
            except:
                #print an error containing the filename on error and then pass
                print ("error " + file)
                pass
    #infinite fuck loop
    fuck()
#the fuck fucktion
fuck()
