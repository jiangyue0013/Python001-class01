import pandas as pd

from douban.models import Comments

# 此文件内容在 django shell 中输入，用于将 result.csv 文件中的内容导入至数据库中。
data = pd.read_csv(r'result.csv', encoding='utf-8')
for x in range(20):
    Comments.objects.create(
        stars=data['n_star'].iloc[x],
        short=data['short'].iloc[x],
        sentiment=data['sentiment'].iloc[x],
    )
