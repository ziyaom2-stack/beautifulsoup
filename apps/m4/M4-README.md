# Milestone-4
In this milestone, I implemented the iterator for the BeautifulSoup,allowing users to use 'for node in
soup' to traverse all nodes in the parse tree. This makes BeautifulSoup work like a native Python iterable.

## Operation on code
bs4/__init__.py
Implemented '__iter__()' method to make BeautifulSoup iterable and implemented the '_traverse_tree()'
function for depth-first traversal based on stack to fulfill the function.

bs4/tests/SoupReplacerTest9-13:
Added 5 comprehensive test cases covering different situations:
SoupReplacerTest9:Basic iteration and node counting for an HTML file
SoupReplacerTest10:Deep nested XML structure traversal
SoupReplacerTest11:Text node iteration for an XML file
SoupReplacerTest12:Link collection for an XML file
SoupReplacerTest13:Deep nested HTML structure traversal

**apps/m4/application.py**
Demonstrated the core iteration feature. This application reads in an HTML or XML file and print all nodes
of the file with the function 'for node in soup:print(node)'

## How to run
cd apps/m4
python application.py (file name)  e.g. if the file name is test.xml then the command is
python application.py test.xml

## Technical Brief
Design choice:The realization chose the method to traverse the tree with a stack instead of recursion
to avoid the recursion depth limits if the input file is large and make it easy to control.

Core strategy:
def _traverse_tree(self):
    stack = [self]
    while stack:
        current = stack.pop()
        yield current
        if hasattr(current, 'contents') and current.contents:
            for child in reversed(current.contents):
                stack.append(child)

The traverse uses the DFS algorithm to traverse because it fits the sequence of HTML/XML file.

## Conclusion
Milestone 4 successfully made BeautifulSoup iterable using a stack-based DFS generator. I tested the 
function with three XML files and three HTML files and all succeeded(including large files and 
nested-structured files. This Pythonic interface allows natural 'for' loop syntax and integrates 
seamlessly with Python's iteration utilities. Meanwhile,the implementation is memory-efficient and 
maintains consistency with BeautifulSoup's existing traversal behavior.