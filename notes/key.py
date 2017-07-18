from random import randint

values=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',\
'A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',\
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']
def key():
	key_length=7
	key_value=[]
	for i in range(key_length):
		random_char=randint(0,len(values))
		key_value.append(values[random_char])
	return "".join(key_value)

