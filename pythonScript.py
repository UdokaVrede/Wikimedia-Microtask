import requests,re,os
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

#get the wikidata for processing
S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "opensearch",
    "search":"namespace",
    "sites":"enwiki",
    "namespace": "828",
    "format": "json"
}
#processing wikidata
R = S.get(url=URL, params=PARAMS)
DATA = R.json()
count=0
for x in DATA:
    for n in x:
        if n != '' and len(n) > 1:
            #search for urls
            urlRegex = re.compile(r'^https://(.*)')
            urlFind = urlRegex.findall(n)
            #iterate through the retrieved url
            for i in urlFind:
                count+=1
                newUrl = "https://"+i
                #get the source codes
                req = requests.get(newUrl)
                page_source=req.text              
                page_source=page_source.split('\n')
                sourcecodes = ' '.join(page_source)
            #save each url with its corresponding source codes
                filename = 'sourcefile %s.txt'%(count)
                header = 'URL: '+ newUrl
                sourcefile = open(filename,'w')
                sourcefile.write(header)
                sourcefile.write("\n++++++++++++++++++++++++++++++\n")
                sourcefile.write(sourcecodes)
                sourcefile.close()

#output pictorial data using histogram
arr = getFileSize('.')
plt.title('Histogram for source code file sizes')
plt.hist(arr,bins= 'auto',alpha=0.9,color='blue',edgecolor='black')
plt.xlabel('file size intervals')
plt.ylabel('number of files')
plt.show()

