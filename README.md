# metadata-editing-python

**csvediting.py**

This script checks personal names from a CSV file to see if there are any punctuation and/or spacing errors. Your CSV should have its personal names in one column entitled Names. Since we wanted our punctuation conventions to be similar to RDA, we checked for the following errors:

1) A single space follows a comma.
2) Initials are followed by a period and there is a space between two initials. (i.e. Adams, E. P., not Adams, EP or Adams E.P.)
3) The pre-RDA abbreviations of fl., ca., cent., b., and d. are not used. 
4) There is not a period at the end of the name unless the name ends with an abbreviation or initial (this is a local convention)

The script makes a new CSV file with two columns called individualName and errorType. The second column tells the user the first punctuation/spacing error that exists for that name (see below for an example.) If there is more than one error, you only see the first error! 

|individualName                   |errorType              | 
| --------------------------------|-----------------------|
|Abbott, David Phelps, 1863-1934. |Remove period          | 
|Abbott, Edwin Abbott,1838-1926.  |Remove period          |   
|Abelson, Paul,1878-	            |Add space after comma  |  
|Aberra, A.A.	                    |Add space after period |  



**originalAndNewHeadings.py**

This script takes a CSV (CSV1) with a list of subjects and creates a new CSV (CSV2) that contains all of the original values with multiple subjects in one column (in their original form) and a list of these values in another column. 

***CSV1***

|value                                     |multipleTerms |Non-delimiterUseOfCharacter|possibleDelimiter|
| -----------------------------------------|--------------|---------------------------|-----------------|
|manuscripts; Sanskrit                     |y             |n                          |;                |
|attention, learning,memory ,visual cortex |y             |n                          |,                |
|unicorns                                  |n             |                           |                 |

***CSV2***

|originalSubject                           |listofSubject                            |
| -----------------------------------------|-----------------------------------------|
|manuscripts; Sanskrit                     |['manuscripts', 'Sanskrit']              |
|attention, learning,memory ,visual cortex |['attention', 'learning', 'memory', 'visual cortex']                                |
