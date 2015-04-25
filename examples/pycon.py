#!/usr/bin/env python2
"""
Masked wordcloud
================
Using a mask you can generate wordclouds in arbitrary shapes.
"""

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# Read the whole text.
text = open(path.join(d, 'pycon2015.txt')).read()

# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
pycon_mask = imread(path.join(d, "pycon2015.png"))

wc = WordCloud(background_color="white", max_words=2000, mask=pycon_mask,
               stopwords=STOPWORDS.add("things"))
# generate word cloud
wc.generate(text)

# store to file
wc.to_file(path.join(d, "pycon.png"))

# show
plt.imshow(wc)
plt.axis("off")
plt.figure()
plt.imshow(pycon_mask, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
