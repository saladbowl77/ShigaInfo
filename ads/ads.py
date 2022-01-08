import pandas as pd
import numpy as np
df = pd.read_excel('./ads/ads.xlsx',engine="openpyxl")

bannerSize = ["200x200","250x250","500x500","300x200","300x250","600x500"]
bannerSizeDF = df[df["バナーサイズ"].isin(bannerSize)]
print(bannerSizeDF)

bannerSizeDF.to_csv('./ads/ads.csv')

adsArr = []

for column in bannerSizeDF.values:
    adsArr.append([
        column[12],
        column[15][20:],
        column[4]
    ])

print(adsArr)

adsDF = pd.DataFrame(adsArr)
adsDF.to_csv('./static/adsList.csv', header=False, index=False)