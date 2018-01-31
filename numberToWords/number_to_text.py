words = ["zero","one", "two", "three", "four","five","six","seven","eight","nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "ninteen",
        "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety",
        "hundred","thousand", "million","billion"]
hundreds = [3,6,9,12]
decs = [2,5,8,11]

inp = 115213
inp = input("\n\n\nIntroduce a number: ")
print ("\n\n\n" + str(inp))
output = ""
if (inp == 0):
    output += words[0]
else:
    inp = str(inp)[::-1]
    count = 1
    dec = 10
    for x in inp:
        current = int(x)
        if (count in decs):
            if (current == 1):
                current = 10 + last
                output = output[:-(len(words[last])+1)]
            elif current != 0:
                current = current + 18
        elif (count in hundreds) and (current != 0):
            output += words[28] + " "
        elif count == 4 and current != 0:
            output += words[29] + " "
        elif count == 7 and current != 0:
            output += words[30] + " "
        elif count == 10 and current != 0:
            output += words[31] + " "
        if (current != 0):
            output += words[current] + " "
        count += 1
        last = current
output = output.split(" ")
output = output[::-1]
del output[0]
output = " ".join(output)
print (output.capitalize() + "\n\n\n")
