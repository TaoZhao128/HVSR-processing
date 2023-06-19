Help to get familar with package 'hvsrpy'
=======================================

1. First thing, we should install 'hvsrpy', which you could figure out in the link (https://github.com/jpvantassel/hvsrpy). You could follow this link and install 'hvsrpy' and I will not cover more details here.

  If you don't install jupyter notebook yet, you may also need to install it before your calculation. You could refer to this link           (https://blog.csdn.net/m0_68678046/article/details/129703799).

  And now you could get yourself familiar with hvsrpy by processing their examples.

2. Second step, we should prepare with the raw data. 

 According to your needs, cut the raw data into different files, you may cut data files in 24hours length unit or 1hour length.
  
 For example, if you prefer 24hours length, you could refer scripts written by Dr.Wang(Wang Xinyang):
 You should preparec these files:
  (a)cut_EPS_day.sh(main script), 
  (b)nzjday.f(needed when you run the script 'cut_EPS_day.sh', you don't need to change it),
  (c)find_EPS_day(needed when you run the script 'cut_EPS_day.sh', you don't need to change it), 
  (d)RD(a txt file including your date range. If your date range of raw data is from 20210418 to 20210420, you should write "20210418 20210419 20210420" in this file. Each date must write on different lines), 
  (e)st(a txt file, include all station's data filename, like P001_sac. When you get your own data, you could run "ls * > st" in the terminal, then you get your own st).

When we prepare all these files and put them in same directory, you could run 'bash cut_EPS_day.sh' in your terminal and just wait! And we should run this code for three times, one time for one component. For example, when we are processing component N, we should check the script(cut_EPS_day.sh), and search all words including "BHZ" or "BHE" and change them into "BHN". 

 !!Pay Attention：No matter how long your data-length is, we must keep three-components-files of one station with the same npts(Number of sampling points).

3. Third step, change sac file into miniseed file. "hvsrpy" need 'miniseed', not 'sac'. 
  You could refer to the script named "sac2miniseed.py" which you could find in this docs.

4. Forth step, do HVSR calculations.
  We mainly need to run two scripts in 'hvsrpy', "simple_hvsrpy_interface.ipynb" and "azimuthal_hvsrpy_interface.ipynb"
  Before calculation, you could change relavant parameters in these two scripts according to your needs.

  !And also, we need to change the file path, make sure the path is correct path whcih link to your own data. You could refer the example path in those two notebooks.
  When fully-prepared, you could run "jupyter notebook" in your terminal and run those two notebook.
  
When you get familar with hvsrpy and want to do batch calculation. You could refer 'batch'. And run those two scripts after doing a little change according to your file path.
