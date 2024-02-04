"""Module to convert int numbers to bin and hex from a txt file"""
import time
import sys

start = time.time()
# READ DATA FROM THE FILE AND GET INT ARRAY
with open(sys.argv[1], encoding="utf-8") as f:
    contents = f.read()
f.close()
l_c = contents.split()
l_int = []
for i in l_c:
    try:
        l_int.append(int(i))
    except ValueError as e:
        print("Not a valid data!")
with open("convertion_results.txt", "w", encoding="utf-8") as file1:
    file1.writelines("#     INT         BIN             HEX" + "\n")

    # NUMBER	TC1	BIN	HEX
    # CONVERTION PROCESS
    C = 0
    res = []
    for i in l_int:
        C += 1
        res.append(str(C) + "     ")
        res.append(str(i) + "     ")
        print(str(C))
        # POSITIVE NUMBER TO BINARY
        save_number = i
        if i >= 0:
            B_ST = ""
            while i > 0:
                digit = i % 2
                B_ST += str(digit)
                i = i // 2
            B_ST = B_ST[::-1]
            print("INT 2 BINARY:    " + B_ST)
            res.append(B_ST + "     ")

        # NEGATIVE NUMBER TO BINARY
        else:
            negative_binary = f"{i:b}"
            print("INT 2 BINARY:    " + negative_binary)
            res.append(negative_binary + "     ")

        # INT TO HEXADECIMAL
        i = save_number
        H_CHAR = "0123456789ABCDEF"
        H = ""
        if i == 0:
            H = "0"

        while i > 0:
            r = i % 16
            H = H_CHAR[r] + H
            i //= 16

        print("INT 2 HEX:       " + H)
        res.append(H + "\n")

        file1.writelines(res)
        res = []

    # WRITE A TXT FILE
    end = time.time()
    file1.write("TIME ELAPSED: " + str(end - start))
    file1.close()
    print("TIME ELAPSED: " + str(end - start))
