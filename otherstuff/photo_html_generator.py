import random
import csv

# 	List 1 is normal display
# 	List 2 is the slider
portrait1 = [
    1, 149, 103, 118, 2, 3, 146, 4, 119, 10, 20, 22, 40, 101, 78, 127, 84, 147,
    85, 124, 86, 96, 100, 102, 105, 125, 31, 126, 113, 120, 122, 123,
]
portrait2 = [
    1, 149, 103, 2, 20, 146, 4, 40, 96, 100, 127, 101, 118,
    ]

events1 = [
    69, 103, 5, 21, 30, 145, 87, 40, 41, 58, 59, 60, 61, 62, 64, 68, 79, 88,
    89, 116, 92, 93, 95, 99, 100, 101, 104, 105, 110, 115,
]
events2 = [69, 62, 61, 40, 60, 145, 100,]

harvard1 = [
    6, 7, 8, 9, 111, 121, 11, 58, 68, 79, 90, 27, 91,
    ]
harvard2 = [
    8, 121, 27, 11, 91, 68, 111,
    ]

nature1 = [
    152, 12, 142, 129, 139, 15, 130, 16, 132, 18, 19, 134, 136, 25, 28, 144,
    108, 29, 33, 34, 35, 36, 37, 38, 43, 44, 109, 45, 46, 47, 48, 49, 50, 51,
    52, 53, 54, 55, 56, 65, 112, 70, 71, 72, 73, 75, 77, 80, 13, 14, 17, 81,
    82, 117, 83, 42, 57, 150, 151, 153, 154, 155,
]
nature2 = [152, 129, 19, 132, 75, 134, 53, 108, 15, 16, 33, 44, 81,]

reader = csv.DictReader(open('../_data/photo_info.csv'))
result = {}
for row in reader:
    key = row.pop('id')
    if key in result:
        pass
    result[key] = row


class Page(object):
    def __init__(self, name, pictures):
        self.name = name
        self.pictures = pictures


def genHTML(photoList, html):
    for i in photoList:
        base = ''
        if i.name == "slider_404":
            shuffled = random.sample(i.pictures, 10)
        elif i.name == "mergedlist":
            shuffled = random.sample(i.pictures, len(i.pictures))
        else:
            shuffled = i.pictures

        for j in shuffled:
            slug = str(j)
            if len(html) == 6:
                base += (html[0] + slug + html[1] + result[slug]["caption"] +
                         html[2] + slug + html[3] + result[slug]["alt"] +
                         html[4] + result[slug]["title"] + html[5])
            else:
                base += html[0] + slug + html[1] + result[slug]["title"] + html[2] + result[slug]["alt"] + html[3]
        file = open("../_includes/" + i.name + ".html", "w")
        file.write(base)
        file.close()


portrait = Page("portrait", portrait1)
portraitslider = Page("portraitslider", portrait2)
events = Page("events", events1)
eventsslider = Page("eventsslider", events2)
harvard = Page("harvard", harvard1)
harvardslider = Page("harvardslider", harvard2)
nature = Page("nature", nature1)
natureslider = Page("natureslider", nature2)
slider_404 = Page("slider_404",
                  set(events.pictures + harvard.pictures + nature.pictures))
mergedlist = Page(
    "mergedlist",
    list(
        set(portrait.pictures + events.pictures +
            harvard.pictures + nature.pictures)))

biglist1 = [
    portrait, events, harvard, nature, mergedlist
    ]
biglist2 = [
    portraitslider, eventsslider, harvardslider, natureslider, slider_404
    ]

html1 = [
    '<div class="qg-img" data-defwidth="435"><a href="/includes/img/highres/highres_',
    '.jpg" data-rel="lightbox[1]" title=" ',
    '" ><img src="/includes/img/photos/photo_', '.jpg" alt="', '''
            "/><div class="qg-overlay"><span class="icon-circle"><span class="pg-icon lightbox-icon">
            </span></span><span class="qg-title">
            ''', '</span></div></a></div>'
]

html2 = [
    '<img src="/includes/img/highres/highres_', '.jpg" title="', '" alt="', '" />'
]

genHTML(biglist1, html1)
genHTML(biglist2, html2)
