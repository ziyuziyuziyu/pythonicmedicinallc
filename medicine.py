# import liabraries
import sys
import random
import codecs

# import liabrary of Pattern
from pattern.search import search

# import search
from pattern.search import Pattern, STRICT
from pattern.en import parsetree
from pprint import pprint

# test

# PREPERATION FOR EDITING
# codecs is a module that somehow solves a lot of encoding
# issues, i guess by encoding text right after opening it.



text_file = codecs.open(sys.argv[1], encoding='utf-8')
whole_text = ""
for line in text_file:
    line = line.strip()
    line = line.lower() 
    print type(line)
    whole_text += line + " "
# print type(text_file)
# print line



# t = parsetree(whole_text)
# print search_out(t, 'VB IN VB IN NN')
# print search('NN', t)
# line = "Cease to exist within society"
def find_all_matches_by_ziyu(text, the_pattern):
    tree = parsetree(text, lemmata=True)
    results = search( the_pattern  , tree, STRICT)
    # print results
    output = []
    for match in results:
        # print "[+]", match
        word_list = []
        for word in match:
            # print "\t", word
            # print "\t\t", word.string
            word_list.append(word.string)
        sentence = " ".join(word_list)
        output.append(sentence)

        # print "\n", sentence, "\n\n"
    return output

results = find_all_matches_by_ziyu(whole_text, 'VB JJ NNS|NN')
print "RESULTS:"
for result in results:
    print result

sys.exit()

# t = parsetree('Dolph Lundgren is cooler than Frank.', lemmata=True)
# p = Pattern.fromstring('{VB} {TO} {VB} {IN} {NN}')
p = Pattern.fromstring('{V*}')

m = p.match(t)
print m

sys.exit()
# NAME OF DRUG
# take the title's first word, first three letters
# combine with suffixes ["phrin","ytril","syn","xyzal","yrhil","nexx"]

print('\n' * 4)
print " "*10 + "NAME OF DRUG" + ":"


# SHORT DESCRIPTION OF DRUG
# example: 100% grass fed supplement for cultrual materialism
print('\n' * 1)
print " "*10 + "DRUG DESCRIPTION" + ":"


# ACTIVE INGREDIENTS
# ??? what should the ingredients be ???
print('\n' * 2)
print " "*10 + "ACTIVE INGREDIENTS" + ":"


# WARNINGS
# print "when using this product"
print('\n' * 2)
print " "*10 + "WARNINGS" + ":"
print " "*10 + "when using this product you may"



# DIRECTIONS
# example: take 5 tablets every 4 months (a verb + random int + tablets + every + random int + second/minute/hour/day)
print('\n' * 2)
print " "*10 + "DIRECTIONS" + ":"




# EXPIRATION DATE
# 2017.x - 3000.x
print('\n' * 2)
print " "*10 + "EXPIRATION DATE" + ":"
print('\n' * 5)







