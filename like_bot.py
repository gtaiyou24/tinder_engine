# -- coding: utf-8 --
import json
import os
import pandas as pd
from datetime import datetime

from modules import tinder_api as api
from modules import features
from modules import config

'''
1. ユーザを取得
2. ユーザをLike
3. Likeしたユーザをファイルに保存
'''


def like_all_users():
    liked_users = {}

    while True:
        recommended = api.get_recommendations()
        features.pause()

        if 'results' not in recommended:
            print(recommended)
            break

        for user in recommended['results']:

            person_id = user['_id']  # This ID for looking up person
            api.like(person_id)

            name = user['name']
            age = features.calculate_age(user['birth_date'])
            bio = user.get('bio', '')
            print("UserName: %s(%s) \n %s" % (name, age, bio[0:31]))

            liked_users[person_id] = {
                "name": user['name'],
                "common_like_count": user.get('common_like_count', 0),
                "teasers": user['teasers'],
                "teaser": user['teaser'],
                "jobs": user['jobs'],
                "schools": user['schools'],
                "photos": features.get_photos(user),
                "bio": user.get('bio', ''),
                "gender": user['gender'],
                "avg_successRate": features.get_avg_successRate(user),
                "age": features.calculate_age(user['birth_date']),
                "distance": api.get_person(person_id)['results']['distance_mi'],
                "liked_datetime": datetime.now().strftime("%Y/%m/%d %H:%M:%S")
            }
    return liked_users


def save_liked_users(new_liked_users, dump_file='liked_users.json', dump_dir='dumps/'):
    if not os.path.exists(dump_dir): os.makedirs(dump_dir)

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
    if api.authverif() == True:
        print("Starting like_all_users on bot...")
        liked_users = like_all_users()
        save_liked_users(liked_users)
    else:
        print("Something went wrong. You were not authorized.")
