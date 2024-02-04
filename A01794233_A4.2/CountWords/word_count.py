"""Module to count words from a txt file"""
import time
import sys

start = time.time()
# READ DATA FROM THE FILE
with open(sys.argv[1], encoding="utf-8") as f:
    contents = f.read()
f.close()
with open("word_count_results.txt", "w", encoding="utf-8") as file1:
    l_c = contents.split()
    print("STRING                                 COUNT")
    file1.writelines("STRING                                 COUNT" + "\n")

    # COUNT ELEMENTS
    d = {}
    for i in l_c:
        if i not in d:
            d[i] = 1
        else:
            d[i] = int(d.get(i)) + 1

    res = []
    # PRINT DICTIONARY
    for key, value in d.items():
        print(str(key) + "                                      " + str(value))
        res.append(
            str(key) + "                                      " + str(value) + "\n"
        )
        file1.writelines(res)
        res = []

    # WRITE A TXT FILE
    end = time.time()
    file1.write("TIME ELAPSED: " + str(end - start))
    file1.close()
    print("TIME ELAPSED: " + str(end - start))
