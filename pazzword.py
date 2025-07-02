from random import choice

note_names = ("C", "D", "E", "F", "G", "A", "B")
accidentals = ("#", "b")
sevenths = ("maj7", "m7", "7")
extensions = ("b9", "5b", "b13")
slash = ("/")
elements = (note_names, accidentals, sevenths, extensions, slash, note_names)

def make_pazzword() -> str:
    pazzword = "|"
    for i in range(2):
        
        for element_tuple in elements:
            pazzword += choice(element_tuple)
        pazzword += "|"
        
    return pazzword 
    
print(make_pazzword())