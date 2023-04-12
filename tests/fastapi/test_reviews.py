import random

import requests


def test_review_set(dataset):
    r = requests.post(f'{dataset["BASE_URL"]}/api/v1/reviews', json={
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "movie_uuid": str(dataset['MOVIE_UUID']),
            "title": dataset['REVIEW_TITLE'],
            "text": dataset['REVIEW_TEXT'],
            "review_uuid": str(dataset['REVIEW_UUID'])

        },
        "topic": dataset['TOPIC_MAP']['reviews']
    })

    assert r.status_code == 200
    assert r.json() == {
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "movie_uuid": str(dataset['MOVIE_UUID']),
            "title": dataset['REVIEW_TITLE'],
            "text": dataset['REVIEW_TEXT'],
            "review_uuid": str(dataset['REVIEW_UUID'])

        },
        "topic": dataset['TOPIC_MAP']['reviews']
    }


def test_review_list(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/reviews', json={
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "movie_uuid": str(dataset['MOVIE_UUID']),
            "title": dataset['REVIEW_TITLE'],
            "text": dataset['REVIEW_TEXT'],
            "review_uuid": str(dataset['REVIEW_UUID'])

        },
        "topic": dataset['TOPIC_MAP']['reviews']
    })
    r = requests.get(f'{dataset["BASE_URL"]}/api/v1/reviews/{dataset["USER_ID"]}')
    assert r.status_code == 200
    assert dataset['USER_ID'] == r.json()[random.randint(0, len(r.json()) - 1)]['user_id']


def test_review_get(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/reviews', json={
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "movie_uuid": str(dataset['MOVIE_UUID']),
            "title": dataset['REVIEW_TITLE'],
            "text": dataset['REVIEW_TEXT'],
            "review_uuid": str(dataset['REVIEW_UUID'])

        },
        "topic": dataset['TOPIC_MAP']['reviews']
    })

    r = requests.get(f'{dataset["BASE_URL"]}/api/v1/reviews/{dataset["USER_ID"]}/{dataset["REVIEW_UUID"]}')
    assert r.status_code == 200
    assert r.json() == {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "movie_uuid": str(dataset['MOVIE_UUID']),
            "title": dataset['REVIEW_TITLE'],
            "text": dataset['REVIEW_TEXT'],
            "review_uuid": str(dataset['REVIEW_UUID'])

        }


def test_review_delete(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/reviews', json={
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "movie_uuid": str(dataset['MOVIE_UUID']),
            "title": dataset['REVIEW_TITLE'],
            "text": dataset['REVIEW_TEXT'],
            "review_uuid": str(dataset['REVIEW_UUID'])

        },
        "topic": dataset['TOPIC_MAP']['reviews']
    })
    r = requests.delete(f'{dataset["BASE_URL"]}/api/v1/reviews/{dataset["USER_ID"]}/{dataset["REVIEW_UUID"]}')
    assert r.status_code == 200

