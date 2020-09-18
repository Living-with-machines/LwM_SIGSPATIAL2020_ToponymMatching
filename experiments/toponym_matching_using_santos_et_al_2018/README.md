# Table 1, SIGSPATIAL paper

Here, we summarize the log files generated while training/evaluating the `Santos et al.` model on the following datasets:
 
- [Santos](#santos)
- [WG:en](#wg:en)
- [WG:es](#wg:es)
- [WG:el](#wg:el)
- [OCR](#ocr)

Refer to Table 1 in the following paper:

```
Coll Ardanuy, M., Hosseini, K., McDonough, K., Krause, A., van Strien, D. and Nanni, F. (2020): A Deep Learning Approach to Geographical Candidate Selection through Toponym Matching, SIGSPATIAL: Poster Paper.
```

## Santos

```bash
Using TensorFlow backend.
Reading dataset... 0.0
Dataset read... 30.9851651192
Temporary files created... 538.050458193
Training classifiers...
Train on 1951851 samples, validate on 1951851 samples
Epoch 1/20
2020-09-17 18:09:04.965844: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
1951840/1951851 [============================>.] - ETA: 0s - loss: 0.3887 - acc: 0.8309Epoch 00000: val_loss improved from inf to 0.36744, saving model to checkpoint1.hdf5
1951851/1951851 [==============================] - 8346s - loss: 0.3887 - acc: 0.8309 - val_loss: 0.3674 - val_acc: 0.8430
Epoch 2/20
1951840/1951851 [============================>.] - ETA: 0s - loss: 0.4034 - acc: 0.8238Epoch 00001: val_loss did not improve
1951851/1951851 [==============================] - 8214s - loss: 0.4034 - acc: 0.8238 - val_loss: 0.3691 - val_acc: 0.8421
Epoch 00001: early stopping
1951840/1951851 [============================>.] - ETA: 0sTrain on 1951851 samples, validate on 1951851 samples
Epoch 1/20
1951840/1951851 [============================>.] - ETA: 0s - loss: 0.3728 - acc: 0.8398Epoch 00000: val_loss improved from inf to 0.32898, saving model to checkpoint2.hdf5
1951851/1951851 [==============================] - 8737s - loss: 0.3728 - acc: 0.8398 - val_loss: 0.3290 - val_acc: 0.8647
Epoch 2/20
1951840/1951851 [============================>.] - ETA: 0s - loss: 0.3500 - acc: 0.8536Epoch 00001: val_loss did not improve
1951851/1951851 [==============================] - 8220s - loss: 0.3500 - acc: 0.8536 - val_loss: 0.5274 - val_acc: 0.7426
Epoch 3/20
1951840/1951851 [============================>.] - ETA: 0s - loss: 0.4802 - acc: 0.7782Epoch 00002: val_loss did not improve
1951851/1951851 [==============================] - 8240s - loss: 0.4802 - acc: 0.7782 - val_loss: 0.4642 - val_acc: 0.7866
Epoch 00002: early stopping
1951840/1951851 [============================>.] - ETA: 0sMatching records...
Metric = Deep Neural Net Classifier : GRU
Bidirectional : True
Accuracy = 0.814343666602
Precision = 0.804832994493
Recall = 0.829943474169
F1 = 0.817195383442
Processing time per 50K records = 48.7630910966
Number of training instances = 1951851
```

## WG:en

```bash
Using TensorFlow backend.
Reading dataset... 0.0
Dataset read... 5.14361977577
Temporary files created... 13.8563718796
Training classifiers...
Train on 301219 samples, validate on 301219 samples
Epoch 1/20
2020-09-17 17:41:59.280300: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
301216/301219 [============================>.] - ETA: 0s - loss: 0.3104 - acc: 0.8613Epoch 00000: val_loss improved from inf to 0.23552, saving model to checkpoint1.hdf5
301219/301219 [==============================] - 1194s - loss: 0.3104 - acc: 0.8613 - val_loss: 0.2355 - val_acc: 0.9007
Epoch 2/20
301216/301219 [============================>.] - ETA: 0s - loss: 0.2210 - acc: 0.9073Epoch 00001: val_loss improved from 0.23552 to 0.22929, saving model to checkpoint1.hdf5
301219/301219 [==============================] - 1183s - loss: 0.2210 - acc: 0.9073 - val_loss: 0.2293 - val_acc: 0.9025
Epoch 3/20
301216/301219 [============================>.] - ETA: 0s - loss: 0.2176 - acc: 0.9078Epoch 00002: val_loss improved from 0.22929 to 0.20798, saving model to checkpoint1.hdf5
301219/301219 [==============================] - 1181s - loss: 0.2176 - acc: 0.9078 - val_loss: 0.2080 - val_acc: 0.9124
Epoch 4/20
301216/301219 [============================>.] - ETA: 0s - loss: 0.2016 - acc: 0.9156Epoch 00003: val_loss did not improve
301219/301219 [==============================] - 1135s - loss: 0.2016 - acc: 0.9156 - val_loss: 0.2161 - val_acc: 0.9078
Epoch 5/20
301216/301219 [============================>.] - ETA: 0s - loss: 0.2124 - acc: 0.9101Epoch 00004: val_loss improved from 0.20798 to 0.20244, saving model to checkpoint1.hdf5
301219/301219 [==============================] - 1122s - loss: 0.2124 - acc: 0.9101 - val_loss: 0.2024 - val_acc: 0.9145
Epoch 00004: early stopping
301216/301219 [============================>.] - ETA: 0sTrain on 301219 samples, validate on 301219 samples
Epoch 1/20
301216/301219 [============================>.] - ETA: 0s - loss: 0.3073 - acc: 0.8644Epoch 00000: val_loss improved from inf to 0.22685, saving model to checkpoint2.hdf5
301219/301219 [==============================] - 1137s - loss: 0.3073 - acc: 0.8644 - val_loss: 0.2268 - val_acc: 0.9038
Epoch 2/20
301216/301219 [============================>.] - ETA: 0s - loss: 0.2147 - acc: 0.9102Epoch 00001: val_loss improved from 0.22685 to 0.19832, saving model to checkpoint2.hdf5
301219/301219 [==============================] - 1138s - loss: 0.2147 - acc: 0.9102 - val_loss: 0.1983 - val_acc: 0.9156
Epoch 3/20
301216/301219 [============================>.] - ETA: 0s - loss: 0.1921 - acc: 0.9199Epoch 00002: val_loss improved from 0.19832 to 0.19119, saving model to checkpoint2.hdf5
301219/301219 [==============================] - 1138s - loss: 0.1921 - acc: 0.9199 - val_loss: 0.1912 - val_acc: 0.9201
Epoch 4/20
301216/301219 [============================>.] - ETA: 0s - loss: 0.1963 - acc: 0.9179Epoch 00003: val_loss improved from 0.19119 to 0.17931, saving model to checkpoint2.hdf5
301219/301219 [==============================] - 1139s - loss: 0.1963 - acc: 0.9179 - val_loss: 0.1793 - val_acc: 0.9252
Epoch 00003: early stopping
301216/301219 [============================>.] - ETA: 0sMatching records...
Metric = Deep Neural Net Classifier : GRU
Bidirectional : True
Accuracy = 0.919822454759
Precision = 0.933283309521
Recall = 0.904288906078
F1 = 0.91855736157
Processing time per 50K records = 44.7421714817
Number of training instances = 301219
```

## WG:es

```bash
Using TensorFlow backend.
Reading dataset... 0.0
Dataset read... 1.17112994194
Temporary files created... 2.96136593819
Training classifiers...
Train on 68412 samples, validate on 68412 samples
Epoch 1/20
2020-09-17 21:02:42.621943: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
68384/68412 [============================>.] - ETA: 0s - loss: 0.4401 - acc: 0.7918Epoch 00000: val_loss improved from inf to 0.34313, saving model to checkpoint1.hdf5
68412/68412 [==============================] - 265s - loss: 0.4401 - acc: 0.7918 - val_loss: 0.3431 - val_acc: 0.8495
Epoch 2/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.3020 - acc: 0.8690Epoch 00001: val_loss improved from 0.34313 to 0.26643, saving model to checkpoint1.hdf5
68412/68412 [==============================] - 260s - loss: 0.3020 - acc: 0.8690 - val_loss: 0.2664 - val_acc: 0.8880
Epoch 3/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.2456 - acc: 0.8965Epoch 00002: val_loss improved from 0.26643 to 0.23497, saving model to checkpoint1.hdf5
68412/68412 [==============================] - 260s - loss: 0.2456 - acc: 0.8965 - val_loss: 0.2350 - val_acc: 0.9026
Epoch 4/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.2182 - acc: 0.9080Epoch 00003: val_loss improved from 0.23497 to 0.23143, saving model to checkpoint1.hdf5
68412/68412 [==============================] - 260s - loss: 0.2183 - acc: 0.9080 - val_loss: 0.2314 - val_acc: 0.9043
Epoch 5/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1959 - acc: 0.9169Epoch 00004: val_loss improved from 0.23143 to 0.21880, saving model to checkpoint1.hdf5
68412/68412 [==============================] - 260s - loss: 0.1960 - acc: 0.9169 - val_loss: 0.2188 - val_acc: 0.9106
Epoch 6/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1770 - acc: 0.9252Epoch 00005: val_loss improved from 0.21880 to 0.21802, saving model to checkpoint1.hdf5
68412/68412 [==============================] - 260s - loss: 0.1771 - acc: 0.9252 - val_loss: 0.2180 - val_acc: 0.9101
Epoch 7/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1621 - acc: 0.9331Epoch 00006: val_loss improved from 0.21802 to 0.21749, saving model to checkpoint1.hdf5
68412/68412 [==============================] - 262s - loss: 0.1621 - acc: 0.9331 - val_loss: 0.2175 - val_acc: 0.9108
Epoch 8/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1470 - acc: 0.9387Epoch 00007: val_loss improved from 0.21749 to 0.21370, saving model to checkpoint1.hdf5
68412/68412 [==============================] - 261s - loss: 0.1469 - acc: 0.9387 - val_loss: 0.2137 - val_acc: 0.9149
Epoch 9/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1369 - acc: 0.9444Epoch 00008: val_loss did not improve
68412/68412 [==============================] - 260s - loss: 0.1369 - acc: 0.9444 - val_loss: 0.2203 - val_acc: 0.9150
Epoch 10/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1249 - acc: 0.9500Epoch 00009: val_loss did not improve
68412/68412 [==============================] - 259s - loss: 0.1249 - acc: 0.9500 - val_loss: 0.2266 - val_acc: 0.9149
Epoch 11/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1167 - acc: 0.9534Epoch 00010: val_loss did not improve
68412/68412 [==============================] - 259s - loss: 0.1167 - acc: 0.9534 - val_loss: 0.2306 - val_acc: 0.9174
Epoch 12/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1097 - acc: 0.9562Epoch 00011: val_loss did not improve
68412/68412 [==============================] - 259s - loss: 0.1097 - acc: 0.9562 - val_loss: 0.2374 - val_acc: 0.9158
Epoch 13/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1033 - acc: 0.9588Epoch 00012: val_loss did not improve
68412/68412 [==============================] - 260s - loss: 0.1033 - acc: 0.9587 - val_loss: 0.2405 - val_acc: 0.9154
Epoch 14/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.0968 - acc: 0.9617Epoch 00013: val_loss did not improve
68412/68412 [==============================] - 259s - loss: 0.0968 - acc: 0.9617 - val_loss: 0.2668 - val_acc: 0.9109
Epoch 15/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.0931 - acc: 0.9632Epoch 00014: val_loss did not improve
68412/68412 [==============================] - 260s - loss: 0.0932 - acc: 0.9631 - val_loss: 0.2558 - val_acc: 0.9160
Epoch 16/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.0864 - acc: 0.9666Epoch 00015: val_loss did not improve
68412/68412 [==============================] - 259s - loss: 0.0864 - acc: 0.9666 - val_loss: 0.2583 - val_acc: 0.9116
Epoch 17/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.0902 - acc: 0.9639Epoch 00016: val_loss did not improve
68412/68412 [==============================] - 259s - loss: 0.0902 - acc: 0.9639 - val_loss: 0.2628 - val_acc: 0.9151
Epoch 00016: early stopping
68412/68412 [==============================] - 59s      
Train on 68412 samples, validate on 68412 samples
Epoch 1/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.4416 - acc: 0.7869Epoch 00000: val_loss improved from inf to 0.32712, saving model to checkpoint2.hdf5
68412/68412 [==============================] - 264s - loss: 0.4416 - acc: 0.7870 - val_loss: 0.3271 - val_acc: 0.8549
Epoch 2/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.2818 - acc: 0.8797Epoch 00001: val_loss improved from 0.32712 to 0.25187, saving model to checkpoint2.hdf5
68412/68412 [==============================] - 260s - loss: 0.2817 - acc: 0.8798 - val_loss: 0.2519 - val_acc: 0.8927
Epoch 3/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.2303 - acc: 0.9039Epoch 00002: val_loss improved from 0.25187 to 0.23111, saving model to checkpoint2.hdf5
68412/68412 [==============================] - 261s - loss: 0.2303 - acc: 0.9039 - val_loss: 0.2311 - val_acc: 0.9024
Epoch 4/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.2020 - acc: 0.9167Epoch 00003: val_loss improved from 0.23111 to 0.21852, saving model to checkpoint2.hdf5
68412/68412 [==============================] - 261s - loss: 0.2020 - acc: 0.9167 - val_loss: 0.2185 - val_acc: 0.9094
Epoch 5/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1815 - acc: 0.9260Epoch 00004: val_loss improved from 0.21852 to 0.21191, saving model to checkpoint2.hdf5
68412/68412 [==============================] - 261s - loss: 0.1815 - acc: 0.9260 - val_loss: 0.2119 - val_acc: 0.9124
Epoch 6/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1661 - acc: 0.9326Epoch 00005: val_loss improved from 0.21191 to 0.21105, saving model to checkpoint2.hdf5
68412/68412 [==============================] - 261s - loss: 0.1662 - acc: 0.9326 - val_loss: 0.2110 - val_acc: 0.9141
Epoch 7/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1503 - acc: 0.9394Epoch 00006: val_loss improved from 0.21105 to 0.20923, saving model to checkpoint2.hdf5
68412/68412 [==============================] - 260s - loss: 0.1503 - acc: 0.9394 - val_loss: 0.2092 - val_acc: 0.9160
Epoch 8/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1361 - acc: 0.9460Epoch 00007: val_loss did not improve
68412/68412 [==============================] - 260s - loss: 0.1360 - acc: 0.9460 - val_loss: 0.2110 - val_acc: 0.9145
Epoch 9/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1235 - acc: 0.9511Epoch 00008: val_loss did not improve
68412/68412 [==============================] - 260s - loss: 0.1234 - acc: 0.9511 - val_loss: 0.2330 - val_acc: 0.9162
Epoch 10/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1142 - acc: 0.9543Epoch 00009: val_loss did not improve
68412/68412 [==============================] - 260s - loss: 0.1142 - acc: 0.9542 - val_loss: 0.2178 - val_acc: 0.9185
Epoch 11/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1040 - acc: 0.9590Epoch 00010: val_loss did not improve
68412/68412 [==============================] - 260s - loss: 0.1040 - acc: 0.9590 - val_loss: 0.2310 - val_acc: 0.9164
Epoch 12/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1001 - acc: 0.9604Epoch 00011: val_loss did not improve
68412/68412 [==============================] - 260s - loss: 0.1002 - acc: 0.9604 - val_loss: 0.2216 - val_acc: 0.9180
Epoch 13/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.0959 - acc: 0.9626Epoch 00012: val_loss did not improve
68412/68412 [==============================] - 260s - loss: 0.0959 - acc: 0.9626 - val_loss: 0.2261 - val_acc: 0.9202
Epoch 14/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.0928 - acc: 0.9638Epoch 00013: val_loss did not improve
68412/68412 [==============================] - 260s - loss: 0.0927 - acc: 0.9639 - val_loss: 0.2471 - val_acc: 0.9157
Epoch 15/20
68384/68412 [============================>.] - ETA: 0s - loss: 0.1282 - acc: 0.9494Epoch 00014: val_loss did not improve
68412/68412 [==============================] - 260s - loss: 0.1282 - acc: 0.9494 - val_loss: 0.2592 - val_acc: 0.8938
Epoch 00014: early stopping
68384/68412 [============================>.] - ETA: 0sMatching records...
Metric = Deep Neural Net Classifier : GRU
Bidirectional : True
Accuracy = 0.904468514296
Precision = 0.908571428571
Recall = 0.899447465357
F1 = 0.903986425439
Processing time per 50K records = 43.3198854546
Number of training instances = 68412
```


## WG:el

```bash
Using TensorFlow backend.
Reading dataset... 0.0
Dataset read... 0.0259101390839
Temporary files created... 0.0687000751495
Training classifiers...
Train on 1389 samples, validate on 1389 samples
Epoch 1/20
2020-09-17 17:34:25.659858: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
1376/1389 [============================>.] - ETA: 0s - loss: 0.6626 - acc: 0.6185Epoch 00000: val_loss improved from inf to 0.58071, saving model to checkpoint1.hdf5
1389/1389 [==============================] - 7s - loss: 0.6604 - acc: 0.6199 - val_loss: 0.5807 - val_acc: 0.7329
Epoch 2/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.5595 - acc: 0.7427Epoch 00001: val_loss improved from 0.58071 to 0.57824, saving model to checkpoint1.hdf5
1389/1389 [==============================] - 5s - loss: 0.5603 - acc: 0.7408 - val_loss: 0.5782 - val_acc: 0.7286
Epoch 3/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.5422 - acc: 0.7587Epoch 00002: val_loss did not improve
1389/1389 [==============================] - 5s - loss: 0.5394 - acc: 0.7610 - val_loss: 0.5882 - val_acc: 0.7214
Epoch 4/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.5102 - acc: 0.7624Epoch 00003: val_loss improved from 0.57824 to 0.53378, saving model to checkpoint1.hdf5
1389/1389 [==============================] - 5s - loss: 0.5098 - acc: 0.7631 - val_loss: 0.5338 - val_acc: 0.7387
Epoch 5/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.4585 - acc: 0.7936Epoch 00004: val_loss improved from 0.53378 to 0.50780, saving model to checkpoint1.hdf5
1389/1389 [==============================] - 5s - loss: 0.4602 - acc: 0.7934 - val_loss: 0.5078 - val_acc: 0.7689
Epoch 6/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.4202 - acc: 0.8183Epoch 00005: val_loss improved from 0.50780 to 0.47991, saving model to checkpoint1.hdf5
1389/1389 [==============================] - 5s - loss: 0.4213 - acc: 0.8164 - val_loss: 0.4799 - val_acc: 0.7862
Epoch 7/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.4007 - acc: 0.8336Epoch 00006: val_loss improved from 0.47991 to 0.47789, saving model to checkpoint1.hdf5
1389/1389 [==============================] - 5s - loss: 0.4019 - acc: 0.8330 - val_loss: 0.4779 - val_acc: 0.7862
Epoch 8/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.3749 - acc: 0.8416Epoch 00007: val_loss did not improve
1389/1389 [==============================] - 5s - loss: 0.3751 - acc: 0.8416 - val_loss: 0.4810 - val_acc: 0.7725
Epoch 9/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.3481 - acc: 0.8467Epoch 00008: val_loss improved from 0.47789 to 0.42072, saving model to checkpoint1.hdf5
1389/1389 [==============================] - 5s - loss: 0.3464 - acc: 0.8474 - val_loss: 0.4207 - val_acc: 0.8042
Epoch 10/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.3073 - acc: 0.8714Epoch 00009: val_loss did not improve
1389/1389 [==============================] - 5s - loss: 0.3079 - acc: 0.8704 - val_loss: 0.4407 - val_acc: 0.7941
Epoch 11/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.2818 - acc: 0.8801Epoch 00010: val_loss did not improve
1389/1389 [==============================] - 5s - loss: 0.2830 - acc: 0.8798 - val_loss: 0.4564 - val_acc: 0.8092
Epoch 12/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.2851 - acc: 0.8757Epoch 00011: val_loss did not improve
1389/1389 [==============================] - 5s - loss: 0.2850 - acc: 0.8762 - val_loss: 0.4577 - val_acc: 0.7984
Epoch 00011: early stopping
1376/1389 [============================>.] - ETA: 0sTrain on 1389 samples, validate on 1389 samples
Epoch 1/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.6537 - acc: 0.6279Epoch 00000: val_loss improved from inf to 0.57491, saving model to checkpoint2.hdf5
1389/1389 [==============================] - 8s - loss: 0.6550 - acc: 0.6271 - val_loss: 0.5749 - val_acc: 0.7423
Epoch 2/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.5899 - acc: 0.7435Epoch 00001: val_loss improved from 0.57491 to 0.53959, saving model to checkpoint2.hdf5
1389/1389 [==============================] - 5s - loss: 0.5901 - acc: 0.7430 - val_loss: 0.5396 - val_acc: 0.7487
Epoch 3/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.5427 - acc: 0.7573Epoch 00002: val_loss did not improve
1389/1389 [==============================] - 5s - loss: 0.5430 - acc: 0.7567 - val_loss: 0.5598 - val_acc: 0.7358
Epoch 4/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.5038 - acc: 0.7733Epoch 00003: val_loss did not improve
1389/1389 [==============================] - 5s - loss: 0.5038 - acc: 0.7725 - val_loss: 0.5824 - val_acc: 0.7430
Epoch 5/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.4659 - acc: 0.8052Epoch 00004: val_loss did not improve
1389/1389 [==============================] - 5s - loss: 0.4651 - acc: 0.8049 - val_loss: 0.5831 - val_acc: 0.7689
Epoch 6/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.4360 - acc: 0.8132Epoch 00005: val_loss improved from 0.53959 to 0.45812, saving model to checkpoint2.hdf5
1389/1389 [==============================] - 5s - loss: 0.4376 - acc: 0.8128 - val_loss: 0.4581 - val_acc: 0.7970
Epoch 7/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.3901 - acc: 0.8365Epoch 00006: val_loss did not improve
1389/1389 [==============================] - 5s - loss: 0.3897 - acc: 0.8373 - val_loss: 0.4960 - val_acc: 0.7855
Epoch 8/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.3851 - acc: 0.8394Epoch 00007: val_loss improved from 0.45812 to 0.43341, saving model to checkpoint2.hdf5
1389/1389 [==============================] - 5s - loss: 0.3843 - acc: 0.8395 - val_loss: 0.4334 - val_acc: 0.8157
Epoch 9/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.3648 - acc: 0.8423Epoch 00008: val_loss did not improve
1389/1389 [==============================] - 5s - loss: 0.3641 - acc: 0.8431 - val_loss: 0.4612 - val_acc: 0.7955
Epoch 10/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.3328 - acc: 0.8561Epoch 00009: val_loss did not improve
1389/1389 [==============================] - 5s - loss: 0.3323 - acc: 0.8560 - val_loss: 0.4636 - val_acc: 0.7984
Epoch 11/20
1376/1389 [============================>.] - ETA: 0s - loss: 0.3350 - acc: 0.8561Epoch 00010: val_loss did not improve
1389/1389 [==============================] - 5s - loss: 0.3341 - acc: 0.8567 - val_loss: 0.4397 - val_acc: 0.8020
Epoch 00010: early stopping
1376/1389 [============================>.] - ETA: 0sMatching records...
Metric = Deep Neural Net Classifier : GRU
Bidirectional : True
Accuracy = 0.800215982721
Precision = 0.810267857143
Recall = 0.784017278618
F1 = 0.796926454446
Processing time per 50K records = 57.1980031812
Number of training instances = 1389
```


## OCR

```bash
Using TensorFlow backend.Reading dataset... 0.0
Dataset read... 0.610898971558
Temporary files created... 1.59253811836
Training classifiers...
Train on 37029 samples, validate on 37029 samples
Epoch 1/20
2020-09-17 15:20:56.094936: I tensorflow/core/platform/cpu_feature_guard.cc:137] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
37024/37029 [============================>.] - ETA: 0s - loss: 0.3414 - acc: 0.8542Epoch 00000: val_loss improved from inf to 0.21811, saving model to checkpoint1.hdf5
37029/37029 [==============================] - 236s - loss: 0.3413 - acc: 0.8542 - val_loss: 0.2181 - val_acc: 0.9231
Epoch 2/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.1947 - acc: 0.9303Epoch 00001: val_loss improved from 0.21811 to 0.19120, saving model to checkpoint1.hdf5
37029/37029 [==============================] - 233s - loss: 0.1947 - acc: 0.9304 - val_loss: 0.1912 - val_acc: 0.9338
Epoch 3/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.1645 - acc: 0.9415Epoch 00002: val_loss improved from 0.19120 to 0.16638, saving model to checkpoint1.hdf5
37029/37029 [==============================] - 233s - loss: 0.1645 - acc: 0.9415 - val_loss: 0.1664 - val_acc: 0.9410
Epoch 4/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.1467 - acc: 0.9476Epoch 00003: val_loss improved from 0.16638 to 0.15190, saving model to checkpoint1.hdf5
37029/37029 [==============================] - 233s - loss: 0.1467 - acc: 0.9476 - val_loss: 0.1519 - val_acc: 0.9466
Epoch 5/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.1337 - acc: 0.9529Epoch 00004: val_loss improved from 0.15190 to 0.15039, saving model to checkpoint1.hdf5
37029/37029 [==============================] - 228s - loss: 0.1337 - acc: 0.9529 - val_loss: 0.1504 - val_acc: 0.9453
Epoch 6/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.1217 - acc: 0.9569Epoch 00005: val_loss did not improve
37029/37029 [==============================] - 233s - loss: 0.1217 - acc: 0.9570 - val_loss: 0.1597 - val_acc: 0.9402
Epoch 7/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.1121 - acc: 0.9613Epoch 00006: val_loss improved from 0.15039 to 0.13603, saving model to checkpoint1.hdf5
37029/37029 [==============================] - 231s - loss: 0.1120 - acc: 0.9613 - val_loss: 0.1360 - val_acc: 0.9527
Epoch 8/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.1023 - acc: 0.9652Epoch 00007: val_loss did not improve
37029/37029 [==============================] - 233s - loss: 0.1023 - acc: 0.9652 - val_loss: 0.1400 - val_acc: 0.9531
Epoch 9/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0938 - acc: 0.9666Epoch 00008: val_loss did not improve
37029/37029 [==============================] - 232s - loss: 0.0938 - acc: 0.9666 - val_loss: 0.1411 - val_acc: 0.9519
Epoch 10/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0822 - acc: 0.9716Epoch 00009: val_loss did not improve
37029/37029 [==============================] - 233s - loss: 0.0822 - acc: 0.9716 - val_loss: 0.1427 - val_acc: 0.9541
Epoch 11/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0808 - acc: 0.9722Epoch 00010: val_loss improved from 0.13603 to 0.13107, saving model to checkpoint1.hdf5
37029/37029 [==============================] - 233s - loss: 0.0808 - acc: 0.9722 - val_loss: 0.1311 - val_acc: 0.9569
Epoch 12/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0670 - acc: 0.9767Epoch 00011: val_loss did not improve
37029/37029 [==============================] - 233s - loss: 0.0670 - acc: 0.9767 - val_loss: 0.1556 - val_acc: 0.9497
Epoch 13/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0631 - acc: 0.9782Epoch 00012: val_loss did not improve
37029/37029 [==============================] - 232s - loss: 0.0631 - acc: 0.9782 - val_loss: 0.1500 - val_acc: 0.9558
Epoch 14/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0579 - acc: 0.9801Epoch 00013: val_loss did not improve
37029/37029 [==============================] - 232s - loss: 0.0579 - acc: 0.9801 - val_loss: 0.1472 - val_acc: 0.9535
Epoch 15/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0531 - acc: 0.9820Epoch 00014: val_loss did not improve
37029/37029 [==============================] - 233s - loss: 0.0531 - acc: 0.9820 - val_loss: 0.1630 - val_acc: 0.9538
Epoch 16/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0599 - acc: 0.9796Epoch 00015: val_loss did not improve
37029/37029 [==============================] - 232s - loss: 0.0599 - acc: 0.9796 - val_loss: 0.1619 - val_acc: 0.9458
Epoch 00015: early stopping
37029/37029 [==============================] - 52s      
Train on 37029 samples, validate on 37029 samples
Epoch 1/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.3411 - acc: 0.8543Epoch 00000: val_loss improved from inf to 0.22114, saving model to checkpoint2.hdf5
37029/37029 [==============================] - 237s - loss: 0.3411 - acc: 0.8543 - val_loss: 0.2211 - val_acc: 0.9164Epoch 2/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.2003 - acc: 0.9283Epoch 00001: val_loss improved from 0.22114 to 0.16984, saving model to checkpoint2.hdf5
37029/37029 [==============================] - 232s - loss: 0.2003 - acc: 0.9283 - val_loss: 0.1698 - val_acc: 0.9384
Epoch 3/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.1692 - acc: 0.9391Epoch 00002: val_loss improved from 0.16984 to 0.15466, saving model to checkpoint2.hdf5
37029/37029 [==============================] - 233s - loss: 0.1691 - acc: 0.9391 - val_loss: 0.1547 - val_acc: 0.9444
Epoch 4/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.1491 - acc: 0.9464Epoch 00003: val_loss improved from 0.15466 to 0.13643, saving model to checkpoint2.hdf5
37029/37029 [==============================] - 233s - loss: 0.1491 - acc: 0.9464 - val_loss: 0.1364 - val_acc: 0.9514
Epoch 5/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.1310 - acc: 0.9544Epoch 00004: val_loss improved from 0.13643 to 0.12560, saving model to checkpoint2.hdf5
37029/37029 [==============================] - 233s - loss: 0.1309 - acc: 0.9544 - val_loss: 0.1256 - val_acc: 0.9559
Epoch 6/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.1148 - acc: 0.9595Epoch 00005: val_loss did not improve
37029/37029 [==============================] - 232s - loss: 0.1148 - acc: 0.9595 - val_loss: 0.1267 - val_acc: 0.9553
Epoch 7/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.1062 - acc: 0.9637Epoch 00006: val_loss improved from 0.12560 to 0.12303, saving model to checkpoint2.hdf5
37029/37029 [==============================] - 232s - loss: 0.1062 - acc: 0.9637 - val_loss: 0.1230 - val_acc: 0.9584
Epoch 8/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.1045 - acc: 0.9643Epoch 00007: val_loss did not improve
37029/37029 [==============================] - 233s - loss: 0.1045 - acc: 0.9642 - val_loss: 0.1257 - val_acc: 0.9575
Epoch 9/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0910 - acc: 0.9678Epoch 00008: val_loss improved from 0.12303 to 0.12026, saving model to checkpoint2.hdf5
37029/37029 [==============================] - 232s - loss: 0.0910 - acc: 0.9678 - val_loss: 0.1203 - val_acc: 0.9606
Epoch 10/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0805 - acc: 0.9719Epoch 00009: val_loss did not improve
37029/37029 [==============================] - 233s - loss: 0.0806 - acc: 0.9719 - val_loss: 0.1248 - val_acc: 0.9607
Epoch 11/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0722 - acc: 0.9753Epoch 00010: val_loss did not improve
37029/37029 [==============================] - 232s - loss: 0.0723 - acc: 0.9753 - val_loss: 0.1332 - val_acc: 0.9563
Epoch 12/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0686 - acc: 0.9762Epoch 00011: val_loss did not improve
37029/37029 [==============================] - 233s - loss: 0.0686 - acc: 0.9762 - val_loss: 0.1285 - val_acc: 0.9597
Epoch 13/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0676 - acc: 0.9755Epoch 00012: val_loss did not improve
37029/37029 [==============================] - 231s - loss: 0.0676 - acc: 0.9755 - val_loss: 0.1313 - val_acc: 0.9588
Epoch 14/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0538 - acc: 0.9826Epoch 00013: val_loss did not improve
37029/37029 [==============================] - 233s - loss: 0.0538 - acc: 0.9826 - val_loss: 0.1276 - val_acc: 0.9626
Epoch 15/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0500 - acc: 0.9827Epoch 00014: val_loss did not improve
37029/37029 [==============================] - 207s - loss: 0.0500 - acc: 0.9827 - val_loss: 0.1318 - val_acc: 0.9605
Epoch 16/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0426 - acc: 0.9854Epoch 00015: val_loss did not improve
37029/37029 [==============================] - 142s - loss: 0.0426 - acc: 0.9854 - val_loss: 0.1292 - val_acc: 0.9628
Epoch 17/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0373 - acc: 0.9884Epoch 00016: val_loss did not improve
37029/37029 [==============================] - 142s - loss: 0.0373 - acc: 0.9884 - val_loss: 0.1497 - val_acc: 0.9592
Epoch 18/20
37024/37029 [============================>.] - ETA: 0s - loss: 0.0427 - acc: 0.9857Epoch 00017: val_loss did not improve
37029/37029 [==============================] - 142s - loss: 0.0427 - acc: 0.9857 - val_loss: 0.1361 - val_acc: 0.9617
Epoch 00017: early stopping
37024/37029 [============================>.] - ETA: 0sMatching records...
Metric = Deep Neural Net Classifier : GRU
Bidirectional : True
Accuracy = 0.953752464285
Precision = 0.953152812989
Recall = 0.954414107861
F1 = 0.953783043437
Processing time per 50K records = 57.7598944604
Number of training instances = 37029
```
