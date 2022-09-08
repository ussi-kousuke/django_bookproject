# django_bookproject  

読みたい本や読んだ本を保存できる本棚アプリケーションです。


# URL  



# Features  

このアプリケーションは詳細画面をよりセールスポイントにしており、詳細画面には楽天ブックス書籍検索API、youtube data api v3、 Custom Search API を使って、該当する書籍に関する情報を
多く収集することを可能にしました。また、詳細画面はさらなる機能追加も考えられるので、詳細画面の機能のコードはオブジェクト指向の考え方を取り入れ、保守性、再利用性がある設計にしました。

# Requirement  

このアプリケーションを動かすのに必要なライブラリなどはrequirements.textに記載されています。

# Installation

requirement.textで列挙したライブラリなどのインストール方法

```bash
pip install -r requirements.txt
```

# Usage

DEMOの実行方法など、"hoge"の基本的な使い方を説明する

```bash
git clone https://github.com/ussi-kousuke/django_bookproject.git
```
### 仮想環境の作成

```bash
python3 -m venv [newenvname]
source [newenvname]/bin/activate
```

# Note

* 書籍を新規登録する際、本のタイトルは誤字、脱字がないように注意してください。
  Amazonなどから該当する書籍のタイトルをコピーすると確実です。

* 会員登録、ログインを行わないと書籍の新規登録、レビューはできないようにしています。






