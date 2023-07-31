### 세트 메소드 ###

# 교집합: intersection()
fruits1 = {'apple', 'banana'}
fruits2 = {'banana', 'orange'}
result_intersect = fruits1.intersection(fruits2)
print(result_intersect)

# 합집합: union()
result_union = fruits1.union(fruits2)
print(result_union)
# set자료형은 중복을 허용하지 않기 때문에
# 동일한 값은 하나의 값만 남긴다.

# 차집합: defference()
result_diff = fruits1.difference(fruits2)
print(result_diff)