# rateLimitTest.py

from ratelimit import limits, RateLimitException, sleep_and_retry
from backoff import on_exception, expo
import tqdm


# @on_exception(expo, RateLimitException, max_tries=8)
@sleep_and_retry
@limits(calls=4, period=4)
def doThing1(i):
	print('Thing1! ', i)


@sleep_and_retry
@limits(calls=4, period=4)
def doThing2(i):
	print('Thing2! ', i)


@sleep_and_retry
@limits(calls=4, period=4)
def doThing3(i):
	print('Thing3! ', i)


@sleep_and_retry
@limits(calls=4, period=4)
def doThing4(i):
	print('Thing4! ', i)


for index in tqdm.trange(0, 1000):
	doThing1(index)
	doThing2(index)
	doThing3(index)
	doThing4(index)

