#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
  import urllib.request as urllib2
except:
  import urllib2

from bs4 import BeautifulSoup

source = "https://fr.wikipedia.org"

# get the html from address
def get_html(address):
 return urllib2.urlopen(source+address).read()

# get the first link from a BeautifulSoup object
def get_first_link(soup):
 for p in soup.find('div',{'id':'bodyContent'}).findAll('p'):
  for a in p.findAll('a'):
   if a and a.get('href').startswith('/wiki/') and not ":" in a.get('href'):
    return a.get('href')

# run search
def get_to_philosophy(initial_address, max_iterations=100, verbose=False):
 target_page = "/wiki/Philosophie"
 iteration = 0
 pages_visited = []
 current_address = initial_address if "/wiki/" in initial_address else "/wiki/"+initial_address
 if verbose:
  print("\ninitial address: " + current_address+"\n Will you go to "+target_page+" ?...\n")
 while iteration < max_iterations:
  current_address = get_first_link(BeautifulSoup(get_html(current_address)))
  if verbose:
   print(current_address)
  if current_address in pages_visited:
   print("Boucle de " + str(iteration - pages_visited.index(current_address)) + " nœuds trouvée à partir de "+str(pages_visited.index(current_address))+" itérations")
   return
  elif current_address.lower() == target_page.lower():
   print(str(iteration) + " itérations pour arriver à la page Philosophie")
   return
  else:
   pages_visited.extend([current_address])
   iteration += 1
 return str(max_iterations)+" itérations atteintes"


if __name__ == "__main__":
  get_to_philosophy('Python_(langage)',verbose=True)
  get_to_philosophy('Spotify',verbose=True)
  get_to_philosophy('Obama',verbose=True)
  get_to_philosophy('Yoda',verbose=True)