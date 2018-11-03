# 단계1
print('########단계1#########')
raw_data = '    코알라 웹개발 스터디에 정상적으로 신청이 완료되었습니다.    '
data = raw_data.strip()
new_data = data.replace('웹개발', '데이터 수집')
data_length = len(new_data)
print(raw_data)
print(data)
print(new_data)
print(data_length)

# 단계 2
print('########단계2#########')
data_length2 = len(raw_data.strip().replace('웹개발', '데이터 수집'))
print(data_length2)