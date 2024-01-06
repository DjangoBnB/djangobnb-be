import csv
import json

# CSV 파일 경로 - 읽을 CSV 파일
csv_file_path = 'dummy_rooms.csv'

# JSON 파일 경로
json_file_path = 'dummy_rooms.json'

# CSV 파일 읽어오기
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    json_data_list = []
    
    n = 1
    for row in csv_reader:
        pk_value = n
        model_name = 'rooms.Room' # 생성할 model 이름
        fields_data = row

        json_object = {
            "pk": pk_value,
            "model": model_name,
            "fields": fields_data
        }

        json_data_list.append(json_object)

        n += 1

    # # CSV 데이터를 JSON으로 변환
    # json_data = json.dumps([row for row in csv_reader], ensure_ascii=False, indent=2)

# JSON 파일로 저장
with open(json_file_path, 'w', encoding='utf-8') as json_file:
    # json_file.write(json_data)
    json.dump(json_data_list, json_file, ensure_ascii=False, indent=2)

print(f'Conversion from CSV to JSON is complete. JSON file saved at {json_file_path}')
