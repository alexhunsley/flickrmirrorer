# universal_rate_limit.py
#

import time
from functools import wraps

current_milli_time = lambda: int(round(time.time() * 1000))

lastCallTime = 0

def universal_rate_limit(limitTimeSecs):
    class local:
        lastCallTime = 0

    def real_universal_rate_limit(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            nowTime = current_milli_time()

            global lastCallTime

            # millisSinceLastCall = nowTime - local.lastCallTime
            millisSinceLastCall = nowTime - lastCallTime

            waitTimeRequired = limitTimeSecs - millisSinceLastCall / 1000.0

            if waitTimeRequired > 0: 
                time.sleep(waitTimeRequired)

            # local.lastCallTime = current_milli_time()
            lastCallTime = current_milli_time()

            return function(*args, **kwargs)

        return wrapper
    return real_universal_rate_limit




@universal_rate_limit(2.0)
def say_whee(a, b):
    """Thing that says wheee!"""
    print("Whee!", a, b)

@universal_rate_limit(2.0)
def say_wheeB(a, b):
    """Thing that says wheee!"""
    print("WheeB!", a, b)

print(say_whee.__doc__)
print(say_whee.__name__)

for i in range(0, 10):
	say_whee(0,1)
	say_wheeB(0,1)
