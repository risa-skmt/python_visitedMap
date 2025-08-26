# python_visitedMap

１．開発作業は[venv\Scripts\activate]で仮想環境に入って行う
２．ライブラリの追加後は[pip freeze > requirements.txt]で requirements.txt に変更を反映
３．github への push は以下コマンド
git add requirements.txt app.py
git commit -m "update app and requirements"
git push

<!-- my_travel_app/
│
├─ app.py                # Flaskのメインアプリ
├─ places.db             # SQLiteのデータベース（初回起動で生成）
│
├─ templates/            # HTMLテンプレート置き場
│   ├─ index.html        # メインページ（フォーム＋地図表示）
│   └─ map.html          # foliumで生成する地図を埋め込むHTML
│
├─ static/               # CSS・JavaScript・画像など
│   ├─ style.css         # 任意のスタイル
│   └─ script.js         # Autocompleteやフォーム補助のJS
│
└─ requirements.txt      # 使用するPythonライブラリ一覧
 -->
