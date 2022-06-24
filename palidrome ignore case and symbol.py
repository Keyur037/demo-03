d=["Go hanga salami I'm a lasagna hog.","Was it a rat i saw ?",\
   'Step on nopets','Sit on a potato pan, Otis','LisaBonet ate no basil',\
   'Satan, oscillate my metallic sonatas','I roamed under it as a tired nude Maori',\
   'Rise to vote sir','Dammit, I\'m mad!']


for i in d:
    e='' 
    for j in i:
        if j.isalpha():
            e+=j
    if e.lower()[:]==e.lower()[::-1]:
        print(d.index(i),'string is palindrome')
    else:
        print(d.index(i),"string is not palindrome")
        
       

        




