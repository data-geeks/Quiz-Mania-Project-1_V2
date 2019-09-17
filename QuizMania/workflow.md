# WorkFlow

Date: 16th

* Made the project named ```QuizMania``` with its first ```webapp``` names as ```QuizMania_V2```
* Made a template folder inside the ```webapp``` and copied the 3 html files inside the templates folder namely ```admin,index,result```
* Inside the ```settings``` file, added the ```templates``` dircetory path and add the ```Installed Apps``` element value to ```QuizMania_V2```
* Made a ```static/QuizMania_v2``` folder inside ```webapp``` and added the ```css js bootstrap``` folders inside it
* configured the ```urls.py``` for index page
* Given ```755``` permission to all files inside static folder

# index.html
Date 17th sep.
* all the links are converted in jinja format(src,href)
```
on the top of the html page load static page
{% load static %}

then replace src,href or all static file links in this format
src = "{% static 'img/vpv.png' %}"

```
* and piyush your
``static/QuizMania_v2/img or css`` directory converted in 
``static/img or css``


