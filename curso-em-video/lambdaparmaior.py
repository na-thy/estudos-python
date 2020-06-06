a = [10,13,17,20,23,16,67,45,44,99,68]

result = list(filter(lambda x:x%2==0 and x>=10, a))

print(result)