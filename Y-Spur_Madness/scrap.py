# Alyssa Miller alyssa.dannielle@gmail.com
# Creating a program that helps sort the packages that don't scan
# The idea is that the user inputs a zip code and the program outputs the packages destination pallet
# RN I'm just working on figuring out how to talk to files correctly

# let's try to make something that will output what we want it to. We'll use one zip for each of the 3 locations we have currently
# SALS = 21810
# NEWC = 19701
# SDVR = 19901
#zip = input("Enter zip: ")

#if len(zip) > 5:
 #   print("Enter 5 digit zip: ")

#if zip == "19701":
 #   print("NEWC")
#elif zip == "19901":
 #   print("SDVR")
#elif zip == "21810":
 #   print("SALS")
#else:
 #   print("OUTBOUND")

#  im going to try sorting the contents of the files in numerical order
#  using some code that i found on a google search *fingers crossed

zips = list()

filename = 'ebal.txt'
with open (filename) as fin:
    for line in fin:
        zips.append(line.strip())

zips.sort()
#print(zips)

filename = 'ebal_sorted.txt'
with open(filename, 'w') as fout:
    for zip in zips:
        fout.write(zip + '\n')



#new_c = open("newc.txt", "r")

#for line in new_c:
 #   if line.startswith("197"):
  #      print(line.rstrip())


#new_c.close()

