import random

import requests


def test_set_view(dataset):
    r = requests.post(f'''{dataset['BASE_URL']}/api/v1/views/''', json={
        "value": {
            "movie_timestamp": dataset['RELATIVE_TIME'],
            "event_timestamp": dataset['ABSOLUTE_TIME'],
            "movie_id": str(dataset['MOVIE_UUID']),
            "user_id": dataset['USER_ID'],
            "genre_uuid": str(dataset['GENRE_UUID']),
        },
        "topic": dataset['TOPIC_MAP']['views']
    })
    assert r.status_code == 200
    assert r.json() == {
        "value": {
            "movie_timestamp": dataset['RELATIVE_TIME'],
            "event_timestamp": dataset['ABSOLUTE_TIME'],
            "movie_id": str(dataset['MOVIE_UUID']),
            "user_id": dataset['USER_ID'],
            "genre_uuid": str(dataset['GENRE_UUID']),
        },
        "topic": dataset['TOPIC_MAP']['views']
    }


def test_get_view(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/views/', json={
        "value": {
            "movie_timestamp": dataset['RELATIVE_TIME'],
            "event_timestamp": dataset['ABSOLUTE_TIME'],
            "movie_id": str(dataset['MOVIE_UUID']),
            "user_id": dataset['USER_ID'],
            "genre_uuid": str(dataset['GENRE_UUID'])
        },
        "topic": dataset['TOPIC_MAP']['views']
    })
    r = requests.get(f'{dataset["BASE_URL"]}/api/v1/views/{dataset["USER_ID"]}/{dataset["MOVIE_UUID"]}')
    assert r.status_code == 200
    assert r.json() == {
        "movie_timestamp": dataset['RELATIVE_TIME'],
        "event_timestamp": dataset['ABSOLUTE_TIME'],
        "movie_id": str(dataset['MOVIE_UUID']),
        "user_id": dataset['USER_ID'],
        "genre_uuid": str(dataset['GENRE_UUID'])
    }


def test_get_list_views(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/views/', json={
        "value": {
            "movie_timestamp": dataset['RELATIVE_TIME'],
            "event_timestamp": dataset['ABSOLUTE_TIME'],
            "movie_id": str(dataset['MOVIE_UUID']),
            "user_id": dataset['USER_ID'],
            "genre_uuid": str(dataset['GENRE_UUID'])
        },
        "topic": dataset['TOPIC_MAP']['views']
    })
    r = requests.get(f'{dataset["BASE_URL"]}/api/v1/views/{dataset["USER_ID"]}')
    assert r.status_code == 200
    assert dataset['USER_ID'] == r.json()[random.randint(0, len(r.json()) - 1)]['user_id']


def test_delete_view(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/views/', json={
        "value": {
            "movie_timestamp": dataset['RELATIVE_TIME'],
            "event_timestamp": dataset['ABSOLUTE_TIME'],
            "movie_id": str(dataset['MOVIE_UUID']),
            "user_id": dataset['USER_ID'],
            "genre_uuid": str(dataset['GENRE_UUID'])
        },
        "topic": dataset['TOPIC_MAP']['views']
    })
    r = requests.delete(f'{dataset["BASE_URL"]}/api/v1/views/{dataset["USER_ID"]}/{dataset["MOVIE_UUID"]}')
    assert r.status_code == 200
