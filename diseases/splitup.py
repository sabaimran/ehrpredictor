import os

def read_file(ofile, folder):
    with open(ofile, mode='r', encoding="utf8") as f:
        lines = f.read().split('\n')

        here = os.path.dirname(os.path.realpath(ofile))
        counter=1

        currf = "{0}{1}.txt".format(folder, counter)

        filepath = os.path.join(here, folder, currf)
        currf = open(filepath, "w+")
        currl = ""
        for line in lines:
            if line == "":
                if currl == "":
                    continue
                currf.write(currl)
                currf.close()
                counter += 1
                currf = "{0}{1}.txt".format(folder, counter)
                filepath = os.path.join(here, folder, currf)
                currf = open(filepath, mode="w+")
                currl = ""
            else:
                currl += line + "\n"

        if currl != "":
            currf.write(currl)
            currf.close()
                
        

if __name__ == '__main__':
    names = ["alzheimer", "acidreflux", "breastcancer", "diabetes", "als", "parkinsons", "multiplesclerosis", "hemophilia"]

    for name in names:
        # name of file, then name of its directory.
        read_file(name+".txt", name)