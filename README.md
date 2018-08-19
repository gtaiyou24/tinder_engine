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

---
## what is Tinder Engine?

本パッケージでは、**マッチング系サービスTinderにおける男性ユーザの女性との面会率を最大にする**ための分析基盤となるものである。マッチングサービスは所与の時間・選好・可処分所得のもとで新たな人脈ネットワークを拡大するためのサービスであり、そのネットワークは①ビジネス型②余暇型の二つがあると考えられる。前者のビジネス型人脈ネットワークは、相互に接続する主体が所得・利潤の最大化を実現するためのネットワークであり、後者の余暇型人脈ネットワークは余暇に自分の効用を最大化するためのネットワークであり、友達/恋人ネットワークがこれに該当する。Tinderはよって、Tinderは余暇型の人脈ネットワークを拡大するためのサービスである。

* どんなサービスなのか？
    * 男性の面会率を最大にするマッチング支援サービス
    * マッチングとは？
    * 男性って？
        * 効用関数は？
        * 制約式は？
        * どのような"情報"を用いて、合理的な"意思決定"を行うのか？
        * マッチング系サービスにおける男性の問題(=需要)
            * $Y_{t}=a_{ t }X_{ t-1 }\\X_{0} = ライクしたユーザ数$
                1. $M_{ マッチ数 } = a_{1}X_{ 0 }$
                2. $C_{ アポイント契約数 } = a_{2}M_{ マッチ数 }$
                3. $S_{ 面会人数 } = a_{3}C_{ アポイント契約数 }$
                4. $Y_{ 有彼女数 } = a_{4}S_{ 面会人数 }$
            * なぜそのような問題が起きているのか？
            * どのようにすれば解決できる？
* なぜサービスを作るのか？
* どのように作るのか？
    * 本サービスは上記の問題を解決できるか？
