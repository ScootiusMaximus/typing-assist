import keyboard as kb

with open("tochange.txt","r",encoding="utf-8") as file:
    lines = file.readlines()

for line in lines:
    line = line.replace("\n","")
    bits = line.split(",")
    kb.add_abbreviation(bits[0],bits[1])
    
kb.wait()
