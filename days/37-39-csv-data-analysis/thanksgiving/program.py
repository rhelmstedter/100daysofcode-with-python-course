##{
import os
from collections import namedtuple
import pandas as pd

#base_folder = os.path.dirname(__file__)
# filename = os.path.join(base_folder, 'thanksgiving-2015-poll-data.csv')

with open("./thanksgiving-2015-poll-data.csv", "r", encoding='utf-8') as f:
    df  = pd.read_csv(f)

df_regions = df.groupby("US Region")
df_regions.head()

##}


