# Bible-API
A simple-to-use wrapper for biblia.com to get Bible verses and search the Bible with python. There are other Bible apis but most of them are either paid or require accounts and/or api keys. This project still gives you access to most things other apis do but is free and super easy to use. 


# Installation
Simply clone the repo or download "Bible.py" and import it into your project:
```python
import Bible as bible
```
# Translation note
If no translation to use is provided in the function, it will default to the English Standard Version, or ESV as it is one of the most accurate, easy to read translations.


# Get a Bible verse the easy way
You can get a certain Bible verse like this. You can get a single verse or multiple. You can also choose any translation. You only have to provide a single string to get a verse which can be far better for users however, this method may have some issues so it might be better to use the harder way below.
```python
bible.get_verse_from_string(john 3:16-17, 'esv'):
```
outputs as a string:
```
 16"For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life.
```

# Get a Bible verse the hard way
You can get a certain Bible verse like this. You can get a single verse or multiple. You can also choose any translation. In a lot of cases, it is easier and better to use the method listed above.
```python
bible.get_verse(john, 3, 16-17, 'esv'):
```
outputs as a string:
```
 16"For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life.
```

# Search the Bible
To search the entire Bible for keywords, you can use the following. You can provide a query and translation.
```python
bible.search('For God so loved the world', 'esv')
```
outputs a list of dictionaries containing the title (where to find the verse) and the verse itself:
```
[{'title': 'John 3:16', 'text': ' 16"For God so loved the world, that he gave his only Son, that whoever believes in him should not perish but have eternal life.'}]
```



