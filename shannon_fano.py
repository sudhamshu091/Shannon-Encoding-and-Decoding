print("Shannon Compression Program")
print("=================================================================")
import collections
h = int(input("Enter 1 if you want to enter in command window, 2 if you are using input as file :"))
if h == 1:
    message = input("Enter the string you want to compress:")
elif h == 2:
    file = input("Enter the filename:")
    with open(file, 'r') as f:
        message = f.read()
else:
    print("You entered invalid input")
print("Entered string is:",message)

c = {}
def create_list(message):
    list = dict(collections.Counter(message))
    for key, value in list.items():
        print(key, ' : ', value)
    list_sorted = sorted(iter(list.items()), key = lambda k_v:(k_v[1],k_v[0]),reverse=True)

    final_list = []
    for key,value in list_sorted:
        final_list.append([key,value,''])
    return final_list
print("Shannon tree with merged pathways:")
def divide_list(list):
    if len(list) == 2:
        print([list[0]],[list[1]])
        return [list[0]],[list[1]]
    else:
        n = 0
        for i in list:
            n+= i[1]
        x = 0
        distance = abs(2*x - n)
        j = 0
        for i in range(len(list)):
            x += list[i][1]
            if distance < abs(2*x - n):
                j = i
    print(list[0:j+1], list[j+1:])
    return list[0:j+1], list[j+1:]


def label_list(list):
    list1,list2 = divide_list(list)
    for i in list1:
        i[2] += '0'
        c[i[0]] = i[2]
    for i in list2:
        i[2] += '1'
        c[i[0]] = i[2]
    if len(list1)==1 and len(list2)==1:
        return
    label_list(list2)
    return c

code = label_list(create_list(message))
print("Shannon's Encoded Code:")
output = open("compressed.txt","w+")
letter_binary = []
for key, value in code.items():
    print(key, ' : ', value)
    letter_binary.append([key,value])
print("Compressed file generated as compressed.txt")
for a in message:
    for key, value in code.items():
        if key in a:
            print(key, ' : ', value)
            output.write(value)
output = open("compressed.txt","r")
intermediate = output.readlines()
bitstring = ""
for digit in intermediate:
    bitstring = bitstring + digit
uncompressed_string =""
code =""
for digit in bitstring:
    code = code+digit
    pos=0
    for letter in letter_binary:
        if code ==letter[1]:
            uncompressed_string=uncompressed_string+letter_binary[pos] [0]
            code=""
        pos+=1

print("Your UNCOMPRESSED data is:")
print(uncompressed_string)

