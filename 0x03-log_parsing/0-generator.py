#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())

    ip_parts = [
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
        random.randint(1, 255),
    ]
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    content_length = random.randint(1, 1024)
    current_time = datetime.datetime.now()

    log_entry = (
        '{:d}.{:d}.{:d}.{:d} - [{}] "GET /projects/260 HTTP/1.1" {} {}'
    ).format(
        ip_parts[0],
        ip_parts[1],
        ip_parts[2],
        ip_parts[3],
        current_time,
        status_code,
        content_length,
    )

    sys.stdout.write(log_entry + "\n")
    sys.stdout.flush()
