#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Xing-hong Zhong"
__pkuid__  = "1700012608"
__email__  = "zxh2017@pku.edu.cn"
"""

import sys
from urllib.request import urlopen
import string

def common(d, topn):
    dd = []
    for word, num in d.items() :
        dd.append((num, word))
    dd.sort(reverse=True)
    return dd

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """

    d = dict()
    lines.replace('-',' ')
    for word in lines.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        d[word] = d.get(word, 0) + 1
    del d['']

    dd = common(d, topn)
    for i in range(topn):
        print(dd[i][1], dd[i][0] ,sep = '\t')

    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
