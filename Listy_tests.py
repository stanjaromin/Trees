import random
from time import time
import numpy as np
import pandas as pd

# Initilize Random
random.seed(time())

#### List Tests ####

# How many test passes to run
num_tests = 25

# Create a dict for which to store tests
data = {'length': [], 'listComprehension': [], 'append': [], 'preAllocate': [], 'while': []}

for i in range(0, num_tests):
    # Randomize list length
    end = random.randint(100_000, 10_000_000)

    startTime = time()
    listComprehension = [i for i in range(0, end)]
    endTime = time()

    # Add timed entry
    tmpdata['listComprehension'].append(endTime - startTime)

# Get the median for all the rows
df = pd.DataFrame(data)
print(df.describe())