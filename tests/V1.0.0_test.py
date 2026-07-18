from director import DisplayTree

if __name__ == "__main__":
       
    custom_path = "custom_path"

    # 1. Test for String Representation
    stringRepresentation = DisplayTree(custom_path,stringRep=True)
    #print(stringRepresentation)

    # 2. Test for Header in String Representation
    stringRepresentation = DisplayTree(custom_path,stringRep=True, header=True)
    print(stringRepresentation)

    # 3. Test for Console-Print and Max Depth >> Actual Depth
    DisplayTree(custom_path,maxDepth=2,ignoreList=["ignore1"])

    # 4. Test for Console-Print, Header for [OS, Path] Info and Not Show Hidden Files/Directories
    DisplayTree(header=True, maxDepth=100, showHidden=False)

    # 5. Test for Console-Print, Header for [OS, Path] Info and Show Hidden Files/Directories
    DisplayTree(maxDepth=2, showHidden=True)

    # 6. Test for Ignore Files / Directories [Absolute Names]
    DisplayTree(maxDepth=4, showHidden=True, ignoreList=["ignore1"])

    # 7. Test for Export TXT
    DisplayTree(maxDepth=4, showHidden=True, ignoreList=["ignore1"], exportTxt=True)

   