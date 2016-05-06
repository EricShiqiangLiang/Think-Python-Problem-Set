import time
t = time.time()
days = t // (60*60*24)
t = t - days*60*60*24
print (days)
hours = t // (60*60)
t = t - hours*60*60
minutes = t // 60
t = t - minutes*60
seconds = t // 1

print(hours, minutes, seconds)
