import uuid
import random
import string

import pytest


@pytest.fixture()
def dataset():
    def _randstr(strlen: int) -> str:
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(strlen))

    return {'TOPIC_MAP': {
        "views": "ugcViews",
        "movie_likes": "ugcMovie_likes",
        "review_likes": "ugcReview_likes",
        "reviews": "ugcReviews",
        "bookmarks": "ugcBookmarks",
        "genre_likes": "ugcGenre_likes"
    },
        'USER_ID': random.randint(1, 1000),
        'MOVIE_UUID': uuid.uuid4(),
        'REVIEW_UUID': uuid.uuid4(),
        'GENRE_UUID': uuid.uuid4(),
        'ABSOLUTE_TIME': random.randint(633801229, 1675180434),
        'RELATIVE_TIME': random.randint(1, 86400),
        'BASE_URL': 'http://127.0.0.1:8000',
        'RATING': random.randint(0, 10),
        'REVIEW_TITLE': _randstr(20),
        'REVIEW_TEXT': _randstr(150)

    }
