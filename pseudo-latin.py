import pytest

vow = ['e','y','u','i','o','a']
sizz = ['ch', 'thr', 'sch', 'th', 'rh','qu']

def convert(s):
    array = []
    array = s.split()
    for n in range(len(array)):
        word = array[n]
        word = word.lower()

        if word[0] in vow or word[:2] == "xr":
            array[n] = word + "ay"

        elif word[:3] in sizz or word[1:3]=='qu':
            if word[3] == 'y':
                array[n] = (word[4:]+word[:4]+"ay")
            else:
                array[n] = (word[3:]+word[:3]+"ay")

        elif word[:2] in sizz:
            if word[2]=='y':
                array[n] = (word[3:]+word[:3]+"ay")
            else:
                array[n] = (word[2:]+word[:2]+"ay")
        
        elif word[0] not in vow:
            array[n] = (word[1:]+word[0]+"ay")
    if len(array) == 1:
        return array[0]
    else:
        return (" ".join(array))

print(convert("Good day Urmo chmo throu squaer thrytm"))

def test_passing():
    assert convert("three") == "eethray"
    assert convert("good day") == "oodgay ayday"
    assert convert("user") == "useray"
    assert convert("it") == "itay"
    assert convert("xray") == "xrayay"
    assert convert("Incredibly large basket of delicious apples") == "incrediblyay argelay asketbay ofay eliciousday applesay"
    
    

