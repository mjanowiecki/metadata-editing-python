# metadata-editing-python

Scripts to merge, pivot, and edit CSV data. Many of these script rely on the pandas library.

**basicPivot.py**
This script does a basic pandas pivot_table by setting the index to the value of a specific column.

**checkIfIdentifiersInSheet.py**

This script checks if two CSVs have the same identifiers by left merging (joining) a list of unique identifiers from the 2nd CSV to the 1st CSV. Then you can visually scan the updated 1st CSV to see what identifiers might be missing.

**collapseMultipleCSVColumnsToOneColumn.py**

This script takes a CSV with multiple columns and collapses them to a single column.

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

**combineMultipleSpreadsheets.py**

This script uses pandas to combine multiple spreadsheets with the same column names into one combined, large spreadsheet. The spreadsheets to combine should all be placed into the same folder.

**combineSubjectHeadingsByBibNumber.py**

Uses pandas pivot_table to combine subject strings by identifier number. Then a left merge combines the pivot table to a metadata spreadsheet if needed.

***original***
|identifier    |subject       |
|--------------|--------------|
|0001          |horses        |
|0001          |goats         |
|0001          |cows          |
|0002          |Mars          |
|0002          |Venus         |

***pivot_table***
|identifier    |subject              |
|--------------|---------------------|
|0001          |horses;goats;cows    |
|0002          |Mars;Venus           |

**convertsUnstructuredListsToStructuredLists.py**

This script takes a CSV with unstructured lists of values and converts them into new structured lists. The original unstructured lists and the new structured lists are imported into a new CSV (structuredAndUnstructuredLists.csv).

***original***

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

**countValuesForEachColumnInSheets.py**

This script looks at multiple spreadsheets in a folder, and counts how many values are found in each column of each spreadsheet. This count information is then added by handle (or filename) to a new CSV.

**createSpreadsheetsForEachColumnInSheets.py**

This script combines multiple spreadsheet from a folder into a dataframe, and makes a new spreadsheet for each column found in the combined dataframe.

**deleteBlankColumnsAndRows.py**
This script deletes any rows and columns that are completely blank from a CSV.

**deleteDuplicateRows.py**

This script deletes any rows with the exact same information from a CSV.

**explodeColumnWithList.py**

This script takes a column with many values in each cell, and creates a new row for each value, duplicating its original identifier or associated values.

**findDuplicateValuesInColumn.py**

This script uses pandas to find any duplicated values within a column of a CSV, and then creates a new CSV containing all of the duplicated rows.

**findFuzzyMatchesWithinAList.py**

This script uses fuzzywuzzy to match nearly identical strings within a list (or a column of a CSV). It produces CSV with the matches and a CSV with the strings that could not be matched.

**findLinkForEachUniqueValue.py**

This script takes a list of unique values from a CSV, and searches for them in 2nd CSV. In the 2nd CSV, each value will be in a column where each cell has multiple value separated by a delimiter. The script will loop through this column and find an identifier or link for each unique value.

**findRepeatedIdentifiersInSheet.py**

Find all identifiers in a sheet that appear more than 1 time in column. Make a new spreadsheet with repeated identifiers and associated information.

**generateNumberedCopiesofFile.py**

This script makes numbered copies of a file for testing purposes.

**getEveryNthRowFromCSV.py**

This script grabs every Nth row from a CSV to create a sample of data.

**getSumAndSizeForColumnInSheet.py**

This script uses pandas groupby to get the sum (sum of values) and size (total count of non-empty value) of each unique value in a specific column.

**guessLanguage.py**

This script uses langdetect to guess the language of the items from their titles.

**matchInfoInTwoSpreadsheetsByIdentifier.py**

This scripts matches information from two CSVs by their identifiers.

**meltMultipleSubjectsByIdentifier.py**

This script melts a wide CSV with multiple column pairs of an auth_name and vocab_id into a long format where each column pair is in its own row with the associated bib number.

***original***
|bib           |0_auth_name   | 0_vocab_id   | 1_auth_name  | 1_vocab_id   |
|--------------|--------------|--------------|--------------|--------------|
|0001          |horses        |1003          |goats         |20394         |
|0002          |Venus         |839402        |Mars          |9842718       |

***melted***
|bib           |auth_name     | vocab_id     |
|--------------|--------------|--------------|
|0001          |horses        |1003          |
|0001          |goats         |20394         |
|0002          |Venus         |839402        |
|0002          |Mars          |9842718       |

**mergeLeftTwoSheets.py**

This script uses a pandas left merge (left join) to join information from CSV 2 to CSV 1 based on identifier.

**mergeTwoColumns.py**
**reformatInversedNames.py**

This script takes basic personal names without dates, and inverses them to follow a Secondary Name, Primary Name format.

**splitCSVBasedOnValues.py**

This script generates a new CSV for each unique value found in a specific column of a CSV. The new CSVs are named based on the unique values found.

**splitCSVForTesting.py**

This script takes a large CSV and divides it evenly into ten CSVs for testing.

**standardizePersonalNames.py**

This script checks personal names from a CSV file to see if there are any punctuation and/or spacing errors. The script bases its punctuation conventions on RDA and checks that these rules are followed:

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
