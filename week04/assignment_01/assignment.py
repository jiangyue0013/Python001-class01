import pandas as pd


df = pd.DataFrame(data)
# 1. SELECT * FROM data;
df
# 2. SELECT * FROM data LIMIT 10;
df[1:11]
# 3. SELECT id FROM data;  //id 是 data 表的特定一列
df['id']
# 4. SELECT COUNT(id) FROM data;
df['id'].count()
# 5. SELECT * FROM data WHERE id<1000 AND age>30;
df[ df['id'] < 1000 && df['age'] > 30]
# 6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
df.groupby('id')['order_id'].unique()
# 7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
df1 = pd.DataFrame(table1)
df2 = pd.DataFrame(table2)
pd.merge(on='id')
# 8. SELECT * FROM table1 UNION SELECT * FROM table2;
pd.merge(df1, df2)
# 9. DELETE FROM table1 WHERE id=10;
df1.drop(df[ df['id']==10 ])
# 10. ALTER TABLE table1 DROP COLUMN column_name; 
df1.drop(columns=['column_name'])