## TASK:
- Write a script that fetches all of the source code on English Wikipedia in the Module: "namespace". Hint: we have APIs that will make your life easier and you can find good examples of how to call the APIs by using your favorite search engine or looking at some of the tools on Toolforge. Please try to limit the number of page or API fetches to one per second. We also have dumps with the same content that can analyzed offline.
- Generate a summary report that includes interesting statistics like number of modules, a histogram of file sizes, and so on.

## STEPS I TOOK:
- First, from the [link](https://en.wikipedia.org/wiki/Special:PrefixIndex?prefix=&namespace=828) in the task, I got a direction to the Api and from documentation,and understood how it is being implemented in a python code. This script contains five(5) functions.
- In line 1 - 4, I imported all modules to be used in the script.
- Lines 7 - 27 contains a function, fileData() that gets file names and their corresponding sizes, in this function, then creates a file, `fileStat` for each classification of modules(Scribunto and Non-Scribunto) containing each file detail.
- Line 29 gets the current working directory.
- Line 31 - 47 , contains a function to retrieve source from the urls of each module and save in individual text files bearing the name of the Module.
- In lines 50 - 56, I defined a function that returns the filenames used in naming the files to which each module's source is extracted according to the module name.i had to do this to avoid errors from having slash in my filenames. It contains a condition check that does not allow duplicate file names.
- The function in lines 59 - 77, returns details of the largest retrieved module, the total number of files retrieved and the sum of all files sizes.
- Lines 80 - 88, creates folders with each module classification name(scribunto or non-scribunto), then retrieves their codes using the ModuleCheck() function defined in Line 31 - 47.
- Lines 91 - 112, contains the parameters for processing and retrieving data from the API and the url to the API.
- Lines 114 - 115, I retrieved the pageid and module title for each module.
- Lines 117 - 118, retrieves the contentmodel and contentformat values of each Module.
- Lines 120 - 125, checks the contentmodel and contentformat values of each Module, then creates it's file in it's corresponding folder.
-In lines 127 - 128, I wrote a condition check using the while loop. The index was used to allow for the first set of modules to be fetched without a value assigned to `apcontinue` in `PARAMS`, then index changed to 0 and and the next module value assigned to `apcontinue` in `PARAMS`.
-Lines 129 - 130, consists of the exception for the error that occurs when the last Module has been fetched and the value assigned to `apcontinue` is inaccurate.
- Using values from the `getFileData` and `getMaxDetail`, I designed a histogram showing some detail about the Modules in lines 133 - 146.

## TASKS COMPLETED
- [x] Write a script that fetches all of the source code on English Wikipedia in the Module: "namespace".
- [x] Generate a summary report that includes interesting statistics like number of modules, a histogram of file sizes, and so on.

## SUMMARY
FROM THE DATA DERIVED AND PROCESSED, 
- THE TOTAL NUMBER OF MODULES DERIVED WHERE: 12,526.
- THE TOTAL NUMBER OF SCRIBUNTO (MO) MODULES WHERE: 1690.
- THE HISTOGRAM, FILESTAT FILES FOR BOTH (SCRIBUNTO & NON-SCRIBUNTO MODULES) FOR RETRIEVED MODULES ON EXECUTION, NON-SCRIBUNTO MODULES FOLDER, SCRIBUNTO MODULES FOLDER AND SOURCE CODE FILES FOR EACH MODULE WOULD BE GENERATED ON PROGRAM EXECUTION.
- ATTACHED IS A PICTORIAL OVERVIEW OF THE HISTOGRAM, A MODULES FILE AND  AND FILESTAT DETAILS FETCHED FROM 1,052 MODULES.
- RETRIEVING ALL 12,526 MODULES MIGHT BE TIME, DATA, AND SPACE CONSUMING, IF YOU DO NOT WANT THIS BUT JUST WANT TO SEE A FEW OF THE MODULE DETAILS, 
    - YOU CAN EITHER RUN THE SCRIPTS AND FETCH SOME SOURCE FILES,THEN PRESS CTRL+C OR CTRL+Z TO EXIT, THEN COMMENT OUT THE LINES 86 - 103, THEN RE-RUN THE SCRIPTS TO VIEW THE DETAILS OF THE FILES CREATED 
    OR
    -  COMMENT OUT LINES 120 - 125, THEN RUN THE SCRIPTS.

#### NOTE:

- A file, "fileStat" for each classification of modules(Scribunto and Non-Scribunto Modules) would be created that contains each text file created and its' corresponding size. If you run this script more than once, you would have to delete that file before re-running the script.
- Also, once the text files have been created on initial execution of this script, re-running this script, you would get an error,"File already exists", delete the files and then re-run the scripts.

## SYSTEM REQUIREMENTS
- Install matplotlib, re and requests
- This solution is written with Python v3.8, Debian Ubuntu O.S

## NOTE TO THE REVIEWER
- I appreciate working on this task and hope to get feedback and modification reports. Thank you for taking out time to vet this task solution I submitted.