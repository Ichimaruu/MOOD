#cd dir C:\Users\Jake\Desktop\therapygame
#cxfreeze mood.py --target-dir C:\Users\Jake\therapygame\mood - run to install

try:


        import random
        import time
        import sys
        import traceback
        import pickle
        import os
        import colorama
        from colorama import Fore, Back, Style
        import subprocess
        colorama.init(autoreset=True)
        #from playsound import playsound






#        def seasons(userinput):
  #              #open this with 'day' command, not 'seasons'
    #            if userinput == 1:
      #          # Add stuff you can buy to shop like a coat to add heat
        #        # See if you have clothes in buffsactive that we can make damp with rain, rain should also negatively affect your mood.
#
#
  #      seasonslist =
    #    currentseason =
      #  yourtemperature = 0
#        outsidetemperature = 20
  #      housetemperature = 0
#
  #      if day > 30:
    #            print("---------------------------------------------------")
      #          print("---------------------------------------------------")
        #        print("The air feels so cold! Brrr! It must be winter")
        def finddictionary_fromvalue(value, dict_list):
            for d in dict_list:
                for key, val in d.items():
                    if val == value:
                        return d
                return None
            return None
        def finddictionary_fromkey(key, dict_list):
            for d in dict_list:
                if key in d:
                    return d
            return None

        def findkey_fromvalue(d, val):
            for key, value in d.items():
                if value == val:
                    return key
            return None

        items = ["makeup", "dress","fancy dress", "t-shirt", "epic t-shirt", "potted plant"]
        hobbyitemsknitting= ["scarf", "headband", "dishcloth", "baby blanket", "hat", "mittens", "sweater", "socks", "shawl", "cardigan", "cabled afghan", "intarsia picture sweater", "cable sweater set", "invisibility cloak", "interstellar sweater"]
        hobbyitemscooking = ["scrambled eggs", "fried eggs", "omelette", "french toast", "pancakes", "crepes", "quiche", "souffle", "chocolate chip cookies", "chocolate cake", "chocolate mousse", "chocolate truffles", "chocolate molecular gastronomy dish", "intergalactic tasting menu"]
        hobbyitemspainting = ["landscape", "still life", "portrait", "abstract painting", "figurative painting", "impressionist painting", "surrealist painting", "perspective painting", "pop art painting", "hyperrealist paintings", "mural paintings", "illusionary painting", "iconic painting", "interstellar portrait", "spacetime breaking painting"]
        hobbyitemsdirecting = ["short film", "music video", "student film", "independent film", "documentary", "commercial", "feature film", "television series", "episodic content", "blockbuster film", "franchise film", "oscar-winning film", "space movie", "movie in space", "interdimensional movie"]
        hobbyitemswriting = ["short story", "poem", "essay", "novel", "non-fiction book", "playscript", "biography", "autobiography", "historical fiction", "best-selling novel", "award-winning book", "classic literature", "film script", "nobel prize-winning book", "world-renowned film script"]
        itemingsknitting = {"scarf": {"thread": 2, "needle": 1}, "headband": {"thread": 3, "yarn": 1}, "dishcloth": {"thread": 2, "yarn": 1,"needle" : 1}, "baby blanket": {"yarn": 1, "crochet hook": 1}, "hat": {"yarn": 2, "needle": 1}, "mittens": {"yarn": 3, "needle": 1},
                            "sweater": {"yarn": 6, "needle": 2}, "socks": {"thread" :5, "yarn": 4, "needle": 2}, "shawl": {"yarn": 6, "needle": 1}, "cardigan": {"yarn": 12, "needle": 2}, "cabled afghan": {"yarn": 20, "needle": 2}, "intarsia picture sweater": {"yarn": 30, "needle": 2}, "cable sweater set": {"yarn": 40, "needle": 3}, "invisibility cloak": {"yarn": 50, "space thread": 2}, "interstellar sweater": {"thread": 120, "yarn": 60, "intergalactic needle": 1, "space thread": 3}}
        ingsknitting = {"thread" : 1, "yarn" : 3, "elastic" : 5, "needle" : 5, "crochet hook" : 8, "space thread" : 250, "intergalatic needle" : 500}
        itemdifficultyknitting = {"scarf" : 2, "headband" : 10, "dishcloth" : 19, "baby blanket" : 26, "hat" : 32, "mittens" : 38, "sweater" : 44, "socks" : 52, "shawl" : 59, "cardigan" : 66, "cabled afghan" : 72, "intarsia picture sweater" : 78, "cable sweater set" : 84, "invisibility cloak" : 92, "interstellar sweater" : 100}
        itemingscooking = {"scrambled eggs": {"eggs": 2}, "fried eggs": {"eggs":4}, "omelette": {"eggs": 2, "butter": 1}, "french toast": {"eggs": 3, "butter" : 2, "flour" : 1, "sugar" : 1}, "pancakes": {"eggs": 3, "flour": 2, "butter": 1, "sugar" : 1},
                                   "crepes": {"eggs": 5, "flour": 3, "butter": 2, "sugar" : 1}, "quiche": {"eggs": 6, "flour": 7,"butter": 1,"sugar": 1}, "souffle": {"eggs": 10, "flour": 8, "butter": 5, "sugar": 4}, "chocolate chip cookies": {"eggs": 20, "chocolate": 2, "sugar": 11}, "chocolate cake": {"eggs": 25, "sugar": 20, "flour": 3,"chocolate":7,"butter":5}, "chocolate mousse": {"eggs": 35, "chocolate": 10, "sugar": 25},
                                   "chocolate truffles": {"eggs": 60, "chocolate": 30}, "chocolate molecular gastronomy dish": {"chocolate": 50, "liquid nitrogen":3}, "intergalactic tasting menu": {"microverse battery": 1,"dream inceptor": 2}}
        ingscooking = {"eggs" : 1, "butter" : 3, "flour":5,"sugar":5,"chocolate":8,"liquid nitrogen":150,"dream inceptor":250,"microverse battery":500}
        itemdifficultycooking = {"scrambled eggs" : 2, "fried eggs" : 10, "omelette" : 19, "french toast" : 26, "pancakes" : 32, "crepes" : 38, "quiche" : 44, "souffle" : 52, "chocolate chip cookies" : 59, "chocolate cake" : 66, "chocolate mousse" : 72, "chocolate truffles" : 78, "chocolate molecular gastronomy dish" : 84, "intergalactic tasting menu" : 100}
        itemingspainting = {"landscape": {"paint brushes": 1, "paint tubes": 1, "canvas": 1}, "still life": {"paint brushes": 3, "paint tubes": 1, "canvas": 1}, "portrait": {"paint brushes": 4, "paint tubes": 5, "canvas": 1}, "abstract painting": {"paint brushes": 2, "paint tubes": 6, "canvas": 1}, "figurative painting": {"paint brushes": 3, "paint tubes": 12, "canvas": 1}, "impressionist painting": {"paint brushes": 25, "paint tubes": 21, "canvas": 2}, "surrealist painting": {"paint brushes": 54, "paint tubes": 14, "canvas": 1},
                            "perspective painting": {"paint brushes": 40, "paint tubes": 23, "canvas": 1}, "pop art painting": {"paint brushes": 54, "paint tubes": 45, "canvas": 2}, "hyperrealist paintings": {"paint brushes": 35, "paint tubes": 75, "canvas": 2}, "mural paintings": {"paint brushes": 70, "paint tubes": 20, "canvas": 7}, "illusionary painting": {"paint brushes": 102, "paint tubes": 40, "canvas": 7}, "iconic painting": {"paint brushes": 60, "paint tubes": 45, "canvas": 5}, "interstellar portrait": {"paint brushes": 45, "canvas": 4, "space paint" : 3},
                            "spacetime breaking painting": {"paint brushes": 8, "paint tubes": 25, "canvas": 1, "space paint": 1, "intergalactic paint brush": 1}}
        ingspainting = {"paint brushes": 1, "paint tubes": 2, "canvas": 20, "space paint": 100, "intergalactic paint brush": 550}
        itemdifficultypainting = {"landscape" : 2, "still life" : 10, "portrait" : 19, "abstract painting" : 26, "figurative painting" : 32, "impressionist painting" : 38, "surrealist painting" : 44, "perspective painting" : 52, "pop art painting" : 59, "hyperrealist paintings" : 66, "mural paintings" : 72, "illusionary painting" : 78, "iconic painting" : 84, "interstellar portrait" : 92, "spacetime breaking painting" : 100}
        itemingsdirecting = {"short film": {"microphone": 1, "editing software": 1}, "music video": {"microphone": 3, "editing software": 1}, "student film": {"camera": 1, "microphone": 5}, "independent film": {"camera": 2, "microphone": 4, "editing software": 5, "music":1},
                                 "documentary": {"camera": 5, "microphone": 10, "editing software": 5, "music":1}, "commercial": {"camera": 7, "microphone": 3, "editing software": 10, "actors": 1}, "feature film": {"camera": 4, "microphone": 45, "editing software": 23, "actors": 3},
                             "television series": {"camera": 9, "microphone": 25, "editing software": 40, "actors": 8}, "episodic content": {"camera": 5, "microphone": 45, "editing software": 67, "actors": 10},
                                 "blockbuster film": {"camera": 20, "microphone": 103, "editing software": 63, "actors": 20}, "franchise film": {"camera": 34, "microphone": 25, "editing software": 154, "actors": 14}, "oscar-winning film": {"camera": 8, "microphone": 2, "editing software": 4, "actors": 30, "visual effects" : 4},
                             "space movie": {"camera": 9, "microphone": 2, "editing software": 4, "actors": 4, "visual effects": 20}, "movie in space": {"camera": 10, "microphone": 3, "editing software": 4, "actors": 50, "visual effects": 30},
                                 "interdimensional movie": {"camera": 11, "microphone": 3, "editing software": 5, "actors": 5, "visual effects" : 34, "space ship" : 1}}
        ingsdirecting = {"camera": 5, "microphone": 1, "editing software": 2, "actors": 20, "music": 8, "visual effects": 50, "space ship": 10000}
        itemdifficultydirecting = {"short film": 2, "music video": 10, "student film": 19, "independent film": 26, "documentary": 32, "commercial": 38, "feature film": 44, "television series": 52, "episodic content": 59, "blockbuster film": 66, "franchise film": 72, "oscar-winning film": 78, "space movie": 84, "movie in space": 92, "interdimensional movie": 100}
        itemingswriting = {"short story": {"paper": 1, "pen": 1}, "poem": {"paper": 2, "pen": 1}, "essay": {"paper": 3, "pen": 2, "pencil": 1}, "novel": {"paper": 50, "computer": 1, "printer": 1, "ink": 1}, "non-fiction book": {"paper": 100, "computer": 1, "printer": 1, "ink": 1}, "playscript": {"paper": 50, "computer": 1, "printer": 1, "ink": 1},
                   "biography": {"paper": 75, "computer": 1, "printer": 1, "ink": 1}, "autobiography": {"paper": 100, "computer": 1, "printer": 1, "ink": 1}, "historical fiction": {"paper": 50, "computer": 1, "printer": 1, "ink": 1}, "best-selling novel": {"paper": 100, "computer": 1, "printer": 1, "ink": 1},
                   "award-winning book": {"paper": 100, "computer": 1, "printer": 1, "ink": 1}, "classic literature": {"paper": 50, "computer": 1, "printer": 1, "ink": 1}, "film script": {"paper": 50, "computer": 1, "printer": 1, "ink": 1}, "nobel prize-winning book": {"paper": 100, "computer": 1, "printer": 1, "ink": 1},
                   "world-renowned film script": {"paper": 500, "computer": 1, "printer": 1, "ink": 5}}
        ingswriting = {"paper": 1, "pen": 2, "pencil": 1, "computer": 100, "printer": 30, "ink": 20, "notebook": 5}
        itemdifficultywriting = {"short story" : 2, "poem" : 10, "essay" : 19, "novel" : 26, "non-fiction book" : 32, "playscript" : 38, "biography" : 44, "autobiography" : 52, "historical fiction" : 59, "best-selling novel" : 66, "award-winning book" : 72, "classic literature" : 78, "film script" : 84, "nobel prize-winning book" : 92, "world-renowned film script" : 100}
        exp = {"knitting" : 1, "cooking" : 1, "painting" : 1, "directing" : 1, "writing" : 1}
        ingslist = {"knitting" :ingsknitting, "cooking" : ingscooking, "painting": ingspainting, "directing" : ingsdirecting, "writing": ingswriting}
        itemingslist = {"knitting" : itemingsknitting, "cooking":itemingscooking,"painting":itemingspainting,"directing":itemingsdirecting,"writing":itemingswriting}
        difficultylist = {"knitting" :itemdifficultyknitting, "cooking" : itemdifficultycooking, "painting": itemdifficultypainting, "directing" : itemdifficultydirecting, "writing": itemdifficultywriting}
        money = 150
        progress = 240
        itemscrafted = 0
        luckyitemsknitting = ["intergalactic needle","space thread","rare scrap"]
        extraluckyitemsknitting = ["legendary scrap","legendary scrap","legendary scrap"]
        uncommonitemsknitting = ["elastic","needle","crochet hook"]
        commonitemsknitting = ["thread","yarn","common scrap"]
        luckyitemspainting = ["space paint", "intergalactic paint brush","rare scrap"]
        extraluckyitemspainting = ["legendary scrap","legendary scrap","legendary scrap"]
        uncommonitemspainting = ["canvas","uncommon scrap","uncommon scrap"]
        commonitemspainting = ["paint brushes", "paint tubes","common scrap"]
        luckyitemscooking = ["liquid nitrogen","microverse battery","dream inceptor"]
        extraluckyitemscooking = ["legendary scrap","legendary scrap","legendary scrap"]
        uncommonitemscooking = ["flour","sugar","chocolate"]
        commonitemscooking = ["eggs", "butter","scrap"]
        luckyitemsdirecting = ["visual effects","rare scrap","rare scrap"]
        extraluckyitemsdirecting= ["spaceship","legendary scrap","legendary scrap"]
        uncommonitemsdirecting = ["music","actors","camera"]
        commonitemsdirecting = ["microphone","editing software","common scrap"]
        extraluckyitemswriting = ["legendary scrap","legendary scrap","legendary scrap"]
        luckyitemswriting = ["computer","printer","common scrap"]
        uncommonitemswriting = ["ink","notebook","uncommon scrap"]
        commonitemswriting = ["pen","pencil","paper"]
        commonitems = (commonitemsknitting + commonitemspainting + commonitemscooking + commonitemsdirecting + commonitemswriting)
        uncommonitems = (uncommonitemsknitting + uncommonitemspainting + uncommonitemscooking + uncommonitemsdirecting + uncommonitemswriting)
        luckyitems = (luckyitemsknitting + luckyitemspainting + luckyitemscooking + luckyitemsdirecting + luckyitemswriting)
        extraluckyitems = (extraluckyitemsknitting + extraluckyitemspainting + extraluckyitemscooking + extraluckyitemsdirecting + extraluckyitemswriting)
        items_prices = {"makeup": 20, "dress": 40, "fancy dress": 80, "t-shirt": 30, "epic t-shirt": 90, "potted plant": 10}
        crates_prices = {"small knitting crate": 150,"large knitting crate": 500, "small cooking crate":150,"large cooking crate":500,"small painting crate":150,"large painting crate":500,"small directing crate":150,"large directing crate":500,"small writing crate":150,"large writing crate":150,"general crate":50}
        crates_hobby = {"small knitting crate": "ingsknitting","large knitting crate": "ingsknitting", "small cooking crate":"ingscooking","large cooking crate":"ingscooking","small painting crate":"ingspainting","large painting crate":"ingspainting","small directing crate":"ingsdirecting","large directing crate":"ingsdirecting","small writing crate":"ingswriting","large writing crate":"ingswriting"}
        hobbies = ("knitting", "cooking", "directing", "painting", "writing")
        hobbylevels = {0 : "Beginner", 10 : "Intermediate", 25: "Advanced", 40:"Expert", 65:"Specialist", 90: "Master"}

        def hobby():
                        global inventory

                        print("Your crafting items consist of:")
                        for fl in list(inventory.keys()):
                                for bl in ingslist:
                                        if fl == bl:
                                                print(inventory[fl])

                        print("")
                        print("1. Knitting")
                        print("2. Cooking")
                        print("3. Directing")
                        print("4. Painting")
                        print("5. Writing")
                        print("6. Exit")
                        try:
                                choice = abs(int(input("What would you like to do?")))
                        except ValueError:
                                print("Incorrect choice, type a number from 1-6!")
                                return
                        if choice == 6:
                                return
                        hobbychoice = hobbies[choice-1]
                        if hobbychoice in hobbies:

                                crafter(hobbychoice)



        def crafter(hobbypicked):
                global inventory
                global exp
                global itemscrafted

                if itemscrafted >= 10:
                        print(Fore.RED + "I'm too tired of crafting to do any more today." + Style.RESET_ALL)
                        return

                yourexp = exp[hobbypicked]
                explist = list(hobbylevels.keys())


                itemingshobbylist = {"knitting" :itemingsknitting, "cooking" : itemingscooking, "painting": itemingspainting, "directing" : itemingsdirecting, "writing": itemingswriting}
                itemingschoice = itemingshobbylist[hobbypicked]
                os.system('cls')

                #itemdifficultywriting = {"short story" : 2, "poem" : 10, "essay" : 19, "novel" : 26, "non-fiction book" : 32, "playscript" : 38, "biography" : 44, "autobiography" : 52, "historical fiction" : 59, "best-selling novel" : 66, "award-winning book" : 72, "classic literature" : 78, "film script" : 84, "nobel prize-winning book" : 92, "world-renowned film script" : 100}
                for item_name, ingredients in itemingschoice.items():
                        if (yourexp + 20) >= difficultylist[hobbypicked][item_name]:
                            print(Fore.GREEN + f"{item_name}:" + Style.RESET_ALL)
                            for ingredient, quantity in ingredients.items():
                                print(Fore.RED + f"{ingredient} : {quantity}" + Style.RESET_ALL)

                i = 0
                levelsHit = []
                while i <= yourexp:
                    if i == 0:
                        levelsHit.append(hobbylevels[0])
                    if i == 10:
                        levelsHit.append(hobbylevels[10])
                    if i == 25:
                        levelsHit.append(hobbylevels[25])
                    if i == 40:
                        levelsHit.append(hobbylevels[40])
                    if i == 65:
                        levelsHit.append(hobbylevels[65])
                    if i == 90:
                        levelsHit.append(hobbylevels[90])
                    i += 1
                print(f"\n{hobbypicked} level: " + Fore.LIGHTCYAN_EX + f"{levelsHit[len(levelsHit)-1]}"+ Style.RESET_ALL)
                yourlevel = levelsHit[len(levelsHit)-1]

                difficultylists = {"knitting" :itemdifficultyknitting, "cooking" : itemdifficultycooking, "painting": itemdifficultypainting, "directing" : itemdifficultydirecting, "writing": itemdifficultywriting}
                difficultylistchoice = difficultylists[hobbypicked]
                try:
                        itemchoice = input("\nWhat would you like to try to make?")


                 #itemingspainting = {"landscape": {"paint brushes": 1, "paint tubes": 1, "canvas": 1}, "still life": {"paint brushes": 3, "paint tubes": 1, "canvas": 1}, "portrait": {"paint brushes": 4, "paint tubes": 5, "canvas": 1}, "abstract painting": {"paint brushes": 2, "paint tubes": 6, "canvas": 1}, "figurative painting": {"paint brushes": 3, "paint tubes": 12, "canvas": 1}, "impressionist painting": {"paint brushes": 25, "paint tubes": 21, "canvas": 2}, "surrealist painting": {"paint brushes": 54, "paint tubes": 14, "canvas": 1},
                        ingredients = itemingslist[hobbypicked][itemchoice]
                except:
                        print("Incorrect item chosen.")
                        return

                for ings in ingredients:
                        if ings in inventory.keys():
                                number = ingredients[ings]
                                if number > inventory[ings]:
                                                print("You don't have the ingredients to make this!")
                                                return
                                else:
                                        inventory[ings] = inventory.get(ings, 0) - number
                                        if inventory[ings] == 0:
                                                del inventory[ings]
                        else:
                                print("You don't have the ingredients to make this!")
                                return

                #itemingschoice = itemingshobbylist[hobbypicked]
                #itemingshobbylist = {"knitting" :itemingsknitting, "cooking" : itemingscooking, "painting": itemingspainting, "directing" : itemingsdirecting, "writing": itemingswriting}
                if itemchoice in itemingschoice:
                        itemdifficulty = difficultylists[hobbypicked][itemchoice]

                        #difficultylistchoice = difficultylists[hobbypicked]
                        #difficultylists = {"knitting" :itemdifficultyknitting, "cooking" : itemdifficultycooking, "painting": itemdifficultypainting, "directing" : itemdifficultydirecting, "writing": itemdifficultywriting}

                        itemlowerbound = itemdifficulty - 20
                        itemupperbound = itemdifficulty + 20
                        #check if lowerbound goes under 0
                        choiceoutput = False
                        if yourexp > itemlowerbound:
                                if yourexp < itemupperbound:
                                        #print how likely it is for player to create item
                                        levelsafterlower = abs(yourexp - itemlowerbound)

                                        chancetocreate = (levelsafterlower / 40)*100
                                        print(f"Based on your skill level in {hobbypicked}, your chance of making a {itemchoice} is: " + Fore.CYAN + f"{int(chancetocreate)}%" + Style.RESET_ALL)
                                        create = input(f"Are you sure you want to try to create a {itemchoice}? yes/no: ")
                                        if create != "yes":
                                                hobby()
                                        else:
                                                print(f"You attempt to make a {itemchoice}!")

                                                #is item made?
                                                if random.randint(0, 100) > chancetocreate:
                                                        time.sleep(0.5)
                                                        print(". . .")
                                                        time.sleep(0.5)
                                                        print(". . .")
                                                        time.sleep(0.5)
                                                        print(". . .")
                                                        time.sleep(0.5)
                                                        print(Fore.RED + f"\nOh no! You failed to make {itemchoice}!" + Style.RESET_ALL)
                                                        time.sleep(1.5)
                                                        crafter(hobbypicked)
                                                else:
                                                        choiceoutput = True
                                else:
                                        choiceoutput = True
                        else:
                                print(f"\nYou aren't a skilled enough at {hobbypicked} to create that yet.")
                        if choiceoutput == True:
                                time.sleep(0.5)
                                print(". . .")
                                time.sleep(0.5)
                                print(". . .")
                                time.sleep(0.5)
                                print(". . .")
                                time.sleep(0.5)
                                print(Fore.GREEN + f"\nYes!! You made a {itemchoice}!" + Style.RESET_ALL)
                                inventory[itemchoice] = inventory.get(itemchoice, 0) + 1
                                #do you grow a level?
                                time.sleep(0.5)
                                if yourexp > itemdifficulty + 15:
                                        print(Fore.RED + f"Hmm, you're not sure you learned much from making that {itemchoice}. Maybe you should practice on something more difficult."+ Style.RESET_ALL)
                                        time.sleep(1.5)
                                        itemscrafted += 1
                                        crafter(hobbypicked)
                                else:
                                       print(Fore.GREEN + f"You feel slightly better at {hobbypicked}!" + Style.RESET_ALL)
                                       exp[hobbypicked] += 3
                                       itemscrafted += 1
                                       time.sleep(1.5)
                                       crafter(hobbypicked)


        petcaredfor = 0
        #remember, number of list starts at 0!!
        housesavailable = {
                #name : (rent, price, furniture slots)
            "studio flat": (25, 125, 1, "Compact flat with minimalist design"),
            "modest flat" : (50, 200, 2, "A small but comfortable flat"),
            "large flat" : (75, 250, 4, "A spacious flat with lots of natural light"),
            "luxury flat": (100, 275, 6, "Spacious and modern flat with high-end finishes"),
            "shed" : (0, 500, 1, "A pretty pricey shed, looks pretty nice for a shed though."),
            "small house" : (0, 1000, 2, "A compact house with a small garden"),
            "cozy cottage": (0, 2000, 6, "Charming cottage with a garden and fireplace"),
            "villa": (0, 3000, 10, "Luxurious villa with private pool and large garden"),
            "townhouse": (75, 1500, 10, "Stylish townhouse with rooftop terrace")
            }
        furnitureavailable = {
            # item : (price, progress, description)
            "chair" : (30, 3, "A comfortable and stylish chair, perfect for any room in your home."),
            "table" : (50, 5, "A sturdy and versatile table, ideal for dining, working, or playing games."),
            "sofa" : (90, 9, "A luxurious and inviting sofa, perfect for relaxing and entertaining guests."),
            "bed" : (100, 10, "A comfortable and supportive bed, essential for a good night's sleep."),
            "television" : (100, 10, "A high-definition television, perfect for watching movies and sports.")
        }
        houseinventory = []
        rentdue = 0
        hasworked = 0
        yourhouse = 0
        petpowermultiplier = {}
        petname = ""
        petmood = 230
        petgoodmoodlist = ["happy","playful","fun","pleased"]
        petgoodmoodevents = {"","",}
        petbadmoodlist = ["bitey","sour","annoying","sad","rotten"]
        petbadmoodevents = [""]
        petlevel = {0 : "weak dog", 1 : "regular dog", 2 : "good dog", 3 : "super dog", 4 : "mega dog" , 5 : "ultra dog"}
        petgroomed = 0
        petbathed = 0
        progressdescriber = ""
        pettrained = 30
        addedprogressterms = ("way, way, WAY WORSE!","way, way, WAY WORSE!","insanely worse","insanely worse","hugely worse","hugely worse","way worse","way worse","much worse","much worse","a good deal worse","a good deal worse","notably worse","notably worse","a small amount worse","a small amount worse","slightly worse","slightly worse","very slightly worse","very slightly worse","more or less the same",
                              "more or less the same","very slightly better","very slightly better","slightly better","slightly better","better","better","noticeably better","noticeably better","a good deal better","a good deal better","much better","much better","way better","way better","hugely better","hugely better","insanely better","insanely better","way, way, WAY BETTER!","way, way, WAY BETTER!")

        def addedprogress(added):
                added = added + 20

                if added >= 0 and added <= 40:
                        returnme = addedprogressterms[added]
                elif added > 40:
                        returnme = addedprogressterms[40]
                elif added < 0:
                        returnme = addedprogressterms[0]

                else:
                        returnme = "I think there might be an error in the addedprogress function"
                return returnme

        trainedtoday = 0
        trained_descriptions = {
                100 : "very obedient",
                90 : "extremely well-trained",
                80 : "highly trained",
                70 : "well-trained",
                60 : "reasonably trained",
                50 : "fairly trained",
                40 : "moderately trained",
                30 : "partially trained",
                20 : "poorly trained",
                10 : "very poorly trained",
                0 : "very disobedient",
                }
        bathedtoday = 0
        groomedtoday = 0
        issues = ["depression", "anxiety", "relationship issues" , "trauma" , "anger" , "regret","sadness", "ptsd" , "ocd", "adhd", "grief", "insomnia", "social anxiety", "phobias", "panic disorder", "dissociation","migraine", "fatigue"]
        issuevalues = {"depression" : 0, "anxiety" : 0, "relationship issues" : 0, "trauma" : 0, "anger" : 0, "regret" : 0,"sadness" : 0, "ptsd" : 0, "ocd" : 0, "adhd" : 0, "grief" : 0, "insomnia" : 0, "social anxiety" : 0, "phobias" : 0, "panic disorder" : 0, "dissociation" : 0,"migraine" : 0, "fatigue" : 0}
        pettoday = 0
        petrandomevents = {}
        bankbalance = 0
        havepet = 0
        inventory = {"nest egg":1}
        bad_events = {"You had a bad interaction with a friend" : (10, 0),
                      "You had a mental health crisis" :  (15, 0),
                      "You had a fight with your parents" :  (15, 0),
                      'A random stranger puked all over you': (20, 0),
                      'Some hobo just mugged you!! WTF?': (0, 20),
                      'You just got hit by a flying burrito': (5, 0),
                      "Your pants just fell down in a public place" : (10,0),
                      "You accidentally wore mismatched shoes" : (5, 0),
                      'A bird just pooped on your head': (5, 0),
                      "You just got stuck in a phone booth" : (10, 0),
                      "Your shoelaces just got tied together" : (5, 0),
                      'You were just photobombed by a spider': (5, 0),
                      "You just got hit by a rogue frisbee" : (10, 0),
                      "You just got stuck in a toilet" : (15, 0),
                      "You just had a really bad case of hiccups" : (5, 0),
                      "Your phone just fell in the toilet" : (5, 50),
                      "You just got lost in a shopping centre" : (10, 20),
                      "You just got chased by a pack of squirrels" : (10, 0),
                      "You just got stuck in an elevator" : (15, 0),
                      "You just stepped on gum" : (5, 0),
                      "You just had a wardrobe malfunction" : (15, 0),
                      "Your laptop just crashed" : (20, 0),
                      "You just got a bad hair cut" : (10, 20)
                      }


                #..(progress,money)
        rare_events = {"You just found £50 lying on the floor!" : (+50, 0),
                                       f'You just sharted at work. When you got up to go to the toilet, everyone saw the giant brown stain on your trousers.' : (-30,0),
                                       f'I got in a massive heated argument with a friend today.' : (-30,0),
                                       f'What a day! A pigeon pooped in my annoying coworkers mouth while they were trying to show off, then a work friend took me out for dinner! \nYou are over the moon about it!' : (+20,0),
                                       f'work gave me a voucher For £100!! Woohoo!!' : (0,+100),
                                       f'You won the lottery and received £300, YESSSSSSS!' : (+10,+300,),
                                       f'My tooth had an issue and it £200 to fix it. Your disappointment is immeasureable and your day is ruined.' : (-20,-200),
                                       f'You received a promotion at work and a raise of £200.' : (+5,+200),
                                       f'You went on a dream vacation and spent £300.' : (+40,-300),
                                       f'You had a terrible day at work and lost £100 on a bad investment.' : (-10,-100)
                               }



        def therapy_game():

                # Set initial values for progress, issues, and money
                y = 0
                suicide = 0
                displayedmessage = ""
                progress_descriptions = {
                    300: "ELATED",
                    295: "ECSTATIC",
                    290: "OVERJOYED",
                    285: "JOYFUL",
                    280: "BLISSFUL",
                    275: "ELATED",
                    270: "EXTREMELY HAPPY",
                    265: "VERY HAPPY",
                    260: "HAPPY",
                    255: "DELIGHTED",
                    250: "THRILLED",
                    245: "PLEASED",
                    240: "SATISFIED",
                    235: "CONTENT",
                    230: "NEUTRAL",
                    225: "MILDLY LOW",
                    220: "SOMEWHAT LOW",
                    215: "LOW",
                    205: "VERY LOW",
                    210: "DOWN",
                    200: "SOMEWHAT DEPRESSED",
                    195: "DEPRESSED",
                    190: "SEVERELY DEPRESSED",
                    185: "HOPELESS",
                    180: "HELPLESS",
                    175: "DESPONDANT",
                    170: "DEVESTATINGLY DEPRESSED",
                    165: "DISTRAUGHT",
                    160: "VERY DISTRAUGHT",
                    155: "ANGUISHED",
                    150: "AGONIZED",
                    145: "SUFFERING",
                    140: "TORMENTED",
                    135: "TORTURED",
                    130: "INCAPACITATED",
                    125: "UTTERLY DEVESTATED",
                    120: "COMPLETE DESPAIR",
                    115: "UTTERLY DESOLATE",
                    110: "A MISERABLE, DESOLATE MESS",
                    15: "A COMPLETE AND UTTER WRECK",
                    10: "DESPERATE"
                }
                insomnia = 0
                global day
                day = 1
                global inventory
                nightmares = 0
                global buff
                buff = 0
                global buffsactive
                buffsactive = {}
                addiction = 0
                session = 1
                useditems = []
                currentissues = []
                global money
                commands = ["sleep","work","shop","inv","hobby","bank","casino","pet","house","self","info"]
                global progress
                global drugs
                drugs = ["antidepressant", "xanax", "ambien"]
                global drugs_prices
                drugs_prices = {"antidepressant": 50, "xanax": 40, "ambien": 70}
                global items_prices
                global bad_events


                yourname = input("Welcome to MOOD! Please enter your " + Fore.YELLOW + "name: " + Style.RESET_ALL)
                time.sleep(1)
                print(f"In this game, you will be playing as {yourname}.")
                time.sleep(1)
                print(f"Your goal is to get to the highest{Fore.YELLOW} day{Style.RESET_ALL} possible.")
                time.sleep(1)
                print(f"You can also visit a{Fore.YELLOW} shop{Style.RESET_ALL} to buy items to help with your mood.")
                time.sleep(1)
                print(f"You will unlock new {Fore.YELLOW}commands{Style.RESET_ALL} as you progress through the days.")
                print(f"Beware, some{Fore.YELLOW} random events{Style.RESET_ALL} may occur that can reduce your mood.")
                time.sleep(1)
                print("\nLet's begin.")
                time.sleep(1)

        # -----------------------------------------USE BLOCK--------------------------------------------------------------------
                def use(instause = 0,itemtouse = "None"):
                        global issues
                        global issuevalues
                        global inventory
                        global buff
                        global buffsactive
                        global useitem
                        global progress
                        global money
                        global houseinventory
                        global yourhouse
                        global housesavailable
                        global furnitureavailable
                        if instause == 1:
                                opencrate(itemtouse)
                                inventory[itemtouse] -= 1
                                if inventory[itemtouse] == 0:
                                        del inventory[itemtouse]
                                return


                        for key, value in list(inventory.items()):
                            if value < 1:
                                del inventory[key]




                        print(f"\nYou currently have {inventory} in your inventory")
                        useitem = input("What item do you want to use? ")
                        if useitem in inventory:
                                if useitem == "nest egg":
                                    eggvalue = abs(250*(1+(day/10)))
                                    print("Your nest egg gains an extra 10% of its value per day")
                                    eggcheck = input(f"Are you sure you want to open your nest egg? It's value is {Fore.GREEN}{eggvalue}{Style.RESET_ALL} yes/no:")
                                    if eggcheck == "yes":
                                        print("Your nest egg EXPLODES! You gain {eggvalue}")
                                        money += eggvalue
                                        del inventory["nest egg"]
                                    else:
                                        return

                                if useitem in furnitureavailable:
                                        if yourhouse == 0:
                                                print("\nYou don't have a house to put this in!")
                                        else:
                                                if len(houseinventory) < housesavailable[yourhouse][2]:
                                                        print("\nYou place {useitem} in your {yourhouse}")
                                                        houseinventory.append(useitem)
                                                        inventory[useitem] -= 1
                                                        if inventory[useitem] == 0:
                                                                del inventory[useitem]

                                                else:
                                                        print("Your house is full!")


                                elif useitem in drugs:
                                        time.sleep(0.5)
                                        print(random.choice(["You snort that shit, your partner gives you a weird look. Whatever, haters gonna hate.","You inject it straight in to your veins!", "You chug it down","You mix it in to your cereal and then pour it all over yourself for some reason","You look at your friend and slowly put it in your mouth"]))
                                        progress += ((drugs_prices[useitem]) // 2)
                                        time.sleep(0.5)
                                        side_effect = random.choice(issues)
                                        issuevalues[side_effect] += 5
                                        print(f"The drug seems to have helped, you feel {addedprogress((drugs_prices[useitem]) // 2)}")
                                        time.sleep(0.5)
                                        print(f"You have experienced the following side effect: {side_effect}")
                                        time.sleep(0.5)
                                        inventory[useitem] -= 1
                                        if inventory[useitem] == 0:
                                                del inventory[useitem]

                                        return
                                elif useitem in items:
                                        print()
                                        time.sleep(1)
                                        if useitem == "makeup":
                                            buff = random.randint(3,6)
                                            statementsmakeup = [
                                                f"The new makeup gives you a flawless look that makes you feel like a supermodel. You feel confident and beautiful for {buff} days.",
                                                f"The new lipstick is the perfect shade and makes your lips look plump and kissable. You feel like a bombshell for {buff} days.",
                                                f"The new eye shadow palette has all the colors you need to create a bold and daring look. You feel like a makeup artist for {buff} days."
                                            ]
                                            print(random.choice(statementsmakeup))
                                            time.sleep(1)
                                            inventory[useitem] -= 1
                                            if inventory[useitem] == 0:
                                                del inventory[useitem]

                                        elif useitem == "dress":
                                                buff = random.randint(9,12)
                                                statementsdress = [
                                                        f"You look great in your new dress! The dress gives you a confidence boost for {buff} days",
                                                        f"The dress hugs your curves in all the right places and makes you feel like a million bucks! You feel like you can take on the world with this confidence boost for {buff} days.",
                                                        f"The dress is a beautiful shade of blue that brings out the color in your eyes. You can't wait to wear it out on your next date and feel extra special for {buff} days.",
                                                        f"The dress is a stunning piece of craftsmanship that makes you feel like royalty. It's perfect for any formal event and will give you a confidence boost for {buff} days."
                                                        ]
                                                print(random.choice(statementsdress))
                                                time.sleep(1)
                                                inventory[useitem] -= 1
                                                if inventory[useitem] == 0:
                                                    del inventory[useitem]

                                        elif useitem == "fancy dress":
                                            buff = random.randint(6,12)
                                            statementsfancydress = [
                                                f"The fancy dress is a work of art that makes you feel like a Hollywood starlet. You feel like a red carpet queen for {buff} days.",
                                                f"The fancy dress is a perfect fit and makes you feel like royalty. You feel like you can rule the world for {buff} days.",
                                                f"The fancy dress is a stunning shade of green that makes you feel like a mermaid. You feel like a sea siren for {buff} days."
                                            ]
                                            print(random.choice(statementsfancydress))
                                            time.sleep(1)
                                            inventory[useitem] -= 1
                                            if inventory[useitem] == 0:
                                                del inventory[useitem]

                                        elif useitem == "t-shirt":
                                            buff = random.randint(6,12)
                                            statementstshirt = [
                                                f"The new t-shirt is comfortable and has a cool design that makes you feel like a rockstar. You feel like a cool kid for {buff} days.",
                                                f"The new t-shirt is a perfect fit and has a funny slogan that makes you laugh. You feel like a comedian for {buff} days.",
                                                f"The new t-shirt is soft and has a positive message that makes you feel good. You feel like a motivational speaker for {buff} days."
                                            ]
                                            print(random.choice(statementstshirt))
                                            time.sleep(1)
                                            inventory[useitem] -= 1
                                            if inventory[useitem] == 0:
                                                        del inventory[useitem]

                                        elif useitem == "epic t-shirt":
                                            buff = random.randint(10,15)
                                            statementsepictshirt = [
                                                f"The epic t-shirt is a limited edition and makes you feel like a collector. You feel like a curator for {buff} days.",
                                                f"The epic t-shirt is a rare and makes you feel like a treasure hunter. You feel like an archaeologist for {buff} days.",
                                                f"The epic t-shirt is a unique and makes you feel like an artist. You feel like a designer for {buff} days."
                                            ]
                                            print(random.choice(statementsepictshirt))
                                            time.sleep(1)
                                            inventory[useitem] -= 1
                                            if inventory[useitem] == 0:
                                                del inventory[useitem]

                                        elif useitem == "potted plant":
                                            buff = random.randint(2,3)
                                            statementspottedplant = [
                                                f"The potted plant is a beautiful and healthy, it reminds you of the beauty of nature and the importance of taking care of it. You feel better for {buff} days.",
                                                f"The potted plant is a small piece of nature in your home, it makes you feel more connected to the environment and it's a source of inspiration for your art or writing. You feel like a naturalist for {buff} days.",
                                                f"The potted plant is a reminder of the simple things in life, it makes you feel more grateful and appreciative of the small things. You feel like a philosopher for {buff} days."
                                            ]
                                            print(random.choice(statementspottedplant))
                                            time.sleep(1)
                                            inventory[useitem] -= 1
                                            if inventory[useitem] == 0:
                                                    del inventory[useitem]
                                        buffsactive.update({useitem:buff})
                                        buff = 0
                                        progress += 5
                                        print(f"\nYour {useitem} made you feel {addedprogress(5)}. You're now " + Fore.CYAN + f"{progress_describe(progress)}" + Style.RESET_ALL + ".")
                                        del useitem


                                        # open crates:
                                elif useitem in crates_prices:
                                        opencrate(useitem)
                                        inventory[useitem] -= 1
                                        if inventory[useitem] == 0:
                                                del inventory[useitem]

                                        del useitem
                                        return
                                else:
                                        print("That is not a valid item")
                                return



                def opencrate(crate):
                                price = crates_prices[crate]



                                print(f"You start to open the {crate}")
                                time.sleep(1)
                                print("IT BURSTS OPEN!")
                                time.sleep(1)
                                price = price // 3
                                i = 0

                                if "knitting" in crate:
                                        while i < price:
                                                roll = random.randint(1,10000)
                                                extraluckychosen = random.choice(extraluckyitemsknitting)
                                                luckychosen = random.choice(luckyitemsknitting)
                                                commonchosen = random.choice(commonitemsknitting)
                                                uncommonchosen = random.choice(uncommonitemsknitting)
                                                if roll > 9950:
                                                        print(Fore.YELLOW + "You obtained: "+ Fore.YELLOW + f"{extraluckychosen}" + Style.RESET_ALL)
                                                        inventory[extraluckychosen] = inventory.get(extraluckychosen,0) + 1
                                                elif 9500 < roll <= 9950:
                                                        print(Fore.YELLOW + "You obtained: "+ Fore.CYAN + f"{luckychosen}" + Style.RESET_ALL)
                                                        inventory[luckychosen] = inventory.get(luckychosen,0) + 1
                                                elif 6500 < roll <= 9500:
                                                        print(Fore.YELLOW + "You obtained: "+ Fore.WHITE + f"{uncommonchosen}" + Style.RESET_ALL)
                                                        inventory[uncommonchosen] = inventory.get(uncommonchosen, 0) + 1
                                                elif roll <= 6500:
                                                        print(Fore.YELLOW + "You obtained: "+ Fore.WHITE + f"{commonchosen}" + Style.RESET_ALL)
                                                        inventory[commonchosen] = inventory.get(commonchosen, 0) + 1
                                                i += 1

                                if "painting" in crate:
                                    while i < price:
                                        roll = random.randint(1,10000)
                                        extraluckychosen = random.choice(extraluckyitemspainting)
                                        luckychosen = random.choice(luckyitemspainting)
                                        commonchosen = random.choice(commonitemspainting)
                                        uncommonchosen = random.choice(uncommonitemspainting)
                                        if roll > 9950:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.YELLOW + f"{extraluckychosen}" + Style.RESET_ALL)
                                            inventory[extraluckychosen] = inventory.get(extraluckychosen,0) + 1
                                        elif 9500 < roll <= 9950:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.CYAN + f"{luckychosen}" + Style.RESET_ALL)
                                            inventory[luckychosen] = inventory.get(luckychosen,0) + 1
                                        elif roll <= 6500:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.WHITE + f"{commonchosen}" + Style.RESET_ALL)
                                            inventory[commonchosen] = inventory.get(commonchosen,0) + 1
                                        elif 6500 < roll <= 9500:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.WHITE + f"{uncommonchosen}" + Style.RESET_ALL)
                                            inventory[uncommonchosen] = inventory.get(uncommonchosen, 0) + 1
                                        i += 1

                                if "directing" in crate:
                                    while i < price:
                                        roll = random.randint(1,10000)
                                        extraluckychosen = random.choice(extraluckyitemsdirecting)
                                        luckychosen = random.choice(luckyitemsdirecting)
                                        commonchosen = random.choice(commonitemsdirecting)
                                        uncommonchosen = random.choice(uncommonitemsdirecting)
                                        if roll > 9950:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.YELLOW + f"{extraluckychosen}" + Style.RESET_ALL)
                                            inventory[extraluckychosen] = inventory.get(extraluckychosen,0) + 1
                                        elif 9500 < roll <= 9950:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.CYAN + f"{luckychosen}" + Style.RESET_ALL)
                                            inventory[luckychosen] = inventory.get(luckychosen,0) + 1
                                        elif roll <= 6500:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.WHITE + f"{commonchosen}" + Style.RESET_ALL)
                                            inventory[commonchosen] = inventory.get(commonchosen,0) + 1
                                        elif 6500 < roll <= 9500:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.WHITE + f"{uncommonchosen}" + Style.RESET_ALL)
                                            inventory[uncommonchosen] = inventory.get(uncommonchosen, 0) + 1
                                        i += 1

                                if "cooking" in crate:
                                    while i < price:
                                        roll = random.randint(1,10000)
                                        extraluckychosen = random.choice(extraluckyitemscooking)
                                        luckychosen = random.choice(luckyitemscooking)
                                        commonchosen = random.choice(commonitemscooking)
                                        uncommonchosen = random.choice(uncommonitemscooking)
                                        if roll > 9950:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.YELLOW + f"{extraluckychosen}" + Style.RESET_ALL)
                                            inventory[extraluckychosen] = inventory.get(extraluckychosen,0) + 1
                                        elif roll > 9500 and roll <= 9950:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.CYAN + f"{luckychosen}" + Style.RESET_ALL)
                                            inventory[luckychosen] = inventory.get(luckychosen,0) + 1
                                        elif roll <= 6500:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.WHITE + f"{commonchosen}" + Style.RESET_ALL)
                                            inventory[commonchosen] = inventory.get(commonchosen,0) + 1
                                        elif roll > 6500 and roll <= 9500:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.WHITE + f"{uncommonchosen}" + Style.RESET_ALL)
                                            inventory[uncommonchosen] = inventory.get(uncommonchosen, 0) + 1
                                        i += 1

                                if "writing" in crate:
                                    while i < price:
                                        roll = random.randint(1,10000)
                                        extraluckychosen = random.choice(extraluckyitemswriting)
                                        luckychosen = random.choice(luckyitemswriting)
                                        commonchosen = random.choice(commonitemswriting)
                                        uncommonchosen = random.choice(uncommonitemswriting)
                                        if roll > 9950:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.YELLOW + f"{extraluckychosen}" + Style.RESET_ALL)
                                            inventory[extraluckychosen] = inventory.get(extraluckychosen,0) + 1
                                        elif roll > 9500 and roll <= 9950:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.CYAN + f"{luckychosen}" + Style.RESET_ALL)
                                            inventory[luckychosen] = inventory.get(luckychosen,0) + 1
                                        elif roll <= 6500:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.WHITE + f"{commonchosen}" + Style.RESET_ALL)
                                            inventory[commonchosen] = inventory.get(commonchosen,0) + 1
                                        elif roll > 6500 and roll <= 9500:
                                            print(Fore.YELLOW + "You obtained: "+ Fore.WHITE + f"{uncommonchosen}" + Style.RESET_ALL)
                                            inventory[uncommonchosen] = inventory.get(uncommonchosen, 0) + 1
                                        i += 1




                #-----------------------------------------USER INPUT-----------------------------------------------------------------------

                def userinput(message):
                        global money
                        global progress
                        global day

                        if message not in commands:
                                return
                        elif message == "inventory":
                                print(f"\nYour inventory consists of: {inventory}")
                                return

                        elif message == "progress":
                                print(f"You feel " + Fore.CYAN + f"{progress_describe(progress)}" + Style.RESET_ALL + "")
                                return

                        elif message == "money":
                                print(f"You have {money} pounds")
                                return

                        elif message == "shop":
                                print("You run to the shop")
                                shop()
                                return

                        elif message == "therapy":
                                therapy()
                                return
                        elif message == "work":
                                work()
                                return
                        elif message == "sleep":
                                sleep()
                                return
                        elif message == "inv":
                                use()
                                return
                        elif message == "bank":
                                if day < 7:
                                        print("The bank doesn't open until day 7!")
                                        return
                                bank(1)
                                return
                        elif message == "casino":
                                if day < 13:
                                        print("The casino doesn't open until day 13!")
                                        return
                                casino()
                                return
                        #elif message == "savegame":
                          #      savegame()
                            #    return
                        elif message == "pet":
                                if day < 10:
                                        print("The 'pet' menu will unlock on day: " + Fore.CYAN + "10" + Style.RESET_ALL)
                                        return
                                pet(1)
                                return
                        elif message == "info":
                                print("\nHere is some info about the game:")
                                print("-You will unlock new menu commands as you progress.")
                                print("-Your mood will be affected by ailments in your 'self' page, luckily they can be cured by the therapist if you decide to talk about them. So remember to check in with your'self' from time to time.")
                                print("-Rare events can happen on day 20 onwards. They can be helpful or dangerous, so prepare for them.")
                                print("-When you feel a certain way, this is what the game is referring to in order:")
                                print(f"{progress_descriptions.values()}")
                                return
                        elif message == "house":
                                housing(1)

                        elif message == "self":
                                if day >= 3:
                                        arefine = 1
                                        for p in issuevalues:
                                                        if issuevalues[p] == 3:
                                                                print("Your " + Fore.RED + f"{p}" + Style.RESET_ALL + " is moderately affecting your mood, you should talk to your therapist about it")
                                                                arefine = 0
                                                        elif issuevalues[p] == 4:
                                                                print("Your " + Fore.RED + f"{p}" + Style.RESET_ALL + " is badly affecting your mood, you should talk to your therapist about it")
                                                                arefine = 0
                                                        elif issuevalues[p] == 5:
                                                                print("Your " + Fore.RED + f"{p}" + Style.RESET_ALL + "is horribly affecting your mood, you should talk to your therapist about it")
                                                                arefine = 0
                                                        elif issuevalues[p] == 6:
                                                                print("Your " + Fore.RED + f"{p}" + Style.RESET_ALL + " is disastrously affecting your mood, you should talk to your therapist about it")
                                                                arefine = 0
                                                        elif issuevalues[p] > 6:
                                                                print("Your " + Fore.RED + f"{p}" + Style.RESET_ALL + " is CATASTROPHICALLY affacting your mood, you should talk to your therapist about it")
                                                                arefine = 0
                                        if arefine == 1:
                                                print(Fore.GREEN + "\nYou don't feel anything that might hurt your mood at the moment."+ Style.RESET_ALL)
                                        time.sleep(0.5)
                                else:
                                        print("The 'self' command isn't available until day 3!")

                        elif message == "hobby":
                                if day < 5:
                                        print("The 'hobby' menu will unlock on day: " + Fore.CYAN + "5" + Style.RESET_ALL)
                                        time.sleep(1)
                                        return
                                hobby()


        #---------------------------------------------SAVE AND LOAD--------------------------------------------------------------------

             #   def savegame():
             #       global day
               #     global money
              #      global inventory
             #       global progress
               #     global buffsactive
              #      global tiredness
                #    global bankbalance
#
  #                  message = input("Would you like to save this game, or load a game? ")
    #                if message == "save":
      #                  savegameid = input("Choose a name for your savegame: ")
        #                variablelist = [day, money, inventory, progress, buffsactive, tiredness, bankbalance]
          #              with open(f"savefile.pickle", 'ab') as filesave:
            #                        pickle.dump({savegameid: variablelist}, filesave)
              #                      print("Your game was saved!")
                #    elif message == "load":
 #                       with open("savefile.pickle", "rb") as fileload:
   #                         loadgame = pickle.load(fileload)
     #                       loadgameid = input("Which game would you like to load? ")
       #                     if loadgameid in loadgame:
         #                       variablelist = loadgame[loadgameid]
           #                     day, money, inventory, progress, buffsactive, tiredness, bankbalance = variablelist
             #                   print("Game Loaded!")
               #             else:
#                                print("That was an invalid name")
  #                  else:
    #                    print("Invalid choice, returning to game.")

        #--------------------------------------------------------PETS BLOCK--------------------------------------------------------

                def pet(useropen):
                        global petcaredfor
                        global pettrained
                        global petbathed
                        global petgroomed
                        global petpowermultiplier
                        global petname
                        global petmood
                        global petgoodmoodlist
                        global petbadmoodlist
                        global progress
                        global havepet
                        global money
                        global groomedtoday
                        global bathedtoday
                        global pettoday
                        global trainedtoday
                        global trained_descriptions

                        if useropen == 1:
                                if havepet == 1:
                                        while True:
                                                print(f"You check in on your pet {petname}, what would you like to do?")

                                                print("\n1. Groom them")
                                                print("2. Bathe them")
                                                print("3. Train them")
                                                print("4. Pet them")
                                                print("5. Give up for adoption")

                                                try:

                                                        choice = int(input("\nWhat do you want to do with your pet?"))
                                                        time.sleep(1)


                                                        if choice == 1:
                                                                if groomedtoday == 0:

                                                                        print(f"You go over to groom {petname}")

                                                                        if random.randint(0, 100) <= pettrained:
                                                                                print(f"\nYou groom {petname}, {random.choice(['they wag their tail happily.', 'they roll over for belly rubs.', 'they jump up and lick your face.', 'they curl up next to you and fall asleep.', 'they stretch and yawn.', 'they sniff around excitedly.', 'they make a contented chirp.', 'they whine softly.', 'they cuddle close to you', 'they scratch their back against the couch.','they dig in their bedding.'])}")
                                                                                petgroomed += 4
                                                                        else:
                                                                                print(f"\nYou try to groom {petname}, but {random.choice(['they run away from the brush', 'they try to bite the brush', 'they growl and snap at the brush', 'they hide under the couch', 'they whine and cry', 'they cower in fear', 'they freeze and become unresponsive', 'they jump and scatter their bedding'])}")
                                                                                time.sleep(1)
                                                                                print(f"Maybe {petname} isn't in the mood, this would be easier if I train them more.")
                                                                        groomedtoday = 1
                                                                else:
                                                                        print(f"You already groomed {petname} today.")

                                                        if choice == 2:
                                                                if bathedtoday == 0:
                                                                        if random.randint(0, 100) <= pettrained:
                                                                                print(f"\nYou wash {petname}, {random.choice(['they stand still and let you wash them.', 'they shake off the excess water after youre done.', 'they sniff around the bathroom excitedly.', 'they shake their head to get the water out of their ears', 'they stretch and yawn after the bath.', 'they enjoy the warm water.', 'they lay down and relax.','they splash around in the water.','they turn around to let you wash their back.'])}")
                                                                                petbathed += 5
                                                                        else:
                                                                                print(f"\nYou try to wash{petname}, but {random.choice(['they run away from the tub.', 'they try to bite you.', 'they growl and snap at you.', 'they lay down and refuse to move.', 'they hide under the couch.', 'they shake and tremble.','they resist getting into the tub.','they try to jump out of the tub.','they make a fuss.'])}")
                                                                                time.sleep(1)
                                                                                print(f"Maybe {petname} isn't in the mood, this would be easier if I train them more.")
                                                                        bathedtoday = 1
                                                                else:
                                                                       print(f"You already bathed {petname} today. ")
                                                        if choice == 3:
                                                                if trainedtoday == 0:
                                                                        print(f"You train {petname} {random.choice(['by training him to sit','by using clicker training','by training him high five','by teaching him to fetch','by teaching him to roll over','by teaching him to come when called','by teaching him to shake','by teaching him to stay','by teaching him to lay down','by teaching him to speak'])}")
                                                                        pettrained += 5
                                                                        trainedtoday= 1
                                                                        if pettrained > 100:
                                                                                pettrained = 100
                                                                else:
                                                                        print(f"You already trained {petname} today.")


                                                        if choice == 4:
                                                                if pettoday == 0:
                                                                        print(f"You play with {petname} {random.choice(['by playing fetch.','by playing tug of war.','by playing hide and seek.','by playing chase.','by playing with interactive toys.','by playing with laser pointer.','by playing dress up.','by playing fetch with a frisbee.','by playing with a ball.','by playing with a squeaky toy.'])}")
                                                                        time.sleep(1)
                                                                        petmood += 3
                                                                        print(f"\nYour pet looks {addedprogress(3)}, he's now {progress_describe(petmood)}")
                                                                else:
                                                                        print(f"You already pet {petname} today.")

                                                        if choice == 5:
                                                                        if input(f"Are you sure you want to give {petname} away? Type their name to continue: ") == petname:
                                                                                time.sleep(1)
                                                                                print(f"\nYou give {petname} to a new owner, you're sure they'll be happy in their new home.")
                                                                                havepet = 0
                                                                                petname = ""
                                                                                return
                                                                        else:
                                                                                print(f"\nYou keep {petname}")
                                                                                return
                                                        break


                                                except:
                                                        print(f"\nInvalid choice. Input the number of the activity you want")
                                                        time.sleep(1)
                                                        break

                                if havepet == 0:
                                        while True:
                                                if progress < 240:
                                                        print("\nYou don't feel ready to take care of a pet yet.. maybe when you feel better")
                                                        time.sleep(1)
                                                        return

                                                else:
                                                       print("\nYou walk to the pet shop to buy a pet.")
                                                       time.sleep(1)
                                                       print("\nThese pets are available for purchase for £300:")
                                                       print("1. Dog")
                                                       print("2. Cat")
                                                       print("3. Fox")
                                                       print("4. Leave shop")

                                                try:
                                                        while True:
                                                                petchoice = int(input("\nWhich pet would you like to buy? (Enter number): "))
                                                                time.sleep(1)
                                                                if money >= 300:
                                                                        if petchoice == 1:
                                                                                petname = input("You bought a dog! What would you like to call them? ")
                                                                                money -= 300
                                                                                break
                                                                        elif petchoice == 2:
                                                                                petname = input("You bought a cat! What would you like to call them? ")
                                                                                money -= 300
                                                                                break
                                                                        elif petchoice == 3:
                                                                                petname = input("You bought a fox! What would you like to call them? ")
                                                                                money -= 300
                                                                                break
                                                                        elif petchoice not in [1,2,3]:
                                                                                print(f"\nInvalid choice. Input the number of the type of pet you want")
                                                                                break
                                                                        elif petchoice == 4:
                                                                                return
                                                                else:
                                                                        print("\nSorry, you don't have enough money to afford a pet!")
                                                                        time.sleep(1)
                                                                        return
                                                        time.sleep(1)
                                                        print(f"\nYou think {petname} is a great name for your pet!, you can now acess your pets menu with the 'pet' command")
                                                        havepet = 1
                                                        time.sleep(1)
                                                        return
                                                except:
                                                        print(f"\nInvalid choice. Input has to be the number of the pet you'd like to buy.")
                                                        time.sleep(1)
                                                        return
                                return


                        if useropen == 0:
                                        if havepet == 1:

                                                print("\nPET STATUS")
                                                print("------------------")


                                                groomedtoday = 0
                                                bathedtoday = 0
                                                trainedtoday = 0
                                                pettoday = 0
                                                petmood -= 5
                                                petbathed -= 1
                                                petgroomed -= 1
                                                petrun = 0


                                                if petbathed <= 0:
                                                        petbathed = 0
                                                        print(f"{petname} smells. It negatively affects your mood. You should probably bathe them..")
                                                        progress -= 4
                                                elif petbathed > 0:
                                                        print(f"{petname} seems content with how bathed they are.")
                                                        petmood += 2

                                                if petgroomed <= 0:
                                                        petgroomed = 0
                                                        print(f"{petname}'s fur is all ruffled and matted, it looks like it's affecting their mood. You should probably groom them..")
                                                        petmood -= 5
                                                elif petgroomed > 0:
                                                        print(f"{petname} seems content with how groomed they are.")
                                                        petmood += 2

                                                print (f"{petname} looks like they feel {progress_describe(petmood)}")
                                                print("\n")

                                                if petmood > 235 and pettrained > 80:
                                                        chance = random.randint(0,100)
                                                        present = random.choice(list(crates_prices.keys()))
                                                        if chance > 80:
                                                            print("My pet found a {present} for me!! It must be because they're well trained and happy!")


                                                #pet run away
                                                if petmood < 200:
                                                        petrunchance = 200 - petmood
                                                        petrundice = random.randint(100,200)
                                                        print(f"Your pet looks {progress_describe(petmood)} it looks like it might run away...")
                                                        time.sleep(3)
                                                        if petrundice >= petrunchance:
                                                                petrun = 0
                                                                print("It looks like they decided to stay. I should try to make them happier..")
                                                        else:
                                                                petrun = 1

                                                if petrun == 1:
                                                           print("\nYour pet, {petname} ran away! Oh no! :(")
                                                           progress = -20
                                                           petname = ""
                                                           havepet = 0
                                                           petmood = 230
                                                           print("\nYou're devestated by this, you now feel " + Fore.CYAN + f"{progress_describe(progress)}" + Style.RESET_ALL + "")
                                                           time.sleep(3)
                        return
        #------------------------------------PROGRESS DESCRIPTOR-----------------------------------------------------------------------------


                def progress_describe(progress):

                        global progressdescriber

                        closest_description = None
                        closest_distance = float("inf")
                        if 100 < progress <= 300:
                                for p in progress_descriptions.keys():
                                        distance = abs(p - progress)
                                        if distance < closest_distance:
                                            closest_distance = distance
                                            closest_description = progress_descriptions[p]

                                            progressdescriber = closest_description

                        elif progress > 300:

                                closest_description = "on top of the world!"

                        else:
                                closest_description = "absolute and utter depressive despair"



                        return closest_description

                def training_describe(progress):
                        closest_description = None
                        closest_distance = float("inf")
                        if 100 < progress <= 300:
                                for p in trained_descriptions.keys():
                                        distance = abs(p - progress)
                                        if distance < closest_distance:
                                            closest_distance = distance
                                            closest_description = trained_descriptions[p]

                        elif progress > 300:

                                closest_description = "on top of the world!"

                        else:
                                closest_description = "absolute and utter depressive despair"

                        return closest_description




                            # -------------------------------------------THERAPY BLOCK---------------------------------------------------------------

                def therapy():
                        global issuevalues

                        currentissues = []
                        i = 0
                        while i < 3:
                                addtocurrentissues = random.choice(issues)
                                if addtocurrentissues not in currentissues:
                                        currentissues.append(addtocurrentissues)
                                        addtocurrentissues = ""
                                        i += 1
                        print("\nYou are discussing the following issues: " + Fore.RED + f"{currentissues}" + Style.RESET_ALL)
                        x = input("Which issue would you like to focus on during this session? ")
                        os.system('cls')
                        if x in currentissues:
                                time.sleep(1)
                                global progress
                                progress += 8
                                print(Fore.GREEN + f"\nYou feel better after therapy." + Style.RESET_ALL)
                                matchingnumb = 0
                                if issuevalues[x] > 2:
                                        print(f"You worked through your " + Fore.RED+ f"{x}" + Style.RESET_ALL + " and you feel completely relieved of the issue.")
                                issuevalues[x] = 0
                                payment = random.randint(15,45)
                                global money
                                money = money - payment
                                print(f"The Therapist takes a payment of £{payment}.")
                                time.sleep(1)
                                return

                        else:
                                print(f"That is not a valid issue. The Therapist gives you a strange look.")
                                return

                    #------------------------------------------------------------WORK BLOCK------------------------------------------------------------------
                def work():
                                global progress
                                global money
                                global issuevalues
                                global hasworked

                                if hasworked == 0:
                                        #playsound("typing.mp3")
                                        earnings = random.randint(42,70)

                                        money += earnings

                                        time.sleep(1)
                                        print("\nYou go to work..")
                                        time.sleep(1)
                                        progressloss = random.randint(8, 16)
                                        progress -= progressloss
                                        print()
                                        print(random.choice(["my junior colleague keeps interrupting my workflow with small talk and it's starting to drive me crazy.",
                                        "my boss just told me I was doing something wrong in front of the whole team and I feel embarrassed.",
                                        "my friend at work just took credit for my idea in the meeting and I'm not sure how to confront him about it.",
                                        "my colleague is always hogging the shared resources and it's slowing down my progress.",
                                        "a friend keeps texting me over and over, its making it hard to focus on my own tasks so I couldn't get much work done.",
                                        "my boss just gave me a deadline that I know is impossible to meet and I don't know how to tell them.",
                                        "my boss just gave me a poor performance review and I don't agree with their assessment.",
                                        "my work friend is spreading rumors about me behind my back and it's affecting my relationships with coworkers.",
                                        "my colleague is always trying to one-up me and it's making me feel insecure in my abilities.",
                                        "my friend just texted to complain about me and it's stressing me out."]))
                                        time.sleep(1)
                                        print(Fore.RED + f"You feel {addedprogress(-progressloss)} because of this." + Style.RESET_ALL)
                                        time.sleep(1)
                                        print(f"\nYou earned " + Fore.LIGHTYELLOW_EX + f"£{earnings}" + Style.RESET_ALL + " at work.")

                                        issuevalues[random.choice(issues)] += 2
                                        hasworked = 1
                                else:
                                        time.sleep(0.5)
                                        print(Fore.RED + "\nYou've already been to work today!" + Style.RESET_ALL)

                                return

                #------------------------------------------------------HOUSING BLOCK---------------------------------------------

                def housing(userinput):
                        global yourhouse
                        global inventory
                        global houseinventory
                        global money
                        global progress
                        global rentdue

                        if userinput == 1:
                                os.system('cls')
                                print("[HOUSING]")
                                print("_______________")
                                print("1. Check on house")
                                print("2. Buy furniture")
                                print("3. Sell house or move out")
                                print("_______________")
                                try:
                                        choice = input("What would you like to do?")
                                        choice = int(choice)
                                        if choice == 1 and yourhouse == 0:
                                                print("You don't have a house, would you like to buy one?")
                                                for house in housesavailable.keys():
                                                        rent = housesavailable[house][0]
                                                        price = housesavailable[house][1]
                                                        description = housesavailable[house][3]
                                                        furniturespace = housesavailable[house][2]
                                                        print(f"\n" + Fore.GREEN + f"{house}" + Style.RESET_ALL)
                                                        time.sleep(0.1)
                                                        print(f"Rent: £{rent}")
                                                        time.sleep(0.1)
                                                        print(f"Price: £{price}")
                                                        time.sleep(0.1)
                                                        print(f"Furniture spaces: {furniturespace}")
                                                        time.sleep(0.1)
                                                        print(f"{description}")
                                                        time.sleep(0.1)
                                                print("[Rent is taken every 5 days, whereas price is a one-time upfront cost.]")
                                                choicehouse = input("\nWhich would you like to buy?: ")
                                                if choicehouse in housesavailable.keys():
                                                        if money >= housesavailable[choicehouse][1]:
                                                                os.system('cls')
                                                                print (Fore.CYAN + f"\nCongratulations! You now own a {choicehouse}" + Style.RESET_ALL)
                                                                yourhouse = choicehouse
                                                                money -= housesavailable[choicehouse][1]
                                                        else:
                                                                os.system('cls')
                                                                print(f"\nYou can't afford {choicehouse}")
                                        elif choice == 1 and yourhouse != 0:
                                                print(f"\nYou check on your {yourhouse}")
                                                if len(houseinventory) > 0:
                                                        print("Your house consists of: ")
                                                        for l in houseinventory:
                                                                print(f"- {l}")
                                                else:
                                                        print("\nYour house is empty, you should buy some furniture for it.")
                                        elif choice == 2:
                                                        for furniture in furnitureavailable.keys() :
                                                                price = furnitureavailable[furniture][0]
                                                                description = furnitureavailable[furniture][2]
                                                                print(f"\n{furniture}")
                                                                print(f"Price: £{price}")
                                                                print(f"{description}")
                                                        furniturechoice = input("\nWhich would you like to buy?")
                                                        if furniturechoice in furnitureavailable.keys():
                                                                if money >= furnitureavailable[furniturechoice][0]:

                                                                        if yourhouse == 0:
                                                                                os.system('cls')
                                                                                print(f"\nYou don't have a house, but you could put {furniturechoice} in your inventory until you do.")
                                                                                if input(f"\nDo you still want to buy {furniturechoice}? yes/no: ") == "yes":
                                                                                                inventory[furniturechoice] = inventory.get(furniturechoice, 0) + 1
                                                                                                money -= furnitureavailable[furniturechoice][0]
                                                                                                time.sleep(0.5)
                                                                                                print(f"\nYou put the {furniturechoice} in your inventory.")
                                                                        else:
                                                                                if len(houseinventory) < housesavailable[yourhouse][2]:
                                                                                    inventory[furniturechoice] = inventory.get(furniturechoice, 0) - 1
                                                                                    if inventory[furniturechoice] == 0:
                                                                                        del inventory[furniturechoice]
                                                                                    money -= furnitureavailable[furniturechoice][0]
                                                                                    time.sleep(0.5)
                                                                                    os.system('cls')
                                                                                    print(f"\nYou put the {furniturechoice} in your {yourhouse}.")
                                                                                else:
                                                                                    print(f"There's no more room for furniture in your {yourhouse}!")
                                                                else:
                                                                        time.sleep(0.5)
                                                                        os.system('cls')
                                                                        print("You can't afford that.")
                                        elif choice == 3:
                                                if yourhouse != 0:
                                                        if input("\nAre you sure you want to sell your {yourhouse}? yes/no: ") == "yes":
                                                                houseinventory = []
                                                                money += housesavailable[yourhouse][1]
                                                                os.system('cls')
                                                                print(f"\nYou sell your house for £{housesavailable[yourhouse][1]}")

                                                                yourhouse = 0
                                                        else:
                                                                os.system('cls')
                                                                print("\nYou don't sell your {yourhouse}")
                                                else:
                                                        os.system('cls')
                                                        print("\nYou don't have a house")


                                except Exception as error: print(error)


                        else:
                                if yourhouse != 0:
                                        rentdue += 1
                                        if rentdue == 5:
                                                rentdue = 0
                                                print("\nYour landlord has asked for your rent.")
                                                print(f"You pay £{housesavailable[yourhouse][0]}.")
                                                money -= housesavailable[yourhouse][0]
                                                time.sleep(2)

                                if len(houseinventory) > 0:
                                        print()
                                for i in houseinventory:
                                        progress += furnitureavailable[i][1]
                                        print(f"Your {i} makes you feel {addedprogress(furnitureavailable[i][1])}")

                        return




                    #------------------------------------------------------------SHOP BLOCK------------------------------------------------------------------
                def shop():
                                global money
                                global inventory
                                global buffsactive
                                global day
                                os.system('cls')
                                itembought = 0
                                print("What would you like to purchase?")
                                print(Fore.CYAN + "1. " + Style.RESET_ALL + "Drugs")
                                print(Fore.CYAN + "2. " + Style.RESET_ALL + "Items")
                                print((Fore.CYAN + "3. " + Style.RESET_ALL + "Crafting crates"))
                                print((Fore.CYAN + "4. " + Style.RESET_ALL + "Sell"))
                                print((Fore.CYAN + "5. " + Style.RESET_ALL + "Scrap trader"))
                                try:
                                        page = int(input("Type a number: "))
                                        if page < 1:
                                                return
                                        if page > 5:
                                                return
                                except:
                                        return

                                if page == 1:
                                        os.system('cls')
                                        print("\nHere are the available items:")
                                        print("********************************")
                                        for drugs, price in drugs_prices.items():
                                                if drugs not in inventory.keys() and drugs not in buffsactive.keys():
                                                    print(f"- {drugs} - price: {price}")
                                        print("********************************")
                                        print(f"You have £{money}")
                                        itembought = input("\nWhich drug would you like to buy? ")
                                if page == 2:
                                        os.system('cls')
                                        print("\nHere are the available items:")
                                        print("********************************")
                                        for items, price in items_prices.items():
                                                if items not in inventory.keys() and items not in buffsactive.keys():
                                                    print(f" - {items} - price: {price}")
                                        print("********************************")
                                        print(f"You have £{money}")
                                        itembought = input("\nWhich item would you like to buy?: ")
                                if page == 3:
                                        os.system('cls')
                                        if day < 5:
                                                print("Crate purchases are not available until day 5.")
                                                return
                                        print("\nHere are the available items:")
                                        print("********************************")
                                        for crate, price in crates_prices.items():
                                                if crate == "general crate":
                                                        donothing = 1
                                                else:
                                                        print(f" - {crate} - price: {price}")
                                        print("********************************")
                                        print(f"You have £{money}")
                                        itembought = input("\nWhich crate would you like to buy?: ")

                                if itembought in inventory.keys():
                                        if itembought not in list(crates_prices.keys()):
                                                print(f"The shop has run out of {itembought}")
                                                return

                                if page == 4:
                                        os.system('cls')
                                        value = 0
                                        difficulty = 0
                                        for ininv in inventory:
                                            if ininv in hobbyitemswriting or ininv in hobbyitemsknitting or ininv in hobbyitemscooking or ininv in hobbyitemsdirecting or ininv in hobbyitemspainting:
                                                print(inventory[ininv])
                                        print(inventory)
                                        print("Note: The shopkeeper will only buy hobby-crafted items!")
                                        itemchosen = input("What would you like to sell?: ")
                                        if itemchosen in inventory:
                                            if itemchosen in hobbyitemswriting or itemchosen in hobbyitemsknitting or itemchosen in hobbyitemscooking or itemchosen in hobbyitemsdirecting or itemchosen in hobbyitemspainting:
                                                for pl in (itemdifficultycooking,itemdifficultywriting,itemdifficultydirecting,itemdifficultyknitting,itemdifficultypainting):
                                                    if pl == itemchosen:
                                                        difficulty = pl
                                                shoppinglist = {}
                                                for hobby,hobbyingslist in itemingslist.items():
                                                    for item, ingswithprice in hobbyingslist.items():
                                                        if item == itemchosen:
                                                            shoppinglist = hobbyingslist[item]
                                                for item, amount in shoppinglist.items():
                                                    shoppinglistcopy = shoppinglist.copy()
                                                    while item in shoppinglistcopy:
                                                            value += shoppinglistcopy[item]
                                                            shoppinglistcopy[item] -= 1
                                                            if shoppinglistcopy[item] == 0:
                                                                del shoppinglistcopy[item]
                                                print(value)






                                                value = value * (1+(difficulty*0.01)) + 30

                                                sale = input(f"Would you like to sell {itemchosen} for {value}? yes/no: ")
                                                if sale == "yes":
                                                    try:
                                                        salenumber = abs(int(input(f"How many would you like to sell?: ")))
                                                    except:
                                                        print("Please enter a number.")
                                                        return
                                                    if salenumber > inventory[itemchosen]:
                                                        print(f"Stop trying to swindle me, I know you don't have that many {itemchosen}'s!")
                                                    else:
                                                        print(f"You have sold {salenumber} {itemchosen}'s.")
                                                        money += value * salenumber
                                                        inventory[itemchosen] = inventory.get(itemchosen, 0) - salenumber
                                                        if inventory[itemchosen] == 0:
                                                                del inventory[itemchosen]
                                                    return
                                                elif sale == "no":
                                                    print("Okay, let me know if you change your mind.")
                                                    return
                                                else:
                                                    print("Invalid input, please enter 'yes' or 'no'.")
                                                    return
                                            else:
                                                print("Sorry, we only buy hobby-crafted items in this store!")
                                                return
                                        else:
                                            print(f"You don't have any {itemchosen}!")
                                        return

                                if page == 5:
                                        if day < 15:
                                                print(f"I'm in a muddle with all my scrap here at Scrappy's Scrap! How about you come back in {15 - day} days time!")
                                        else:
                                            os.system('cls')
                                            print("You have:")
                                            for scrapcheck in list(inventory.keys()):
                                                    if "scrap" in scrapcheck:
                                                            print(f"{inventory[scrapcheck]}")

                                            scrapitem = input("Howdy, welcome to Scrappy's Scraps! What ingredient would you like me, Scrappy to make with yer scrap?: ")
                                            scrapitemamount = int(input(f"Okay that's spectilitacular! And how many {scrapitem}'s can I do yer for?: "))

                                            if scrapitem not in ["legendary scrap", "rare scrap", "uncommon scrap", "common scrap"]:
                                                    if scrapitem in extraluckyitems:
                                                            if inventory["legendary scrap"] >= (3*scrapitemamount):
                                                                    inventory[scrapitem] = inventory.get(scrapitem, 0) + scrapitemamount
                                                                    inventory["legendary scrap"] -= 3
                                                                    if inventory["legendary scrap"] == 0:
                                                                        del inventory["legendary scrap"]
                                                    if scrapitem in luckyitems:
                                                            if inventory["rare scrap"] >= (3*scrapitemamount):
                                                                    inventory[scrapitem] = inventory.get(scrapitem, 0) + scrapitemamount
                                                                    if inventory["rare scrap"] == 0:
                                                                        del inventory["rare scrap"]
                                                    if scrapitem in uncommonitems:
                                                            if inventory["uncommon scrap"] >= (3*scrapitemamount):
                                                                    inventory[scrapitem] = inventory.get(scrapitem, 0) + scrapitemamount
                                                                    if inventory["uncommon scrap"] == 0:
                                                                        del inventory["uncommon scrap"]
                                                    if scrapitem in commonitems:
                                                            if inventory["common scrap"] >= (3*scrapitemamount):
                                                                    inventory[scrapitem] = inventory.get(scrapitem, 0) + scrapitemamount
                                                                    if inventory["common scrap"] == 0:
                                                                        del inventory["common scrap"]
                                                            else:
                                                                    print("Heh heh! Sorry! You'll need 3 scraps to make one item! I just LOOOOOVE scrap!")
                                                                    return
                                                    else:
                                                            print("Uhhh, you know I can make just about any ingredient here at Scrappy's Scraps, but that just ain't somethin' I've heard of before!")
                                                            return

                                            else:
                                                    print("You want to make scrap out of scrap? That sounds like somethin ol' Scrappy would enjoy doing! Sorry! I'm not giving you any scrap!")
                                            return


                                else:

                                        if itembought in drugs_prices:
                                            if money >= drugs_prices[itembought]:
                                                money -= drugs_prices[itembought]
                                                print(f"\nYou have successfully bought {itembought} for £{drugs_prices[itembought]}, you put it in your [inventory]")
                                                #playsound("cashmachine.mp3")
                                                inventory[itembought] = inventory.get(itembought, 0) + 1

                                            else:
                                                print("You don't have enough money to buy this drug")
                                                return
                                        elif itembought in items_prices:
                                            if money >= items_prices[itembought]:
                                                money -= items_prices[itembought]
                                                print(f"You have successfully bought {itembought} for £{items_prices[itembought]}, you put it in your [inventory]")
                                                #playsound("cashmachine.mp3")
                                                inventory[itembought] = inventory.get(itembought, 0) + 1
                                            else:
                                                print("You don't have enough money to buy this item.")
                                                return
                                        elif itembought in crates_prices:
                                            if money >= crates_prices[itembought]:
                                                money -= crates_prices[itembought]
                                                print(f"You have successfully bought {itembought} for £{crates_prices[itembought]}.")
                                                #playsound("cashmachine.mp3")
                                                inventory[itembought] = inventory.get(itembought, 0) + 1
                                                use(1,itembought)
                                            else:
                                                print("You don't have enough money to buy this item.")
                                                return

                                        else:
                                            time.sleep(0.5)
                                            return

        #----------------------------------------------CASINO BLOCK---------------------------------------------
                def casino():
                        os.system('cls')
                        choiceslist = ["1. Roulette", "2. Exit"]
                        choicesnum = len(choiceslist)
                        choice = 2
                        print("\nActivities available at the casino:")
                        print(choiceslist)
                        try:
                                choice = int(input("\nType the number of the activity you'd like to do: "))
                        except:
                                print(f"\nInvalid choice. Input the number of the activity you want")
                                casino()
                        if choice <= choicesnum:
                                if choice == 1:
                                     roulette()
                                elif choice == 2:
                                    return



                def roulette():
                    global money
                    os.system('cls')
                    while money > 0:
                        print(f"\nYou have £{money}.")
                        print("1. Bet on a specific number")
                        print("2. Bet on a color")
                        print("3. Leave the game")
                        choice = int(input("What would you like to do? "))

                        if choice == 1:
                            number = int(input("Which number would you like to bet on (0-36)? "))
                            bet = int(input("How much would you like to bet? "))
                            if bet > money:
                                print("You don't have enough money.")
                                continue
                            money -= bet
                            winning_number = random.randint(0, 36)
                            if number == winning_number:
                                print("Congratulations! You won £" + str(bet * 35) + "!")
                                money += bet * 35
                            else:
                                print("Sorry, the winning number was " + str(winning_number) + ".")
                        elif choice == 2:
                            color = input("Which color would you like to bet on (red or black)? ")
                            bet = int(input("How much would you like to bet? "))
                            if bet > money:
                                print("You don't have enough money.")
                                continue
                            money -= bet
                            winning_number = random.randint(0, 36)
                            if (color == "red" and winning_number in range(1, 36, 2)) or (color == "black" and winning_number in range(0, 36, 2)):
                                print("Congratulations! You won $" + str(bet) + "!")
                                money += bet * 2
                            else:
                                print("Sorry, the winning number was " + str(winning_number) + ".")
                        elif choice == 3:
                            print("Thanks for playing!")
                            break
                        else:
                            print("Invalid choice.")
                    if money <= 0:
                        print("You have no money. The casino throws you out.")

        #-----------------------------------------BANK BLOCK-----------------------------------------------

                def bank(useropen):
                        global bankbalance
                        global money
                        dailybankearning = 0

                        if useropen == 1:
                                os.system('cls')
                                time.sleep(1)
                                print(f"\nWelcome to " + Fore.LIGHTYELLOW_EX +f"{yourname} BANK LTD." + Style.RESET_ALL + "Any money stored here will accrue " +Fore.LIGHTCYAN_EX + "5% interest per day" + Style.RESET_ALL)
                                time.sleep(1)
                                print(f"\nYou have £{bankbalance} in your bank")
                                print(f"You have £{money} in your wallet")
                                time.sleep(1)
                                bankchoice = (input("\nWhat would you like to do at the bank? deposit/withdraw: "))

                                if bankchoice == "deposit":
                                        try:
                                                invest = float(input("How much money would you like to deposit?: "))
                                        except:
                                                print(f"\nAn internal {yourname} BANK LTD error has occurred, sorry for the inconvenience. Exiting bank")
                                                return

                                        if  invest <= money and invest > 0:
                                                money -= invest
                                                bankbalance += invest
                                                bankbalance = round(bankbalance, 2)
                                                time.sleep(1)
                                                print (f"\nYour bank balance is now £{bankbalance}")
                                                time.sleep(1)
                                                return
                                        else:
                                                print("You don't have enough money to invest that amount")
                                                return


                                elif bankchoice == "withdraw":
                                        try:
                                                withdrawamount = float(input(f"Your balance is £{bankbalance}, how much would you like to withdraw?"))
                                        except:
                                                print(f"\nAn internal {yourname} BANK LTD error has occurred, sorry for the inconvenience. Exiting bank")
                                                return
                                        print("You enter your pin number. Beep boop boop bee-, no wait.. Boop beep beep boop!")
                                        time.sleep(1)

                                        if withdrawamount <= bankbalance:
                                                money += withdrawamount
                                                bankbalance -= withdrawamount
                                                time.sleep(1)
                                        else:
                                                print(f"The ATM returns an error: You don't have that much money.")
                                                print("Damn.. it was worth a try...")
                                        return

                                else:
                                        return

                        else:
                                if bankbalance > 0:
                                        dailybankearning = round((bankbalance * 1.05), 2) - bankbalance
                                        bankbalance = bankbalance + dailybankearning



                    #---------------------SLEEP BLOCK-------------------------
                def sleep():
                            global suicide
                            global money
                            global progress
                            global day
                            global bad_events
                            global rare_events
                            global issuevalues
                            global itemscrafted
                            global hasworked
                            global bankbalance
                            global commands

                            suicide = 0
                            print("\nYou go to bed.....")
                            time.sleep(0.5)
                            print(". . . .")
                            time.sleep(0.5)
                            print(". . . .")
                            time.sleep(0.5)

                        # Check for suicide

                            if progress < 200:
                                suicidechance = 300 - progress
                                suicidedice = random.randint(100,200)
                                print(f"You are feeling suicidal, there is a {suicidechance-100}% chance of you committing suicide.")
                                time.sleep(1)
                                print("You pace back and forth.")
                                time.sleep(1)
                                print("You cry.")
                                time.sleep(1)
                                print("You scream.")
                                time.sleep(3)
                                if suicidedice >= suicidechance:
                                        suicide = 0
                                        print("You decide against it..")
                                else:
                                        suicide = 1

                            if suicide == 1:
                                   print(f"\nYou hate feeling " + Fore.CYAN + f"{progress_describe(progress)}" + Style.RESET_ALL + ", you decide to commit suicide")
                                   print(f"You made it to day: {day}")
                                   print("\nGAME OVER")
                                   time.sleep(3)
                                   sys.exit()



                            day += 1

                            print("----------------------------------------------------------------------")
                            print(Fore.BLACK + Back.YELLOW+f"A new day begins, it is now day {day}!")
                            print(Fore.GREEN + chinese_proverbs[day-2] + Style.RESET_ALL)
                            print("----------------------------------------------------------------------")

                            #playsound("rooster.mp3")
                            hasworked = 0
                            bank(0)
                            housing(0)
                            issuevalues[random.choice(issues)] += 2
                            itemscrafted = 0


                            for r in issuevalues:
                                    if issuevalues[r] > 2:
                                            issueeffect = issuevalues[r]
                                            progress -= issueeffect

                            time.sleep(1)
                            progressbeforebuffs = progress
                            for n in buffsactive.copy():
                                if buffsactive[n] > 0:
                                    progress += 3
                                    print(f"You feel {addedprogress(3)} because of your {n}")
                                    time.sleep(1)
                                    buffsactive[n] -= 1
                                    if buffsactive[n] == 0:
                                        del buffsactive[n]




                            # Check for random events
                            if random.randint(1, 10) > 5:
                                bad_event_list = list(bad_events.keys())
                                event = random.choice(bad_event_list)
                                print(event)
                                progress -= bad_events[event][0]
                                money -= bad_events[event][1]
                                print(f"You lost £{bad_events[event][1]} and feel {addedprogress(-bad_events[event][0])}")
                                time.sleep(0.5)
                            else:
                                print("\nYou avoid any bad events today.")

                            #Check for rare events
                            if day > 20:
                                    if random.randint(1,12) > 11:
                                            print(Fore.CYAN + "\n__[RARE EVENT!!!!]__" + Style.RESET_ALL)
                                            #playsound("ding.mp3")
                                            eventpicked = random.choice(list(rare_events.keys()))
                                            print(eventpicked)
                                            money = money + rare_events[eventpicked][1]
                                            progress = progress + rare_events[eventpicked][0]
                                            print(f'\nYou now have: £{money} you feel {addedprogress(rare_events[eventpicked][0])}.')



                            pet(0)

                            totalcash = money + bankbalance
                            if totalcash < 0:
                                time.sleep(0.5)
                                progress -= int(abs(totalcash))
                                changeinprogress = -int(abs(totalcash))
                                print(f"\nYou're pretty broke, that makes you feel " + Fore.CYAN + f"{addedprogress(changeinprogress)}" + Style.RESET_ALL + "")

                            print("\nYou walk to therapy...")
                            therapy()
                            if day == 3:
                                    print("\nI should probably be more specific about what I would like my therapist to work with me on.")
                                    print(Fore.MAGENTA + "You unlocked the 'self' command!\n" + Style.RESET_ALL)
                            if day == 5:
                                    print("\nHmm, it's been a long time since I did anything apart from working and sleeping.. maybe I should take up a hobby.")
                                    print(Fore.MAGENTA + "You unlocked the 'hobby' command!\n" + Style.RESET_ALL)
                            if day == 7:
                                    print("\nI should probably look to invest some of my money in a savings account if I want to have any for later.")
                                    print(Fore.MAGENTA + "You unlocked the 'bank' command!\n" + Style.RESET_ALL)
                            if day == 10:
                                    print("\nI could use some company. If I feel up to it, maybe I should get a furry companion.")
                                    print(Fore.MAGENTA + "You unlocked the 'pet' command!\n" + Style.RESET_ALL)
                            if day == 13:
                                    print("\nI could use a little fun in my life, time to risk it all at vegas!")
                                    print(Fore.MAGENTA + "You unlocked the 'casino' command!\n" + Style.RESET_ALL)
                            return


                # -----------------------------------------------BACK TO USER MENU------------------------------------------------

                while y == 0 or y != commands:
                                    if day < 3:
                                            commands = ["sleep","work","shop","inv","house","info"]
                                    if day >= 3 and day < 5:
                                            commands = ["sleep","work","shop","inv","house","self","info"]
                                    elif day >= 5 and day < 7:
                                            commands = ["sleep","work","hobby","shop","inv","house","self","info"]
                                    elif day >= 7 and day < 10:
                                            commands = ["sleep","work","hobby","shop","inv","bank","house","self","info"]
                                    elif day >= 10 and day < 13:
                                            commands = ["sleep","work","hobby","shop","inv","bank","house","pet","self","info"]
                                    elif day >= 13:
                                            commands = ["sleep","work","hobby","shop","inv","bank","house","pet","casino","self","info"]
                                    if inventory != {}:
                                            print ()
                                            print (f"Your inventory consists of {inventory}")
                                    else:
                                            print ()
                                            print("You have nothing in your inventory.")

                                    print ("_________________________________________")
                                    print (Fore.YELLOW + f"£{money}" + Style.RESET_ALL + " in your wallet. You feel " + Fore.CYAN + f"{progress_describe(progress)}." + Style.RESET_ALL)
                                    print ("_________________________________________")
                                    time.sleep(0.5)


                                    y = input("What do you do next?" + Fore.MAGENTA + f"{commands}" + Style.RESET_ALL + ": ")
                                    if y in commands:
                                        os.system('cls')
                                        userinput(y)
                                        y = 1



        chinese_proverbs = [
                "A journey of a thousand miles begins with a single step.",
                "One day at a time",
                "Give a man a fish and you feed him for a day; teach a man to fish and you feed him for a lifetime.",
                "The best time to plant a tree was 20 years ago. The second best time is now.",
                "It does not matter how slowly you go as long as you do not stop.",
                "The will to win, the desire to succeed, the urge to reach your full potential.",
                "Success consists of going from failure to failure without loss of enthusiasm.",
                "Do not wait for opportunity, create it.",
                "The person who moves a mountain begins by carrying away small stones.",
                "It is better to light one small candle than to curse the darkness.",
                "The gem cannot be polished without friction, nor man perfected without trials.",
                "The man who asks a question is a fool for a minute, the man who does not is a fool for life.",
                "If you want one year of prosperity, grow grain. If you want ten years of prosperity, grow trees. If you want one hundred years of prosperity, grow people.",
                "You cannot prevent the birds of sorrow from flying over your head, but you can prevent them from building nests in your hair.",
                "A wise man makes his own decisions, an ignorant man follows public opinion.",
                "If you want to know the road ahead, ask someone coming back.",
                "When you drink the water, remember the spring.",
                "Learning is a treasure that will follow its owner everywhere.",
                "A book is like a garden carried in the pocket.",
                "A closed mouth catches no flies.",
                "A single conversation with a wise man is better than ten years of study.",
                "To know the road ahead, ask those coming back.",
                "The best time to plant a tree is twenty years ago. The second best time is now.",
                "The person who asks a question is a fool for a minute, the person who does not is a fool for life.",
                "If you want to go fast, go alone. If you want to go far, go together.",
                "A bird does not sing because it has an answer, it sings because it has a song.",
                "A fall into a ditch makes you wiser.",
                "A single spark can start a prairie fire.",
                "A wise man changes his mind, a fool never will.",
                "A wise man makes his own decisions, an ignorant man follows public opinion.",
                "Better to light a candle than curse the darkness.",
                "Better to be safe than sorry.",
                "Better to be the head of a chicken than the tail of an ox.",
                "Better to be the hammer than the anvil.",
                "Better to die standing than live on your knees.",
                "Better to light one small candle than to curse the darkness.",
                "Bitter medicine is good for a serious illness.",
                "Do not fear going forward slowly, fear only to stand still.",
                "Do not judge others by your own standards.",
                "Do not put off till tomorrow what you can do today.",
                "Do not try to catch two frogs with one hand.",
                "He who asks is a fool for five minutes, but he who does not remains a fool forever.",
                "He who hurries cannot walk with dignity.",
                "If you want happiness for an hour, take a nap. If you want happiness for a day, go fishing. If you want happiness for a year, inherit a fortune. If you want happiness for a lifetime, help somebody.",
                "If you want one year of prosperity, grow grain. If you want ten years of prosperity, grow trees. If you want one hundred years of prosperity, grow people.",
                "If you want to go fast, go alone. If you want to go far, go together.",
                "The best time to plant a tree is ten years ago. The second best time is now.",
                "The best time to plant a tree is twenty years ago. The second best time is now.",
                "The person who asks a question is a fool for a minute, the person who does not is a fool for life."
                "The proof of the pudding is in the eating"
                "The squeaky wheel gets the grease"
                "A word to the wise is enough"
                "Actions speak louder than words"
                "There is no such thing as a free lunch"
                "A picture is worth a thousand words"
                "The early bird catches the worm"
                "A problem shared is a problem halved"
                "An inch of gold can't buy an inch of time."
                "Seize the day",
                "Fortune favors the bold",
                "Love conquers all",
                "Man is a wolf to man",
                "God from the machine",
                "Out of nothing, nothing comes",
                "Fortune favors the strong",
                "In wine there is truth",
                "Remember that you must die",
                "There is nothing new under the sun",
                "Through hardships to the stars",
                "After death, there is nothing, and death itself is nothing",
                "Something for something",
                "Dare to be wise",
                "Time flies",
                "Spoken words fly away, written words remain",
                "The voice of the people is the voice of God",
                "I do not speak against the sun",
                "In peace, as a wise man, prepare suitable things for war",
                "You can drive nature out with a pitchfork, but she always comes back",
                "We learn not for school, but for life",
                "Few words",
                "What is asserted without reason may be denied without reason",
                "Without anger and bias",
                "Virtue stands in the middle"


        ]




        therapy_game()

except Exception:
    print(traceback.format_exc())
    # or
    print(sys.exc_info()[2])
    input("There was an error, input anything to quit game")
