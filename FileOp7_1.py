f = open("test.txt",'rt',encoding="utf-8")
print(f.readline())
print(f.readline())
print(f.readline())
f.seek(3,0)
print(f.readline())
f.close()