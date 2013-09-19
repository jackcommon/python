import math

adict = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
    '10': 'ten',
    '11': 'eleven',
    '12': 'twelve',
    '13': 'thirteen',
    '14': 'fourteen',
    '15': 'fifteen',
    '16': 'sixteen',
    '17': 'seventeen',
    '18': 'eighteen',
    '19': 'nineteen',
    '20': 'twenty',
    '30': 'thirty',
    '40': 'forty',
    '50': 'fifty',
    '60': 'sixty',
    '70': 'seventy',
    '80': 'eighty',
    '90': 'ninety',
    }
print(adict)

result = 0
for i in range(1,1000):
    s = str(i)
    explain = ''
    while len(s) != 0:
        c = s[0]
        if c!= '0':
            if len(s) == 3:
                if s[1:] == '00':
                    explain += adict[c]+'hundred'
                    break
                else:
                    explain += adict[c]+'hundredand'
            elif len(s) == 2:
                if s in adict:
                    explain += adict[s]
                    break
                else:
                    explain += adict[c+'0']
            else:
                explain += adict[c]
        s = s[1:]
    print(str(i)+ '-->'+explain)
    result += len(explain)
result += len('onethousand')            
print(result)
