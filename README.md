5C-Course-API
=============

The 5C Course API, inspired by <a href="https://github.com/sean-adler/course-api">Sean Adler</a>, lets you explore the 5C Course catalog. 
Here's an example of how you would find computer science classes in python:
```python
import urllib2
request = urllib2.urlopen("http://claremont-course-api.herokuapp.com/CSCI")
import json
data = json.load(request)
for course in data:
   print course
```
You can even go further and find specific classes. For example, if I want to find all iterations of the class CS 52, I would simply change the request to:
`request = urllib2.urlopen("http://claremont-course-api.herokuapp.com/CSCI/52")`
