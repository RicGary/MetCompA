"""
Atividade no link:
https://drive.google.com/file/d/1-YsAtKQrzTQBtIRKuXi8uIcaEc_lJ1CZ/view?usp=sharing

Arquivo .dat está junto dos códigos, seu nome é Hubble.dat
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r'hubble.dat')

redshift = list(df.head(17))

print(redshift)                0





