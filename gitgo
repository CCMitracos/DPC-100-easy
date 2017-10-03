# DPC 100 [E]
# Sleep Cycle Estimator


print "Enter wakeup time military style"
print "ex: 6:20am = 0620"

wake_up = int(raw_input("type a number less than 2400 >> "))

hours = wake_up/100
minutes = wake_up - hours*100
wtime = hours + minutes/60.0
for k in range(1,7):
  utime = wtime - k*1.5

  if (utime < 0):
    utime += 24
  else:
    utime += 0

  hours2 = int(utime/1)
  minutes2 = int((utime - hours2)*60)

  if (hours2 >12):
    hours2 -= 12
    am = False
  elif (hours2 == 0):
    hours2 += 12
    am = True
  else:
    am = True

  if (am == True):
    mthing = "am"
  else:
    mthing = "pm"

  if (minutes2 == 0):
    minutes2 = "00"
    print "%d:%s %s" %(hours2,minutes2,mthing)
  else:
    print "%d:%d %s" %(hours2,minutes2,mthing)

