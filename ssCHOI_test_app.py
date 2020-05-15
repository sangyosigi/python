# 마지막 테스트 파이썬

import json

dic_mcu = []

# print(dic_mcu)
# with open("./data/mcu_movies.json", "w", encoding="UTF-8") as mcu_list:
#   json.dump(dic_mcu, mcu_list, ensure_ascii=False)

with open("./mcu_movies.json", "r", encoding="UTF-8") as mcu_list:
  dic_mcu = json.load(mcu_list)


# 문제 1번
# 페이즈가 1인 마블 시네마틱 유니버스 영화면 뽑기
result = []
for x in dic_mcu :
    if x['시리즈'].find('페이즈2')!=-1 :
        result.append(x['영화명'])
        result.append(x['개봉일'])
print(result)
# 문제 2번
# 박스오피스가 450000000 이상인 영화들의 감독이름 리스트와 전체 합계금액, 평균 박스오피스 구하기
def get_sum(self,value):
  return self.박스오피스 + value.박스오피스
def get_average(self):
  return self.get_sum()/9
def __eq__(self, value):
  return self.get_sum()> value.get_sum()

dir=[]
for x in dic_mcu:
  if x['박스오피스']>(450000000) :
    dir.append(x['감독'])
dir=list(set(dir))
print(dir)

sum=[]
for x in dic_mcu:
  if x['박스오피스']>(450000000) :
    sum.append(x['박스오피스'])
get_sum(self,value)
print(sum)

avg=[]
for x in dic_mcu:
  if x['박스오피스']>(450000000) :
    avg.append(x['박스오피스'])
get_average(self)
print(avg)

