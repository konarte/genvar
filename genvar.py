import random


groupe = []
spisok = []
itog =[]
variant = ''

with open('spisok.txt','r', encoding="utf-8", errors='ignore') as f01:
    for line in f01:
        groupe.append(line.replace("\n",""))
        
with open('zadaniy.txt','r', encoding="utf-8", errors='ignore') as f02:
    for line in f02:
        spisok.append(line.replace("\n",""))

print (groupe)
print (spisok)

for element in groupe:
    variant = random.choice(spisok)
    spisok.pop(spisok.index(variant))
    #print('==================================')
    #print(spisok)
    itog.append(str(element)+' '+ str(variant))

#print (itog)
with open('itog.txt','w', encoding="utf-8") as f03:
    for element in itog:
        print(int(itog.index(element))+1, element)
        f03.write(str(int(itog.index(element))+1) +' '+ str(element) + '\n')
    
    
    
