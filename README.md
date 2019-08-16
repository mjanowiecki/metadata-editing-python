# metadata-editing-python

**checkStringAgainstFAST.py**

**collapseMultipleCSVColumnsToOneColumn.py**

This script takes a CSV with multiple columns and collapses them to a single column. The CSV to convert is selected when entering the script into the terminal. Type python collaspingMultipleCSVColumnsToOneColumn.py -f filename.csv

***original***

|breed1         |breed2         |breed3         |breed4         |breed5         |
|---------------|---------------|---------------|---------------|---------------|
|boston terrier	|bulldog        |corgi        	|great dane	    |dalmatian      |
|beagle         |               |               |               |               |
|lab            |whippet        |               |               |               |

***oneColumn***

|dogs           |
|---------------|
|boston terrier	|
|bulldog        |
|corgi  	      |
|great dane   	|
|dalmatian      |
|beagle         |
|lab            |
|whippet        |

**combineRowsWithIdenticalValuesInColumn.py**

**convertLCSHToFAST.py**

**convertsUnstructuredListsToStructuredLists.py**
This script takes a CSV (CSV1) with unstructured lists of values and converts them into new structured lists. The original unstructured lists and the new structured lists are imported into a new CSV(structuredAndUnstructuredLists.csv). This script is useful when many values have been entered into a single field. The CSV to convert is selected when entering the script into the terminal. Type python convertsUnstructuredListsToStructuredLists.py -f filename.csv

***CSV1***

|value                                     |multipleTerms |possibleDelimiter|
| -----------------------------------------|--------------|-----------------|
|manuscripts; Sanskrit                     |y             |;                |
|attention, learning,memory ,visual cortex |y             |,                |
|corgis; golden retrievers;bulldog;        |y             |;                |
|unicorns                                  |n             |                 |

***structuredAndUnstructuredLists.csv***

|unstructuredList                          |structuredList                                        |
| -----------------------------------------|------------------------------------------------------|
|manuscripts; Sanskrit                     |['manuscripts', 'Sanskrit']                           |
|attention, learning,memory ,visual cortex |['attention', 'learning', 'memory', 'visual cortex']  |
|corgis; golden retrievers;bulldog;        |['corgis', 'golden retrievers', 'bulldog']            |


**decadeFASTConversion.py**

**deleteDuplicateRows.py**

**expandIdentifierBasedOnPattern.py**

**getEveryNthRowFromCSV.py**

**matchInfoInTwoSpreadsheetsByIdentifier.py**

**standardizingPersonalNames.py**

This script checks personal names from a CSV file to see if there are any punctuation and/or spacing errors. The CSV to convert is selected when entering the script into the terminal. Type "python standardizingPersonalNames.py -f filename.csv" to run the script. Your CSV should have its personal names in one column entitled Names. Since we wanted our punctuation conventions to be similar to RDA, we checked for the following errors:

1) A single space follows a comma.
2) Initials are followed by a period and there is a space between two initials. (i.e. Adams, E. P., not Adams, EP or Adams E.P.)
3) The pre-RDA abbreviations of fl., ca., cent., b., and d. are not used.
4) There is not a period at the end of the name unless the name ends with an abbreviation or initial (this is a local convention). To remove, delete or edit rows 32-34.

The script makes a new CSV file (namesStandardized.csv) with two columns called personalName and errorType. The second column tells the user the first punctuation/spacing error that exists for that name (see below for an example.) If there is more than one error, you only see the first error!

|personalName                     |errorType                    |
| --------------------------------|-----------------------------|
|Abbott, David Phelps, 1863-1934. |Remove period                |
|Abbott, Edwin Abbott,1838-1926.  |Remove period                |   
|Abelson, Paul,1878-	            |Add space after comma        |  
|Aberra, A.A.	                    |Add space after period       |
|Albert, Jane, b. 1889            |Not updated to RDA standards |



