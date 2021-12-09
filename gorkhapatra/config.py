############################################################################
'''
Configuration for Gorkhapatra Scraper

This entire site is divided into many topics and subtopics. 
Topics and their page count are given below.

Visit https://gorkhapatraonline.com/mainnews to understand the structre
of this site.

Each page links to 5 articles.

⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ 
Careful while while setting very high index value. Beacuse while topics like 
mainnews and nationalnews will have valid links but others like interview will not.
And hence script will iterate for a long time only to get 404 errors.   

⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ ⚠️ 
'''
############################################################################

COUNT = {
    'mainnews': 1192,
    'national': 1122,
    'economics': 912,
    'opinion': 734,
    'entertainment': 81,
    'loksewa': 31,
    'interview': 28,


}
TOPICS = ['mainnews', 'national', 'economics',
          'opinion', 'entertainment', 'loksewa', 'interview']

START_INDEX = 1
END_INDEX = 2
