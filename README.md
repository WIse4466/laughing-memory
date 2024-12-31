# Data_Model_Final_Project
分析迷因幣的價量分析，還有持幣者結構分析
資料來源 : https://drive.google.com/drive/folders/10R8rxzjpwdN8E3Gegz7JkoZgBfS3friS

## 關鍵字熱度
我們認為關鍵字熱度可以一定程度的代表市場的情緒，與新聞為市場帶來的資訊影響
使用pytrend API抓取Ethereum上前5大的meme coin在2024年關鍵字熱度的變化  
分別是
- PEPE
- SHIB
- BONK
- FLOKI
- MOG
將數據同取log進行壓縮，避免極端值得影響，也使數據分布較為平滑  
觀察5種迷因幣的表現，可以發現各種幣之間搜尋的熱度有相似趨勢，而PEPE幣的熱度相較於其他幣明顯更高  
![Log-Transformed Trend of Meme Coins Over Time](https://github.com/user-attachments/assets/1e3de221-d4a6-47fe-bc03-d8092b301c4d)
這張圖表現了Ethereum上前5大的meme coin在2024年關鍵字熱度的變化  

## 價格、熱度、成交量
接著我們將2024年這5種迷因幣的資料與2024年關鍵字熱度資料進行整合  
利用畫圖與變數之間彼此的關係係數，分析三個變量之間的關係  
從圖中可以發現，Shiba-inu, Floki 和 Bonk三種迷因幣其變量間的趨勢很相近，猜測相關度較高  
計算相關係數後可以發現，這三種幣其變量確實呈現正相關，應可作為機器學習的訓練資料，以預測未來價格  
![bonk_normalized_metrics_over_time](https://github.com/user-attachments/assets/d569e0be-55b8-4306-8901-107e11f84b96)
![floki_normalized_metrics_over_time](https://github.com/user-attachments/assets/23ab3c25-fbe6-4681-bc9f-0526602ae12a)
![mog-coin_normalized_metrics_over_time](https://github.com/user-attachments/assets/ae0e0a85-55ae-48a1-9669-359b652ba2ba)
![pepe_normalized_metrics_over_time](https://github.com/user-attachments/assets/9eff763b-7d49-480c-b561-4b432eb87003)
![shiba-inu_normalized_metrics_over_time](https://github.com/user-attachments/assets/ae6a310d-76c7-4ca0-b071-4c5518033d96)

## 相關係數矩陣
Correlation matrix for shiba-inu:  
|                   |price | trading_volume  |   trend | 
|price     |      1.000000   |     0.541018 | 0.359334  |
|trading_volume | 0.541018     |   1.000000 | 0.634280  |
|trend     |      0.359334    |    0.634280 | 1.000000  |

Correlation matrix for pepe:
                   price  trading_volume     trend
price           1.000000        0.672708 -0.143642
trading_volume  0.672708        1.000000  0.151011
trend          -0.143642        0.151011  1.000000

Correlation matrix for bonk:
                   price  trading_volume     trend
price           1.000000        0.737057  0.032744
trading_volume  0.737057        1.000000  0.262896
trend           0.032744        0.262896  1.000000

Correlation matrix for floki:
                   price  trading_volume     trend
price           1.000000        0.642937  0.300401
trading_volume  0.642937        1.000000  0.472558
trend           0.300401        0.472558  1.000000

Correlation matrix for mog-coin:
...
price           1.000000        0.702583 -0.450808
trading_volume  0.702583        1.000000 -0.229812
trend          -0.450808       -0.229812  1.000000

## 機器學習
### LinearRegression
bonk - MSE: 0.000000, RMSE: 0.000007, MAE: 0.000005, MAPE: 23.39%, R²: 0.5888
floki - MSE: 0.000000, RMSE: 0.000055, MAE: 0.000049, MAPE: 58.03%, R²: 0.4757
mog-coin - MSE: 0.000000, RMSE: 0.000000, MAE: 0.000000, MAPE: 44.39%, R²: 0.8256
pepe - MSE: 0.000000, RMSE: 0.000003, MAE: 0.000003, MAPE: 56.15%, R²: 0.7233
shiba-inu - MSE: 0.000000, RMSE: 0.000006, MAE: 0.000005, MAPE: 28.98%, R²: 0.2403

### RandomForestRegressor
bonk - MSE: 0.000000, RMSE: 0.000004, MAE: 0.000003, MAPE: 9.10%, R²: 0.8695
floki - MSE: 0.000000, RMSE: 0.000023, MAE: 0.000016, MAPE: 9.09%, R²: 0.9080
mog-coin - MSE: 0.000000, RMSE: 0.000000, MAE: 0.000000, MAPE: 17.65%, R²: 0.9180
pepe - MSE: 0.000000, RMSE: 0.000002, MAE: 0.000001, MAPE: 9.72%, R²: 0.9367
shiba-inu - MSE: 0.000000, RMSE: 0.000003, MAE: 0.000002, MAPE: 8.68%, R²: 0.8602

### LSTM
bonk - MSE: 0.000012, RMSE: 0.003418, MAE: 0.001871, MAPE: 7721.17%, R²: -113363.2700
floki - MSE: 0.000003, RMSE: 0.001828, MAE: 0.001275, MAPE: 1373.49%, R²: -569.1073
mog-coin - MSE: 0.000004, RMSE: 0.002102, MAE: 0.001347, MAPE: 296078.73%, R²: -5331541.6923
pepe - MSE: 0.000005, RMSE: 0.002170, MAE: 0.001665, MAPE: 33146.05%, R²: -111659.1706
shiba-inu - MSE: 0.000093, RMSE: 0.009637, MAE: 0.003086, MAPE: 15698.15%, R²: -2008314.4229

### ARIMA
bonk - MSE: 0.000000, RMSE: 0.000010, MAE: 0.000008, MAPE: 46.97%, R²: -0.0135
floki - MSE: 0.000000, RMSE: 0.000085, MAE: 0.000067, MAPE: 185.80%, R²: -0.2249
mog-coin - MSE: 0.000000, RMSE: 0.000001, MAE: 0.000001, MAPE: 429.84%, R²: -0.0135
pepe - MSE: 0.000650, RMSE: 0.025491, MAE: 0.025491, MAPE: 924284.98%, R²: -15414892.7402
shiba-inu - MSE: 0.000000, RMSE: 0.000008, MAE: 0.000006, MAPE: 99.59%, R²: -0.3312
