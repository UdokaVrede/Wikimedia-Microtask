import requests,re,os, inspect,importlib
import matplotlib.pyplot as plt #import modules

#function to get file size
def getFileSize(path):    #function definition    
    arrFileSize =[]
    for folders, subfolders, files in os.walk(path):      #walk through the contents of the file path
        for eachFile in files:
            if eachFile.endswith('.txt'):
                fileSize =os.path.getsize(eachFile)
                arrFileSize.append(fileSize)
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
    "aplimit": "3"
}

index = 1
#check for index or params 
while index == 1 or PARAMS['apcontinue'] != 'Zh':
    #processing wikidata
    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    count=0
    #iterating through to get the data in Module:Namespace
    v = diction(DATA)
    if type(v) == dict:
        w = diction(v)
        if type(w) == dict:
            x = diction(w)
        elif type(w) == list:
            for at in w:
                if type(at) is dict:
                    de = diction(at)
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
                    print(filename)
                    header = 'URL: '+ dataUrl
                    if not os.path.exists(filename):
                        sourcefile = open(filename,'w')
                        sourcefile.write(header)
                        sourcefile.write("\n++++++++++++++++++++++++++++++\n")
                        sourcefile.write(sourcecodes)
                        sourcefile.close()
                    else:
                        #raise exception where file already exists and exit the loop
                        raise Exception(filename+' already exists')
    #specify the value of index and params for the next iteration               
    index=0
    PARAMS['apcontinue'] = DATA['continue']['apcontinue']


    #output pictorial data using histogram
    arr = getFileSize('.')
    plt.style.use('dark_background')
    plt.title('Histogram for source code file sizes')
    plt.hist(arr,bins= 'auto',alpha=0.4,color='blue',edgecolor='black')
    plt.xlabel('file size intervals')
    plt.ylabel('number of files')
    plt.show()