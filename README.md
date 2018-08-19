# Tinder Engine

tinder_engineモジュールの構成
```
tinder_engine
 |
 |----analytics: 分析用のフォルダ
 |
 |----dumps: データの出力先フォルダ
 |
 |----modules
 |       |
 |       |--__init__.py
 |       |--fb_auth_token.py
 |       |--features.py
 |       |--README.md
 |       |--tinder_api.py
 |
 |--like_bot.py
 |--README.md
 |--requirements.txt
```

## How to use?
### 1. 必要なパッケージをインストール

```
pip install -r requirements.txt
```

### 2. `modules`フォルダに`config.py`を作成する
新規作成する`config.py`ファイルは以下のコードである

```python
from modules import fb_auth_token

fb_username = """Your facebook email"""
fb_password = """Your facebook password"""
fb_access_token = fb_auth_token.get_fb_access_token(fb_username, fb_password)
fb_user_id = fb_auth_token.get_fb_id(fb_access_token)
host = 'https://api.gotinder.com'
```

### 3. スクリプトを実行する
`python like_bot.py`で自動LikeとLikeしたユーザをjsonで保存

---
## How to develop this package
### (1. VirtualBox&Vagrantのインストール)
Vagrantの公式ページの[ダウンロードページ](https://www.vagrantup.com/downloads.html)にアクセスして使っている環境に合うインストーラーを選択してダウンロードする。そしたら、インストーラーが自動的に`vagrant`コマンドのパスを通してくれる。

VirtualBoxのバージョンは`5.1.30`です。

VirtualBoxのインストールが完了したらVagrantをインストールする
```
brew cask install vagrant
brew cask install vagrant-manager
```

### 2. 開発

まずはじめにvagrantを起動する。(初回はプロビジョニングも行うため20分ほど時間がかかる)
```
$ cd /path/to/tinder_engine
$ vagrant up
```

起動したら、ローカル環境で実装しpythonファイルの実行は仮想環境で行う。
```
$ vagrant ssh
[vagrant@localhost ~]$ cd /vagrant_data/
[vagrant@localhost ~]$ python like_bot.py
```

一通りの開発が済んだらローカル環境でpushする。
