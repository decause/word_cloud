#!/usr/bin/env python2
"""
Using custom colors
====================
Using the recolor method and custom coloring functions.
"""

from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import random

from wordcloud import WordCloud, STOPWORDS


def grey_color_func(word, font_size, position, orientation, random_state=None):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

d = path.dirname(__file__)

# read the mask image
# taken from
mask = imread(path.join(d, "Fedora_logo_simple.png"))

# preprocessing text to remove timestamps
filename = "infrastructure.2015-04-30-18.00.log.txt"

with open(filename, "r") as f:
    lines = f.readlines()

# Strip timestamp and the nick of speakers
lines = [
    line[8:].split('> ', 1)[-1].split(' * ', 1)[-1].strip()
    for line in lines
    if line.strip()
]

text = "".join(lines)


# preprocessing the text a little bit
text = text.replace("HAN", "Han")
text = text.replace("LUKE'S", "Luke")

# adding movie script specific stopwords
stopwords = STOPWORDS.copy()
stopwords.add("int")
stopwords.add("ext")

wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10,
               random_state=1).generate(text)

# store default colored image
default_colors = wc.to_array()
plt.title("Custom colors")
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3))
wc.to_file("fedora-mail-cloud.png")
# wc.to_file('%s' + ".png") %s filename
plt.axis("off")
plt.figure()
plt.title("Default colors")
plt.imshow(default_colors)
plt.axis("off")
plt.show()
