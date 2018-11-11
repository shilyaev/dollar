print('veweeerev')

input_file = open('kursUSD.txt', 'r')
max_dolr=1
max_data= " "
for line in input_file:
    date,d = map(str, line.split())
    dolr= float(d)
    if dolr > max_dolr:
        max_dolr=dolr
        max_data=date
print(max_data,max_dolr)