# Milestone-2

#Part1 

This is the part1 of Milestone2 and I implemented 3 different tasks that demonstrate common HTML/XML 
parsing operations with SoupStrainer instead of BeautifulSoup.

#Environment
Python 3.13.6
BeautifulSoup4
lxml parser

#TestFiles
I did tests with most of files used in MileStone1 and compared the time used to get the result in some certain large and middle files
to compare the performance.
(1)the stackoverflow.com-Votes.7z on https://archive.org/details/stackexchange 
this file is an large XML file which is 1.18GB
        Time Taken Originally    Time Taken Now
task2   166.32seconds            46.13seconds
task3   363.22seconds            387.2seconds
task4   172.27seconds            52.9seconds

(2)the nested.xml provided on the ED discussing platform which is only 4KB which contains 5 levels.

(3)the the testdepth.html is created by myself.It includes 8 levels which is a nested XML file too to test nested files.

(4)softwareengineering.stackexchange.com.7z on https://archive.org/details/stackexchange
this file is an medium file which is 335.3MB
        Time Taken Originally    Time Taken Now
task2   7.89seconds              7.20seconds
task3   60.16seconds             51.76seconds
task4   12.13seconds             7.92seconds

(5)the html file on https://www.tooplate.com/view/2143-inner-peace this file is only 25KB and it is an html file
and it passed too

(6)codereview.stackexchange.com.7z on https://archive.org/details/stackexchange
this file is 775.6MB and it is also a medium file
        Time Taken Originally    Time Taken Now
task2   12.45seconds             8.98seconds
task3   60.16seconds             79.9seconds
task4   12.13seconds             8.61seconds

(7)The largest html file I found on the website is only 25KB so I asked chatgpt 
to create a html file which is 5.24MB to do test
        Time Taken Originally    Time Taken Now    
task2   3.70seconds              0.05s
task3   12.66seconds             0.88s
task4   3.88seconds              0.07s

#Summary
Significant speedups were observed for tasks 2 and 4 when using SoupStrainer especially on large and medium
files. However, Task3 did not see consistent improvements; in some large files and it is slower mainly 
because the task is used to parse all tags so the soupstrainer cannot help so much. Meanwhile, the step
to use soupstrainer also costs time so the time may even longer.Overall, selective parsing with SoupStrainer
is highly effective when only a subset of tags is needed. For full-document parsing, the benefits are 
limited.


#Part2
      APIs                       location                           use 
   BeatifulSoup()          bs4/__init__.py: line 135       create the parsing object
   prettify()              bs4/element.py: line 2601       generate formatted HTML/XML file
   find_all()              bs4/element.py: line 2715       find all tags
   find()                  bs4/element.py: line 2684       find first matching tag
   find_parent()           bs4/element.py: line 992        find parent of a node
   find_parents()          bs4/element.py: line 1022       find all parent nodes
      Tag()                bs4/element.py: line 1569       tag object
   descendant()            bs4/element.py: line 2764       iterate over all descendant nodes
find_previous_siblings()   bs4/element.py: line 953        find all previous siblings
find_previous_sibling()    bs4/element.py: line 927        find the one previous sibling
find_next_siblings()       bs4/element.py: line 827        find all next siblings
find_next_sibling()        bs4/element.py: line 803        find the one next sibling
   SoupStrainer()           bs4/filter.py: line 343         parse specific nodes



   





