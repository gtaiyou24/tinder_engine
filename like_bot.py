# -- coding: utf-8 --
import json
import os
import time
from datetime import datetime


from modules import features
from modules import tinder_api as api

'''
1. ユーザを取得
2. ユーザをLike
3. Likeしたユーザをファイルに保存
'''


def like_all_users():
    """全ユーザをlikeする関数.

    1. ユーザを取得.
    2. 取得したユーザをLike.
    """
    liked_users = {}

    while True:
        recommended = api.get_recommendations()
        features.pause()

        if 'results' not in recommended:
            print(recommended)
            break

        for user in recommended['results']:

            person_id = user['_id']  # This ID for looking up person
            res = api.like(person_id)

            if res['likes_remaining'] == 0:
                print('likes_remaining is zero...(><;)')
                print('stop like process.')
                return liked_users

            time.sleep(1)

            name = user['name']
            age = features.calculate_age(user['birth_date'])
            bio = user.get('bio', '')
            print("UserName: %s(%s) \n %s" % (name, age, bio[0:31]))

            try:
                liked_users[person_id] = {
                    "name": user['name'],
                    "common_like_count": user.get('common_like_count', 0),
                    "teasers": user.get('teasers', None),
                    "teaser": user.get('teaser', None),
                    "jobs": user.get('jobs', None),
                    "schools": user.get('schools', None),
                    "photos": features.get_photos(user),
                    "bio": user.get('bio', ''),
                    "gender": user.get('gender', None),
                    "avg_successRate": features.get_avg_successRate(user),
                    "age": features.calculate_age(user['birth_date']),
                    "distance": api.get_person(person_id)['results']['distance_mi'],
                    "liked_datetime": datetime.now().strftime("%Y/%m/%d %H:%M:%S")
                }
            except TypeError:
                print("TypeError Exception occured!!")
                continue
            except KeyError as e:
                print("KeyError Exception occured!!")
                print(e.message)
                continue

    return liked_users


def save_liked_users(new_liked_users, dump_file='liked_users.json', dump_dir='dumps/'):
    """likeしたユーザをファイルに保存する関数."""
    if not os.path.exists(dump_dir):
        os.makedirs(dump_dir)

    liked_users_file_path = dump_dir + dump_file

    if not os.path.exists(liked_users_file_path):
        f = open(liked_users_file_path, 'w')
        json.dump(
            new_liked_users, f,
            ensure_ascii=False, indent=4,
            sort_keys=True, separators=(',', ': ')
        )
    else:
        liked_users = json.load(open(liked_users_file_path, 'r'))
        liked_users.update(new_liked_users)
        json.dump(
            liked_users, open(liked_users_file_path, 'w'),
            ensure_ascii=False, indent=4,
            sort_keys=True, separators=(',', ': ')
        )
    return None


if __name__ == '__main__':
    if api.authverif() is True:
        print("Starting like_all_users on bot...")
        liked_users = like_all_users()
        save_liked_users(liked_users)
    else:
        print("Something went wrong. You were not authorized.")
