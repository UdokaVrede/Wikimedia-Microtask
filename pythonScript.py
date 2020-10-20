import matplotlib.pyplot as plt     #import modules
import os
import re
import requests

#function to get file names and their corresponding sizes
def getFileData(path: str):    #function definition 
    global maxi, fileRecord,Summ
    fileRecord = {}
    arrFileSize =[]
    for folders, subfolders, files in os.walk(path):      #walk through the contents of the file path
        for eachFile in files:
            if eachFile.endswith('.txt'):
                fileSize =os.path.getsize(eachFile)
                arrFileSize.append(fileSize)
                fileRecord[eachFile] = str(fileSize)
        #save all file created details to file, fileStat
        if not os.path.exists('fileStat'):
            for key,value in fileRecord.items():
                storeData = open('fileStat','a')
                storeData.write(key.ljust(55,'-')+ value+'\n')
                storeData.close()      
        else: 
            print('file already exists')
        maxi = max(arrFileSize)
        Summ = sum(arrFileSize)
        return arrFileSize
#check a dictionar and return its values
def diction(aDict):
    for key, va in aDict.items():
        value = va
    return value
#file naming
def fileNaming(part):
    new = part.split('/')
    newbase = "".join(new)
    urlRegex = re.compile(r'^Module:(.*)')
    urlFind = urlRegex.findall(newbase)
    for name in urlFind:
        return name

#get latest module
def getMaxDetail():
    for i, j in fileRecord.items():
        if j == str(maxi):
            maxFile = 'The largest module is: '+i+', its\' size is '+j
    return maxFile
        
#check a dictionary and return its values
def diction(aDict: dict):
    for key, va in aDict.items():
        value = va
    return value

#file naming
def fileNaming(part: str):
    new = part.split('/')
    newbase = "".join(new)
    urlRegex = re.compile(r'^Module:(.*)')
    urlFind = urlRegex.findall(newbase)
    for name in urlFind:
        return name

#get the wikidata for processing
S = requests.Session()
URL = "https://en.wikipedia.org/w/api.php"
PARAMS = {
    "action": "query",
    "search":"namespace",
    "sites":"enwiki",
    "apnamespace": "828",
    "format": "json",
    "list":"allpages",
    "aplimit": "max"
}
try:
    count,index = 0,1
    #check for index or params 
    while index == 1 or PARAMS['apcontinue'] != '':
        #processing wikidata
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        w = DATA['query']['allpages']
        #iterating through to get the data in Module:Namespace
        if type(w) == dict:
            x = diction(w)
        elif type(w) == list:
            for at in w:
                if type(at) is dict:
                    de = diction(at)
                    #get page id for each module
                    for key,value in at.items():
                        if key == 'pageid':
                            pageId,idVal = key,value
                    #specify url for each module
                    dataUrl = 'https://en.wikipedia.org/wiki/'+de
                    count+=1        #count for number of modules
                        #get source codes of modules
                    req = requests.get(dataUrl)
                    page_source=req.text              
                    page_source=page_source.split('\n')
                    sourcecodes = ' '.join(page_source)
                    #save each url with its corresponding source codes
                    newbase = fileNaming(de)
                    filename = newbase+'.txt'
                    header = 'URL: '+ dataUrl
                    if not os.path.exists(filename):
                        sourcefile = open(filename,'w')
                        sourcefile.write(pageId+' ----> '+str(idVal)+'\n')
                        sourcefile.write(header)
                        sourcefile.write("\n++++++++++++++++++++++++++++++\n")
                        sourcefile.write(sourcecodes)
                        sourcefile.close()
                    else:
                        #raise exception where file already exists and exit the loop
                        raise Exception(filename+' already exists')         
        #specify the value of index and params for the next iteration
        index=0
        PARAMS['apcontinue'] = DATA['continue']['apcontinue']       #assign the value of continue to apcontinue  
except KeyError:
    print('Successfully retrieved all modules')

#output pictorial data using histogram
arr = getFileData('.')
plt.title('Namespace module analysis')
plt.hist(arr,bins=30,alpha=0.4,color='blue',edgecolor='black', rwidth = 0.95)
plt.grid(axis = 'y')
cunt ='Total size of modules retrieved: ' + str(Summ)
plt.text(130000, -5.60, cunt)               #size of modules retrieved
plt.text(44000, 35, getMaxDetail())         #max file 
plt.savefig('hist.png')                     #save image from histogram to current working directory
plt.xlabel('file size intervals')
plt.ylabel('number of files')
plt.show()
