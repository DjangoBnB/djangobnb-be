import requests
import random
import numpy as np
import pandas as pd
from scipy.stats import skewnorm 
from faker import Faker



def create_rooms(room_size, host_id_size):
    fake = Faker('ko_KR')
    # df_rooms = pd.DataFrame(columns=['host_id', 'title', 'description', 'address' , 'lat', 'lng' ,
    #                             'bathroom_count', 'bed_count', 'bedroom_count', 'header_count_capacity',
    #                             'cleaning_fee', 'daily_price', 'lodging_tax_ratio', 'sale_ratio', 'service_fee',
    #                             'rating_star_score', 'review_count'])
    df_rooms = pd.DataFrame(columns=['host_id', 'title', 'room_type', 'description', 'address' , 'lat', 'lng' ,
                                'header_count_max', 'daily_price', 'rating_star_score', 'review_count'])
    
    room_types = ['호텔', '모텔', '펜션', '아파트']

    # skew_norm_distribution = skewnorm.rvs(20, size=room_size + 300)
    # price_distribution = np.round((skew_norm_distribution[skew_norm_distribution > 0] * 300000) + 3000, 1)
    for row_i in range(room_size):
        lat_lng = fake.local_latlng(country_code= 'KR') # ('37.1759', '128.9889', 'T‚Äôaebaek', 'KR', 'Asia/Seoul')
        # print(lat_lng)
        host_id = random.randint(1, host_id_size)
        title = fake.company() + ' ' + np.random.choice(room_types) # 숙소 이름 e.g. 김김이 게스트하우스
        # print(title)
        room_type = np.random.choice(room_types)
        description = fake.text() # 숙소 설명 e.g. Quibusdam voluptatem omnis odio. Veniam nihil amet. Ratione minus repudiandae enim accusamus possimus.
        # print(description)
        address = fake.address() # 
        lat = lat_lng[0] # 위도 e.g 34.8825
        lng = lat_lng[1] # 경도 e.g 128.62667
        # bathroom_count = random.randint(1, 3) # 화장실 수 e.g. 3
        # bed_count = random.randint(1, 5) # 침대 수 e.g. 2
        # bedroom_count = random.randint(1, 5) # 침실 수 e.g. 2
        # headcount_max = random.randint(1, 10) # 최대 인원수 e.g. 8
        headcount_max = int(4) # 최대 인원수 e.g. 8
        # cleaning_fee = random.randint(10, 100) * 100 # 청소비 e.g. 5000
        # daily_price = int(price_distribution[row_i]) # 일일 가격 e.g. 30000 ~ 1500000 편향분포
        daily_price = int(30000) # 일일 가격 
        # lodging_tax_ratio = 10 # 세금(10%) e.g. 10
        # sale_ratio = random.randint(1, 10) # 할인률(10%) e.g. 10
        # service_fee = random.randint(5, 50) * 100 # 서비스 비용 e.g. 5000
        rating_star_score = round(random.uniform(1, 5), 2) # 평점 e.g. 3.3 
        review_count = random.randint(10, 500) # 리뷰개수

        # df_rooms.loc[row_i] = [host_id, title, description, address, lat, lng,
        #                         bathroom_count, bed_count, bedroom_count, headcount_capacity,
        #                         cleaning_fee, daily_price, lodging_tax_ratio, sale_ratio, service_fee,
        #                         rating_star_score, review_count]
        df_rooms.loc[row_i] = [host_id, title, room_type, description, address, lat, lng, 
                                headcount_max, daily_price, rating_star_score, review_count]
    
    return df_rooms


# def create_room_images(room_size, random_image_size = 100, image_size_row = 400, image_size_col = 400):
    
#     df_room_image = pd.DataFrame(columns=['room_id', 'image_url'])

#     room_image_list = []
#     for _ in range(1, random_image_size):
#         image_url = 'https://picsum.photos/' + str(image_size_row) + '/' + str(image_size_col) + '?random=1'
#         r = requests.get(image_url, allow_redirects=False)
#         room_image_list.append(str(r.headers['Location']))

#     global_image_i = 0
#     for room_i in range(1, room_size + 1):        
#         for _ in range(random.randint(1, 7)):
#             df_room_image.loc[global_image_i] = [room_i, random.choice(room_image_list)]
#             global_image_i = global_image_i + 1
            
#     return df_room_image
            
df_rooms = create_rooms(500, 200) # 5000개의 숙소 데이터 생성, FK host id는 2000 까지 있다고 가정
# df_room_image = create_room_images(500) 
#df_room_image = create_room_images(500, 100, 400, 400) # 랜덤 이미지개수, 사이즈 조정 가능 (400x400)

# df_rooms.to_csv('./dummy_rooms.csv', index = False, encoding='utf-8')
df_rooms.to_csv('./dummy_rooms.csv', index=False, encoding='utf-8-sig')

# df_room_image.to_csv('./dummy_room_images.csv', index = False)