# python-print-Tips
This repo contains some cool tips on how to make the output of print() command in python more readable.
 print('{0:n.mf}'.format(...))
n defines how many digit spaces to be reserved and the m allocates some of those spaces to the decimal digits. 
Alignment Result:
   0.000
  93.630
 187.260
 280.890
 374.520
 468.150
 561.780
 655.410
 749.040
 842.670
 936.300
1029.930

 print("%nd"%...)
n defines how many digit spaces to be reserved just like above.
for example:
print("%3d"%1)
  1
print("%4d"%1)
   1
Times Table Result:
  1   2   3   4   5   6   7   8   9  10 
  2   4   6   8  10  12  14  16  18  20 
  3   6   9  12  15  18  21  24  27  30 
  4   8  12  16  20  24  28  32  36  40 
  5  10  15  20  25  30  35  40  45  50 
  6  12  18  24  30  36  42  48  54  60 
  7  14  21  28  35  42  49  56  63  70 
  8  16  24  32  40  48  56  64  72  80 
  9  18  27  36  45  54  63  72  81  90 
 10  20  30  40  50  60  70  80  90 100
