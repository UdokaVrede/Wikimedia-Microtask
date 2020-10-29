import matplotlib.pyplot as plt     #import modules
import os
import re
import requests

# #function to get file names and their corresponding sizes
def getFileData(path):    #function definition 
    fileRecord = {}
    arrFileSize, arrFileName = [], []
    for eachFile in os.listdir(path):      #walk through the contents of the file path
        os.chdir(path)
        fullPath = os.getcwd()
        basePath = os.path.basename(fullPath)
        if eachFile.endswith('.txt'):
            fileSize =os.path.getsize(eachFile)
            arrFileSize.append(fileSize)
            fileRecord[eachFile] = str(fileSize)
            os.chdir(ini_dir)
            #save all file created details to file, fileStat
    if not os.path.exists('fileStat-{}'.format(basePath)):
        for key,value in fileRecord.items():
            storeData = open('fileStat-{}'.format(basePath),'a')
            storeData.write(key.ljust(70,'-')+ value+'\n')
            storeData.close()   
    else: 
        print('file already exists')
    return arrFileSize

ini_dir = os.getcwd()

def ModuleCheck(ModulTitle):
    dataUrl = 'https://en.wikipedia.org/wiki/'+ModulTitle
        #get source codes of modules
    req = requests.get(dataUrl)
    page_source=req.text       
    page_source=page_source.split('\n')
    sourcecodes = ' '.join(page_source)
    #save each url with its corresponding source codes
    newbase = fileNaming(ModulTitle)
    filename = newbase+'.txt'
    if not os.path.exists(filename):
        sourcefile = open(filename,'w')
        sourcefile.write(sourcecodes)
        sourcefile.close()
    else:
        #raise exception where file already exists and exit the loop
        raise Exception(filename+' already exists')

#file naming
def fileNaming(part):
    new = re.split('/| ', part)
    newbase = "".join(new)
    urlRegex = re.compile(r'^Module:(.*)')
    urlFind = urlRegex.findall(newbase)
    for name in urlFind:
        return name

#get latest module
def getMaxDetail():
    global maxi,Summ, fileCount
    fileCount = 0
    allFileSize = []
    allFileDict = {}
    for folders,subfold, files in os.walk('.'):
        for oneFile in files:
            oneFilePath = os.path.join(folders, oneFile)
            if oneFilePath.endswith('.txt'):
                fileCount += 1
                allFileSize.append(os.path.getsize(oneFilePath))
                allFileDict[oneFile] = str(os.path.getsize(oneFilePath))
    maxi = max(allFileSize)
    Summ = sum(allFileSize)
    for k,v in allFileDict.items():
        if v == str(maxi):
            kx = ''.join(k.split('.txt'))
            maxFile = 'Max module: '+kx+' Module Size:'+v
            return maxFile

def segModule(segPath):
    if not os.path.exists(segPath):
        os.makedirs(segPath)
        os.chdir(segPath)
        ModuleCheck(modTitle)
        os.chdir(ini_dir)
    else:
        os.chdir(segPath)
        ModuleCheck(modTitle)  
        os.chdir(ini_dir)

#get the wikidata for processing
S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"
PARAMS = {
    "action": "query",
    "apnamespace": "828",
    "prop": "revisions",
    "format": "json",
    "list":"allpages",
    "aplimit": "1",
    "rvslots": "*",
    "rvprop": "content"
}
count,index = 0,1
try:
    while index == 1 or PARAMS['apcontinue'] != "":
    #initial processing to get title parameter
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        PARAMS['titles'] = DATA['query']['allpages'][0]['title']
    #processing wikidata
        Rj = S.get(url=URL, params=PARAMS)
        DAT = Rj.json()
    #get pageid and module titles
        Pageid = DAT['query']['allpages'][0]['pageid']
        modTitle = DAT['query']['allpages'][0]['title']
    #get contentmodel and contentformat for each module  
        Model = DAT['query']['pages'][str(Pageid)]['revisions'][0]['slots']['main']['contentmodel']
        formaT =  DAT['query']['pages'][str(Pageid)]['revisions'][0]['slots']['main']['contentformat']
        
        if (formaT == 'text/plain' and Model == 'Scribunto'):
            scribMod = './Scribunto-Modules'
            segModule(scribMod) 
        else:
            nonScribMod = './Non-Scribunto-Modules'
            segModule(nonScribMod)
#set apcontinue value and reset index to 0.
        index = 0
        PARAMS['apcontinue'] = DATA['continue']['apcontinue']
except KeyError:
    print('Successfully retrieved all modules')

#output pictorial data using histogram
Scrib_arr = getFileData(os.path.abspath('./Scribunto-Modules'))         #get filesizes in scribunto module folder
NonScrib_arr = getFileData(os.path.abspath('./Non-Scribunto-Modules'))  #get filesizes in Non-Scribunto Module folders
plt.title(getMaxDetail())
plt.suptitle('Namespace module analysis'+" Retrieved Modules: "+str(fileCount),fontsize=13)
cunt ='Total size of modules retrieved: ' + str(Summ)
plt.text(130000, -22, cunt, fontsize=13)               #size of all modules retrieved
plt.hist(Scrib_arr,bins=round(fileCount/10),alpha=0.6,label = 'Non-Scribunto Modules', color='green',edgecolor='black', rwidth = 0.75)
plt.hist(NonScrib_arr,bins=round(fileCount/10),alpha=0.6,label = 'Scribunto Modules',color='red',edgecolor='black', rwidth = 0.75)
plt.grid(axis = 'y')
plt.legend(loc = "best")                    
plt.savefig('hist.png')                     #save image from histogram to current working directory
plt.xlabel('file size intervals')
plt.ylabel('number of files')
plt.show()
