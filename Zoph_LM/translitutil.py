#! /usr/bin/env python
import argparse
import sys
import codecs

# utilities for transliteration

escmap = {'"':"QUOTE",
          '_':"UNDERSCORE",
          '\\':"BACKSLASH"}

invescmap = dict((v,k) for k, v in escmap.iteritems())


