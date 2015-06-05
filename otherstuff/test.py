#	TO USE:
#	$ python test.py > start.txt
#	$ tr -d '\n' < start.txt > output.txt


import random

all = []
people = [33,41,46,50,55,9,11,12,20,21,26,27,28,29,32,74,75,78,84]
events = [34,36,42,43,49,10,12,13,14,15,16,17,19,22,23,24,25,30,31]
harvard = [33,35,40,41,49,56,58,59,64,65,71,72,73,76,77,78,79]
nature = [38,44,45,47,48,51,52,53,60,61,66,67,68,69,70,80,81,82,83]
assorted = [37,39,54,57,59,62,63,18]

for i in range(1, 84):
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
for i in people:
	aa += '<img src="/includes/img/photos/' + str(i) + '.jpg" title="" alt="" />'
print (aa)
print ('----------VV--EVENTS_SLIDER--VV')
for i in events:
	bb += '<img src="/includes/img/photos/' + str(i) + '.jpg" title="" alt="" />'
print (bb)
print ('----------VV--HARVARD_SLIDER--VV')
for i in harvard:
	cc += '<img src="/includes/img/photos/' + str(i) + '.jpg" title="" alt="" />'
print (cc)
print ('----------VV--NATURE_SLIDER--VV')
for i in nature:
	dd += '<img src="/includes/img/photos/' + str(i) + '.jpg" title="" alt="" />'
print (dd)
print ('----------VV--ASSORTED_SLIDER--VV')
for i in assorted:
	ee += '<img src="/includes/img/photos/' + str(i) + '.jpg" title="" alt="" />'
print (ee)