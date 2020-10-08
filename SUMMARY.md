## TASK:
- Write a script that fetches all of the source code on English Wikipedia in the Module: "namespace". Hint: we have APIs that will make your life easier and you can find good examples of how to call the APIs by using your favorite search engine or looking at some of the tools on Toolforge. Please try to limit the number of page or API fetches to one per second. We also have dumps with the same content that can analyzed offline.
- Generate a summary report that includes interesting statistics like number of modules, a histogram of file sizes, and so on.

## STEPS I TOOK:
- First, from the [link](https://en.wikipedia.org/wiki/Special:PrefixIndex?prefix=&namespace=828) in the task, I got a direction to the Api and from documentation,and understood how it is being implemented in a python code.
- Next, From lines 15 -28, I wrote a python script to get the data for the module from the Api which returned a multi-dimensional array.
- I looped through the array to get the contents of each inner array in lines 30 -32.
- In lines 41 -52,I checked for links and extracted their source using  re and requests modules and also wrote them to seperate text files with their respective urls at the top of each file .
- From lines 5 - 12, where I defined the function to get the filesizes, In line 55, I called the function to retrieve the array of filesize values which it returns.
- I used these values to plot the histogram in lines 56 - 60 using matplotlib module.

## TASKS COMPLETED
- [ ] Write a script that fetches all of the source code on English Wikipedia in the Module: "namespace".
- [ ] Generate a summary report that includes interesting statistics like number of modules, a histogram of file sizes, and so on.

## SUMMARY
FROM THE DATA DERIVED AND PROCESSED, 
- THE NUMBER OF MODULES DERIVED WHERE: 29
- THE LINKS FROM WHICH I DERIVED THE SOURCE FILES WHERE:10.
- THE HISTOGRAM AND SOURCE CODE FILES WOULD BE GENERATED ON PROGRAM EXECUTION

## SYSTEM REQUIREMENTS
- Install matplotlib, re and requests
- This solution is written with Python v3.8, Debian Ubuntu O.S

## NOTE TO THE REVIEWER
- I appreciate working on this task and hope to get feedback and modification reports. Thank you for taking out time to vet this task solution I submitted.