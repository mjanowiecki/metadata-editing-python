# metadata-editing-python

Scripts to merge, pivot, and edit CSV data. Many of these script rely on the pandas library.

## clean-up

**convertUnstructuredListsToStructuredLists.py**<br>
Converts unstructured lists of values and converts them into new structured lists.

***original***

| value                                     | multipleTerms | possibleDelimiter |
| ----------------------------------------- | ------------- | ----------------- |
| manuscripts; Sanskrit                     | y             | ;                 |
| attention, learning,memory ,visual cortex | y             | ,                 |
| corgis; golden retrievers;bulldog;        | y             | ;                 |
| unicorns                                  | n             |                   |

***structuredAndUnstructuredLists.csv***

| unstructuredList                          | structuredList                                       |
| ----------------------------------------- | ---------------------------------------------------- |
| manuscripts; Sanskrit                     | ['manuscripts', 'Sanskrit']                          |
| attention, learning,memory ,visual cortex | ['attention', 'learning', 'memory', 'visual cortex'] |
| corgis; golden retrievers;bulldog;        | ['corgis', 'golden retrievers', 'bulldog']           |

**deleteBlankColumnsAndRows.py**<br>
Deletes any rows and columns that are completely blank from a CSV.

**deleteDuplicateRows.py**<br>
Deletes any rows with the exact same information from a CSV.

**deleteRowsWithIdentifiers.py**<br>Deletes rows from first spreadsheet using list of identifiers from second spreadsheet.

**stripWhiteSpaces.py**<br>Strips white spaces from all cells in CSV.

## evaluate

**getDuplicatedIdentifiersInSheet.py**<br>
Finds all identifiers in a spreadsheet that appear more than 1 time in column. Creates a new spreadsheet containing all of rows with duplicated identifiers.

**getDuplicateValuesInColumn.py**<br>
Find any duplicated values within a column of a spreadsheet, and then creates a new spreadsheet containing all of the duplicated rows.

**getExtensionsFromFilenames.py**<br>Loops through a spreadsheet of filenames and add columns of just file extensions to original sheet.

**getIdentifiersNotRepeatedInSheet.py**<br>
Finds identifiers that only appear once in a sheet's column. Creates a new spreadsheet containing all of rows with non-repeated identifiers.

**getInProgressAndCompletedRows.py**<br>
Finds rows where the cell is empty (nan) for certain columns, and creates a new spreadsheet with these rows.

**getSumAndSizeForColumnInSheet.py**<br>Gets the sum (sum of values) and size (total count of non-empty value) of each unique value in a specific column.

**getTotalValuesByIdentifierInSheet.py**<br>For spreadsheet where some identifiers are repeated in multiple rows, and each row has a number value , add up number values for each identifier.

**getValuesDuplicatedInTwoColumns.py**<br>Get any values duplicated in two columns in a sheet..

**printDuplicatedIdentifiersPairsInSheet.py**<br>Print any duplicated identifier pairs to terminal.

**printUniqueIdentifiersInSheet.py**<br>Print list of unique identifiers to terminal.

## match-values

**findFuzzyMatchesWithinAList.py**<br>Matches nearly identical strings within a list (or a column of a CSV) using fuzzywuzzy. It produces CSV with the matches and a CSV with the strings that could not be matched.

**getLinkForEachUniqueValue.py**<br>This script takes a list of unique values from a CSV, and searches for them in second CSV. In the second CSV, each value will be in a column where each cell has multiple value separated by a delimiter. The script will loop through this column and find an identifier or link for each unique value.

**guessLanguage.py**<br>Guesses the language of items from their titles using langdetect.

## merge

**combineStringColumns.py**<br>Combines strings from numerous columns into a new column.

**mergeLeftTwoSheets.py**<br>Joins two spreadsheets using pandas left merge (left join) on an identifier.

**mergeTwoSheetsWithoutPandas.py**<br>Joins information from two spreadsheets by their identifiers.

## multiple

**combineMultipleSpreadsheets.py**<br>Combines multiple spreadsheets with the same column names into one combined, large spreadsheet. The spreadsheets to combine should all be placed into the same directory.

**compareIdentifiersInMultipleSheets.py**<br>Collects identifiers from multiple spreadsheets in a directory and lists the spreadsheets where each identifier appears.

**createSpreadsheetsForEachColumnInSheets.py**<br>Combines multiple spreadsheets in a directory into a dataframe, and makes a new spreadsheet for each column found in the combined dataframe.

**getIdentifiersMissingInSecondSheet.py**<br>Finds any identifiers that exist in the first sheet but *not* in the first sheet.

**getStatusOfAllIdentifiersInTwoSheets.py**<br>Creates a spreadsheet with a list of all identifiers from both sheets and records if the identifier is in both sheets, only sheet_1, or only sheet_2.

**getValueCountsForEachColumnInSheets.py**<br>Counts how many values are found in each column of spreadsheets in a directory. This count information is then added by handle (or filename) to a new CSV.

**mergeMultipleSheetsOnIdentifier.py**<br>Merges multiple spreadsheets in a directory on an identifier column found in all of the sheets.

## reformat-values

**addPrefixToIdentifiers.py**<br>Adds a string prefix to an identifier column.

**convertToETDF.py**<br>Converts a wide variety of date formats to ETDF using regular expressions.

**createFileNameFromCallNum.py**<br>Creates a unique filename based on an item's call number.

**reformatInversedNames.py**<br>Converts personal names without dates to follow a Secondary Name, Primary Name format.

**standardizePersonalNames.py**<br>Checks personal names from a CSV file to see if there are any punctuation and/or spacing errors. The script bases its punctuation conventions on RDA and checks that these rules are followed:

1) A single space follows a comma.
2) Initials are followed by a period and there is a space between two initials. (i.e. Adams, E. P., not Adams, EP or Adams E.P.)
3) The pre-RDA abbreviations of fl., ca., cent., b., and d. are not used.
4) There is not a period at the end of the name unless the name ends with an abbreviation or initial (this is a local convention). To remove, delete or edit rows 32-34.

The script makes a new CSV file (namesStandardized.csv) with two columns called personalName and errorType. The second column tells the user the first punctuation/spacing error that exists for that name (see below for an example.) If there is more than one error, you only see the first error!

| personalName                     | errorType                    |
| -------------------------------- | ---------------------------- |
| Abbott, David Phelps, 1863-1934. | Remove period                |
| Abbott, Edwin Abbott,1838-1926.  | Remove period                |
| Abelson, Paul,1878-              | Add space after comma        |
| Aberra, A.A.                     | Add space after period       |
| Albert, Jane, b. 1889            | Not updated to RDA standards |

**stripTimeFromDateTime**<br>Strips the time from a standard DateTime stamp.

## reshape

**basicMelt.py**<br>Melts a spreadsheet on a specific identifier column.

**basicPivot.py**<br>Pivots a spreadsheet by setting the index to the value of a specific column.

**basicPivotTable.py**<br>Pivots and aggregates a spreadsheet by setting the index to the value of a specific column.

***original***

| column1 | column2      |
| ------- | ------------ |
| 001     | Smith, Jane  |
| 002     | Smith, Ed    |
| 002     | Austen, Jane |
| 003     | Smith, Ed    |

***new***

| column2      | column1   |
| ------------ | --------- |
| Austen, Jane | 002       |
| Smith, Ed    | 002 \|003 |
| Smith, Jane  | 001       |

**collapseAllColumnsToOneColumn.py**

**collectSubjectsByIdentifier.py**<br>Combine subject strings by identifier number. Then a left merge combines the pivot table to a metadata spreadsheet if needed.

***original***

| identifier | subject |
| ---------- | ------- |
| 0001       | horses  |
| 0001       | goats   |
| 0001       | cows    |
| 0002       | Mars    |
| 0002       | Venus   |

***pivot_table***

| identifier | subject           |
| ---------- | ----------------- |
| 0001       | horses;goats;cows |
| 0002       | Mars;Venus        |

**explodeAndPivotByIdentifier.py**<br>Reshapes sheet indexed by column1 (column2 aggregated) to sheet indexed by column2 (column1 aggregated).

***original***

| column1     | column2           |
| ----------- | ----------------- |
| Smith, Ed   | 001 \| 004 \| 005 |
| Smith, Jane | 004               |

***new***

| column2 | column1                  |
| ------- | ------------------------ |
| 001     | Smith, Ed                |
| 004     | Smith, Ed \| Smith, Jane |
| 005     | Smith, Ed                |

**explodeColumnWithList.py**<br>Takes a column where each cell contains multiple values, and creates a new row for each value, duplicating its original identifier.

**meltMultipleSubjectsByIdentifier.py**<br>Melts a wide CSV with multiple column pairs of an auth_name and vocab_id into a long format where each column pair is in its own row with the associated bib number.

***original***

| bib  | 0_auth_name | 0_vocab_id | 1_auth_name | 1_vocab_id |
| ---- | ----------- | ---------- | ----------- | ---------- |
| 0001 | horses      | 1003       | goats       | 20394      |
| 0002 | Venus       | 839402     | Mars        | 9842718    |

***melted***

| bib  | auth_name | vocab_id |
| ---- | --------- | -------- |
| 0001 | horses    | 1003     |
| 0001 | goats     | 20394    |
| 0002 | Venus     | 839402   |
| 0002 | Mars      | 9842718  |

**splitCSVByUniqueValueInColumn.py**<br>Generates a new CSV for each unique value found in a column of a spreadsheet. The new CSVs are named based on the unique values found.

## testing

**generateNumberedCopiesofFile.py**<br>Generates numbered copies of a file for testing purposes.

**getEveryNthRowFromCSV.py**<br>Collects every Nth row from a CSV to create a sample of data.

**splitCSVForTesting.py**<br>Spilts a large spreadsheet evenly into ten CSVs for testing.

**testLink.py**<br>Tests URLs listed in spreadsheet to see if they work.
