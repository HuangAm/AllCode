import pandas as pd
import numpy as np

df = pd.read_csv('601318.csv',index_col='date',parse_dates=['date',])

#第一步:计算MA

#方案一:手动计算

# df['ma5'] = np.nan
# df['ma10'] = np.nan
# for i in range(4,len(df)):
#     df.loc[df.index[i],'ma5'] = df['close'][i-4:i+1].mean()
#
# for i in range(9,len(df)):
#     df.loc[df.index[i],'ma10'] = df['close'][i-9:i+1].mean()

#方案二: cumsum

# sr = df['close'].cumsum()
# df['md5'] = (sr - sr.shift(1).fillna(0).shift(4))/5
# df['ma10'] = (sr - sr.shift(1).fillna(0).shift(9))/10

#方案三：

df['ma5'] = df['close'].rolling(5).mean()
df['ma10'] = df['close'].rolling(10).mean()

#第二步：找出金叉和死叉的节点

#去掉NaN
df = df.dropna()

#方案1：直接搜索

# golden_cross = []
# death_cross = []
# sr = df['ma10'] >= df['ma5']
# for i in range(1,len(sr)):
#     if sr.iloc[i] == True and sr.iloc[i-1] == False:
#         death_cross.append(sr.index[i])
#     if sr.iloc[i] == False and sr.iloc[i-1] == True:
#         golden_cross.append(sr.index[i])

#方案2：shift

# death_cross = df[(df['ma10']>=df['ma5'])&(df['ma10']<df['ma5']).shift(1)].index
# golden_cross = df[(df['ma10']<=df['ma5'])&(df['ma10']>df['ma5']).shift(1)].index