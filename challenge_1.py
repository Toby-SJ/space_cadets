import requests
from bs4 import BeautifulSoup

prefix = input('enter the email prefix of the teacher to search: ')

# cheat way using url
print(requests.get(f'https://www.ecs.soton.ac.uk/people/{prefix}').url.split('/')[-1].replace('-', ' ').title())

# less cheating way using html parsing
html = requests.get(f'https://www.ecs.soton.ac.uk/people/{prefix}').text

parser = BeautifulSoup(html, 'html.parser')

print(parser.find('h1', {'class': "heading-m inline-block text-prussianDark"}).text)
