#	TO USE:
#	$ python test.py > start.txt
#	$ tr -d '\n' < start.txt > output.txt


import random

all = []
people = [33,41,46,50,55,9,11,12,20,21,28,29,32,74,75,87,88,89,100,109,121]
peopleslider = [3,2,5,4,16,17,18,24,26,25,27,37,45,64,68,69,75] 
events = [34,36,42,43,49,10,12,13,14,15,16,17,19,22,23,24,25,30,31,85,86,102,110,113,115]
eventsslider = [1,29,28,31,30,33,32,36,46,50,51,70]
harvard = [33,35,40,41,49,56,58,59,64,65,71,72,73,76,77,78,79,101,105]
harvardslider = [22,23,42,41,43,54,56,55,58,71,81]
nature = [38,44,45,47,48,51,52,53,60,61,66,67,68,69,70,81,82,90,91,92,93,94,95,96,97,98,99,108,116,117,118,119,120,123,124,125,126,127,128,129,130,131,132,133,134,135,136]
natureslider = [7,6,9,8,10,11,12,14,13,15,20,44,59,60,63,66,67,73,72,74,76,78,77,80,79,82,83,85,86,87,88,89,90,91,92]
assorted = [37,39,54,57,59,62,63,18,103,104,106,107,111,112,114,122]
assortedslider = [49,53,52,57,61,62,65,35,34,39,38,40,48,47,84]

for i in range(1, 119):
	all.append(i)

random.shuffle(people)
random.shuffle(events)
random.shuffle(harvard)
random.shuffle(nature)
random.shuffle(assorted)
random.shuffle(all)

# For the picture display
a = ''
b = ''
c = ''
d = ''
e = ''
f = ''
for i in all:
	a += ('<div class="qg-img" data-defwidth="435"><a href="/includes/img/photos/' + str(i) + '.jpg" data-rel="lightbox[group-14681]" title="" ><img src="/includes/img/photos/' + str(i) + '.jpg" alt=""/><div class="qg-overlay"><span class="icon-circle"><span class="pg-icon lightbox-icon"></span></span><span class="qg-title"></span></div></a></div>')
print ('----------VV--ALL_PHOTOS--VV----------')
print (a)
print ('----------VV--PEOPLE--VV----------')
for i in people:
	b += '<div class="qg-img" data-defwidth="435"><a href="/includes/img/photos/' + str(i) + '.jpg" data-rel="lightbox[group-14681]" title="" ><img src="/includes/img/photos/' + str(i) + '.jpg" alt=""/><div class="qg-overlay"><span class="icon-circle"><span class="pg-icon lightbox-icon"></span></span><span class="qg-title"></span></div></a></div>'
print (b)
print ('----------VV--EVENTS--VV----------')
for i in events:
	c += '<div class="qg-img" data-defwidth="435"><a href="/includes/img/photos/' + str(i) + '.jpg" data-rel="lightbox[group-14681]" title="" ><img src="/includes/img/photos/' + str(i) + '.jpg" alt=""/><div class="qg-overlay"><span class="icon-circle"><span class="pg-icon lightbox-icon"></span></span><span class="qg-title"></span></div></a></div>'
print (c)
print ('----------VV--HARVARD--VV----------')
for i in harvard:
	d += '<div class="qg-img" data-defwidth="435"><a href="/includes/img/photos/' + str(i) + '.jpg" data-rel="lightbox[group-14681]" title="" ><img src="/includes/img/photos/' + str(i) + '.jpg" alt=""/><div class="qg-overlay"><span class="icon-circle"><span class="pg-icon lightbox-icon"></span></span><span class="qg-title"></span></div></a></div>'
print (d)
print ('----------VV--NATURE--VV----------')
for i in nature:
	e += '<div class="qg-img" data-defwidth="435"><a href="/includes/img/photos/' + str(i) + '.jpg" data-rel="lightbox[group-14681]" title="" ><img src="/includes/img/photos/' + str(i) + '.jpg" alt=""/><div class="qg-overlay"><span class="icon-circle"><span class="pg-icon lightbox-icon"></span></span><span class="qg-title"></span></div></a></div>'
print (e)
print ('----------VV--ASSORTED--VV----------')
for i in assorted:
	f += '<div class="qg-img" data-defwidth="435"><a href="/includes/img/photos/' + str(i) + '.jpg" data-rel="lightbox[group-14681]" title="" ><img src="/includes/img/photos/' + str(i) + '.jpg" alt=""/><div class="qg-overlay"><span class="icon-circle"><span class="pg-icon lightbox-icon"></span></span><span class="qg-title"></span></div></a></div>'
print (f)
print ('----------VV--PEOPLE_SLIDER--VV')

# For the picture slider
aa = ''
bb = ''
cc = ''
dd = ''
ee = ''
for i in peopleslider:
	aa += '<img src="/includes/img/highres/slider' + str(i) + '.jpg" title="" alt="" />'
print (aa)
print ('----------VV--EVENTS_SLIDER--VV')
for i in eventsslider:
	bb += '<img src="/includes/img/highres/slider' + str(i) + '.jpg" title="" alt="" />'
print (bb)
print ('----------VV--HARVARD_SLIDER--VV')
for i in harvardslider:
	cc += '<img src="/includes/img/highres/slider' + str(i) + '.jpg" title="" alt="" />'
print (cc)
print ('----------VV--NATURE_SLIDER--VV')
for i in natureslider:
	dd += '<img src="/includes/img/highres/slider' + str(i) + '.jpg" title="" alt="" />'
print (dd)
print ('----------VV--ASSORTED_SLIDER--VV')
for i in assortedslider:
	ee += '<img src="/includes/img/highres/slider' + str(i) + '.jpg" title="" alt="" />'
print (ee)