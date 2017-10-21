# -*- coding: utf-8 -*-

import glob
import os
import re
from builtins import any as b_any
from collections import Counter


# Core Data-Gathering
def get_files(path, extensions):
    """
    Returns a set of files as discovered recursively
    in the provided config_path, so long as it matches
    the allowed file extensions.

    param: config_path (str) the directory containing files to search through
    param: extension (list) acceptable file extensions for files to include
    """
    all_files = list()
    for ext in extensions:
        # Get a list of all files matching our preferred extensions
        found_files = \
            [file for file in glob.iglob(path + '/**/*{}'
             .format(ext), recursive=True) if os.path.isfile(file)]
        for file in found_files:
            all_files.append(file)
    # return a set of files to attempt to remove duplicates
    return set(all_files)


def get_tags(files, mod, search):
    """
    Returns a dictionary of tags, stripped of their identifier for sorting and
    parsing. Dictionary values found in the following format:

    { 'tag': 'count_of_tag' }

    param: files  -- (list/set) list/set of files to parse
    """
    tags = Counter()
    construct = mod + search
    for file in files:
        with open(file, 'r') as fl:
            contents = fl.read()
            taglist = set(re.findall(construct, contents))
            tags.update([item.strip(mod) for item in taglist])
    # return dictionary (from counter), may be adjusted later
    return dict(tags)


def search(files, mod, tag, search):
    """
    Return a dictionary of files containing the specific tag,
    as well as the tags that exist in those files for additional
    context to be provided to the user.
    """

    # construct relevant pieces
    search_construct = mod + search

    tags_per_file = dict()

    for file in files:
        with open(file, 'r') as fl:
            contents = fl.read()
            # get all tags in a file
            taglist = set(re.findall(search_construct, contents))
            # strip modifier from all tags
            taglist_stripped = [tag.strip(mod) for tag in taglist]
            # substring match our tag against the items in taglist_stripped
            if b_any(tag in tags for tags in taglist_stripped):
                # file contains a match, store all tags for context
                tags_per_file[file] = taglist_stripped
    return tags_per_file


# output control
def pprint_tags(tags):
    counter = 0
    alphabetical = sorted(tags.keys())
    for key in alphabetical:
        if counter < 2 and key != alphabetical[-1]:
            counter += 1
            print("{:4} {:30}".format(tags[key], key), end="")
        else:
            counter = 0
            print("{:4} {}".format(tags[key], key))


def pprint_files(files):
    for item in files.keys():
        print('{:70} {:6}'.format(item, "TAGS: "), end=" ")
        for tag in files[item]:
            print(tag, end=" ")
        print()
