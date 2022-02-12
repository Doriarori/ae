data = ''
with open('data.txt', 'r', encoding='utf-8') as f:
	for line in f:
		data = data + line

print(data)
s = 'hello'
res = []

hot = input('Hot: ')
cold = input('Cold: ')		



res = res[:-1]
print(res)

data += '\n'
data += 'Hot water: ' + hot + '\n'
data += 'Cold water: ' + cold + '\n'

print(data)

with open('data.txt', 'w', encoding='utf-8') as f:
	f.write(data)