# 리스트 인덱스
cities = ['서울', '인천', '수원', '성남', '대전', '원주', '대구', '김해', '군산', '경주', '청주']
# print(cities)
# print(cities[0], '롯데타워')
# cities[2] = '안양'
# print(cities)

# 중첩 리스트
citiesLandmark = ['서울', ['롯데타워', '청와대'], '인천', ['인천국제공항', '차이나타운'], '수원', ['수원 화성', '박지성로'],
                  '성남', ['네이버', '판교 현대백화점'], '대전', ['성심당', '대전엑스포']]
# print(citiesLandmark[1][0])

# 리스트 슬라이싱
cities = ['서울', '인천', '수원', '성남', '대전', '원주', '대구', '김해', '군산', '경주', '청주']
# print(cities[0:3])
# print(cities[:5])
# print(cities[5:])
# print(cities[-1])
# print(cities[1:-1])

# 문자열 슬라이싱
price = '가격 : 13,000 원'
price2 = '가격 : 113,000 원'

# print(price[:3])
# print(price[5:11].replace(',',''))
# print(price2[5:-2].replace(',',''))

# 실습!
hit = '조회 수 - 139,153회'
print(hit[7:-1].replace(',',''))
print(hit.split('-')[1].strip()[:-1].replace(',',''))
print(hit[hit.index('-') + 2 :-1].replace(',',''))
