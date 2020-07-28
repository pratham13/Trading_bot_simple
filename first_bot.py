# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:49:07 2020

@author: zbfypn
"""

import robin_stocks as r
import pandas as pd
import matplotlib.pyplot as plt

r.login("username","password")

my_stocks = r.build_holdings()

# %% Get the data in data frame format

df = pd.DataFrame(my_stocks)
df = df.T

df['ticker'] = df.index
df = df.reset_index(drop=True)


cols = df.columns.drop(['id','type','name','pe_ratio','ticker'])
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')


# %% exploring the data

# make the required changes in filter criteria to make the buy and sell stocks

df_buy = df[(df['average_buy_price'] <= 25.000) & (df['quantity'] <= 5.000000) & (df['percent_change'] <= -.50)]
df_sell = df[(df['percent_change'] >= 20)]


tkr_buy_list  = df_buy['ticker'].tolist()
tkr_sell_list = df_sell['ticker'].tolist()



# %%

#sell execution

if len(tkr_sell_list) > 0:
    [r.orders.order_sell_market(i,4,timeInForce= 'gfd') for i in tkr_sell_list]
    [print(i) for i in tkr_sell_list]
    
else:
    print('Nothing to sell right now!')

#buy execution
if len(tkr_buy_list) > 0:
    [r.orders.order_buy_market(i,4,timeInForce= 'gfd') for i in tkr_buy_list]
    [print(i) for i in tkr_buy_list]
   
else:
    print('Nothing to buy right now!')