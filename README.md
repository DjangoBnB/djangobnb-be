# djangobnb-be

[ERD URL 작성중](https://www.erdcloud.com/d/2H4dsj384NJDdRbaG)

# AirBnB 클론코딩 (DjangoBnB)

## 🧑🏻‍💻 FE 개발자

| 기용  | 연우 |  진우  |
| ---------- | ------ | --------- |
| <img src="" width="100" /> | <img src="" width="100" /> | <img src="" width="100" /> |
| [github](https://github.com/ssafykwon)                                                                                  | [github](https://github.com/dusdn0224)  | [github](https://github.com/JWhan96)  |                                                                                  |

<br><br>

## 🛠 Stack

`django`, `django-REST-framework`

<br><br>

## 💡 브랜치 전략

Github flow + dev

- main : 무결성 유지, dev 브랜치에서만 PR 가능
- dev : 개발용, 기능 브랜치들 merge용, 버그 해결용
- 기능 : 새로운 기능 개발용 (브랜치명을 명시적으로 작성)

```
main
 └─ dev
     ├── 기능1
     ├── 기능2
     └── 기능3
```

<br><br>

## 🤙🏻 commit 컨벤션

```
💡 feat : 새로운 기능 추가
🐞 fix : 버그 수정
📄 docs : 문서 수정
🛠 refact : 코드 리팩토링
💅 style : 코드 의미에 영향을 주지 않는 변경사항
📦 chore : 빌드 부분 혹은 패키지 매니저 수정사항
```

<br><br>

## 👊🏻 PR 컨벤션

```
[브랜치명] 작업내용

[detail] 캘린더 라이브러리 추가 및 수정
```

- 자세한 사항은 내용에 목록 형태로 작성
- 이렇게 써주세요