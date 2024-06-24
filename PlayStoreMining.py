import pandas as pd
import numpy as np
from google_play_scraper import app, Sort, reviews_all

# Importing reviews from Jobstreet App
google_reviews = reviews_all(
    "com.jobstreet.jobstreet",
    sleep_milliseconds=0, # default to 0
    lang='en',
    country='sg',
    sort=Sort.NEWEST
)

# Transform data into DataFrame
google_df = pd.DataFrame(np.array(google_reviews), columns=['review'])
google_df2 = google_df.join(pd.DataFrame(google_df.pop('review').tolist()))
print(google_df)
print(google_df2.columns)

# Data prep and cleaning
google_df2.drop(columns=['userImage', 'reviewCreatedVersion'], inplace=True)  # Not needed
google_df2.rename(columns={'score': 'rating',
                           'userName': 'user_name',
                           'reviewId': 'review_id',
                           'content': 'review_description',
                           'at': 'review_date',
                           'replyContent': 'developer_response',
                           'repliedAt': 'developer_response_date',
                           'appVersion': 'app_version',
                           'thumbsUpCount': 'likes_count'}, inplace=True)
google_df2.insert(loc=0, column='source', value='Google Play')
google_df2.insert(loc=3, column='review_title', value='None')
google_df2['likes_count'] = google_df2['likes_count'].fillna('None', inplace=True)
google_df2['language_code'] = 'en'
google_df2['country_code'] = 'sg'
print(google_df2)

