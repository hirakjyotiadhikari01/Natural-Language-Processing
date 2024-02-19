import time
sec = 42 * 60 + 42 # number of seconds in 42 minutes 42 seconds
result = time.strftime("%H:%M:%S", time.gmtime(sec)) # convert seconds to HH:MM:SS format
print(result) # print the result
