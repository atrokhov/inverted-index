# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os


def create_indexes_for_file(document):
    tie = {}
    words = []
    with open(document) as opened_document:
        words = opened_document.read().split()
        tie = {document: words}
    return tie

def find_files():
    path =  os.getcwd()
    all_files = os.listdir(path)
    doc_files = []
    for i in all_files:
        if i.find('.txt') != -1:
            doc_files.append(i)
    return doc_files

def find_words(searching_word):
    ties = []
    for document in find_files():
        for key, value in create_indexes_for_file(document).iteritems():
            positions = [i for i, word in enumerate(value) if word == searching_word]
            tie = {key: positions}
    
            ties.append(tie)

    return ties