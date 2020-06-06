from datetime import datetime
import time


def hora():
    return datetime.now()

# 36
h1 = hora()
time.sleep(2)

# 38
hf = hora
time.sleep(2)

# 40
h2 = hora()

time.sleep(2)


print(h1) # 18:15:00

print(hora)
print(hf) # hora

print(hf()) # erro
print(hora())

print(h2) # 18:15:05
        
