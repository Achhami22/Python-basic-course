#  Write a program to fill in a letter template given below with name and date.
# letter = ''' Dear <|NAME|>,

# You are selected!
# <|DATE|>'''

letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''

print(letter.replace("<|Name|>", "Sabina").replace("<|Date|", "02 feb 2002"))