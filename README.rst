This repository is for better-using of hvsrpy, especially when new student want to get fast familar with hvsrpy and their own dataset.
=======================================

1. First thing, we should install 'hvsrpy', which you could figure out in the link (https://github.com/jpvantassel/hvsrpy). You could follow this link and install 'hvsrpy' and I will not cover more details here.

  If you don't install jupyter notebook yet, you may also need to install it before your calculation. You could refer to this link           (https://blog.csdn.net/m0_68678046/article/details/129703799).

  And now you could get yourself familiar with hvsrpy by processing their examples.
-------------------------------------------------------------------------------
2. Second step, we should prepare with the raw data. 
  (1)According to your needs, cut the raw data into different files, you may cut data files in 24hours length unit or 1hour length.
  
  For example, if you prefer 24hours length, you could refer scripts written by Dr.Wang(Wang Xinyang):
  You should preparec these files:
  (a)cut_EPS_day.sh(main script), 
  (b)nzjday.f(needed when you run the script 'cut_EPS_day.sh', you don't need to change it),
  (c)find_EPS_day(needed when you run the script 'cut_EPS_day.sh', you don't need to change it), 
  (d)RD(a txt file including your date range. If your date range of raw data is from 20210418 to 20210420, you should write "20210418 
 20210419 20210420" in this file. Each date must write on different lines), 
  (e)st(a txt file, include all station's data filename, like P001_sac. When you get your own data, you could run "ls * > st" in the terminal, then you get your own st).

  Pay Attention：No matter how long your data-length is, we must keep three-components-files of one station with the same npts(Number of sampling points).

  When we prepare all these files and put them in same directory, you could run 'bash cut_EPS_day.sh' in your terminal and just wait! And we should run this code for three times, one time for one component. For example, when we are processing component N, we should check the script(cut_EPS_day.sh), and search all words including "BHZ" or "BHE" and change them into "BHN". 
-------------------------------------------------------------------------------
