import requests
from lxml import etree
import re
import json



def get_verse(book, chapter, verse, translation='esv'):
    response = requests.get(f'https://biblia.com/bible/{translation}/{book}/{chapter}/{verse}')
    if response.status_code == 200:
        # Request was successful
        content = response.text  # Get the content of the webpage as a string
        parser = etree.HTMLParser()
        tree = etree.fromstring(content, parser)
        element = tree.xpath('//*[@id="content-bible"]/div/div[1]/div[1]/div[1]/p/button')[0]
        data_copytext = element.get('data-copytext')
        return _clean_output(data_copytext)
    else:
        return 'error'



def _clean_output(data):
    # Remove non-printable characters
    cleaned_data = ''.join(filter(lambda x: x.isprintable(), data))

    # Remove verse numbers and book abbreviation
    pattern = r'\b[A-Za-z]+\s?\d+:\d+\b'
    main_data = re.sub(pattern, '', cleaned_data)

    main_data = main_data.replace('“', '"')
    
    # Remove leading and trailing whitespace
    main_data = main_data.strip()
    main_data = main_data.split(':')[1]


    return(main_data)





def _split_string(string):
    input_string = string
    if string[1] == ' ':
        index = 1
        new_character = "%20"

        input_string = input_string[:index] + new_character + input_string[index+1:]


    list = input_string.split(' ')

    for i in list[1].split(':'):
        list.append(i)
    del list[1]
    dict = {
        'book' : list[0],
        'chapter' : list[1],
        'verse' : list[2]
        }
    return(dict)



def get_verse_from_string(string, translation='esv'):
    split = _split_string(string)
    return(get_verse(split['book'], split['chapter'], split['verse'], translation))




def search(query, translation):
    response = requests.get(f'https://biblia.com/search?query={query}&resources={translation}&contentType=js')
    if response.status_code == 200:
        # Request was successful
        content = response.text  # Get the content of the webpage as a string
        data = json.loads(content)['results']
        results = []
        for i in data:
            #print (i['title'])
            results.append(get_verse_from_string(i['title']))
        return results
    else:
        return 'error'