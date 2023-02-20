import os
import json


topics = json.loads(os.getenv('TOPICS'))

for topic in topics:
    with open(f'./utils/conf/topics/{topic}', mode='w', encoding='UTF-8') as file:
        pass

