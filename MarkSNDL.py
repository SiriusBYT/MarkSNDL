def MarkSNDL(MDFile):
    FileLineArray = []
    cycle = 0
    StringHotReplace = ""
    with open(MDFile) as MarkDown_File:
        for line in MarkDown_File:
            FileLineArray.append(line)
    for cycle in range (len(FileLineArray)): # This is dumb stupid code but it'll do for now.
        if FileLineArray[cycle][0:6] == "######":
            StringHotReplace = FileLineArray[cycle]
            StringHotReplace = StringHotReplace.replace("######", "<h6>") + StringHotReplace.replace("\n", "</h6>" + "\n")
            FileLineArray[cycle] = StringHotReplace
        elif FileLineArray[cycle][0:5] == "#####":
            StringHotReplace = FileLineArray[cycle]
            StringHotReplace = StringHotReplace.replace("#####", "<h5>") + StringHotReplace.replace("\n", "</h5>" + "\n")
            FileLineArray[cycle] = StringHotReplace
        elif FileLineArray[cycle][0:4] == "####":
            StringHotReplace = FileLineArray[cycle]
            StringHotReplace = StringHotReplace.replace("####", "<h4>") + StringHotReplace.replace("\n", "</h4>" + "\n")
            FileLineArray[cycle] = StringHotReplace
        elif FileLineArray[cycle][0:3] == "###":
            StringHotReplace = FileLineArray[cycle]
            StringHotReplace = StringHotReplace.replace("###", "<h3>") + StringHotReplace.replace("\n", "</h3>" + "\n")
            FileLineArray[cycle] = StringHotReplace
        elif FileLineArray[cycle][0:2] == "##":
            StringHotReplace = FileLineArray[cycle]
            StringHotReplace = StringHotReplace.replace("##", "<h2>") + StringHotReplace.replace("\n", "</h2>" + "\n")
            FileLineArray[cycle] = StringHotReplace
        elif FileLineArray[cycle][0:1] == "#":
            StringHotReplace = FileLineArray[cycle]
            StringHotReplace = StringHotReplace.replace("#", "<h1>") + StringHotReplace.replace("\n", "</h1>" + "\n")
            FileLineArray[cycle] = StringHotReplace
        else:
            StringHotReplace = "<p>" + FileLineArray[cycle] + StringHotReplace.replace("\n", "</p>" + "\n")
            FileLineArray[cycle] = StringHotReplace
            
    for cycle in range (len(FileLineArray)):
        print(FileLineArray[cycle])

MarkSNDL("README.md")