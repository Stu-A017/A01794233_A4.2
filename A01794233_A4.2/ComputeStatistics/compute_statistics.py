"""Module to calculate descriptive statistics from a txt file"""
import sys
import math
import time
from collections import Counter

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
if len(l_int) == 0:
    for i in l_c:
        try:
            l_int.append(float(i))
        except ValueError as e:
            print("Not a valid data!")

# COUNT & MEAN
res = []
COUNT = 0
GET_SUM = 0
for i in l_int:
    GET_SUM = GET_SUM + i
    COUNT += 1

mean = GET_SUM / COUNT

print("COUNT    " + str(COUNT))
print("MEAN     " + str(mean))
res.append("COUNT    " + str(COUNT) + "\n")
res.append("MEAN     " + str(mean) + "\n")

# MEDIAN
if COUNT % 2 == 0:
    median_left = l_int[COUNT // 2]
    median_right = l_int[COUNT // 2 - 1]
    median = (median_left + median_right) / 2
else:
    median = l_int[COUNT // 2]
print("MEDIAN   " + str(median))
res.append("MEDIAN   " + str(median) + "\n")

# MODE
get_mode = Counter(l_int)
mode = get_mode.most_common(1)
print("MODE     " + str(mode[0][0]))
res.append("MODE     " + str(mode[0][0]) + "\n")

# VARIANCE & SD
var = (sum((i - mean) ** 2 for i in l_int)) / len(l_int)
std = math.sqrt(var)
print("VARIANCE " + str(var))
print("SD       " + str(std))
res.append("VARIANCE " + str(var) + "\n")
res.append("SD       " + str(std) + "\n")

# WRITE A TXT FILE
with open("statistics_results.txt", "w", encoding="utf-8") as file1:
    file1.writelines(res)
    end = time.time()
    file1.write("TIME ELAPSED: " + str(end - start))
    file1.close()

print("TIME ELAPSED: " + str(end - start))
