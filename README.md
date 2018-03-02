# metadata-editing-python

<b>csv.editing</b>

This script checks personal names from a csv file and reports if there are any punctuation and/or spacing errors. This script follows punctuation conventions similar to RDA. 
It checks to ensure that:
1) A single space follows a comma.
2) Initials are followed by a period and there is a space between two initails. (i.e. Adams, E. P., not Adams, EP or Adams E.P.)
3) The pre-RDA abbreviations of fl., ca., cent., b., and d. are not used. 
4) There is not a period at the end of the name unless the name ends with an abbreviation or initial (this is a local convention).
