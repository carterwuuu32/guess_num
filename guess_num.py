import random
r = random.randint(1, 100)

ans = input('猜數字')
ans = int(ans)

while r != ans:
	if ans > r:
		print('比答案大')
		ans = input('繼續猜：')
		ans = int(ans)
	else:
		print('比答案小')
		ans = input('繼續猜：')
		ans = int(ans)

print('終於猜對了，答案是', r)








