#!/usr/bin/.env python3
"""
Utility for parsing HTML5 entity definitions available from:

    http://dev.w3.org/html5/spec/entities.json

Written by Ezio Melotti and Iuliia Proskurnia.

"""

import os
import sys
import json
from urllib.request import urlopen
from html.entities import html5

entities_url = 'http://dev.w3.org/html5/spec/entities.json'

def get_json(url):
    """Download the json file from the url and returns a decoded object."""
    with urlopen(url) as f:
        data = f.read().decode('utf-8')
    return json.loads(data)

def create_dict(entities):
    """Create the html5 dict from the decoded json object."""
    new_html5 = {}
    for name, value in entities.items():
        new_html5[name.lstrip('&')] = value['characters']
    return new_html5

def compare_dicts(old, new):
    """Compare the old and new dicts and print the differences."""
    added = new.keys() - old.keys()
    if added:
        print('{} entitie(s) have been added:'.format(len(added)))
        for name in sorted(added):
            print('  {!r}: {!r}'.format(name, new[name]))
    removed = old.keys() - new.keys()
    if removed:
        print('{} entitie(s) have been removed:'.format(len(removed)))
        for name in sorted(removed):
            print('  {!r}: {!r}'.format(name, old[name]))
    changed = set()
    for name in (old.keys() & new.keys()):
        if old[name] != new[name]:
            changed.add((name, old[name], new[name]))
    if changed:
        print('{} entitie(s) have been modified:'.format(len(changed)))
        for item in sorted(changed):
            print('  {!r}: {!r} -> {!r}'.format(*item))

def write_items(entities, file=sys.stdout):
    """Write the items of the dictionary in the specified file."""
    # The keys in the generated dictionary should be sorted
    # in a case-insensitive way, however, when two keys are equal,
    # the uppercase version should come first so that the result
    # looks like: ['Aacute', 'aacute', 'Aacute;', 'aacute;', ...]
    # To do this we first sort in a case-sensitive way (so all the
    # uppercase chars come first) and then sort with key=str.lower.
    # Since the sorting is stable the uppercase keys will eventually
    # be before their equivalent lowercase version.
    keys = sorted(entities.keys())
    keys = sorted(keys, key=str.lower)
    print('html5 = {', file=file)
    for name in keys:
        print('    {!r}: {!a},'.format(name, entities[name]), file=file)
    print('}', file=file)


if __name__ == '__main__':
    # without args print a diff between html.entities.html5 and new_html5
    # with --create print the new html5 dict
    # with --patch patch the Lib/html/entities.py file
    new_html5 = create_dict(get_json(entities_url))
    if '--create' in sys.argv:
        print('# map the HTML5 named character references to the '
              'equivalent Unicode character(s)')
        print('# Generated by {}.  Do not edit manually.'.format(__file__))
        write_items(new_html5)
    elif '--patch' in sys.argv:
        fname = 'Lib/html/entities.py'
        temp_fname = fname + '.temp'
        with open(fname) as f1, open(temp_fname, 'w') as f2:
            skip = False
            for line in f1:
                if line.startswith('html5 = {'):
                    write_items(new_html5, file=f2)
                    skip = True
                    continue
                if skip:
                    # skip the old items until the }
                    if line.startswith('}'):
                        skip = False
                    continue
                f2.write(line)
        os.remove(fname)
        os.rename(temp_fname, fname)
    else:
        if html5 == new_html5:
            print('The current dictionary is updated.')
        else:
            compare_dicts(html5, new_html5)
            print('Run "./python {0} --patch" to update Lib/html/entities.html '
                  'or "./python {0} --create" to see the generated ' 'dictionary.'.format(__file__))
