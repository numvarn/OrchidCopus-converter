#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk.corpus
import codecs

path = nltk.data.find('orchid97.txt')
outfile_path = './csv/orchid-utf8.csv'

header = ['thai', 'pos']
header_str = ','.join(header).encode('utf-8')+'\n'
with open(outfile_path, 'a') as outfile:
    outfile.write(header_str)

lines = codecs.open(path,encoding='utf-8').readlines()
for line in lines:
    line = line.rstrip('\n')
    if line[0]!='%' and line[0]!='#' and line[0]!='<' and line[0]!='/':
        token = line.split('/')
        if len(token) == 2:
            print "%s : %s\n" %(token[0], token[1])
            csv_line = ",".join(token).encode('utf-8')+'\n'

            with open(outfile_path, 'a') as outfile:
                outfile.write(csv_line)
