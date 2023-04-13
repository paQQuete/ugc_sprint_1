import random

import requests


def test_set(dataset):
    r = requests.post(f'http://ctube-study.ru:8080/api/v1/bookmarks', json={
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "movie_uuid": str(dataset['MOVIE_UUID'])
        },
        "topic": dataset['TOPIC_MAP']['bookmarks']
    })

    assert r.status_code == 200
    assert r.json() == {
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "movie_uuid": str(dataset['MOVIE_UUID'])
        },
        "topic": dataset['TOPIC_MAP']['bookmarks']
    }


def test_get_list(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/bookmarks', json={
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "movie_uuid": str(dataset['MOVIE_UUID'])
        },
        "topic": dataset['TOPIC_MAP']['bookmarks']
    })
    r = requests.get(f"{dataset['BASE_URL']}/api/v1/bookmarks/{dataset['USER_ID']}")
    assert r.status_code == 200
    assert dataset['USER_ID'] == r.json()[random.randint(0, len(r.json())-1)]['user_id']


def test_get_bookmark(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/bookmarks', json={
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "movie_uuid": str(dataset['MOVIE_UUID'])
        },
        "topic": dataset['TOPIC_MAP']['bookmarks']
    })
    r = requests.get(f"{dataset['BASE_URL']}/api/v1/bookmarks/{dataset['USER_ID']}/{dataset['MOVIE_UUID']}")
    assert r.status_code == 200
    assert dataset['USER_ID'] == r.json()['user_id']
    assert str(dataset['MOVIE_UUID']) == r.json()['movie_uuid']


def test_del_bookmark(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/bookmarks', json={
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "movie_uuid": str(dataset['MOVIE_UUID'])
        },
        "topic": dataset['TOPIC_MAP']['bookmarks']
    })
    r = requests.delete(f"{dataset['BASE_URL']}/api/v1/bookmarks/{dataset['USER_ID']}/{dataset['MOVIE_UUID']}")
    assert r.status_code == 200