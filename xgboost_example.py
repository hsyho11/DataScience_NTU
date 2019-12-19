attr_x,attr_y = ['artist_name','genres','artist_popularity','acousticness','danceability', 'duration_ms','energy', 'instrumentalness', 'key', 'liveness', 'loudness',
               'speechiness', 'tempo', 'valence'],['popularity'] # 'release_date'
df_tmp = df[attr_x]
df_tmp.genres = pd.factorize(df_tmp.artist_name)[0]
df_tmp.artist_name = pd.factorize(df_tmp.genres)[0]

#X,Y = StandardScaler().fit_transform(df_tmp),df[attr_y]
X,Y = df_tmp,df[attr_y]

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, random_state=87)

from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error

xgb = XGBRegressor(objective ='reg:squarederror',
                 colsample_bytree=0.4,
                 gamma=0,                 
                 learning_rate=0.07,
                 max_depth=100,
                 min_child_weight=1.5,
                 n_estimators=10000,                                                                    
                 reg_alpha=0.75,
                 reg_lambda=0.45,
                 subsample=0.6,
                 seed=42) 
'''
(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1, 
                   max_depth = 5, alpha = 10, n_estimators = 10)
'''
xgb.fit(X_train, Y_train)

preds = xgb.predict(X_test)
rmse = np.sqrt(mean_squared_error(Y_test, preds))
print("RMSE: %f" % (rmse))
