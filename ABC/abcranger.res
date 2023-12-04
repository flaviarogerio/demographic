num stats: 63
all params: T1 T2 M_EU_BR rho M_BR_EU N_ANC S3 M_NA_BR S2 N_BR theta N_EU S1 m M_NA_EU M_BR_NA M_EU_NA
common params T1 M_EU_BR rho M_BR_EU M_NA_BR S2 N_BR theta N_EU S1 m M_NA_EU M_BR_NA M_EU_NA

### max: 100000 ###

selected model: M33
votes: 10 19 154 6 25 9 6 2 96 38 62 1 72
proba: 0.7358666666666667

# modelchoice_out.settings #

Model choice analyses proceeded using: 
- 1300000 simulated datasets
- 500 trees
- Minimum node size of 1
- 63 summary statistics
- 12 axes of summary statistics LDA linear combination
- 5 noise variables

# modelchoice_out.importance #

LDA2: 6350.22
LDA1: 5821.15
LDA3: 5761.85
LDA4: 4675.59
pair:NA-BR_Dxy: 3984.58
pair:BR-EU_Dxy: 3748.74
pair:NA-EU_Dxy: 2935.94
pair:NA-BR_Dj: 2284.48
all_D: 2212.4
all_R2: 2205.6
LDA5: 2124.81
pair:NA-BR_Da: 1966.39
pop:EU_D: 1937.28
pair:BR-EU_Dj: 1915.36
pop:EU_R2: 1803.42
pair:NA-EU_Dj: 1783.88
pair:NA-BR_FstWC: 1777.26
pair:BR-EU_Da: 1734.97
pair:NA-EU_Da: 1694.34
pop:BR_D: 1529.59
pop:NA_D: 1512.47
pair:BR-EU_FstWC: 1379.89
pair:NA-EU_FstWC: 1343.21
LDA6: 1076.45
LDA7: 1051.48
LDA8: 1049.03
pop:BR_Hsd: 1044.38
pop:NA_Hsd: 1031.13
pop:NA_R2: 963.812
LDA11: 955.687
all_FstWC: 896.265
all_Dj: 893.795
LDA10: 850.949
LDA9: 787.14
LDA12: 749.679
pop:EU_Hsd: 634.983
pop:NA_Ch: 618.246
pop:EU_Ch: 601.604
pop:BR_R2: 600.269
all_Hsd: 593.109
pop:BR_Ch: 564.72
NOISE2: 539.049
NOISE4: 538.041
NOISE5: 535.857
pop:BR_Ki: 535.851
NOISE1: 534.677
NOISE3: 532.951
pop:EU_KoP: 487.265
pop:BR_KoP: 485.893
pop:NA_KoP: 484.628
pop:NA_Ki: 453.622
all_KoP: 408.493
pair:NA-BR_numShP: 394.257
pop:EU_Ki: 392.637
pop:BR_Pi: 377.405
pair:BR-EU_numShP: 367.977
pair:BR-EU_numSpd: 363.9
pair:NA-BR_numSpd: 357.3
pop:BR_KoS: 355.427
all_Ki: 355.199
pair:NA-EU_numShP: 355.002
pop:NA_Pi: 354.948
pair:NA-EU_numSpd: 353.534
pop:BR_thetaW: 348.989
pop:BR_S: 348.778
all_KoS: 348.266
pop:NA_KoS: 348.136
pop:EU_KoS: 339.2
pop:NA_S: 326.906
pop:NA_thetaW: 326.4
all_Ch: 315.628
pop:EU_Pi: 301.816
pair:NA-BR_numShA: 301.115
pop:EU_thetaW: 295.03
pop:EU_S: 293.035
pair:BR-EU_numShA: 283.164
pair:NA-EU_numShA: 280.854
all_S: 280.085
all_thetaW: 280.005
all_Pi: 279.29

# modelchoice_out.predictions #

        model1        model2        model3        model4        model5        model6        model7        model8        model9       model10       model11       model12       model13 selected model  post proba
         0.020         0.038         0.308         0.012         0.050         0.018         0.012         0.004         0.192         0.076         0.124         0.002         0.144              3       0.736
         0.001         0.001         0.844         0.000         0.002         0.000         0.000         0.000         0.111         0.003         0.009         0.000         0.028              3       1.000
         0.000         0.000         0.736        -0.000         0.001         0.000        -0.000        -0.000         0.212         0.004         0.007        -0.000         0.039              3       1.000

# modelchoice_out.confusion #

Prior error rate: 0.220715

Class specific prediction errors:
                1     2     3     4     5     6     7     8     9     10     11     12     13 class.error
predicted 1     77216 264   235   6622  4121  1218  319   605   31    823   6684  622   4546   0.252551
predicted 2     453   80033 5179  259   303   406   5197  1493  260   60    884   7321  4406   0.246777
predicted 3     427   8446  82259 912   885   648   336   23    8396  1190  4604  623   6673   0.28732
predicted 4     3183  192   393   72853 945   4659  20    256   255   290   278   5424  6439   0.234633
predicted 5     4676  452   804   2307  83368 11065 8     1     31    239   197   65    1107   0.200844
predicted 6     1711  437   487   6329  8739  80521 14    102   12    3     46    320   927    0.191946
predicted 7     304   3563  56    11    12    2     84449 11197 9     3     745   795   236    0.167022
predicted 8     913   898   22    73    14    74    7919  81056 0     31    944   5794  612    0.175841
predicted 9     9     76    3560  207   6     4     14    2     81160 8120  886   197   459    0.142978
predicted 10     260   92    1341  614   286   7     4     13    7423  80033 3817  590   1509   0.166227
predicted 11     9131  572   3189  470   650   12    909   808   787   7155  78769 783   6724   0.283651
predicted 12     394   2953  401   4916  28    705   584   4171  231   321   610   73214 8223   0.243274
predicted 13     1323  2022  2074  4427  643   679   227   273   1405  1732  1536  4252  58139  0.261558

### max: 200000 ###

selected model: M35
votes: 54 16 102 16 129 24 5 1 36 12 42 4 59
proba: 0.6835000000000001

# modelchoice_out.settings #

Model choice analyses proceeded using: 
- 2600000 simulated datasets
- 500 trees
- Minimum node size of 1
- 63 summary statistics
- 12 axes of summary statistics LDA linear combination
- 5 noise variables

# modelchoice_out.importance #

LDA2: 6449.39
LDA1: 5752.47
LDA3: 5744.25
LDA4: 4749.42
pair:NA-BR_Dxy: 4129
pair:BR-EU_Dxy: 3813.77
pair:NA-EU_Dxy: 2867.58
pair:NA-BR_Dj: 2223.69
all_R2: 2222.91
all_D: 2218.06
LDA5: 2078.34
pair:NA-BR_Da: 1988.47
pop:EU_D: 1883.9
pair:BR-EU_Dj: 1873.72
pair:NA-EU_Dj: 1807.03
pair:NA-BR_FstWC: 1783.06
pop:EU_R2: 1763
pair:BR-EU_Da: 1694.84
pair:NA-EU_Da: 1640.57
pop:NA_D: 1565.28
pop:BR_D: 1503.6
pair:BR-EU_FstWC: 1395.94
pair:NA-EU_FstWC: 1323.54
LDA6: 1062.23
pop:NA_Hsd: 1053.48
LDA7: 1051.67
LDA8: 1047.26
pop:BR_Hsd: 1025.32
LDA11: 967.194
pop:NA_R2: 946.035
all_FstWC: 914.524
all_Dj: 884.402
LDA10: 856.087
LDA9: 763.403
LDA12: 756.714
pop:EU_Hsd: 629.398
pop:NA_Ch: 618.717
pop:BR_R2: 600.603
pop:EU_Ch: 597.999
all_Hsd: 590.924
pop:BR_Ch: 562.188
pop:BR_Ki: 540.543
NOISE5: 539.017
NOISE2: 537.841
NOISE3: 537.466
NOISE4: 537.345
NOISE1: 535.766
pop:BR_KoP: 488.439
pop:NA_KoP: 482.927
pop:EU_KoP: 481.504
pop:NA_Ki: 453.581
all_KoP: 415.605
pop:EU_Ki: 397.541
pair:NA-BR_numShP: 395.205
pop:BR_Pi: 376.974
pair:BR-EU_numShP: 369.744
pair:BR-EU_numSpd: 364.753
pair:NA-EU_numShP: 359.787
pair:NA-BR_numSpd: 359.289
pop:BR_KoS: 358.904
pair:NA-EU_numSpd: 356.849
all_Ki: 356.206
pop:NA_Pi: 355.616
pop:BR_thetaW: 353.339
pop:BR_S: 352.557
all_KoS: 349.889
pop:NA_KoS: 349.511
pop:EU_KoS: 339.673
pop:NA_thetaW: 327.425
pop:NA_S: 324.675
all_Ch: 315.618
pop:EU_Pi: 301.537
pair:NA-BR_numShA: 301.119
pop:EU_thetaW: 294.033
pop:EU_S: 292.008
pair:BR-EU_numShA: 286.678
pair:NA-EU_numShA: 280.346
all_thetaW: 280.334
all_Pi: 279.381
all_S: 277.742

# modelchoice_out.predictions #

        model1        model2        model3        model4        model5        model6        model7        model8        model9       model10       model11       model12       model13 selected model  post proba
         0.108         0.032         0.204         0.032         0.258         0.048         0.010         0.002         0.072         0.024         0.084         0.008         0.118              5       0.684
         0.008         0.000         0.081         0.000         0.886         0.001         0.000         0.000         0.002         0.000         0.003         0.000         0.020              5       1.000
         0.007         0.000         0.262        -0.000         0.683        -0.000        -0.000        -0.000         0.004        -0.000         0.003        -0.000         0.040              5       1.000

# modelchoice_out.confusion #

Prior error rate: 0.220382

Class specific prediction errors:
                1     2     3     4     5     6     7     8     9     10     11     12     13 class.error
predicted 1     154700562   466   13308 8254  2550  642   1239  40    1654  13286 1298  9126   0.253108
predicted 2     927   15980610575 523   611   837   10311 2785  540   121   1824  14601 8803   0.247136
predicted 3     860   16766 1644241778  1833  1221  619   50    16926 2450  9085  1210  13157  0.286289
predicted 4     6459  452   799   1457171814  9247  30    533   521   592   589   10923 13007  0.235815
predicted 5     9311  930   1569  4595  16659422009 15    3     40    487   396   127   2194   0.200106
predicted 6     3431  930   944   12663 17476 16124727    226   30    3     82    634   1727   0.19142
predicted 7     581   7123  99    16    20    4     16912722227 21    10    1468  1529  507    0.165761
predicted 8     1731  1795  49    149   22    144   15848 1623273     50    1855  11481 1199   0.174551
predicted 9     24    122   7185  401   6     16    26    5     16199016155 1748  366   904    0.142674
predicted 10     521   191   2747  1236  570   13    6     25    15091 1600097478  1163  2961   0.166668
predicted 11     18054 1140  6209  927   1373  33    1776  1592  1638  14311 1579251544  13544  0.282374
predicted 12     805   6077  798   9898  58    1427  1090  8402  460   681   1233  14678116510  0.244254
predicted 13     2596  4106  4136  8789  1369  1252  483   586   2700  3477  3031  8343  116361 0.259927

### max: 300000 ###

selected model: M35
votes: 51 21 116 18 119 38 1 0 34 9 28 0 65
proba: 0.7368666666666667

# modelchoice_out.settings #

Model choice analyses proceeded using: 
- 3900000 simulated datasets
- 500 trees
- Minimum node size of 1
- 63 summary statistics
- 12 axes of summary statistics LDA linear combination
- 5 noise variables

# modelchoice_out.importance #

LDA2: 6359.5
LDA3: 5829.58
LDA1: 5706.53
LDA4: 4753.61
pair:NA-BR_Dxy: 4145.35
pair:BR-EU_Dxy: 3852.69
pair:NA-EU_Dxy: 2956.93
pair:NA-BR_Dj: 2273.83
all_R2: 2235.81
all_D: 2149.19
LDA5: 2112.91
pair:NA-BR_Da: 2012.41
pair:BR-EU_Dj: 1882.26
pop:EU_D: 1861.73
pair:NA-EU_Dj: 1790.54
pop:EU_R2: 1777.12
pair:NA-BR_FstWC: 1743.88
pair:BR-EU_Da: 1734.43
pair:NA-EU_Da: 1653.14
pop:BR_D: 1488.92
pop:NA_D: 1480.44
pair:BR-EU_FstWC: 1397.89
pair:NA-EU_FstWC: 1327.27
LDA6: 1071.38
pop:NA_Hsd: 1060.77
LDA8: 1056.94
LDA7: 1054.69
pop:BR_Hsd: 1028.94
LDA11: 964.958
pop:NA_R2: 931.864
all_FstWC: 903.71
LDA10: 860.618
all_Dj: 844.552
LDA12: 754.198
LDA9: 749.478
pop:EU_Hsd: 629.209
pop:NA_Ch: 615.323
pop:BR_R2: 604.959
all_Hsd: 597.585
pop:EU_Ch: 594.583
pop:BR_Ch: 565.273
pop:BR_Ki: 538.977
NOISE1: 537.584
NOISE5: 537.494
NOISE3: 536.414
NOISE2: 535.375
NOISE4: 535.315
pop:EU_KoP: 490.107
pop:BR_KoP: 489.975
pop:NA_KoP: 486.776
pop:NA_Ki: 451.677
all_KoP: 408.254
pop:EU_Ki: 396.098
pair:NA-BR_numShP: 389.665
pop:BR_Pi: 379.757
pair:BR-EU_numShP: 370.311
pair:BR-EU_numSpd: 364.823
pair:NA-EU_numShP: 357.692
pop:BR_KoS: 357.241
all_Ki: 356.763
pair:NA-BR_numSpd: 356.188
pair:NA-EU_numSpd: 355.686
pop:NA_Pi: 353.6
pop:BR_S: 352.658
all_KoS: 350.595
pop:NA_KoS: 349.617
pop:BR_thetaW: 348.916
pop:EU_KoS: 336.657
pop:NA_thetaW: 327.085
pop:NA_S: 324.912
all_Ch: 316.984
pair:NA-BR_numShA: 301.958
pop:EU_Pi: 300.423
pop:EU_S: 295.659
pop:EU_thetaW: 294.032
pair:BR-EU_numShA: 284.85
all_Pi: 282.144
all_thetaW: 280.827
pair:NA-EU_numShA: 279.958
all_S: 278.739

# modelchoice_out.predictions #

        model1        model2        model3        model4        model5        model6        model7        model8        model9       model10       model11       model12       model13 selected model  post proba
         0.102         0.042         0.232         0.036         0.238         0.076         0.002         0.000         0.068         0.018         0.056         0.000         0.130              5       0.737
         0.007         0.000         0.085         0.000         0.881         0.003         0.000         0.000         0.002         0.000         0.001         0.000         0.022              5       1.000
         0.014        -0.000         0.207        -0.000         0.737         0.003        -0.000        -0.000         0.002        -0.000         0.001        -0.000         0.036              5       1.000

# modelchoice_out.confusion #

Prior error rate: 0.220236

Class specific prediction errors:
                1     2     3     4     5     6     7     8     9     10     11     12     13 class.error
predicted 1     232111844   716   20002 12252 3863  948   1840  56    2489  19979 1966  13723  0.253156
predicted 2     1365  24001215729 798   953   1283  15495 4130  806   177   2733  21978 13379  0.247229
predicted 3     1248  25068 2469222701  2782  1898  921   79    25349 3726  13763 1820  19858  0.286631
predicted 4     9624  632   1200  2184512727  13961 42    774   760   904   911   16413 19420  0.235702
predicted 5     13907 1360  2336  6945  25005032992 29    5     55    678   616   172   3234   0.19953
predicted 6     5163  1381  1377  18972 26135 24162843    315   56    4     121   957   2569   0.191125
predicted 7     880   10702 151   32    27    4     25383033407 36    8     2247  2378  748    0.166267
predicted 8     2596  2664  72    210   31    213   23604 2433144     68    2769  17183 1751   0.173748
predicted 9     25    217   10749 652   9     20    51    10    24300324325 2580  552   1359   0.143004
predicted 10     806   296   4134  1843  873   24    7     42    22763 24020011271 1750  4417   0.167204
predicted 11     27114 1676  9230  1371  2020  51    2645  2471  2439  21258 2367262263  20168  0.281412
predicted 12     1232  9080  1206  14826 91    2150  1642  12736 637   1024  1867  22005224594  0.244163
predicted 13     3929  6068  6178  13197 2050  1913  743   877   4036  5139  4417  12516 174780 0.258914

### max: 400000 ###

selected model: M33
votes: 39 21 156 15 67 20 5 0 58 29 31 1 58
proba: 0.7606666666666666

# modelchoice_out.settings #

Model choice analyses proceeded using: 
- 5200000 simulated datasets
- 500 trees
- Minimum node size of 1
- 63 summary statistics
- 12 axes of summary statistics LDA linear combination
- 5 noise variables

# modelchoice_out.importance #

LDA2: 6207.56
LDA1: 5830.48
LDA3: 5743.43
LDA4: 4697
pair:NA-BR_Dxy: 4139
pair:BR-EU_Dxy: 3773.53
pair:NA-EU_Dxy: 2977.04
all_R2: 2208.46
all_D: 2168.26
pair:NA-BR_Dj: 2156.03
LDA5: 2107
pair:NA-BR_Da: 1994.45
pair:BR-EU_Dj: 1914.28
pop:EU_D: 1865.98
pop:EU_R2: 1793.48
pair:BR-EU_Da: 1779.86
pair:NA-EU_Dj: 1759.25
pair:NA-BR_FstWC: 1736.01
pair:NA-EU_Da: 1705.44
pop:NA_D: 1548.81
pop:BR_D: 1523.44
pair:BR-EU_FstWC: 1376.2
pair:NA-EU_FstWC: 1364.19
LDA6: 1099.29
LDA7: 1065.22
LDA8: 1057.96
pop:NA_Hsd: 1050.4
pop:BR_Hsd: 1041.23
LDA11: 959.835
pop:NA_R2: 937.267
all_FstWC: 903.022
all_Dj: 876.409
LDA10: 868.342
LDA9: 763.588
LDA12: 758.166
pop:EU_Hsd: 634.153
pop:NA_Ch: 605.086
pop:BR_R2: 600.992
pop:EU_Ch: 597.637
all_Hsd: 597.515
pop:BR_Ch: 568.947
pop:BR_Ki: 539.857
NOISE2: 537.591
NOISE1: 537.412
NOISE4: 536.918
NOISE5: 536.753
NOISE3: 535.041
pop:EU_KoP: 498.215
pop:BR_KoP: 493.416
pop:NA_KoP: 485.77
pop:NA_Ki: 455.79
all_KoP: 411.341
pair:NA-BR_numShP: 398.444
pop:EU_Ki: 394.236
pop:BR_Pi: 382.466
pair:BR-EU_numShP: 372.86
pair:BR-EU_numSpd: 366.756
pop:NA_Pi: 357.724
pair:NA-BR_numSpd: 357.335
pair:NA-EU_numSpd: 356.297
pop:BR_KoS: 355.68
pair:NA-EU_numShP: 355.517
all_Ki: 355.421
pop:BR_S: 353.057
all_KoS: 352.775
pop:BR_thetaW: 352.427
pop:NA_KoS: 350.412
pop:EU_KoS: 338.884
pop:NA_thetaW: 329.286
pop:NA_S: 326.186
all_Ch: 317.679
pop:EU_Pi: 304.17
pair:NA-BR_numShA: 302.617
pop:EU_thetaW: 297.647
pop:EU_S: 293.066
pair:BR-EU_numShA: 285.957
pair:NA-EU_numShA: 283.365
all_Pi: 282.231
all_thetaW: 281.818
all_S: 280.095

# modelchoice_out.predictions #

        model1        model2        model3        model4        model5        model6        model7        model8        model9       model10       model11       model12       model13 selected model  post proba
         0.078         0.042         0.312         0.030         0.134         0.040         0.010         0.000         0.116         0.058         0.062         0.002         0.116              3       0.761
         0.004         0.000         0.858         0.000         0.099         0.000         0.000         0.000         0.026         0.001         0.002         0.000         0.010              3       1.000
         0.003         0.000         0.761         0.000         0.186         0.000         0.000         0.000         0.037         0.001         0.000         0.000         0.012              3       1.000

# modelchoice_out.confusion #

Prior error rate: 0.220514

Class specific prediction errors:
                1     2     3     4     5     6     7     8     9     10     11     12     13 class.error
predicted 1     3095121125  901   26791 16416 5125  1289  2485  58    3304  26686 2622  18182  0.253281
predicted 2     1772  31946820904 1000  1284  1716  20577 5469  1037  216   3608  29051 17718  0.246218
predicted 3     1725  33668 3295723656  3704  2513  1229  99    33890 5003  18344 2446  26848  0.287715
predicted 4     12916 852   1591  2910083657  18804 56    1022  1009  1187  1206  21699 26031  0.236276
predicted 5     18684 1891  3127  9169  33322343724 37    5     79    917   829   223   4334   0.199449
predicted 6     6814  1826  1876  25485 34838 32228659    409   71    8     156   1283  3456   0.191388
predicted 7     1178  14203 200   40    37    7     33798644216 58    16    3025  3166  1003   0.165745
predicted 8     3472  3613  108   310   48    281   31958 3250805     93    3710  23146 2304   0.175192
predicted 9     46    301   14322 917   19    29    72    13    32388932667 3441  750   1802   0.143758
predicted 10     1029  373   5392  2489  1172  35    9     56    30282 31970614934 2374  5963   0.167029
predicted 11     36068 2364  12326 1878  2715  89    3508  3269  3320  28595 3155763011  26972  0.282278
predicted 12     1564  12163 1563  19826 116   2833  2214  16717 859   1365  2494  29345032818  0.24365
predicted 13     5220  8153  8118  17431 2771  2558  1006  1160  5443  6923  5991  16779 232569 0.259622

### max: 500000 ###

selected model: M33
votes: 34 27 142 15 83 15 0 0 50 16 41 0 77
proba: 0.734

# modelchoice_out.settings #

Model choice analyses proceeded using: 
- 6500000 simulated datasets
- 500 trees
- Minimum node size of 1
- 63 summary statistics
- 12 axes of summary statistics LDA linear combination
- 5 noise variables

# modelchoice_out.importance #

LDA2: 6316.67
LDA1: 5832.11
LDA3: 5822.6
LDA4: 4729.34
pair:NA-BR_Dxy: 4130.02
pair:BR-EU_Dxy: 3837.37
pair:NA-EU_Dxy: 2981.02
pair:NA-BR_Dj: 2212.86
all_R2: 2195.2
all_D: 2140.07
LDA5: 2096.63
pair:NA-BR_Da: 1967.68
pop:EU_D: 1919.76
pair:BR-EU_Dj: 1882.57
pop:EU_R2: 1806.11
pair:NA-EU_Dj: 1775.31
pair:NA-BR_FstWC: 1738.85
pair:BR-EU_Da: 1712.33
pair:NA-EU_Da: 1627.79
pop:NA_D: 1560.1
pop:BR_D: 1483.06
pair:BR-EU_FstWC: 1396.8
pair:NA-EU_FstWC: 1322.26
LDA6: 1083.18
LDA7: 1065.61
LDA8: 1060.07
pop:NA_Hsd: 1048.82
pop:BR_Hsd: 1023.57
pop:NA_R2: 965.465
LDA11: 957.065
all_FstWC: 898.893
all_Dj: 865.791
LDA10: 860.512
LDA12: 759.244
LDA9: 758.052
pop:EU_Hsd: 624.484
pop:NA_Ch: 606.545
pop:BR_R2: 603.486
pop:EU_Ch: 596.289
all_Hsd: 593.733
pop:BR_Ch: 563.721
NOISE2: 538.21
NOISE5: 538.083
NOISE3: 537.322
NOISE4: 537.209
NOISE1: 536.552
pop:BR_Ki: 535.001
pop:BR_KoP: 491.599
pop:EU_KoP: 490.581
pop:NA_KoP: 474.429
pop:NA_Ki: 455.241
all_KoP: 407.169
pop:EU_Ki: 394.865
pair:NA-BR_numShP: 389.499
pop:BR_Pi: 378.452
pair:BR-EU_numShP: 370.392
pair:BR-EU_numSpd: 365.161
all_Ki: 358.387
pair:NA-EU_numSpd: 357.795
pair:NA-BR_numSpd: 357.05
pop:BR_KoS: 356.726
pair:NA-EU_numShP: 355.682
pop:NA_Pi: 352.381
pop:BR_thetaW: 352.096
all_KoS: 350.18
pop:BR_S: 350.179
pop:NA_KoS: 347.989
pop:EU_KoS: 341.38
pop:NA_thetaW: 328.72
pop:NA_S: 324.553
all_Ch: 317.377
pair:NA-BR_numShA: 303.356
pop:EU_Pi: 301.339
pop:EU_thetaW: 292.804
pop:EU_S: 292.627
pair:BR-EU_numShA: 284.95
pair:NA-EU_numShA: 280.999
all_Pi: 280.347
all_thetaW: 280.337
all_S: 278.736

# modelchoice_out.predictions #

        model1        model2        model3        model4        model5        model6        model7        model8        model9       model10       model11       model12       model13 selected model  post proba
         0.068         0.054         0.284         0.030         0.166         0.030         0.000         0.000         0.100         0.032         0.082         0.000         0.154              3       0.734
         0.002         0.001         0.852         0.000         0.100         0.000         0.000         0.000         0.011         0.001         0.004         0.000         0.028              3       1.000
         0.002         0.002         0.734         0.000         0.216        -0.000        -0.000        -0.000         0.005         0.001         0.004        -0.000         0.035              3       1.000

# modelchoice_out.confusion #

Prior error rate: 0.220341

Class specific prediction errors:
                1     2     3     4     5     6     7     8     9     10     11     12     13 class.error
predicted 1     3869861399  1097  33475 20600 6389  1585  3059  81    4176  33173 3250  22601  0.252737
predicted 2     2249  39993126197 1313  1601  2132  25845 6860  1337  284   4480  36634 22293  0.247055
predicted 3     2143  41662 4117394440  4452  3114  1548  133   42206 6097  22831 3053  33214  0.285959
predicted 4     16094 1069  1969  3635704585  23195 75    1246  1275  1527  1474  27235 32540  0.235963
predicted 5     23303 2336  3865  11584 41714655339 52    10    94    1109  1063  282   5413   0.200251
predicted 6     8627  2298  2365  31966 43008 40254477    518   89    5     212   1568  4312   0.191011
predicted 7     1494  17749 260   48    44    8     42285655740 62    26    3847  3983  1305   0.166658
predicted 8     4191  4416  131   371   56    349   39328 4055695     109   4522  28756 2857   0.173422
predicted 9     62    395   17802 1133  21    34    83    22    40496540301 4274  934   2267   0.142556
predicted 10     1292  460   6867  3115  1466  46    9     67    37788 40011418659 2956  7488   0.166997
predicted 11     44988 3005  15415 2248  3385  121   4474  4072  4214  35799 3947283786  33874  0.282455
predicted 12     2013  15059 1948  24596 156   3561  2775  21251 1074  1746  3169  36643640634  0.243554
predicted 13     6558  10221 10345 22141 3480  3168  1293  1453  6810  8707  7568  21127 291202 0.261046
### fit M_BR_EU ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: M_BR_EU
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 14 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

pop:BR_D: 122.362
pop:BR_R2: 80.2223
Comp 1: 79.4442
Comp 2: 78.345
Comp 6: 63.9691
Comp 5: 60.3031
Comp 7: 49.681
pair:NA-BR_FstWC: 44.6203
Comp 8: 43.9435
Comp 9: 37.7247
Comp 12: 37.2977
Comp 4: 35.9007
Comp 13: 29.2445
Comp 11: 28.2954
pair:NA-BR_Dxy: 27.9357
Comp 3: 26.1776
NOISE1: 26.137
NOISE2: 26.0949
NOISE3: 26.0486
NOISE5: 25.8844
NOISE4: 25.8359
Comp 14: 24.6814
pop:BR_Ch: 22.4646
pop:NA_Hsd: 22.4242
pop:BR_Hsd: 22.2723
pop:BR_KoP: 22.1905
pair:NA-BR_Da: 21.5352
Comp 10: 21.2223
pop:EU_R2: 20.8008
pop:EU_Ch: 20.5625
pop:EU_D: 20.1595
pair:BR-EU_numShP: 20.0353
pop:NA_D: 19.7087
pop:NA_R2: 19.5435
all_R2: 19.3817
pop:EU_Hsd: 18.7986
pop:NA_Ch: 18.7543
pop:BR_Ki: 18.7113
all_D: 18.6374
pair:BR-EU_Dxy: 18.608
all_Hsd: 18.5322
pair:NA-EU_Dxy: 18.2164
pair:NA-BR_Dj: 18.0343
pop:EU_KoP: 17.2568
pair:BR-EU_Da: 16.9505
pair:BR-EU_numSpd: 16.8833
pop:EU_Ki: 16.8284
pair:NA-EU_numSpd: 15.0443
pair:BR-EU_FstWC: 14.7728
pair:BR-EU_Dj: 14.6488
pop:NA_KoP: 14.5709
pop:BR_KoS: 14.4802
pop:NA_Ki: 14.3199
all_Dj: 13.946
all_FstWC: 13.7533
all_Ki: 13.6624
pair:NA-EU_Dj: 13.2598
pair:NA-EU_FstWC: 13.183
pair:NA-EU_Da: 13.1596
all_KoP: 12.8446
all_KoS: 12.1229
pop:EU_KoS: 11.5806
pair:NA-BR_numSpd: 11.3648
pair:NA-BR_numShP: 11.0511
pop:NA_KoS: 10.8016
pair:NA-EU_numShP: 10.3365
pop:BR_thetaW: 10.182
pop:BR_Pi: 10.1577
pop:BR_S: 10.087
pop:EU_Pi: 8.05466
all_Ch: 7.93261
pop:EU_thetaW: 7.11747
pop:NA_Pi: 6.91505
pop:EU_S: 6.75174
pair:NA-BR_numShA: 6.23521
all_thetaW: 6.23206
pop:NA_thetaW: 6.11343
pair:BR-EU_numShA: 6.0618
pop:NA_S: 6.01618
all_Pi: 5.87574
all_S: 5.80603
pair:NA-EU_numShA: 5.78427

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
      0.436408      0.428865      0.149552      0.721705     0.0282554

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 13.170115263094125
                      MSE : 0.013387634135399168
                     NMSE : 2.153024493778293
Computed from the median taken as point estimate
                     NMAE : 1.196439162013958
                      MSE : 0.011082032675753863
                     NMSE : 0.16099526874201056
Confidence interval measures
             90% coverage : 0.96         
              Mean 90% CI : 0.4026977685123984
     Mean relative 90% CI : 4.516362301789031
            Median 90% CI : 0.4196855793396633
   Median relative 90% CI : 2.3495673470068112

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.4579707119978497
                      MSE : 0.028255438526334012
                     NMSE : 0.10047600019225274

### fit M_BR_NA ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: M_BR_NA
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 17 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

pop:BR_D: 104.765
pop:BR_R2: 100.353
Comp 2: 70.7949
pair:NA-BR_FstWC: 57.7173
Comp 9: 48.905
Comp 1: 47.3558
Comp 8: 40.0928
Comp 12: 36.8607
Comp 10: 34.7068
Comp 6: 34.0513
pair:NA-BR_Da: 33.5198
Comp 17: 32.5347
Comp 3: 28.8973
Comp 15: 28.6252
Comp 4: 27.9574
Comp 16: 27.9175
Comp 5: 27.8602
Comp 13: 26.3652
Comp 11: 26.2346
NOISE2: 26.1507
NOISE1: 25.9639
NOISE3: 25.9146
Comp 14: 25.9139
NOISE5: 25.8784
NOISE4: 25.8541
pop:NA_Hsd: 25.5454
pair:NA-BR_Dj: 25.0682
pop:BR_KoP: 23.8364
pop:BR_Ch: 23.4536
pair:NA-BR_numShP: 23.0789
pop:BR_Hsd: 22.7297
Comp 7: 22.5508
pair:BR-EU_Dxy: 21.1117
pair:NA-BR_numSpd: 20.444
pair:NA-BR_Dxy: 20.337
all_Hsd: 19.9373
pop:NA_R2: 19.2415
pop:NA_D: 19.2378
pop:EU_Ch: 19.0182
pop:BR_Ki: 18.9102
pop:EU_R2: 18.9071
pop:EU_Hsd: 18.6553
pop:EU_D: 18.3298
pop:NA_Ch: 18.3103
pair:NA-EU_Dxy: 17.197
all_R2: 17.1847
all_D: 16.9621
pop:EU_KoP: 16.1144
pop:EU_Ki: 15.0374
pop:NA_Ki: 14.7919
all_Ki: 14.5173
pop:NA_KoP: 14.3756
pair:NA-EU_numSpd: 13.6417
pop:BR_KoS: 13.4324
pair:BR-EU_Dj: 13.1431
all_KoP: 13.0543
all_Dj: 12.9876
pair:BR-EU_FstWC: 12.8568
pair:BR-EU_Da: 12.8046
all_FstWC: 12.5142
pair:BR-EU_numSpd: 12.3062
pair:NA-EU_Da: 12.2713
pair:NA-EU_Dj: 12.1891
all_KoS: 12.1317
pair:NA-EU_FstWC: 12.0987
pop:EU_KoS: 11.6002
pop:NA_KoS: 10.9746
pair:BR-EU_numShP: 10.657
pair:NA-EU_numShP: 10.3654
pop:BR_Pi: 9.69875
pop:BR_thetaW: 9.44431
pop:BR_S: 9.29415
all_Ch: 7.96059
pop:EU_Pi: 7.4928
pop:NA_Pi: 7.48048
pop:EU_thetaW: 6.63337
pop:NA_thetaW: 6.41728
pop:EU_S: 6.36319
pair:NA-BR_numShA: 6.30681
all_thetaW: 6.27947
pop:NA_S: 6.14047
all_S: 6.10638
pair:BR-EU_numShA: 6.08036
all_Pi: 5.93034
pair:NA-EU_numShA: 5.61577

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
       0.33143      0.319892     0.0666814      0.618239     0.0216459

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 5.86014513762354
                      MSE : 0.013928499435943813
                     NMSE : 0.9170567627438119
Computed from the median taken as point estimate
                     NMAE : 1.2678279934398626
                      MSE : 0.014069149787265733
                     NMSE : 0.21568322831478426
Confidence interval measures
             90% coverage : 0.98         
              Mean 90% CI : 0.41415035899657776
     Mean relative 90% CI : 4.059276317453042
            Median 90% CI : 0.42842035221556823
   Median relative 90% CI : 2.1873246594804057

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 2.118620168808502
                      MSE : 0.021645942450216202
                     NMSE : 0.4464703829331327
Computed from the median taken as point estimate
                     NMAE : 0.4153891752792392
                      MSE : 0.027213942616592435
                     NMSE : 0.0685252939700421

### fit M_EU_BR ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: M_EU_BR
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 18 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

Comp 4: 131.688
Comp 5: 78.1852
pop:EU_R2: 71.6113
Comp 1: 68.8467
Comp 10: 68.7009
pop:EU_D: 68.3719
Comp 2: 67.9079
Comp 3: 50.4642
Comp 12: 47.2977
all_D: 46.7881
all_R2: 44.2812
Comp 9: 32.1316
Comp 11: 32.0149
Comp 18: 31.2031
Comp 17: 27.4662
Comp 13: 26.3615
Comp 7: 26.3394
pair:BR-EU_FstWC: 24.3536
Comp 15: 24.0382
Comp 16: 22.6937
Comp 8: 22.644
Comp 6: 22.4501
Comp 14: 22.2309
pop:EU_Ch: 22.1505
pop:EU_Hsd: 21.2991
pair:BR-EU_numShP: 20.8002
pop:BR_D: 20.7054
NOISE3: 20.6322
NOISE2: 20.6302
NOISE4: 20.5097
NOISE5: 20.4921
NOISE1: 20.4482
pair:BR-EU_Da: 20.1933
pop:EU_KoP: 19.6198
pair:BR-EU_Dxy: 18.8834
pop:BR_R2: 18.1633
all_FstWC: 18.0366
pair:NA-BR_Dxy: 18.0328
pop:NA_R2: 17.676
pop:BR_Hsd: 17.3241
pop:NA_Hsd: 17.2414
pair:NA-BR_FstWC: 16.8857
pop:NA_D: 16.7069
all_Hsd: 16.3551
pair:NA-EU_Dxy: 16.3279
pair:NA-EU_FstWC: 16.2258
pair:BR-EU_Dj: 15.8523
pop:BR_Ch: 15.7428
pair:BR-EU_numSpd: 15.4494
pop:NA_Ch: 15.0426
pair:NA-BR_Dj: 14.7825
pair:NA-BR_Da: 14.7514
pop:BR_Ki: 14.2996
pair:NA-EU_Da: 14.282
pair:NA-EU_Dj: 14.1426
all_Dj: 13.4767
pop:BR_KoP: 12.4358
pop:NA_KoP: 11.8278
pair:NA-EU_numSpd: 11.5522
pop:NA_Ki: 11.2993
pop:EU_Ki: 11.2202
all_KoP: 11.0839
pop:BR_KoS: 9.63418
all_KoS: 9.48726
pair:NA-BR_numShP: 9.43325
pair:NA-BR_numSpd: 9.22341
all_Ki: 9.21405
pop:EU_KoS: 8.91372
pop:NA_KoS: 8.44027
pair:NA-EU_numShP: 8.02777
pop:BR_Pi: 7.43439
pop:BR_thetaW: 6.21069
pop:BR_S: 6.16731
all_Ch: 5.71897
pop:EU_Pi: 5.25238
pop:NA_Pi: 5.14299
pair:NA-BR_numShA: 4.93096
pop:EU_thetaW: 4.9107
pop:EU_S: 4.84466
pair:BR-EU_numShA: 4.73395
pop:NA_thetaW: 4.51838
pop:NA_S: 4.40668
all_thetaW: 4.08989
all_S: 3.97323
pair:NA-EU_numShA: 3.89331
all_Pi: 3.84405

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
      0.422879      0.418974      0.143661      0.723284     0.0279878

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 4.336539916682058
                      MSE : 0.01135678034833269
                     NMSE : 0.5934614742588044
Computed from the median taken as point estimate
                     NMAE : 1.2000838228335813
                      MSE : 0.01397539730487677
                     NMSE : 0.14642956251897596
Confidence interval measures
             90% coverage : 0.92         
              Mean 90% CI : 0.39310986020258537
     Mean relative 90% CI : 4.4566297645324005
            Median 90% CI : 0.40423611508475416
   Median relative 90% CI : 1.8194645118733592

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.36512185236622635
                      MSE : 0.027987809486749914
                     NMSE : 0.06655413579164156

### fit M_EU_NA ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: M_EU_NA
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 22 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

Comp 1: 100.041
pop:EU_D: 88.7137
pop:EU_R2: 82.5006
Comp 4: 74.714
all_R2: 62.1701
Comp 17: 54.7152
all_D: 54.3731
Comp 2: 49.6662
Comp 12: 47.4251
Comp 10: 47.1389
Comp 5: 44.1997
Comp 11: 34.4822
Comp 9: 30.3221
Comp 18: 30.2235
Comp 20: 27.1075
Comp 13: 27.0444
pop:EU_KoP: 26.1837
Comp 14: 24.3498
pair:NA-EU_FstWC: 24.0741
Comp 6: 23.5392
pop:EU_Ch: 21.8983
NOISE4: 21.8905
NOISE5: 21.7643
NOISE1: 21.6388
NOISE3: 21.6208
Comp 22: 21.5272
NOISE2: 21.4102
Comp 21: 20.8399
Comp 19: 19.86
Comp 8: 19.4956
Comp 3: 18.8793
pair:NA-EU_Da: 18.8401
Comp 15: 18.4793
pop:NA_Hsd: 18.0577
all_FstWC: 17.9098
pop:NA_R2: 17.6736
pop:BR_R2: 17.6336
Comp 16: 17.215
Comp 7: 17.1761
pop:BR_D: 17.085
pair:NA-EU_Dxy: 17.0645
pop:NA_D: 16.9399
pair:NA-BR_Dxy: 16.7054
pop:EU_Hsd: 16.4706
pop:BR_Hsd: 16.3658
pair:NA-EU_Dj: 16.062
all_Hsd: 15.8558
pair:BR-EU_Dxy: 15.1441
pop:NA_Ch: 14.8423
pair:NA-EU_numSpd: 14.8405
pop:BR_Ch: 14.4275
pop:BR_Ki: 13.8499
pair:NA-EU_numShP: 13.5867
pair:NA-BR_FstWC: 13.4969
pop:BR_KoP: 12.695
pair:BR-EU_FstWC: 12.2263
pop:EU_Ki: 11.8502
pop:NA_KoP: 11.4495
pop:NA_Ki: 11.449
pair:NA-BR_Dj: 11.3988
pair:NA-BR_Da: 11.3411
all_KoP: 11.2075
all_Dj: 11.054
pair:BR-EU_numSpd: 10.9814
pair:BR-EU_Dj: 10.2845
pair:BR-EU_Da: 10.1473
pop:BR_KoS: 10.0591
all_Ki: 9.41698
pair:BR-EU_numShP: 9.33809
all_KoS: 9.28892
pop:EU_KoS: 9.13366
pair:NA-BR_numSpd: 8.82927
pop:NA_KoS: 8.35103
pair:NA-BR_numShP: 8.29563
pop:BR_Pi: 7.36382
pop:BR_thetaW: 6.18134
pop:BR_S: 6.05412
all_Ch: 5.88247
pop:EU_thetaW: 5.57624
pop:EU_Pi: 5.55685
pop:EU_S: 5.35491
pair:NA-BR_numShA: 5.3076
pair:BR-EU_numShA: 5.18354
pop:NA_Pi: 5.14617
pop:NA_thetaW: 4.57606
pop:NA_S: 4.4333
all_thetaW: 4.1808
pair:NA-EU_numShA: 3.99346
all_S: 3.98322
all_Pi: 3.88608

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
      0.474174      0.478764       0.19201      0.761589     0.0303294

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 17.151870848476225
                      MSE : 0.012316733915021078
                     NMSE : 2.4511122487694874
Computed from the median taken as point estimate
                     NMAE : 2.82137966314036
                      MSE : 0.012117395860707132
                     NMSE : 0.32843179637795705
Confidence interval measures
             90% coverage : 0.92         
              Mean 90% CI : 0.3888715848039621
     Mean relative 90% CI : 9.412613102037412
            Median 90% CI : 0.41041681002293323
   Median relative 90% CI : 2.0188616688962155

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.3134881886403434
                      MSE : 0.03032939705939895
                     NMSE : 0.05870105606369769

### fit M_NA_BR ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: M_NA_BR
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 16 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

Comp 5: 83.0205
Comp 2: 81.3154
pop:NA_R2: 78.0638
Comp 3: 77.577
pop:NA_D: 75.1957
Comp 12: 52.1131
Comp 8: 48.3611
pair:NA-BR_FstWC: 45.1904
Comp 1: 41.9711
Comp 6: 41.3346
Comp 10: 39.0765
Comp 9: 32.0933
Comp 4: 30.7233
Comp 7: 29.4059
Comp 13: 29.3392
Comp 11: 28.9325
NOISE4: 25.207
NOISE2: 25.1114
NOISE5: 24.9576
NOISE3: 24.9544
NOISE1: 24.768
Comp 16: 24.3834
pop:BR_R2: 22.1591
pair:NA-EU_Dxy: 22.1188
Comp 15: 22.047
Comp 14: 21.9202
pop:NA_Hsd: 21.7764
pair:NA-BR_Da: 21.7024
pop:BR_D: 21.5477
pop:EU_Hsd: 21.2766
pair:NA-BR_Dxy: 21.2291
pop:NA_Ch: 21.1704
pop:BR_Hsd: 20.564
pop:EU_Ch: 20.3779
all_Hsd: 20.0103
all_R2: 19.7622
pop:EU_D: 19.3603
pop:BR_Ch: 19.2915
all_D: 19.221
pop:EU_R2: 18.7995
pair:NA-EU_FstWC: 18.4486
pair:NA-BR_Dj: 17.8629
pair:NA-EU_Dj: 17.2876
pair:NA-EU_Da: 17.2258
pair:BR-EU_FstWC: 16.7129
pair:NA-BR_numSpd: 16.4354
pop:BR_Ki: 16.4013
pop:EU_KoP: 16.3882
pair:BR-EU_Dxy: 16.2433
pop:NA_KoP: 15.9372
all_FstWC: 15.6446
pair:BR-EU_Da: 15.463
pair:NA-EU_numSpd: 15.3698
pop:BR_KoP: 14.8901
pair:BR-EU_Dj: 14.6983
pop:NA_Ki: 14.6719
pop:EU_Ki: 14.1179
all_Dj: 13.3411
all_KoP: 12.7537
all_KoS: 12.1122
pop:BR_KoS: 11.916
all_Ki: 11.607
pop:EU_KoS: 11.2328
pair:BR-EU_numSpd: 11.1721
pop:NA_KoS: 10.994
pair:NA-BR_numShP: 10.8648
pair:BR-EU_numShP: 10.5127
pair:NA-EU_numShP: 9.68275
pop:BR_Pi: 8.75318
pop:BR_thetaW: 7.59303
all_Ch: 7.43772
pop:BR_S: 7.42468
pop:EU_Pi: 7.28714
pop:NA_Pi: 6.93915
pop:NA_thetaW: 6.87242
pop:NA_S: 6.50532
pop:EU_thetaW: 6.39523
pop:EU_S: 6.16676
pair:BR-EU_numShA: 6.00527
pair:NA-BR_numShA: 5.83325
all_thetaW: 5.7317
pair:NA-EU_numShA: 5.56831
all_S: 5.48209
all_Pi: 5.33519

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
      0.466777      0.463264      0.168255      0.751664     0.0397442

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 4.198860959932309
                      MSE : 0.013311983321792514
                     NMSE : 0.6715865346823424
Computed from the median taken as point estimate
                     NMAE : 1.1872499640122658
                      MSE : 0.010964527147207281
                     NMSE : 0.1704725842159624
Confidence interval measures
             90% coverage : 0.92         
              Mean 90% CI : 0.38001694524321517
     Mean relative 90% CI : 4.306705043371832
            Median 90% CI : 0.39881973148323596
   Median relative 90% CI : 2.3954189540442785

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.5489221557289977
                      MSE : 0.03974423170509334
                     NMSE : 0.12300819323096526

### fit M_NA_EU ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: M_NA_EU
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 20 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

pop:NA_D: 124.503
pop:NA_R2: 110.208
Comp 7: 65.1283
Comp 1: 61.3321
Comp 2: 42.1122
Comp 5: 41.126
Comp 16: 36.094
all_R2: 34.2194
Comp 10: 33.9077
Comp 9: 32.3738
Comp 12: 31.2493
Comp 4: 30.8641
Comp 17: 30.5636
all_D: 30.3408
Comp 6: 29.693
Comp 13: 29.1375
Comp 14: 29.1371
Comp 8: 25.3239
NOISE3: 25.2141
NOISE5: 25.1914
NOISE1: 25.0464
NOISE2: 24.9595
NOISE4: 24.9508
pop:NA_Hsd: 24.5891
pair:NA-BR_FstWC: 24.5227
Comp 3: 24.1314
Comp 11: 23.992
Comp 20: 23.1436
Comp 15: 23.0156
Comp 18: 22.6123
pair:NA-EU_Dxy: 22.5918
pop:NA_Ch: 22.5737
pair:NA-BR_Dxy: 22.3032
pair:NA-EU_FstWC: 22.0313
Comp 19: 21.6765
pop:BR_R2: 20.4606
pop:EU_D: 20.3539
pop:BR_D: 20.2055
pop:EU_R2: 19.7965
pop:BR_Hsd: 19.531
pair:BR-EU_Dxy: 19.225
pop:EU_Hsd: 19.192
pop:NA_KoP: 18.9656
pair:NA-EU_Da: 18.8225
all_Hsd: 18.7672
pair:NA-EU_Dj: 18.5788
pop:EU_Ch: 18.5027
pop:EU_Ki: 17.3967
pop:BR_Ch: 16.7321
pop:EU_KoP: 15.5039
pop:BR_Ki: 15.0376
all_FstWC: 14.8978
pair:BR-EU_FstWC: 14.8374
pop:NA_Ki: 13.8492
pair:NA-BR_Da: 13.6716
pair:NA-BR_Dj: 13.6145
pop:BR_KoP: 13.538
pair:BR-EU_Dj: 12.7242
pair:NA-EU_numSpd: 12.1747
all_Dj: 12.1006
pair:BR-EU_Da: 12.0624
pair:NA-BR_numSpd: 10.9313
all_KoP: 10.9051
all_Ki: 10.739
pop:BR_KoS: 10.7298
all_KoS: 10.4868
pop:EU_KoS: 9.83231
pop:NA_KoS: 9.1475
pair:BR-EU_numShP: 9.07429
pair:NA-EU_numShP: 9.03802
pair:NA-BR_numShP: 9.02
pair:BR-EU_numSpd: 8.61915
pop:BR_Pi: 7.61952
pop:EU_Pi: 7.32724
all_Ch: 6.46891
pop:BR_thetaW: 6.46626
pop:EU_thetaW: 6.25032
pop:BR_S: 6.22383
pop:EU_S: 6.10569
pop:NA_thetaW: 5.93186
pop:NA_Pi: 5.81509
pair:NA-BR_numShA: 5.80668
pop:NA_S: 5.55527
pair:BR-EU_numShA: 5.50574
all_thetaW: 4.66903
all_S: 4.56011
all_Pi: 4.49987
pair:NA-EU_numShA: 4.24634

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
      0.374221      0.368419     0.0789447      0.683544     0.0281499

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 4.907579396791854
                      MSE : 0.01382414755222192
                     NMSE : 0.8528054499487701
Computed from the median taken as point estimate
                     NMAE : 0.6419247034095282
                      MSE : 0.013919465334928145
                     NMSE : 0.07726982502295288
Confidence interval measures
             90% coverage : 0.96         
              Mean 90% CI : 0.3967862383145173
     Mean relative 90% CI : 3.042468869850643
            Median 90% CI : 0.4186435950199763
   Median relative 90% CI : 2.0565428526184713

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 1.3978329807590397
                      MSE : 0.02814990430576772
                     NMSE : 0.3275041883783766
Computed from the median taken as point estimate
                     NMAE : 0.4226842125462032
                      MSE : 0.08867002536864904
                     NMSE : 0.12586484443931067

### fit N_BR ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: N_BR
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 6 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

pair:NA-BR_Da: 9764
pair:NA-BR_Dj: 5824.46
pop:BR_Hsd: 3367.73
Comp 1: 3108.11
pair:NA-BR_FstWC: 2827.53
Comp 5: 1337.19
Comp 6: 1258.32
pop:BR_Ki: 1145.78
pair:BR-EU_Da: 1050.3
Comp 4: 978.096
Comp 3: 956.718
Comp 2: 932.017
pop:BR_R2: 687.781
pair:NA-EU_FstWC: 667.015
pair:NA-EU_Da: 661.318
pop:NA_Hsd: 638.945
pair:NA-EU_Dj: 637.906
all_Hsd: 618.953
pair:BR-EU_Dj: 576.691
pop:BR_D: 559.119
pop:EU_Hsd: 535.853
pair:NA-BR_Dxy: 508.813
pair:NA-EU_Dxy: 477.461
pop:NA_R2: 470.352
NOISE5: 465.425
NOISE2: 462.79
NOISE1: 461.986
NOISE4: 461.353
NOISE3: 461.077
all_Dj: 459.879
pop:NA_D: 446.236
all_D: 407.405
pop:NA_Ki: 405.861
pair:BR-EU_FstWC: 405.203
all_R2: 385.552
pop:BR_Ch: 376.887
pair:BR-EU_Dxy: 373.547
pop:EU_D: 373.299
pop:EU_R2: 370.131
pop:EU_Ch: 369.344
pop:BR_KoP: 334.583
all_FstWC: 325.037
pop:NA_Ch: 319.619
pop:EU_Ki: 309.05
pop:EU_KoP: 285.502
pop:BR_Pi: 263.262
all_Ki: 247.826
pop:NA_KoP: 244.378
pop:BR_thetaW: 241.584
pair:NA-BR_numShP: 236.849
pop:BR_KoS: 236.255
pop:BR_S: 228.541
all_KoP: 218.611
pair:BR-EU_numShP: 218.596
pair:NA-EU_numSpd: 213.412
all_KoS: 209.378
pair:BR-EU_numSpd: 198.944
pair:NA-EU_numShP: 194.175
pair:NA-BR_numSpd: 184.613
pop:EU_KoS: 184.036
pop:NA_KoS: 171.783
pop:EU_Pi: 127.427
all_Ch: 127.01
pop:NA_Pi: 126.914
pop:NA_thetaW: 116.812
pop:EU_thetaW: 115.538
pop:EU_S: 110.286
pop:NA_S: 109.868
pair:NA-EU_numShA: 105.155
all_Pi: 94.5087
all_thetaW: 94.4523
all_S: 90.8286
pair:BR-EU_numShA: 90.2925
pair:NA-BR_numShA: 88.9142

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
        1.5928       1.55075       0.73259       2.58517      0.289678

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.3059338463965808
                      MSE : 0.21176856224437537
                     NMSE : 0.1597765107363308
Computed from the median taken as point estimate
                     NMAE : 0.2943600815070024
                      MSE : 0.26674076193923363
                     NMSE : 0.15947423698450708
Confidence interval measures
             90% coverage : 0.94         
              Mean 90% CI : 1.4920483859493279
     Mean relative 90% CI : 1.357201986624321
            Median 90% CI : 1.6743042416870595
   Median relative 90% CI : 1.3052204536775118

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.2533150374711661
                      MSE : 0.2896780878485286
                     NMSE : 0.14665014097879944

### fit N_EU ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: N_EU
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 5 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

pair:NA-EU_Dj: 9666.09
pair:NA-EU_Da: 5545.48
pair:NA-EU_Dxy: 4203.1
pair:NA-EU_FstWC: 4065.26
all_FstWC: 2845.91
pair:BR-EU_Dxy: 2213.65
Comp 1: 1793.94
pair:BR-EU_FstWC: 1429.16
pop:EU_R2: 1247.93
all_R2: 1074.13
Comp 3: 1026.98
pop:EU_D: 979.868
pair:BR-EU_Dj: 843.474
pair:NA-BR_Dxy: 831.884
all_D: 788.155
Comp 4: 721.973
pair:BR-EU_Da: 589.78
Comp 5: 577.289
all_Dj: 486.204
pop:NA_D: 436.718
pair:NA-BR_FstWC: 428.663
pair:NA-BR_Dj: 424.048
NOISE2: 405.754
NOISE1: 403.717
NOISE4: 402.997
NOISE3: 402.51
NOISE5: 401.491
pair:NA-BR_Da: 394.752
pop:BR_D: 377.388
pop:BR_Hsd: 377.33
pop:EU_Ch: 370.397
pop:NA_Hsd: 362.722
pop:NA_R2: 354.647
pop:BR_R2: 352.565
pop:EU_Hsd: 334.381
pop:EU_KoP: 321.965
Comp 2: 319.081
all_Hsd: 313.848
pop:EU_Ki: 294.016
pop:BR_Ch: 274.668
pop:BR_Ki: 264.357
pop:NA_Ch: 263.275
pop:BR_KoP: 212.319
pop:NA_KoP: 191.913
pop:NA_Ki: 189.762
all_KoP: 186.811
all_KoS: 183.796
pop:EU_KoS: 178.687
all_Ki: 175.138
pair:NA-EU_numSpd: 171.339
pop:BR_KoS: 155.274
pair:BR-EU_numSpd: 139.36
pair:NA-BR_numSpd: 137.188
pop:NA_KoS: 130.277
pair:NA-BR_numShP: 121.687
pair:BR-EU_numShP: 120.63
pop:BR_Pi: 112.046
pop:BR_S: 94.7802
pair:NA-EU_numShP: 94.631
all_Ch: 94.2396
pop:BR_thetaW: 93.7391
pop:EU_thetaW: 79.9332
pop:EU_S: 77.4437
pop:EU_Pi: 76.6812
pair:BR-EU_numShA: 71.814
pair:NA-BR_numShA: 71.3144
pop:NA_Pi: 70.1682
pop:NA_thetaW: 63.4621
pop:NA_S: 62.4426
all_thetaW: 61.0372
all_S: 59.1198
pair:NA-EU_numShA: 58.0262
all_Pi: 57.6696

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
       2.57594       2.59081       1.49027       3.79001      0.573374

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.25461789797546763
                      MSE : 0.1794008941957028
                     NMSE : 0.13379598474654675
Computed from the median taken as point estimate
                     NMAE : 0.2471646217502095
                      MSE : 0.13541167416052502
                     NMSE : 0.13652826371293356
Confidence interval measures
             90% coverage : 0.94         
              Mean 90% CI : 1.3079034009358395
     Mean relative 90% CI : 1.0985753588347602
            Median 90% CI : 1.3374626643778313
   Median relative 90% CI : 0.8727295421674959

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.2287870067533207
                      MSE : 0.5733743947448259
                     NMSE : 0.19283361144638753
Computed from the median taken as point estimate
                     NMAE : 0.017176198128033872
                      MSE : 0.0007753288238951939
                     NMSE : 0.0004782665484486771

### fit S1 ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: S1
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 14 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

pop:EU_D: 633.38
pop:EU_R2: 487.192
Comp 1: 217.761
pair:NA-EU_Dxy: 181.177
all_R2: 143.066
pair:NA-EU_Dj: 141.546
all_D: 126.564
pair:NA-BR_Dxy: 112.956
pair:NA-EU_Da: 90.4858
all_FstWC: 88.8827
pair:NA-EU_FstWC: 78.3004
Comp 3: 76.7978
pair:BR-EU_Dxy: 71.6731
Comp 4: 70.1059
Comp 6: 54.6115
pair:NA-BR_FstWC: 52.6011
pair:BR-EU_FstWC: 44.9722
pop:EU_Ch: 44.0773
Comp 5: 38.7927
Comp 9: 33.9576
pop:EU_KoP: 31.6816
Comp 11: 29.7229
Comp 14: 26.7913
NOISE3: 25.7108
NOISE5: 25.579
NOISE2: 25.3758
NOISE1: 25.3414
NOISE4: 25.3059
pop:NA_D: 25.2485
Comp 10: 25.2384
pop:EU_Hsd: 23.4669
Comp 12: 23.2485
pop:NA_R2: 22.9373
pop:BR_Hsd: 22.5958
pair:BR-EU_Dj: 22.4895
Comp 7: 22.4112
pop:BR_D: 22.3362
pop:BR_R2: 22.1905
pop:NA_Hsd: 21.6591
Comp 13: 21.3838
Comp 2: 21.243
Comp 8: 20.9752
pair:NA-BR_Da: 20.6514
all_Dj: 20.2339
pair:NA-BR_Dj: 20.0718
all_Hsd: 19.9136
pair:BR-EU_Da: 18.5984
pop:NA_Ch: 17.9032
pop:BR_Ch: 17.6105
pop:EU_Ki: 17.0247
pop:BR_Ki: 16.6752
pop:NA_KoP: 14.7157
pop:BR_KoP: 14.5179
all_KoP: 13.6639
pop:NA_Ki: 13.1094
pair:NA-EU_numSpd: 12.0599
pop:BR_KoS: 11.4742
pop:EU_KoS: 11.4384
all_KoS: 11.3641
pair:NA-BR_numShP: 10.65
all_Ki: 10.6257
pair:BR-EU_numShP: 10.3281
pop:NA_KoS: 10.3048
pair:NA-BR_numSpd: 9.66307
pair:BR-EU_numSpd: 9.26791
pair:NA-EU_numShP: 8.92784
pop:BR_Pi: 8.08105
pop:EU_Pi: 6.96253
all_Ch: 6.92974
pop:BR_thetaW: 6.80015
pop:BR_S: 6.72801
pop:EU_thetaW: 6.58154
pop:EU_S: 6.27116
pop:NA_Pi: 6.12762
pair:NA-BR_numShA: 5.63252
pair:BR-EU_numShA: 5.59274
pop:NA_thetaW: 5.25671
pop:NA_S: 5.24593
all_thetaW: 4.5968
pair:NA-EU_numShA: 4.51269
all_S: 4.46232
all_Pi: 4.45759

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
      0.628039      0.626322      0.335033      0.903825     0.0298284

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 2.2370727816353195
                      MSE : 0.013598118262946596
                     NMSE : 0.26846730315553907
Computed from the median taken as point estimate
                     NMAE : 0.6299502402017121
                      MSE : 0.012741552730866608
                     NMSE : 0.08042019740691947
Confidence interval measures
             90% coverage : 0.96         
              Mean 90% CI : 0.3952172410538264
     Mean relative 90% CI : 2.6502994404745848
            Median 90% CI : 0.4082071215527313
   Median relative 90% CI : 1.5855112864363199

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.23389669914098749
                      MSE : 0.029828388381150515
                     NMSE : 0.04537984605102736

### fit S2 ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: S2
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 11 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

pop:BR_D: 536.796
Comp 1: 193.865
Comp 4: 132.875
pop:BR_Hsd: 125.13
Comp 5: 104.052
Comp 11: 92.8176
pair:NA-BR_Da: 80.2633
pop:BR_Ch: 77.9587
pair:NA-BR_FstWC: 74.015
Comp 7: 73.6431
pair:NA-BR_Dj: 64.4185
Comp 3: 58.6443
Comp 6: 57.8593
Comp 10: 57.263
pop:BR_R2: 57.0247
Comp 9: 56.8135
Comp 2: 51.9282
all_D: 50.3953
NOISE3: 50.2281
NOISE2: 50.1745
NOISE4: 50.1528
NOISE5: 49.9481
NOISE1: 49.906
Comp 8: 48.3269
all_R2: 46.2218
pop:BR_KoP: 45.7953
pop:NA_Hsd: 45.7915
pop:NA_D: 42.2818
pop:NA_R2: 41.9793
all_Hsd: 40.8721
pop:BR_Ki: 39.3258
pop:EU_Hsd: 38.7979
pair:NA-BR_Dxy: 38.7435
pair:BR-EU_Dxy: 38.4696
pop:EU_Ch: 38.3998
pop:EU_R2: 38.2365
pop:EU_D: 37.1781
pair:NA-EU_Dxy: 37.0961
pop:NA_Ch: 34.7208
pair:NA-EU_FstWC: 30.6297
pop:EU_KoP: 29.5831
pop:NA_KoP: 29.2235
pair:NA-EU_Da: 28.1099
pop:NA_Ki: 27.7576
pair:BR-EU_FstWC: 27.5125
pair:BR-EU_Da: 27.388
pair:NA-EU_Dj: 27.3324
pop:BR_KoS: 27.283
all_FstWC: 27.0143
pair:BR-EU_Dj: 26.857
all_Dj: 26.1792
pop:BR_Pi: 26.1314
all_KoP: 26.1221
pair:NA-BR_numShP: 25.8116
pop:EU_Ki: 24.254
all_KoS: 22.9512
pop:EU_KoS: 22.1104
pair:NA-EU_numSpd: 21.7152
pop:NA_KoS: 21.6172
pair:BR-EU_numShP: 21.3609
all_Ki: 20.8831
pair:NA-EU_numShP: 20.6033
pop:BR_thetaW: 19.2163
pop:BR_S: 18.742
pair:NA-BR_numSpd: 17.9757
pair:BR-EU_numSpd: 17.5798
all_Ch: 15.2999
pop:NA_Pi: 14.3598
pop:EU_Pi: 12.7379
pop:NA_thetaW: 11.8776
pair:NA-BR_numShA: 11.6952
pop:NA_S: 11.6938
pop:EU_thetaW: 11.5277
pop:EU_S: 11.2009
pair:BR-EU_numShA: 10.9503
pair:NA-EU_numShA: 10.1941
all_Pi: 9.67736
all_thetaW: 9.64939
all_S: 9.42692

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
      0.408298      0.398222      0.102777      0.764722     0.0359459

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 5.082123382032028
                      MSE : 0.024421841071189714
                     NMSE : 0.9761578410628089
Computed from the median taken as point estimate
                     NMAE : 2.1121418915930565
                      MSE : 0.03640640064043756
                     NMSE : 0.2962857551064275
Confidence interval measures
             90% coverage : 0.88         
              Mean 90% CI : 0.5416729007516397
     Mean relative 90% CI : 7.397626676453066
            Median 90% CI : 0.5569171566702426
   Median relative 90% CI : 1.993085025574484

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.7987745017394177
                      MSE : 0.035945894771493195
                     NMSE : 0.1907814553892385

### fit T1 ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: T1
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 3 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

Comp 1: 425.048
all_D: 248.3
all_R2: 153.026
pair:NA-BR_FstWC: 139.52
Comp 3: 106.204
Comp 2: 98.5378
pair:NA-EU_FstWC: 87.1302
pair:BR-EU_Dxy: 86.2375
pair:NA-BR_Dxy: 78.3725
pair:NA-EU_Da: 75.699
pop:NA_D: 56.3647
pop:EU_D: 53.1777
pair:NA-EU_Dj: 43.7565
pop:EU_R2: 30.3077
all_FstWC: 19.5878
pair:NA-EU_Dxy: 12.972
pair:BR-EU_Dj: 12.7481
pair:NA-BR_Da: 12.7244
pop:NA_R2: 12.5683
pair:BR-EU_FstWC: 11.0949
pair:BR-EU_Da: 9.64061
pair:NA-BR_Dj: 8.59833
pair:NA-EU_numSpd: 8.1399
pop:EU_Ch: 7.35071
all_Dj: 6.83791
pop:NA_KoP: 6.72633
all_KoP: 5.81127
pop:BR_D: 5.55791
pop:NA_Hsd: 4.19151
pair:NA-EU_numShP: 3.79976
pop:NA_Pi: 3.79074
all_Hsd: 3.61326
pop:BR_R2: 3.59757
pop:BR_Hsd: 3.40644
pop:EU_Hsd: 3.3851
pop:EU_Pi: 3.37932
pop:NA_Ch: 3.37352
pair:NA-BR_numShP: 3.2717
pop:EU_Ki: 3.02457
NOISE4: 2.96909
NOISE5: 2.965
NOISE1: 2.95402
NOISE2: 2.94885
NOISE3: 2.93589
pop:BR_Ch: 2.9175
pop:EU_KoP: 2.79126
all_Pi: 2.52944
pop:BR_KoP: 2.35091
pop:NA_Ki: 2.33567
pop:BR_Ki: 2.23701
all_thetaW: 2.22088
pop:NA_thetaW: 2.20528
pop:NA_S: 2.14973
all_Ch: 2.14139
pair:NA-BR_numSpd: 2.0179
all_S: 1.91504
pair:BR-EU_numSpd: 1.79272
pop:BR_KoS: 1.76006
all_KoS: 1.66362
pop:EU_thetaW: 1.66356
pair:BR-EU_numShP: 1.61368
pop:NA_KoS: 1.57094
pop:EU_S: 1.55127
pop:EU_KoS: 1.55097
all_Ki: 1.46936
pop:BR_Pi: 1.44999
pair:NA-BR_numShA: 1.25412
pair:BR-EU_numShA: 1.19541
pop:BR_S: 1.16887
pop:BR_thetaW: 1.15462
pair:NA-EU_numShA: 0.795131

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
      0.132438      0.132458     0.0748311      0.192053   0.000285642

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.5286378136539984
                      MSE : 0.0013650009317761349
                     NMSE : 0.011799446811436765
Computed from the median taken as point estimate
                     NMAE : 0.4225820206167463
                      MSE : 0.0025518656521934524
                     NMSE : 0.009608969444584536
Confidence interval measures
             90% coverage : 0.96         
              Mean 90% CI : 0.14306877322428488
     Mean relative 90% CI : 1.7506522171065333
            Median 90% CI : 0.13968590431270145
   Median relative 90% CI : 0.6934861966973904

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.10203351635066246
                      MSE : 0.0002856423566410991
                     NMSE : 0.0021449456153309985

### fit T2 ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: T2
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 12 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

Comp 4: 83.5986
Comp 1: 51.9734
pair:NA-BR_Dj: 40.4821
Comp 2: 29.4442
pair:NA-BR_Da: 26.2665
pair:NA-EU_Dxy: 24.2982
Comp 9: 18.1434
Comp 3: 18.0798
pair:NA-BR_Dxy: 16.9664
Comp 5: 16.3283
pair:BR-EU_Dxy: 12.3862
Comp 11: 11.3329
pair:NA-BR_FstWC: 10.7543
Comp 7: 10.1596
Comp 10: 9.91886
Comp 8: 9.38578
pop:BR_Hsd: 9.25244
pop:BR_Ki: 8.87631
Comp 6: 7.93867
pop:BR_D: 6.48199
pair:BR-EU_Dj: 6.36295
pair:NA-EU_Dj: 6.33061
pair:NA-EU_Da: 5.86786
pair:BR-EU_Da: 5.26167
pop:NA_D: 5.00695
pop:NA_R2: 4.85327
pop:EU_D: 4.78719
Comp 12: 4.65475
pair:BR-EU_FstWC: 4.63925
pop:EU_R2: 4.56632
pop:BR_R2: 4.5496
pop:NA_Hsd: 4.44163
NOISE5: 4.37304
NOISE4: 4.35113
NOISE3: 4.33865
NOISE1: 4.33026
NOISE2: 4.32924
all_D: 4.29497
pair:NA-EU_FstWC: 4.11188
all_Hsd: 4.03795
all_R2: 3.99228
pop:BR_Ch: 3.98984
pop:EU_Hsd: 3.97862
pop:BR_KoP: 3.91608
pop:EU_Ch: 3.72887
pop:EU_KoP: 3.54246
pop:BR_thetaW: 3.49669
all_Dj: 3.49004
pop:BR_Pi: 3.39874
pop:NA_Ch: 3.38962
pop:BR_S: 3.3392
all_FstWC: 3.18187
all_KoP: 3.12212
pop:NA_KoP: 2.97018
pop:NA_Ki: 2.96403
pop:BR_KoS: 2.87579
all_KoS: 2.73822
pair:BR-EU_numShP: 2.61188
pop:EU_KoS: 2.56592
pair:NA-BR_numShP: 2.45695
pop:EU_Ki: 2.45418
pair:NA-BR_numSpd: 2.37189
pop:NA_KoS: 2.23532
pair:NA-EU_numSpd: 2.23272
pair:NA-EU_numShP: 2.15365
all_Ki: 1.97799
pair:BR-EU_numSpd: 1.96898
all_Ch: 1.44727
pop:NA_Pi: 1.26855
pop:EU_Pi: 1.24787
pair:NA-BR_numShA: 1.12601
pop:EU_thetaW: 1.10788
pop:NA_thetaW: 1.10471
pop:NA_S: 1.08954
pop:EU_S: 1.05611
pair:BR-EU_numShA: 1.0364
pair:NA-EU_numShA: 0.978279
all_thetaW: 0.942966
all_S: 0.921638
all_Pi: 0.898555

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
      0.261762       0.26057      0.134002      0.380917    0.00334098

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 2.5647386931318708
                      MSE : 0.0022940644948177187
                     NMSE : 0.16499235565983003
Computed from the median taken as point estimate
                     NMAE : 9.773111636245977
                      MSE : 0.0014239051288527974
                     NMSE : 0.4941092449041463
Confidence interval measures
             90% coverage : 0.96         
              Mean 90% CI : 0.17610682958807714
     Mean relative 90% CI : 22.399301244011507
            Median 90% CI : 0.17531689834263592
   Median relative 90% CI : 1.2962978592558891

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.22769222622450314
                      MSE : 0.003340984637468751
                     NMSE : 0.017403131565794122

### fit m ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: m
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 1 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

all_Hsd: 742.173
Comp 1: 457.25
pop:NA_Hsd: 269.023
pop:EU_Hsd: 146.728
pair:BR-EU_FstWC: 27.9875
pop:BR_Hsd: 24.5312
pop:EU_KoP: 21.6332
all_FstWC: 12.6886
pop:EU_Pi: 11.2562
all_D: 8.9575
pair:BR-EU_Dj: 8.54957
pop:EU_Ki: 8.39484
pair:NA-EU_numShP: 8.083
pop:EU_D: 7.93387
pair:BR-EU_Dxy: 7.87587
all_KoP: 7.41234
pair:NA-EU_FstWC: 7.30663
all_R2: 6.04965
all_Dj: 5.7083
pair:NA-EU_Dxy: 5.44292
pair:BR-EU_Da: 5.25515
pair:NA-BR_FstWC: 5.24722
pair:NA-BR_Dxy: 5.05765
pair:NA-EU_Dj: 4.74566
pair:NA-EU_Da: 4.58814
all_Ch: 4.35126
pop:EU_R2: 4.32934
pop:EU_thetaW: 3.93417
pop:EU_S: 3.64143
pop:NA_KoP: 3.6032
pop:EU_Ch: 3.52126
pair:BR-EU_numShP: 3.34083
pop:NA_D: 3.21159
pair:BR-EU_numSpd: 3.12606
pop:NA_R2: 2.78863
pop:BR_R2: 2.72436
pop:NA_Ki: 2.67132
pop:BR_D: 2.65343
pair:NA-BR_numSpd: 2.6436
pop:NA_Ch: 2.63167
NOISE2: 2.63047
NOISE5: 2.62484
NOISE3: 2.61538
NOISE1: 2.61516
pop:NA_Pi: 2.59236
pair:NA-EU_numSpd: 2.58802
NOISE4: 2.5836
pair:NA-BR_Da: 2.58353
pop:BR_KoP: 2.57222
pop:BR_Ch: 2.55269
pair:NA-BR_Dj: 2.24743
pair:NA-BR_numShP: 2.23633
pop:BR_Ki: 2.11925
all_Ki: 2.08115
pop:BR_KoS: 2.01201
pop:EU_KoS: 1.98167
pair:BR-EU_numShA: 1.94683
all_KoS: 1.82126
pop:NA_KoS: 1.80255
pop:NA_S: 1.65671
pop:NA_thetaW: 1.64831
pop:BR_Pi: 1.58658
all_Pi: 1.43698
pair:NA-EU_numShA: 1.43408
all_thetaW: 1.36695
pair:NA-BR_numShA: 1.35042
pop:BR_thetaW: 1.27871
pop:BR_S: 1.24645
all_S: 1.19366

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
      0.273054      0.276327      0.208416      0.328687   0.000719061

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 1.2012344717396652
                      MSE : 0.001377370376545697
                     NMSE : 0.051835776066549336
Computed from the median taken as point estimate
                     NMAE : 0.21356159524900112
                      MSE : 0.0005810174314607051
                     NMSE : 0.005857909541141635
Confidence interval measures
             90% coverage : 0.98         
              Mean 90% CI : 0.11079217815805106
     Mean relative 90% CI : 1.1992687534362583
            Median 90% CI : 0.10095185748494115
   Median relative 90% CI : 0.7601559122550141

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.0861466482598923
                      MSE : 0.0007190610412532168
                     NMSE : 0.004943420208318205

### fit rho ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: rho
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 13 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

Comp 1: 0.00193237
pop:NA_Ki: 0.000931046
all_KoS: 0.000474483
all_Ki: 0.000462776
pop:NA_KoS: 0.000292086
Comp 3: 0.000228903
Comp 2: 0.000199014
pop:BR_Ki: 0.000198929
pop:EU_KoS: 0.000154819
pop:EU_Ki: 0.000151454
all_KoP: 0.00010853
pop:BR_KoS: 7.11262e-05
Comp 12: 6.37376e-05
pop:NA_Pi: 5.0984e-05
pair:BR-EU_Dj: 4.17786e-05
pop:NA_S: 4.07233e-05
Comp 5: 4.05945e-05
pair:BR-EU_Da: 3.80623e-05
pop:BR_R2: 3.78511e-05
pop:NA_thetaW: 3.67042e-05
Comp 11: 3.14447e-05
pair:BR-EU_Dxy: 2.62224e-05
Comp 4: 2.2696e-05
all_Dj: 2.05903e-05
all_Pi: 2.05297e-05
all_thetaW: 1.78819e-05
pair:NA-BR_numShA: 1.67918e-05
pair:NA-BR_Dxy: 1.51471e-05
all_S: 1.50973e-05
pop:BR_Ch: 1.493e-05
all_Ch: 1.47256e-05
pop:NA_Ch: 1.39027e-05
pair:BR-EU_FstWC: 1.30992e-05
Comp 10: 1.29624e-05
pair:NA-EU_numShA: 1.28006e-05
pop:NA_KoP: 1.25053e-05
all_FstWC: 1.14019e-05
Comp 13: 1.05884e-05
pop:EU_KoP: 1.04773e-05
Comp 9: 1.04018e-05
pair:NA-BR_numSpd: 9.57446e-06
pair:NA-EU_numShP: 9.47141e-06
Comp 6: 9.37447e-06
pair:BR-EU_numShA: 9.11896e-06
pair:NA-BR_Dj: 9.07473e-06
NOISE5: 9.05482e-06
pair:NA-EU_numSpd: 8.89815e-06
NOISE2: 8.83509e-06
pair:NA-BR_Da: 8.83422e-06
NOISE1: 8.81754e-06
NOISE3: 8.81396e-06
NOISE4: 8.80399e-06
pop:NA_R2: 8.79454e-06
pop:BR_Hsd: 8.67059e-06
all_R2: 8.62783e-06
Comp 7: 8.5402e-06
pair:NA-EU_Dxy: 8.51099e-06
pop:BR_KoP: 8.43885e-06
pop:BR_D: 8.34264e-06
pair:BR-EU_numShP: 8.18303e-06
pop:NA_D: 8.12356e-06
pop:EU_Ch: 8.10702e-06
pair:NA-EU_FstWC: 8.10489e-06
all_D: 8.10121e-06
pair:BR-EU_numSpd: 7.94114e-06
pop:EU_Pi: 7.9189e-06
pair:NA-BR_FstWC: 7.91467e-06
Comp 8: 7.86919e-06
pop:NA_Hsd: 7.81724e-06
pop:EU_R2: 7.58356e-06
pair:NA-EU_Da: 7.57745e-06
pop:EU_thetaW: 7.54989e-06
pop:EU_D: 7.39637e-06
pop:BR_thetaW: 7.33962e-06
pop:BR_Pi: 7.23722e-06
pop:EU_Hsd: 7.07837e-06
pair:NA-EU_Dj: 7.06308e-06
pair:NA-BR_numShP: 7.03285e-06
all_Hsd: 6.8749e-06
pop:EU_S: 6.66587e-06
pop:BR_S: 6.60099e-06

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
   0.000329319   0.000317009    0.00019479   0.000494441   1.62065e-09

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.5224804597382328
                      MSE : 4.853277226090326e-09
                     NMSE : 3.214527784269063e-05
Computed from the median taken as point estimate
                     NMAE : 0.46559426860836856
                      MSE : 4.573511357887297e-09
                     NMSE : 2.3348273006263176e-05
Confidence interval measures
             90% coverage : 0.92         
              Mean 90% CI : 0.00025177778101235484
     Mean relative 90% CI : 2.6646466630546564
            Median 90% CI : 0.00023095642214120542
   Median relative 90% CI : 1.5824190908486941

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.10954617919202923
                      MSE : 1.6206508170470392e-09
                     NMSE : 5.847140190223389e-06

### fit theta ###

# estimparam_out.settings #

Parameter estimation analyses proceeded using: 
- Parameter name: theta
- Scenario 3
- 500000 simulated datasets
- 500 trees
- Minimum node size of 5
- 63 summary statistics
- 0 axes of summary statistics PLS linear combination
- 5 noise variables
- 50 out-of-band samples used as test

# estimparam_out.importance #

pop:NA_Pi: 0.00201335
pop:NA_thetaW: 0.00134921
pop:NA_S: 0.00112421
pair:NA-BR_numShA: 0.000549256
pop:NA_KoP: 0.000361143
all_Ch: 0.000327834
all_Pi: 0.000184676
pop:NA_KoS: 7.67577e-05
pair:NA-EU_numShA: 6.50206e-05
all_thetaW: 4.44306e-05
pop:NA_Ch: 4.0738e-05
all_S: 2.26012e-05
pair:BR-EU_numShA: 1.32796e-05
pop:NA_D: 1.13809e-05
pop:BR_KoP: 9.86525e-06
pop:NA_R2: 8.39733e-06
pop:EU_Ch: 3.75885e-06
pop:BR_KoS: 3.37112e-06
pop:NA_Ki: 2.54313e-06
pair:NA-EU_FstWC: 1.87943e-06
pair:NA-EU_Da: 1.84191e-06
pair:NA-EU_Dj: 1.67229e-06
pop:EU_KoS: 1.44591e-06
all_FstWC: 8.86234e-07
pair:NA-EU_numShP: 6.77279e-07
pair:NA-EU_Dxy: 6.01657e-07
pair:NA-EU_numSpd: 5.83784e-07
pair:BR-EU_FstWC: 5.77282e-07
all_D: 4.66129e-07
all_Dj: 4.54312e-07
pop:EU_Pi: 4.2892e-07
pair:BR-EU_Da: 4.0639e-07
pop:EU_D: 3.86238e-07
all_R2: 3.82392e-07
pop:BR_Ch: 3.68799e-07
pair:BR-EU_Dj: 3.58463e-07
NOISE3: 3.5544e-07
NOISE4: 3.53285e-07
NOISE1: 3.52295e-07
pop:EU_KoP: 3.51129e-07
NOISE5: 3.50615e-07
NOISE2: 3.48908e-07
pair:NA-BR_numSpd: 3.44241e-07
pair:NA-BR_Dxy: 3.38482e-07
pop:BR_R2: 3.38277e-07
pop:BR_Pi: 3.35261e-07
pop:EU_R2: 3.31187e-07
pop:BR_D: 3.14391e-07
pair:BR-EU_Dxy: 3.10913e-07
all_KoP: 3.09976e-07
pop:BR_Hsd: 2.99608e-07
all_Hsd: 2.98469e-07
all_KoS: 2.9265e-07
pop:NA_Hsd: 2.8898e-07
pair:BR-EU_numSpd: 2.86785e-07
pop:EU_Hsd: 2.78714e-07
all_Ki: 2.70483e-07
pop:BR_thetaW: 2.54576e-07
pair:NA-BR_Da: 2.46809e-07
pop:BR_Ki: 2.46748e-07
pair:NA-BR_numShP: 2.38462e-07
pair:BR-EU_numShP: 2.35926e-07
pair:NA-BR_Dj: 2.34585e-07
pair:NA-BR_FstWC: 2.153e-07
pop:EU_Ki: 2.04546e-07
pop:BR_S: 2.03722e-07
pop:EU_S: 1.92085e-07
pop:EU_thetaW: 1.81756e-07

# estimparam_out.predictions #

Parameter estimation (point estimates)
   Expectation        Median Quantile_0.05 Quantile_0.95      Variance
   0.000446071   0.000450053    0.00038664   0.000491492   5.00037e-10

# estimparam_out.oobstats #

Global (prior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.05037452249929035
                      MSE : 1.8239266342721784e-10
                     NMSE : 4.7178231366366935e-07
Computed from the median taken as point estimate
                     NMAE : 0.03930188657923728
                      MSE : 2.0405260421391657e-10
                     NMSE : 4.578561778600079e-07
Confidence interval measures
             90% coverage : 0.92         
              Mean 90% CI : 3.997747479385584e-05
     Mean relative 90% CI : 0.21896957132394923
            Median 90% CI : 2.3984567226186674e-05
   Median relative 90% CI : 0.20204292489337305

Local (posterior) errors
Computed from the mean taken as point estimate
                     NMAE : 0.03965802183091458
                      MSE : 5.000373688851874e-10
                     NMSE : 1.1905354574824923e-06
Computed from the median taken as point estimate
                     NMAE : 0.005287115574430857
                      MSE : 7.0458489852555174e-12
                     NMSE : 1.403412916670601e-08

### model choice table ###

max simulations model
         100000 M33
         200000 M35
         300000 M35
         400000 M33
         500000 M33

### parameter estimation table ###

parameter	expectation	media	Q_0.05	Q_0.95	variance
M_BR_EU	0.43640773875877603	0.4288653564453125	0.14955220937728883	0.7217051219940186	0.028255438526334012
M_BR_NA	0.3314303603574691	0.3198919004864163	0.06668141186237334	0.6182393153508504	0.021645942450216202
M_EU_BR	0.42287858298294223	0.41897414207458494	0.14366102814674375	0.7232841658592224	0.027987809486749914
M_EU_NA	0.47417372050054984	0.4787638491597669	0.19201016863187154	0.7615889617374965	0.03032939705939895
M_NA_BR	0.4667773216924513	0.4632644116878508	0.1682548626263936	0.7516638278961182	0.03974423170509334
M_NA_EU	0.3742208917077972	0.36841864824295045	0.07894474655389784	0.6835435557365416	0.02814990430576772
N_BR	1.592797327948393	1.5507527962327006	0.7325900197029114	2.585169689995902	0.2896780878485286
N_EU	2.575939011237027	2.59080749352773	1.4902669191360474	3.790011803309123	0.5733743947448259
S1	0.6280394688707593	0.6263220429420471	0.33503338664770127	0.9038246154785157	0.029828388381150515
S2	0.4082976726904005	0.39822188615798954	0.102776872832328	0.7647220439910888	0.035945894771493195
T1	0.13243766552460323	0.13245780989527703	0.0748311263819535	0.19205291668574012	0.0002856423566410991
T2	0.2617619535410401	0.26057038894598034	0.13400214612483977	0.3809173831343651	0.003340984637468751
m	0.2730535136782133	0.27632716496785475	0.20841626644134514	0.3286865496635437	0.0007190610412532168
rho	0.0003293190870862687	0.00031700863386783997	0.00019478988212684	0.00049444141867302	1.6206508170470392e-09
theta	0.0004460707698914673	0.00045005252538449626	0.0003866399033565	0.00049149235133116	5.000373688851874e-10
finished
