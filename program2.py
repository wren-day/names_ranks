rank = []
firstnames = []
lastnames = []

with open("girl_boy_names_2004.csv","r") as names_csv:
        lines = names_csv.readlines()
        for i in lines:
                new_list = i.split(",")
                rank.append(new_list[0])
                firstnames.append(new_list[1])
                lastnames.append(new_list[2])

for i in range(len(firstnames)):
        print ("~~~~~~~~~~~~~")
        print ("Rank: " + rank[i])
        print ("Girl Name: " + firstnames[i])
        print ("Boy Name: " + lastnames[i])
