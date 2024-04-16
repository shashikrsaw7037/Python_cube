## A = "OOTD.YOLO.ASAP.BRB.GTG.DTW"
## Write a program to separate the following string into coma(,) separates values
A = "OOTD. YOLO. ASAP. BRB. GTG. DTW"
b = A.split(", ")
c = A.split(". ")
print(b)#['OOTD. YOLO. ASAP. BRB. GTG. DTW']
print(c)#['OOTD', 'YOLO', 'ASAP', 'BRB', 'GTG', 'DTW']
