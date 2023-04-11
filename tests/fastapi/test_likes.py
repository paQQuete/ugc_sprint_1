import random

import requests


def test_set_movie(dataset):
    r = requests.post(f'{dataset["BASE_URL"]}/api/v1/likes/movie/', json={
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "movie_uuid": str(dataset['MOVIE_UUID']),
            "rating": dataset['RATING']
        },
        "topic": dataset['TOPIC_MAP']['movie_likes']
    })

    assert r.status_code == 200
    assert r.json() == {
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "movie_uuid": str(dataset['MOVIE_UUID']),
            "rating": dataset['RATING']
        },
        "topic": dataset['TOPIC_MAP']['movie_likes']
    }


def test_set_review(dataset):
    r = requests.post(f'{dataset["BASE_URL"]}/api/v1/likes/review/', json={
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "review_uuid": str(dataset['REVIEW_UUID']),
            "rating": dataset['RATING']
        },
        "topic": dataset['TOPIC_MAP']['review_likes']
    })

    assert r.status_code == 200
    assert r.json() == {
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "review_uuid": str(dataset['REVIEW_UUID']),
            "rating": dataset['RATING']
        },
        "topic": dataset['TOPIC_MAP']['review_likes']
    }


def test_set_genre(dataset):
    r = requests.post(f'{dataset["BASE_URL"]}/api/v1/likes/genre/', json={
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "genre_uuid": str(dataset['GENRE_UUID']),
            "rating": dataset['RATING']
        },
        "topic": dataset['TOPIC_MAP']['genre_likes']
    })

    assert r.status_code == 200
    assert r.json() == {
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "genre_uuid": str(dataset['GENRE_UUID']),
            "rating": dataset['RATING']
        },
        "topic": dataset['TOPIC_MAP']['genre_likes']
    }


def test_movie_list(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/likes/movie/', json={
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "movie_uuid": str(dataset['MOVIE_UUID']),
            "rating": dataset['RATING'],
            "genre_uuid": str(dataset['GENRE_UUID'])
        },
        "topic": dataset['TOPIC_MAP']['movie_likes']
    })

    r = requests.get(f'{dataset["BASE_URL"]}/api/v1/likes/movie/{dataset["USER_ID"]}')

    assert r.status_code == 200
    assert dataset['USER_ID'] == r.json()[random.randint(0, len(r.json()) - 1)]['user_id']


def test_review_list(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/likes/review/', json={
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "review_uuid": str(dataset['REVIEW_UUID']),
            "rating": dataset['RATING']
        },
        "topic": dataset['TOPIC_MAP']['review_likes']
    })

    r = requests.get(f'{dataset["BASE_URL"]}/api/v1/likes/review/{dataset["USER_ID"]}')

    assert r.status_code == 200
    assert dataset['USER_ID'] == r.json()[random.randint(0, len(r.json()) - 1)]['user_id']


def test_genre_list(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/likes/genre/', json={
        "value": {
            "created_at": dataset['ABSOLUTE_TIME'],
            "updated_at": dataset['ABSOLUTE_TIME'],
            "user_id": dataset['USER_ID'],
            "genre_uuid": str(dataset['GENRE_UUID']),
            "rating": dataset['RATING']
        },
        "topic": dataset['TOPIC_MAP']['genre_likes']
    })

    r = requests.get(f'{dataset["BASE_URL"]}/api/v1/likes/genre/{dataset["USER_ID"]}')

    assert r.status_code == 200
    assert dataset['USER_ID'] == r.json()[random.randint(0, len(r.json()) - 1)]['user_id']


def test_movie_like(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/likes/movie/',
                  json={
                      "value": {
                          "created_at": dataset['ABSOLUTE_TIME'],
                          "updated_at": dataset['ABSOLUTE_TIME'],
                          "user_id": dataset['USER_ID'],
                          "movie_uuid": str(dataset['MOVIE_UUID']),
                          "rating": dataset['RATING']
                      },
                      "topic": dataset['TOPIC_MAP']['movie_likes']
                  })

    r = requests.get(f'{dataset["BASE_URL"]}/api/v1/likes/movie/{dataset["USER_ID"]}/{dataset["MOVIE_UUID"]}')

    assert r.status_code == 200
    assert r.json() == {
        "created_at": dataset['ABSOLUTE_TIME'],
        "updated_at": dataset['ABSOLUTE_TIME'],
        "user_id": dataset['USER_ID'],
        "movie_uuid": str(dataset['MOVIE_UUID']),
        "rating": dataset['RATING']
    }


def test_review_like(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/likes/review/',
                  json={
                      "value": {
                          "created_at": dataset['ABSOLUTE_TIME'],
                          "updated_at": dataset['ABSOLUTE_TIME'],
                          "user_id": dataset['USER_ID'],
                          "review_uuid": str(dataset['REVIEW_UUID']),
                          "rating": dataset['RATING']
                      },
                      "topic": dataset['TOPIC_MAP']['review_likes']
                  })

    r = requests.get(f'{dataset["BASE_URL"]}/api/v1/likes/review/{dataset["USER_ID"]}/{dataset["REVIEW_UUID"]}')

    assert r.status_code == 200
    assert r.json() == {
        "created_at": dataset['ABSOLUTE_TIME'],
        "updated_at": dataset['ABSOLUTE_TIME'],
        "user_id": dataset['USER_ID'],
        "review_uuid": str(dataset['REVIEW_UUID']),
        "rating": dataset['RATING']
    }


def test_genre_like(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/likes/genre/',
                  json={
                      "value": {
                          "created_at": dataset['ABSOLUTE_TIME'],
                          "updated_at": dataset['ABSOLUTE_TIME'],
                          "user_id": dataset['USER_ID'],
                          "genre_uuid": str(dataset['GENRE_UUID']),
                          "rating": dataset['RATING']
                      },
                      "topic": dataset['TOPIC_MAP']['genre_likes']
                  })

    r = requests.get(f'{dataset["BASE_URL"]}/api/v1/likes/genre/{dataset["USER_ID"]}/{dataset["GENRE_UUID"]}')

    assert r.status_code == 200
    assert r.json() == {
        "created_at": dataset['ABSOLUTE_TIME'],
        "updated_at": dataset['ABSOLUTE_TIME'],
        "user_id": dataset['USER_ID'],
        "genre_uuid": str(dataset['GENRE_UUID']),
        "rating": dataset['RATING']
    }


def test_movie_delete(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/likes/movie/',
                  json={
                      "value": {
                          "created_at": dataset['ABSOLUTE_TIME'],
                          "updated_at": dataset['ABSOLUTE_TIME'],
                          "user_id": dataset['USER_ID'],
                          "movie_uuid": str(dataset['MOVIE_UUID']),
                          "rating": dataset['RATING']
                      },
                      "topic": dataset['TOPIC_MAP']['movie_likes']
                  })

    r = requests.delete(f'{dataset["BASE_URL"]}/api/v1/likes/movie/{dataset["USER_ID"]}/{dataset["MOVIE_UUID"]}')

    assert r.status_code == 200


def test_review_delete(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/likes/review/',
                  json={
                      "value": {
                          "created_at": dataset['ABSOLUTE_TIME'],
                          "updated_at": dataset['ABSOLUTE_TIME'],
                          "user_id": dataset['USER_ID'],
                          "review_uuid": str(dataset['REVIEW_UUID']),
                          "rating": dataset['RATING']
                      },
                      "topic": dataset['TOPIC_MAP']['review_likes']
                  })

    r = requests.delete(f'{dataset["BASE_URL"]}/api/v1/likes/review/{dataset["USER_ID"]}/{dataset["REVIEW_UUID"]}')

    assert r.status_code == 200


def test_genre_delete(dataset):
    requests.post(f'{dataset["BASE_URL"]}/api/v1/likes/genre/',
                  json={
                      "value": {
                          "created_at": dataset['ABSOLUTE_TIME'],
                          "updated_at": dataset['ABSOLUTE_TIME'],
                          "user_id": dataset['USER_ID'],
                          "genre_uuid": str(dataset['GENRE_UUID']),
                          "rating": dataset['RATING']
                      },
                      "topic": dataset['TOPIC_MAP']['genre_likes']
                  })

    r = requests.delete(f'{dataset["BASE_URL"]}/api/v1/likes/genre/{dataset["USER_ID"]}/{dataset["GENRE_UUID"]}')

    assert r.status_code == 200
