# Ouverture du fichier sample.txt
text = open("sample.txt", "r") 

# Creation d'un dictionaire vide
d = dict() 

for line in text:
    # Supprimez les espaces de début et le caractère de nouvelle ligne
    line = line.strip() 
    
    #separation des mots dans une ligne
    words = line.split(" ") 

    # Comptage de nombre de chaque mot
    for word in words: 
        if word in d: 
            d[word] = d[word] + 1
        else: 
            d[word] = 1
            
# Affichage des résultats sous forme des Tuples
for key in list(d.keys()): 
       print("(",key, ",", d[key],")")

### Hello
print('wordCount')
