countText = Counter(text)
balloon = Counter("balloon")

res = len(text)
for c in balloon:
	res = min(res, countText[c] // balloon[c])
return res
