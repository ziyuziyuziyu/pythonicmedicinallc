import sys, codecs, random, re
from pattern.search import search, Pattern, STRICT
from pattern.en import parsetree
from random import randint


import tracery
from tracery.modifiers import base_english


# TITLE
def get_title(text):
    with open(text, 'r') as f:
        title = f.readline().strip().lower()
    return title

# NAME OF DRUG
# take the title's first word, first three letters
# combine with suffixes ["phrin","ytril","syn","xyzal","yrhil","nexx"]
def generate_drug_name(text):
    with open(text, 'r') as f:
        first_line = f.readline().strip().lower()
        first_line_words = first_line.split(" ")

        char_list = list(first_line_words[0])
        alpha_list = list()
        for char in char_list:
            alpha_list.append(char)
        first_three_letters = "".join(alpha_list[0:3])

        drug_suffixes = ["phrin","ytril","syn","xyzal","yrhil","nexx"]
        random_suffix = drug_suffixes[randint(0,5)]

    # return first_line_words
    return first_three_letters + random_suffix


# WARNINGS
# print "when using this product, you might"
def find_all_matches_by_ziyu(text, the_pattern):
    tree = parsetree(text, lemmata=True)
    results = search( the_pattern  , tree, STRICT)
    output = []
    for match in results:
        word_list = []
        for word in match:
            word_list.append(word.string)
        sentence = " ".join(word_list)
        output.append(sentence)
    
    # gen_num = 0
    # if len(output) > 0 and len(output)<2:
    #     gen_num=1
    # elif len(output) >= 2:
    #     gen_num=2

    # random_number = []
    
    # while len(random_number) != gen_num:
    #     r = random.randint(0,len(output))
    #     if r not in random_number:
    #         random_number.append(r)

    # final_output = []

    # if len(output) > 0:
    #     print "have OUTPUT"
    #     print random_number
    #     for i in range(gen_num):
    #         print i
    #         final_output.append(output[random_number[i]])

    return output


# READING THE FILE
def get_raw_text_from_file_with_codecs(text_file, title):
    text_file = codecs.open(text_file, encoding='utf-8')
    whole_text = ""
    for line in text_file:
        line = line.strip()
        line = line.lower() 
        whole_text += line + " "
        
    titles = title.split()

    for t in titles:
        whole_text = re.sub(t.lower(),'',whole_text)
    return whole_text





# ***********************************************
# HERE IS WHERE THE PROGRAMMING START
if __name__ == "__main__":
    
    # OPEN TEXT FILE
    title = get_title(sys.argv[1])
    text = get_raw_text_from_file_with_codecs(sys.argv[1], title)

    # GET DRUG NAME
    first = generate_drug_name(sys.argv[1])
    

    #title_words = title.split()
    #a = str(title_words[0])
    #b = str(title_words[1])




    # NAME OF DRUG
    print('\n' * 4)
    print " "*10 + "NAME OF DRUG" + ":"
    print " "*10 + first


    # DESCRIPTION
    # SHORT DESCRIPTION OF DRUG
    # example: 100% grass fed supplement for cultrual materialism
    rules = {
    'origin': '#grassfed# #supplement# for ',
    # 'percentage': ['100%', '90%', '85%', '30%','','','','','20%'],
    'grassfed': ['grass fed', 'vegan', 'natural artificial intelligence', 'natural falvored','food based','gluten free','cage free'],
    'supplement': ['supplement', 'aid', 'tablets', 'drug', 'antidepressant'],
    }

    grammar = tracery.Grammar(rules)
    grammar.add_modifiers(base_english)
    print('\n' * 2)
    print " "*10 + "DRUG DESCRIPTION" + ":"
    print " "*10 + grammar.flatten("#origin#") + title + " syndrome"


    # ACTIVE INGREDIENTS
    # ??? what should the ingredients be ???
    print('\n' * 2)
    print " "*10 + "ACTIVE INGREDIENTS" + ":"
    pattern = 'JJ NNS'
    results = find_all_matches_by_ziyu(text, pattern)


    for result in results:
        # if result.isalpha():
        if title.lower() not in result.lower():
            print " "*10 + result + " ............... " + str(random.randint(1,9)) + "mg" 


    # WARNINGS
    # need to fix (1) repeating title issues (2) repeating lines
    print('\n' * 2)
    print " "*10 + "WARNINGS" + ":"
    print " "*10 + "WHEN USING THIS PRODUCT YOU MAY"

    pattern = 'VB JJ NNS|NN'
    results = find_all_matches_by_ziyu(text, pattern)
    for result in results:
        print " "*10 + result

    pattern = 'VB|VBP TO VB IN NN'
    results = find_all_matches_by_ziyu(text, pattern)
    for result in results:
        print " "*10 + result

    pattern = 'VB|VBP TO VB'
    results = find_all_matches_by_ziyu(text, pattern)
    for result in results:
        print " "*10 + result




    # pattern = 'VP'
    # results = find_all_matches_by_ziyu(text, pattern)
    # for result in results:
    #     print " "*10 + result
    # # pattern = 'VB|VBP RB' doesn't work

    # EXPIRATION DATE
    # 2017.x - 3000.x
    print('\n' * 2)
    print " "*10 + "EXPIRATION DATE" + ":"
    print " "*10 + str(random.randint(2018,2100)) + "." + str(random.randint(1,12))
    print('\n' * 5)