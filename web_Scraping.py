import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

################
# This script get the audio book names and rating
# from audible.com and put that in CSV file

f = open("books.csv", 'w')

def get_data(url):
	data= requests.get(url).text
	print(url)
	soup = BeautifulSoup(data, "html.parser")
#print(soup.head)
	html_rating =soup.find_all(class_={"bc-text bc-pub-offscreen","bc-link bc-color-link" })
#
#	print(html_rating[6].text)
	pd_found = False

	for x in range (0, len(html_rating)):
		if('class="bc-link bc-color-link" href="/pd/' in str(html_rating[x])  ): 
			if (str(html_rating[x].text.strip() )):
				f.write( (html_rating[x].text))
		#	print( " I am x " , x)
				pd_found =True
			for n in range(0,2):
				if pd_found:
					if('star' in str(html_rating[x+n])):
						f.write(", ")
						f.write(html_rating[x+n].text )
						f.write("\n")
				#		print("XXXXXXXXXXXXXXXXXXX \n\n\n\n\n")
						pd_found = False
	


	
for  n in  range(0,26):
	print(f"page {n} is being processed. \n")
	
	url = f"https://www.audible.com/search?keywords=book&node=18573211011&page={n}"
	
	print(url)
	get_data(url)
