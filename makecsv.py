import requests
import random
import numpy as np
import pandas as pd
from scipy.stats import skewnorm 
from faker import Faker


def create_hosts(host_size):
    fake = Faker('ko-KR')
    df_hosts = pd.DataFrame(columns=['name'])
    for row_i in range(host_size):
        name = fake.name()

        df_hosts.loc[row_i] = [name]
    
    return df_hosts

def create_rooms(room_size): # ,host_id_size
    fake = Faker('ko-KR')
    df_rooms = pd.DataFrame(columns=['room_name', 'room_address_latitude', 'room_address_longitude',
                                    'room_address', 'room_des', 'room_capacity', 'room_types',
                                    'room_host', 'room_daily_price', 'room_created_at', 'room_updated_at'])

    skew_norm_distribution = skewnorm.rvs(20, size=room_size + 300)
    price_distribution = np.round((skew_norm_distribution[skew_norm_distribution > 0] * 300000) + 3000, 1)
    for row_i in range(room_size):
        room_name = fake.company() # 숙소 이름 e.g. 김김이
        lat_lng = fake.local_latlng(country_code= 'KR') # ('37.1759', '128.9889', 'T‚Äôaebaek', 'KR', 'Asia/Seoul')
        # host_id = random.randint(1, host_id_size)
        room_address_latitude = lat_lng[0] # 위도 e.g 34.8825
        room_address_longitude = lat_lng[1] # 경도 e.g 128.62667
        room_address = fake.address()
        room_des = fake.text() # 숙소 설명 e.g. Quibusdam voluptatem omnis odio. Veniam nihil amet. Ratione minus repudiandae enim accusamus possimus.
        room_capacity = random.randint(1, 10) # 최대 인원수 e.g. 8
        room_types = random.randint(1, 4)
        room_host = row_i + 1
        daily_price = int(price_distribution[row_i]) # 일일 가격 e.g. 30000 ~ 1500000 편향분포
        room_daily_price = round(daily_price, -3)
        room_created_at = fake.date_time_this_decade()
        room_updated_at = fake.date_time_this_year()
        df_rooms.loc[row_i] = [room_name, room_address_latitude, room_address_longitude, room_address,
                                    room_des, room_capacity, room_types,
                                    room_host, room_daily_price, room_created_at, 
                                    room_updated_at]

    return df_rooms


def create_reviews(review_size):
    fake = Faker('ko-KR')
    df_reviews = pd.DataFrame(columns=['review_user', 'review_room', 'review_rating', 'review_comment',
                                'review_created_at', 'review_updated_at'])

    for row_i in range(review_size):
        review_user = random.randint(1, 20)
        review_room = random.randint(1, 20)
        review_rating = round(random.uniform(3, 5), 2)
        review_comment = fake.text()
        review_created_at = fake.date_time_this_decade()
        review_updated_at = fake.date_time_this_year()

        df_reviews.loc[row_i] = [review_user, review_room, review_rating, review_comment,
                                review_created_at, review_updated_at]
    return df_reviews


def create_room_images(room_size, random_image_size = 100, image_size_row = 400, image_size_col = 400):
    
    df_room_image = pd.DataFrame(columns=['room_id', 'image_url'])

    room_image_list = []
    for _ in range(1, random_image_size):
        image_url = 'https://picsum.photos/' + str(image_size_row) + '/' + str(image_size_col) + '?random=1'
        r = requests.get(image_url, allow_redirects=False)
        room_image_list.append(str(r.headers['Location']))

    global_image_i = 0
    for room_i in range(1, room_size + 1):        
        for _ in range(random.randint(1, 7)):
            df_room_image.loc[global_image_i] = [room_i, random.choice(room_image_list)]
            global_image_i = global_image_i + 1
            
    return df_room_image
            

df_hosts = create_hosts(20)
df_rooms = create_rooms(20) # 20개의 숙소 데이터 생성, FK host id는 20 까지 차례대로 있다고 가정
df_reviews = create_reviews(50)
df_room_image = create_room_images(20) 
#df_room_image = create_room_images(500, 100, 400, 400) # 랜덤 이미지개수, 사이즈 조정 가능 (400x400)

df_hosts.to_csv('./dummy_hosts.csv', index = False)
df_rooms.to_csv('./dummy_rooms.csv', index = False)
df_reviews.to_csv('./dummy_reviews.csv', index = False)
df_room_image.to_csv('./dummy_room_images.csv', index = False)