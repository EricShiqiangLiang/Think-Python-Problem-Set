def shift_n_letters(letter, n):
    return chr(((ord(letter) % 97 + n) % 26) + 97)

def rotate(s, n):
    res = ''
    for letter in s:
        if letter != ' ':
            res =  res + shift_n_letters(letter, n)
        else:
            res = res + ' '
    return res
    

print (rotate('sarah', 13))
#>>> 'fnenu'
print (rotate('fnenu',13))
#>>> 'sarah'
print (rotate('dave',5))
#>>>'ifaj'
print (rotate('ifaj',-5))
#>>>'dave'
print (rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
                "sv rscv kf ivru kyzj"),-17))