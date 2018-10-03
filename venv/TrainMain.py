import numpy as np
import os, configparser
import osuT as o
import makeDataset,readSongs

# This is a main script that automatically makes dataset according to given configuration.

readSongs.main()
makeDataset.main()