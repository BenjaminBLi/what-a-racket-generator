#Stuff for primitives
alphabet = ['#\\'+chr(ord('a')+i) for i in range(26)]
special_chars = ["#\\newline", "#\\space"]
digits = ['#\\' + str(i) for i in range(10)]

chars = alphabet + special_chars + digits

#Stuff for structs

primitives = ('Bool', 'Num', 'Float', 'Char', 'Str', 'Nat')
