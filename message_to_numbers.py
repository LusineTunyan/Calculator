mydict = {
        1:".,?!:",
        2:"ABC",
        3:"DEF",
        4:"GHI",
        5:"JKL",
        7:"PQRS",
        8:"TUV",
        9:"WXYZ",
        0:" "
}

text=input('Enter your message: ').upper()
numbers= ''
for i in text:
    for j in mydict:
        if i in mydict[j]:
            numbers+=str(j)*(mydict[j].index(i)+1)
print(numbers) 