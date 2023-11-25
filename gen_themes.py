import random


students = []
themes = []
itog=[]

with open('students.txt', 'r', encoding='utf-8') as fil01:
    for line in fil01:
        #print(line)
        students.append(line.replace('\n','').split(','))


with open('zadaniy.txt', 'r', encoding='utf-8') as fil02:
    for line in fil02:
        themes.append(line.replace('\n','').split(','))
        

#print(students)
#print(themes)  


with open('itog.txt', 'w', encoding='utf-8') as fil03:
    for element in students:
        thema = random.choice(themes)
        themes.pop(themes.index(thema))
        print(str(element) + ' ==> ' + str(thema)+'\n')
        fil03.write(str(element) + ' ==> '  + str(thema)+'\n')
        itog.append(str(element) + '  ==> ' + str(thema))
#print (endless)
print('================================')  
#print(itog)  
