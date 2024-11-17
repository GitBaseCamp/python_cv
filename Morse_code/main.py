import json

with open('morse-code.json', 'r') as file:
	data = json.load(file)


translated=[]
word = input("what word need to translated in morse code? :")

print(word)

for let in word:
	
	translated.append(data[let])
    
print(' '.join(translated))
