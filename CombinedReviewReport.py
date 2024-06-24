from PlayStoreMining import google_df2
from AppStoreMining import apple_df2
import pandas as pd


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 200)
pd.set_option('display.max_colwidth', None)
review_result = pd.concat([google_df2, apple_df2])
print(review_result)

review_result.to_csv('StoreReviews.csv', index=False)
review_result.to_excel('StoreReviews.xlsx', index=False)
