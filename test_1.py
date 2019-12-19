import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'Condition 1': np.random.rand(20),
                   'Condition 2': np.random.rand(20) * 0.9,
                   'Condition 3': np.random.rand(20) * 1.1
                   })
string = str(round(print(df)))
with open("D:\\test2.txt", 'w') as file_object:
    file_object.write(string)
