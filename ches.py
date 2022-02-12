data = ''
with open('data.txt', 'r', encoding='utf-8') as f:
	for line in f:
		data = data + line

print(data)
s = 'hello'
res = []

hot = int(input('Hot: '))
cold = int(input('Cold: '))	



res = res[:-1]
print(res)

data += '\n'
data += 'Hot water: ' + str(hot * 1000) + '\n'
data += 'Cold water: ' + str(cold * 1000) + '\n'

print(data)

with open('data.txt', 'w', encoding='utf-8') as f:
	f.write(data)