# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/141sa9YCmlfUggwVXl5cggSerYqSYF5Fw
"""

import pandas as pd
import plotly.express as ps
import csv
import plotly.figure_factory as ff

df = pd.read_csv("data.csv")
fig=ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist=False)
fig.show()