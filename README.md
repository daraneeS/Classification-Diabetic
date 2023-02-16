# Classification_Diabetic
Data Cleaning, Preprocessing to improve Diabetic Classification Models.

![png](images/hist_all_features.png)
```
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(df[to_scale])
df[to_scale] = pd.DataFrame(scaler.transform(df[to_scale]), columns=to_scale)
hist_plot_pd(df[to_scale])
```

![png](images/scaled_features.png)

```
from sklearn.preprocessing import PowerTransformer
pt = PowerTransformer()
df[to_log] = pd.DataFrame(
    pt.fit_transform(df[to_log]), columns=to_log
)
hist_plot_pd(df[to_log])
```
![png](images/log_transform.png)

