# target:convert SAC to miniseed
#  sac -> miniseed
# date:2023.06.15 
# author: Tao Zhao
import glob
from obspy import read
for mfile in glob.glob('./*SAC', recursive=True):
    for (i, tr) in enumerate(read(mfile)):
        tr.write(mfile.replace('.SAC','{}.MSEED'.format(i)))
