# django_bookproject  

自分が読みたい本に関する情報を集めた本のまとめサイトです。


# URL  
https://django-bookproject-portfolio.herokuapp.com/

# problem to solve  
このアプリケーションを使うことによって、ネットで書籍を購入する際の判断材料が増えるため、実際に購入して、読んだときのミスマッチが減ると考えられます。また、書籍の情報を詳しく記載した詳細画面にはGoogleからの検索結果から取り出した書籍の要約記事、youtubeから取り出した要約動画も抽出しているので、本を買わずに内容だけを効率に知りたい人にとっても価値があるアプリケーションになっています。

# Features  

このアプリケーションは詳細画面をよりセールスポイントにしており、詳細画面には楽天ブックス書籍検索API、youtube data api v3、 Custom Search API を使って、該当する書籍に関する情報を
多く収集することを可能にしました。また、トップページと詳細画面はさらなる機能追加も考えられるので、そこの機能のコードはオブジェクト指向の考え方を取り入れ、保守性、再利用性がある設計にしました。


# Requirement  

このアプリケーションを動かすのに必要なライブラリなどはrequirements.textに記載されています。
<br>
# Installation

requirements.textで列挙したライブラリなどのインストール方法

```bash
pip install -r requirements.txt
```

# Usage

django_bookprojectの基本的な使い方を説明する

```bash
git clone https://github.com/ussi-kousuke/django_bookproject.git
```
### 仮想環境の作成

```bash
$ python3 -m venv [newenvname]
$ source [newenvname]/bin/activate
```
### .envファイルの作成  
```bash
$ cd django_bookproject
$ touch .env
```
#### .envファイルの中身
```bash
SECRET_KEY='django-insecure-*********'

APP_ID='************'

YOUTUBE_DATE_API_ID='***************'

GOOGLE_API_KEY='*****************'

CUSTOM_SEARCH_ENGINE_ID='**************'

```
#### SECRET_KEYを再生成
```bash
$ python manage.py shell
```
```bash
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
'xxx-xxxx'
```

#### API_IDを生成  
[API詳細 楽天ブックス書籍検索API (version:2017-04-04)](https://webservice.rakuten.co.jp/documentation/books-book-search)

#### YOUTUBE_DATE_API_IDを生成  
[YouTube Data API v3 を使って YouTube 動画を検索する](https://qiita.com/koki_develop/items/4cd7de3898dae2c33f20)

#### GOOGLE_API_KEY、CUSTOM_SEARCH_ENGINE_IDを生成
[Custom Search APIを使ってGoogle検索結果を取得する](https://qiita.com/zak_y/items/42ca0f1ea14f7046108c)


## 必要なライブラリーをインストール
```bash
$ pip install -r requirements.txt
```

## 開発用サーバーの立ち上げ
```bash
$ python3 manage.py runserver
```

# Note

* 書籍を新規登録する際、本のタイトルは誤字、脱字がないように注意してください。
  Amazonなどから該当する書籍のタイトルをコピーすると確実です。

* 会員登録、ログインを行わないと書籍の新規登録、レビューはできないようにしており、ログイン画面に遷移するようにしています。






