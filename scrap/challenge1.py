# Naver 동영상 TOP3 추출

import requests
from bs4 import BeautifulSoup

raw = requests.get('https://tv.naver.com/r').text

# html 구조로 파싱
html = BeautifulSoup(raw, 'html.parser')

clips = html.select('div.info')
# first_clip = clips[0]

# select 는 list 수집   /  select_one 은 제일 처음 요소 하나만 수집
for clip in clips:
    title = clip.select_one('strong.tit > span').text
    chn = clip.select_one('span.ch').text
    hit = clip.select_one('span.hit').text
    like = clip.select_one('span.like').text
    print(title, '/', chn, '/', hit, '/', like)


# print(clips[0].select_one('tooltip').text)
