from PIL import Image
from IPython.display import display
import random
import json
import os
import itertools
import math




def allchances(atchcount):
    alllists = []
    finallen = 0
    z = 0
    while len(alllists) < atchcount:
        currentlist = []
        y = 0
        for x in range(0,atchcount):
            if y>z:
                resultplus = atchcount - y
                for i in range(0,resultplus):
                    currentlist.append(0)
                break
            currentlist.append(1)
            y +=1
        #print(currentlist)
        alllists.append(currentlist)
        z +=1
    allcombination = []
    #print(alllists)
    for i in range(0,atchcount):
        final =  []
        per = (list(itertools.permutations(alllists[i])))
        for element in per:
            try:
                final.index(element)
            except:
                final.append(element)

        finallen += len(final)
        allcombination.append(final)


    return allcombination

def atcdict(path):
    restdict = {}
    files = os.listdir(path)
    for i in range(0,len(files)):
        restdict[i]=files[i]

    print(restdict)
    return restdict





#list(itertools.permutations([1,1,0]))
id = 1

def factoryatc(finalimg):
    global id
    path = './traits/pre items'
    allcomb = allchances(len(os.listdir(path)))
    atchsindct = atcdict(path)
    firstshoe = id -1
    for combs in allcomb:
        for x in combs:
            finalimgforporcs = Image.open("./NFTS/" + str(firstshoe) + ".png").convert('RGBA')

            print("\n\n\n"+str(x) + " : "+str(id))
            for comb in range(0,len(x)):
                if x[comb] == 1:
                    atch = Image.open(path+"/"+atchsindct[comb]).convert("RGBA")
                    finalimgforporcs.paste(atch, atch)
                    print("ADDED : "+atchsindct[comb]+"  " + str(id))
            finalimgforporcs.save("./NFTS/" + str(id) + ".png", format="png")
            print("OK : ", id)

            id +=1
            print(firstshoe)


topes = os.listdir("./Shoes/Ups")
soles = os.listdir("./Shoes/Soles")
for top in topes:
    for sole in soles:
        background = Image.open("./Shoes/Ups/"+top).convert('RGBA')
        frontImage = Image.open("./Shoes/Soles/"+sole).convert('RGBA')




        background.paste(frontImage, frontImage)

        # Save this image
        background.save("./NFTS/"+str(id)+".png", format="png")
        print("OK : ",id)
        id +=1












#im3 = Image.open(f'./scripts/face_parts/ears/{ears_files[item["Ears"]]}.png').convert('RGBA')
#com2 = Image.alpha_composite(com1, im3)




