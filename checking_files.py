import glob , os 


for root , dirs , files in os.walk("."):
    for filename in files:  	
        filename , separator , extension = filename.partition('.')
    	#print(extension)
        #print(filename)
        extension = str(extension)
        if (extension == 'txt'):
            print(filename)

#for file in os.listdir("."):
#        if file.endswith(".txt"):
#                    print(os.path.join(".", file))
