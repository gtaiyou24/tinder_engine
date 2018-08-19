# -- coding: utf-8 --
import json
import os
import pandas as pd
from pandas import DataFrame
from datetime import datetime

from modules import tinder_api as api
from modules import features
from modules import config

'''
1. マッチしたユーザを取得
2. ファーストメッセージを送信していないユーザにメッセージを送信
3. マッチした新しいユーザをファイルに保存
'''

MSG = """{name}さん、はじめまして！

ここにマッチングしたユーザ宛に送るメッセージを書きましょう！
"""


def save_matching_users(new_matching_users, dump_file='matching_users.json', dump_dir='dumps/'):
    if not os.path.exists(dump_dir):
        os.makedirs(dump_dir)

    matching_users_file_path = dump_dir + dump_file

    if not os.path.exists(matching_users_file_path):
        f = open(matching_users_file_path, 'w')
        json.dump(
            new_matching_users, f,
            ensure_ascii=False, indent=4,
            sort_keys=True, separators=(',', ': ')
        )
    else:
        matching_users = json.load(open(matching_users_file_path, 'r'))
        matching_users.update(new_matching_users)
        json.dump(
            matching_users, open(matching_users_file_path, 'w'),
            ensure_ascii=False, indent=4,
            sort_keys=True, separators=(',', ': ')
        )
    return None

if __name__ == '__main__':
    if api.authverif() == True:
        print("Gathering Data on your matches...")

        updated_match_info = features.get_match_info()
        save_matching_users(updated_match_info)

        updated_match_df = DataFrame(updated_match_info)
        updated_match_df = updated_match_df.T

        first_message_indexs = [
            i for i, m in updated_match_df.messages.to_dict().items() if m == []]

        for i in first_message_indexs:
            name,  match_id = updated_match_df.loc[i, ['name', 'match_id']]
            msg = MSG.format(name=name)
            api.send_msg(match_id, msg)
    else:
        print("Something went wrong. You were not authorized.")
