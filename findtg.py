#!/usr/bin/env python3.6

from tgfilecopier import jobiterator
from tgiterator import findtg

# Copy all dep.in and test.out files from Ben's runs on google drive
datapath = '/home/nerve/Documents/UW/gdrive/DMREF/MD/Rc_database/TEMP/Pd-Si/Si0.00/667'
jobiterator(datapath)

# Calculate Tg from the copied files in a path
path = './'
findtg(path)

# Create a dataframe containing all Tg imformation
import tgdf

# Create a dataframe containting all Tg averaged by jobs
import tgaverager

# Create a dataframe containing all Tg averaged by jobs and filtered
import tgaveragerwithfilter
