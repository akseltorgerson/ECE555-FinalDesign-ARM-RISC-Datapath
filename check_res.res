Expected results are:
dst<0> x 0 1 0 0 1 0
dst<1> x 1 0 1 0 1 0
dst<2> x 1 0 0 1 1 0
dst<3> x 1 0 0 1 1 0
dst<4> x 0 0 1 1 1 0
dst<5> x 0 1 1 1 0 0
dst<6> x 0 1 0 1 0 0
dst<7> x 1 1 0 0 1 0
dst<8> x 1 0 1 1 1 0
dst<9> x 1 0 1 0 0 0
dst<10> x 1 1 1 0 0 0
dst<11> x 0 0 1 0 0 0
dst<12> x 1 0 1 0 0 0
dst<13> x 1 1 0 1 0 0
dst<14> x 0 1 1 1 1 0
dst<15> x 1 0 0 0 0 0
cout x x x x x x x
clock found in column 1
current of V0 found in column 19
----------------- Comparing Results -------------------
Rising clock occurred at time 1.125000e-09
Rising clock occurred at time 3.000000e-09
Rising clock occurred at time 4.875000e-09
Rising clock occurred at time 6.750000e-09
Rising clock occurred at time 8.625000e-09
Rising clock occurred at time 1.047500e-08
Rising clock occurred at time 1.235000e-08
ERROR: at time 12.30ns (vector 6) signal dst<14> was expected to be a 0, was: 0.94
Average current consumption was: 1.1155244907 mA
