from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]
        
def process_madlib(mad_lib):
    processed = ""
    # your code here
    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len
    if mad_lib.find('NOUN') != -1 :
        word = 'NOUN'
        x = mad_lib.find('NOUN')
        y = mad_lib[:x] + word_transformer(word) + mad_lib[x+4:]  
        if mad_lib.find('VERB') != -1 :
            word = 'VERB'
            z = mad_lib.find('VERB')
            f = y[:z] +" "+ word_transformer(word) + " "+ y[z+5:]
            return f
test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)
