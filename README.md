### DBにテーブル作成
- models.pyで定義
```python
class TestModel(models.Model):
    memo = models.TextField(
        null=True,
        blank=True
    )
    insert_date = models.DateTimeField(
        auto_now_add=True
    )

    # ここで返す項目が大見出しになる
    def __str__(self):
        return self.memo

    class Meta:
        # memo項目でソート
        ordering = ["memo"]
```

- 下記コマンドでテーブル作成
```powershell
python manage.py makemigrations
python manage.py migrate
# 
```

### 管理画面

###### ルートユーザの作成
```powershell
python manage.py createsuperuser
```
###### 管理画面に入る
```powershell
# サーバー起動
python manage.py runserver
# http://127.0.0.1:8000/admin/ にアクセスしてログイン
```

### templatesの作成
- アプリディレクトリ直下にtemplatesフォルダを作成しhtmlファイルを作成
- views.pyとurls.pyに呼び出すmodelを定義
- 下記のようにsettings.pyのDIRSにtemplatesの設定を定義
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### リダイレクト
###### クラスベースでviews.pyを定義してる場合
- reverse_lazyを使う
```python
# 例
import django.urls import reverse_lazy


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
```