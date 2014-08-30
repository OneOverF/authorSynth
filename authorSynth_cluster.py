#!/usr/bin/python

# This is to run for a single author (on Sherlock cluster)
# Usage : authorSynth_cluster.py uuid "author" email outdirectory
# Use this script if you have a pre-set of doi or pmid to look up
# If you want to query pubmed and crosslist with neurosynth
# database, use authorSynth_cluster_pubmed.py

# import authorSynth module
import authorSynth as AS
import sys
import re

# Get arguments
uuid = sys.argv[1]
author = sys.argv[2]
outdirectory = sys.argv[3]
ids = sys.argv[4]

papers = ids.split(",")
if bool(re.search("[/]",ids[0])):
  print "Input are DOI."
else:
  print "Input are pmid."

# Init Neurosynth database, use "3000" terms
db = AS.neurosynthInit("3000")

print "Processing author " + author
ma = AS.neurosynthMatch(db,papers,author,outdirectory,uuid)

