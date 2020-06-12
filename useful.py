import sys


# Persistently prompt the user until user input is in the sequence "lst"
def p_prompt(prompt, lst):
    while True:
        ans = input(prompt)
        if ans not in lst:
            print('Invalid choice!')
            print()
            continue
        return ans


# Class for multi-key dictionary. Use the .get(key) method to find the value. Multiple keys can return the same value.
class DictPlus():
    def __init__(self, dictionary):
        if type(dictionary) == dict:
            self.dictionary = dictionary
        else:
            self.dictionary == dict(dictionary)

    def get(self, ke):
        self.dictionary = self.dict_expand()
        for key in self.dictionary:
            if (ke == key) or (ke in key):
                return self.dictionary[key]


    def help(self):
        help_msg = '''
Use the DictPlus class to give your dictionary the ability to return a dictionary value from than one dictionary key.

* Syntax:
    dict_plus = DictPlus(arg)
        - 'arg' could either be a type dict variable, or a sequence such that type( dict(sequence) ) == dict 

* Methods:
    - DictPlus.get(key)
        returns the dictionary value if 'key' is among the dictionary keys, or in a sequence within a key
        
'''

