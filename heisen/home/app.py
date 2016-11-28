import time

from rq import Queue
from redis import Redis
from tasks import updater


redis_conn = Redis()
queue = Queue(connection=redis_conn)
job = queue.enqueue(updater)
print(job.result)
