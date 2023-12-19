import os
from django import setup

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PJT.settings")
setup()

# 이제 get_user_model()을 호출해도 오류가 발생하지 않아야 합니다.

# 이하 코드는 동일하게 진행
import random
from faker import Faker
from django.contrib.auth import get_user_model

# Fake 데이터 생성을 위한 인스턴스 생성
fake = Faker()

def create_fake_users(num_users=20):
    User = get_user_model()
    
    for _ in range(num_users):
        # 임의의 사용자 정보 생성
        first_name = fake.first_name()
        last_name = fake.last_name()
        username = fake.user_name()
        email = fake.email()
        password = fake.password()

        # User 모델 인스턴스 생성
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        # 추가 필드에 대한 정보 설정 (nickname)
        user.nickname = fake.user_name()
        user.save()

if __name__ == '__main__':
    create_fake_users()
