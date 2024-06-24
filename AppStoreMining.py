import pandas as pd
import numpy as np
from app_store_scraper import AppStore
import json
import os
import uuid


# Importing review from Jobstreet App
apple_reviews = AppStore('sg', 'jobstreet-job-search-career', '367294492')
apple_reviews.review()

# Transform data into DataFrame
apple_df = pd.DataFrame(np.array(apple_reviews.reviews), columns=['review'])
apple_df2 = apple_df.join(pd.DataFrame(apple_df.pop('review').tolist()))
apple_df2 = apple_df2.sort_values('date', ascending=False)
print(apple_df)
print(apple_df2.columns)

# Data prep and cleaning
apple_df2.drop(columns=['isEdited'], inplace=True)
apple_df2.insert(loc=0, column='source', value='App Store')
apple_df2['developer_response_date'] = None
apple_df2['likes_count'] = None
apple_df2['app_version'] = None
apple_df2['language_code'] = 'en'
apple_df2['country_code'] = 'sg'
apple_df2.insert(loc=1, column='review_id', value=[uuid.uuid4() for _ in range(len(apple_df2.index))])
apple_df2.rename(columns={'date': 'review_date', 'review': 'review_description', 'title': 'review_title',
                          'userName': 'user_name', 'developerResponse': 'developer_response'}, inplace=True)
apple_df2 = apple_df2.where(pd.notnull(apple_df2), None)


pd.set_option('display.max_columns', None)
print(apple_df2)
