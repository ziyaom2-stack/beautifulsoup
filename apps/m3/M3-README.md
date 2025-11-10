# Milestone-3
In this milestone,I extended the SoupReplacer API to support functional transformations on 
tags, making it more powerful and flexible than in Milestone 2.
Previously, SoupReplacer only supported simple tag-to-tag replacements (og-tag, alt-tag),
but now it provides a more general interface that allows users to customize how tag names, 
attributes, or even the entire tag object are transformed during parsing.

Operation on the code:

bs4/SoupReplacer.py
Implemented the new logic that applies name_xformer, attrs_xformer, and xformer functions in sequence.
name_xformer(tag) → returns a replacement name for the tag
attrs_xformer(tag) → returns modified attributes
xformer(tag) → allows side effects on the tag, does not return anything

bs4/SoupReplacerTest3.py ~ bs4/SoupReplacerTest8.py
Added six new test cases to validate all three transformer modes with both HTML and XML.
Verified that transformations (renaming tags, editing attributes, and modifying tags in-place) occur correctly during parsing.

apps/m3/task7.py
Reimplemented the task from Milestone 1, this time using the new SoupReplacer API.
The program adds a "class=test" attribute to every <p> tag in the document.
It supports both .html and .xml inputs and did test on both large HTML and XML files.

I did test on 3 files and compared the time with the milestone1 task7:
                         Milestone1(without soupReplacer)    Milestone3(with SoupReplacer)     improvement
Votes.xml(1.18GB)             226.75s                               170.82s                    24.7% faster
PostHistory.xml(775.6MB)      20.15s                                10.87s                     46.1% lower
Comments.xml(106.8MB)          2.79s                                3.57s                      27.9% slower
Conclusion: The speed was faster on large datas when using the soupReplacer.

how to run: 
cd apps/m3
python task7.py (file_name)


#technical brief
Evolution of the SoupReplacer API from milestone2 to milestone3:
1 Introduction
From milestone2 to milestone3, the SoupReplacer API evolved from a simple renaming tool into a transforming
framework and added the functions of modifying tag names, replacing tag attributes or xformer for arbitrary 
tag-level logic.

2 Milestone2 summary
Capabilities: Only replacing tag name.
Strength: Simple and easy to use
Trade-off: cannot modify other things like attributes and structure

3 Milestone3 enhancement
New functions
name_xformer: Function for transforming or replacing tag names.
attr_xformer: Function for modifying, or filtering attributes.
xformer: General-purpose transformation hook that operates on the entire tag object.

Benefits:
Flexible: the milestone3 supports both simple and complex transformations.
Composable: it can unify name and attribute logic under one interface.
Extensible: Easily integrates with downstream processing

Trade-offs:
Slightly higher learning curve and complexity.
Requires clear documentation to guide usage.

4 Recommendation
The milestone3 is more recommended because it was more solidly developed and more robust functions. And it 
is likely to deal with large files efficiently. Meanwhile, xformer is likely to be  adopted as the primary extension
point within the SoupReplacer API because compared to the specialized name_xformer and attr_xformer functions, 
xformer offers superior flexibility and long-term maintainability.


5 Conclusion
Milestone 2 delivered a minimal baseline; Milestone 3 transforms it into a robust, extensible transformation 
engine.
