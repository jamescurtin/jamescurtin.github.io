#	TO USE:
#	$ python photo_html_generator.py

import random

# 	List 1 is normal display
# 	List 2 is the slider
people1 = [33,41,46,50,55,9,11,12,20,21,28,29,32,74,87,88,89,100,109,121]
people2 = [3,2,5,4,16,17,18,24,26,25,27,37,45,64,68,69,75]

events1 = [34,36,42,43,49,10,12,13,14,15,16,17,19,22,23,24,25,30,31,85,86,102,110,113,115]
events2 = [1,29,28,31,30,33,32,36,46,50,51,70]

harvard1 = [33,35,40,41,49,56,58,59,64,65,71,73,76,77,79,101,105]
harvard2 = [22,23,42,41,43,54,56,55,58,71,81]

nature1 = [38,44,45,47,48,51,52,53,60,61,66,67,68,69,70,81,82,90,91,92,93,94,95,96,97,98,99,108,116,117,118,119,120,123,124,125,126,127,128,129,130,131,132,133,134,135,136]
nature2 = [7,6,9,8,10,11,12,14,13,15,20,44,59,60,63,66,67,73,72,74,76,78,77,80,79,82,83,85,86,87,88,89,90,91,92]

assorted1 = [37,39,54,57,59,62,63,18,103,104,106,107,111,112,114,122]
assorted2 = [49,53,52,57,61,62,65,35,34,39,38,40,48,47,84]

slider404 = [5,8,10,11,13,18,19]


class Page(object):
    def __init__(self, name, pictures):
        self.name = name
        self.pictures = pictures

def genHTML(photoList, html):
	for i in photoList:
		base = ''
		shuffled = random.sample(i.pictures, len(i.pictures))
		for j in shuffled:
			if len(html) == 3:
				base += html[0] + str(j) + html[1] + str(j) + html[2]
			else:
				base += html[0] + str(j) + html[1]
		file = open("../_includes/" + i.name + ".html", "w")
		file.write(base)
		file.close()

people = Page("people", people1)
peopleslider = Page("peopleslider", people2)
events = Page("events", events1)
eventsslider = Page("eventsslider", events2)
harvard = Page("harvard", harvard1)
harvardslider = Page("harvardslider", harvard2)
nature = Page("nature", nature1)
natureslider = Page("natureslider", nature2)
assorted = Page("assorted", assorted1)
assortedslider = Page("assortedslider", assorted2)
slider_404 = Page("slider_404", slider404)
mergedlist = Page("mergedlist", list(set(people.pictures + events.pictures + harvard.pictures + nature.pictures + assorted.pictures)))

biglist1 = [people,events,harvard,nature,assorted,mergedlist]
biglist2 = [peopleslider,eventsslider,harvardslider,natureslider,assortedslider, slider_404]

html1 = ['<div class="qg-img" data-defwidth="435"><a href="/includes/img/photos/','.jpg" data-rel="lightbox[group-14681]" title="" ><img src="/includes/img/photos/','.jpg" alt=""/><div class="qg-overlay"><span class="icon-circle"><span class="pg-icon lightbox-icon"></span></span><span class="qg-title"></span></div></a></div>']
html2 = ['<img src="/includes/img/highres/slider','.jpg" title="" alt="" />']

genHTML(biglist1, html1)
genHTML(biglist2, html2)