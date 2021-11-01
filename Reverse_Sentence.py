# Revers the Sentence

initStr = input("Enter a Sentence:\n =>")
lst = initStr.split(" ")
revers = ''
for i in range(len(lst)):
    revers = lst[i] + " " + revers

print("Reversed Sentence : \n =>{0}".format(revers))
