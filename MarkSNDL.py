def MarkSNDL(MDFile):
    FileLineArray = []
    cycle = 0
    StringHotReplace = ""
    with open(MDFile) as MarkDown_File:
        for line in MarkDown_File:
            FileLineArray.append(line)
    for cycle in range (len(FileLineArray)):
        if FileLineArray[cycle][0:6] == "######":
            StringHotReplace = FileLineArray[cycle]
            StringHotReplace.replace("######", "<h6>")
            FileLineArray[cycle] = StringHotReplace + "</h6>"
        elif FileLineArray[cycle][0:5] == "#####":
            StringHotReplace = FileLineArray[cycle]
            FileLineArray[cycle].replace("#####", "<h5>")
            FileLineArray[cycle] = FileLineArray[cycle] + "</h5>"
        elif FileLineArray[cycle][0:4] == "####":
            StringHotReplace = FileLineArray[cycle]
            FileLineArray[cycle].replace("####", "<h4>")
            FileLineArray[cycle] = FileLineArray[cycle] + "</h4>"
        elif FileLineArray[cycle][0:3] == "###":
            StringHotReplace = FileLineArray[cycle]
            FileLineArray[cycle].replace("###", "<h3>")
            FileLineArray[cycle] = FileLineArray[cycle] + "</h3>"
        elif FileLineArray[cycle][0:2] == "##":
            StringHotReplace = FileLineArray[cycle]
            FileLineArray[cycle].replace("##", "<h2>")
            FileLineArray[cycle] = FileLineArray[cycle] + "</h2>"
        elif FileLineArray[cycle][0:1] == "#":
            StringHotReplace = FileLineArray[cycle]
            StringHotReplace.replace("#", "<h1>")
            FileLineArray[cycle] = StringHotReplace + "</h1>"
            
    for cycle in range (len(FileLineArray)):
        print(FileLineArray[cycle])

MarkSNDL("README.md")