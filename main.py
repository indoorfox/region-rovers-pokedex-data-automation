import re
import os
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

parsed = open(os.path.join(__location__, 'Untitled spreadsheet - parsed.csv'), 'r')
holder = []
linesplit = []
line = re.split('\n',parsed.readline())[0]
while True:
    line = re.split('\n', parsed.readline())[0]
    if(line == ""):
        break
    linesplit = re.split(",",line)
    holder.append(linesplit)
#    print(linesplit[3])
parsed.close


# for i in range(3):
#     if(i==0):
#         print("gens 1-3")
#         gens = "Generation 1-3 Pokedex"
#         dex = 387
#         min = 0
#     else:
#         if(i==1):
#             print("gens 4-6")
#             gens = "Generation 4-6 Pokedex"
#             dex = 722
#             min = 387
#         else:
#             print("gens 7-9")
#             gens = "Generation 7-9 Pokedex"
#             dex = 1026
#             min = 722
            

#     output = open(os.path.join(__location__, gens+'.txt'),'w')
#     for pokemon in holder:
#         valid = False
#         if(pokemon[25]=="y"):
#             if(int(pokemon[1])<dex):
#                 if(int(pokemon[1])>=min):
#                     valid = True
#         if(valid):
#             output.write("Species: "+pokemon[3]+" Type: ")
#             if(pokemon[5]==""):
#                 output.write(pokemon[4])
#             else:
#                 output.write(pokemon[4]+" / "+pokemon[5])
#             output.write(" Level: 5     Nature: _____ Size: "+pokemon[16]+" Weight: "+pokemon[18]+" Exp: 0/100\n\n")
#             output.write("HP: "+pokemon[7]+" HP Class: ("+pokemon[6]+")\n")
#             output.write("Attack: "+pokemon[8]+"\nDefense: "+pokemon[9]+"\nSpecial Attack: "+pokemon[10]+"\nSpecial Defense: "+pokemon[11]+"\nSpeed: "+pokemon[12]+"\n")
#             output.write("Movement:\n\n")
#             output.write("Abilities:\n")
#             abilities = ""
#             if(pokemon[21]!=""):
#                 abilities+=pokemon[21]
#             if(pokemon[22]!=""):
#                 if(abilities!=""):
#                     abilities+=", "+pokemon[22]
#                 else:
#                     abilities+=pokemon[22]
#             if(pokemon[23]!=""):
#                 if(abilities!=""):
#                     abilities+=", "+pokemon[23]
#                 else:
#                     abilities+=pokemon[23]
#             output.write(abilities+"\n\n")
#             output.write("Moves\n\n\nTalents\n\n\nDiet & Habitat\n\n\nEgg Group\n")
#             egggroup = pokemon[19]
#             if(pokemon[20]!=""):
#                 egggroup+=", "+pokemon[20]
#             output.write(egggroup+"\n\n")
#             output.write("Evolution:\n\n\n\n\n\n")
#             print("completed "+pokemon[3])
#     print("done with Gens")

def whitespacegenerator(text,num):
    for letter in text:
        if(letter == 'i' or letter == 'l' or letter == 'I'):
            num-=1
        else:
            num-=2
    if (num <= 2):
        num = 2
    output = text
    for i in range(num):
        output+=" "
    return output


helper = open(os.path.join(__location__,"helper.txt"),'w')
helper.write("List of Pokemon Generated:\n")
helper.close
helper = open(os.path.join(__location__,"helper.txt"),'a')

for i in range(3):
    if(i==0):
        print("gens 1-3")
        gens = "Generation 1-3 Pokedex"
        dex = 387
        min = 0
    else:
        if(i==1):
            print("gens 4-6")
            gens = "Generation 4-6 Pokedex"
            dex = 722
            min = 387
        else:
            print("gens 7-9")
            gens = "Generation 7-9 Pokedex"
            dex = 1026
            min = 722
            
    
    output = open(os.path.join(__location__, gens+'.md'),'w')
    for pokemon in holder:
        valid = False
        if(pokemon[25]=="y"):
            if(int(pokemon[1])<dex):
                if(int(pokemon[1])>=min):
                    valid = True
        if(valid):
            output.write("|")
            output.write("Species: "+whitespacegenerator(pokemon[3],34)+"Type: ")
            type = ""
            if(pokemon[5]==""):
                type = pokemon[4]
            else:
                type = pokemon[4]+" / "+pokemon[5]
            output.write(whitespacegenerator(type,32))
            output.write("Level: 5           Nature:             Size: "+whitespacegenerator(pokemon[16],22)+"Weight: "+whitespacegenerator(pokemon[18],16)+"Exp: 0/100<br><br>")
            hpclass = ""
            if(pokemon[6]=="+1d4/lvl"):
                hpclass = "Weak ("
            if(pokemon[6]=="+1d6/lvl"):
                hpclass = "Average ("
            if(pokemon[6]=="+1d8/lvl"):
                hpclass = "Above Average ("
            if(pokemon[6]=="+1d10/lvl"):
                hpclass = "Bulky ("
            if(pokemon[6]=="+1d12/lvl"):
                hpclass = "Tank ("
            
            output.write("HP: "+pokemon[7]+" / "+pokemon[7]+"                HP Class: "+hpclass+""+pokemon[6]+")<br>")
            output.write("Attack: "+pokemon[8]+"<br>Defense: "+pokemon[9]+"<br>Special Attack: "+pokemon[10]+"<br>Special Defense: "+pokemon[11]+"<br>Speed: "+pokemon[12]+"<br>")
            output.write("Movement:<br><br>")
            output.write("Abilities<br>")
            abilities = ""
            if(pokemon[21]!=""):
                abilities+=pokemon[21]
            if(pokemon[22]!=""):
                if(abilities!=""):
                    abilities+=", "+pokemon[22]
                else:
                    abilities+=pokemon[22]
            if(pokemon[23]!=""):
                if(abilities!=""):
                    abilities+=", "+pokemon[23]
                else:
                    abilities+=pokemon[23]
            output.write(abilities+"<br><br>")
            output.write("Learnset<br><br>Talents<br><br><br>Diet & Habitat<br><br><br>Egg Group<br>")
            egggroup = pokemon[19]
            if(pokemon[20]!=""):
                egggroup+=", "+pokemon[20]
            output.write(egggroup+"<br><br>")
            output.write("Evolution:")
            output.write("|\n|---|\n\n")
            print("completed "+pokemon[3])
            helper.write(pokemon[3]+"\n")
    print("done with Gens")
        

