import os
def isBinod(filename):
    with open (filename,"r") as f:
        fileContent=f.read()
    if "binod" in fileContent.lower():
        return True
    else: return False


if __name__ == "__main__":
    dir_contents = os.listdir()
    for items in dir_contents:
        if items.endswith("txt"):
            print(f"Detecting Binod in {items}")
            isBinod(items)
            flag =isBinod(items)
            if(flag):
                print(f"Binod found in {items}")
            else:
                 print(f"Binod not found in {items}")