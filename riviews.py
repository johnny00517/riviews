data = []
count = 0

with open('reviews.txt', 'r')as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))

print('檔案讀取完成,共有', len(data), '筆資料')



sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
	
print('每筆檔案平均有', sum_len/len(data), '個字')


new = []
for d in data:
	if len(new) < 200:
		new.append(d)
print('一共有', len(new), '筆資料長度小於200')


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆資料提到good')
print('第一筆留言為:', good[0])


#以下為速寫法
good = [d for d in data if 'good' in d]
print('一共有', len(good), '筆資料提到good')