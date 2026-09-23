# personal-homepage · Django 个人主页

> Django 入门期的练手工程：一个能显示时间的个人主页，外加图片与文案的后台录入。

**维护状态**：学习作品，已归档。

---

## 一、这是个什么项目

这是跟着《Django 入门》系教程搭出来的第一个站点，主要目的不是做产品，而是把
**模型 → 视图 → 模板 → 路由 → 后台**这条链路跑通一遍。

代码里能看到几个经典的"教科书"视图：

| 视图 | 路由 | 作用 |
|---|---|---|
| `hello` | `/` 与 `/hello/` | 取 `Image(id=1)` + `Text(id=1)` 渲染 `index.html`，即主页内容由后台控制 |
| `current_datetime` | `/time/` | 直接返回当前时间的 HTML |
| `hours_ahead` | `/time/plus/<n>/` | 返回 N 小时后的时间，带参数校验（`ValueError` → 404） |

## 二、数据模型

| 模型 | 字段 | 用途 |
|---|---|---|
| `Image` | `img`（ImageField） | 主页图片，后台上传 |
| `Text` | `text`（CharField 1024） | 主页文案 |

## 三、技术栈

| 项 | 说明 |
|---|---|
| 语言 | Python **2.7**（已 EOL） |
| 框架 | Django **1.7 / 1.8** |
| 数据库 | SQLite（`db.sqlite3`） |
| 后台 | Admin + `bootstrap_admin` 皮肤 |
| 静态资源 | `media/` 上传目录 + 模板目录 |

## 四、目录结构

```
mysite/
├── manage.py
├── db.sqlite3
├── media/img/                  后台上传的图片
└── mysite/
    ├── settings.py             配置（含 SECRET_KEY）
    ├── urls.py                 路由
    ├── views.py                hello / current_datetime / hours_ahead
    ├── models.py               Image / Text
    ├── admin.py                两个模型的后台注册
    ├── templates/index.html    主页模板
    └── static/
```

## 五、本地运行

```bash
pyenv local 2.7.18          # 或用 conda 起 Python 2.7 环境
pip install "Django<1.9" Pillow bootstrap-admin

python manage.py runserver 0.0.0.0:8000
```

访问：

- `http://127.0.0.1:8000/` —— 主页（先到 `/admin` 传一张图、写一条文案，否则会因查不到 `id=1` 报错）
- `http://127.0.0.1:8000/time/` —— 当前时间
- `http://127.0.0.1:8000/time/plus/3/` —— 3 小时后的时间
- `http://127.0.0.1:8000/admin/` —— 后台

## 六、已知问题

- 主页视图用 `objects.get(id=1)` 硬取第一条，`id=1` 不存在就 500 —— 属于练习写法，没做兜底
- `DEBUG = True`，`SECRET_KEY` 明文入库，不能用于任何线上环境
- 仓库内的 `db.sqlite3` 含当年后台账号信息，已公开，相关密码请勿复用

## 七、许可

学习用途代码，随意参考。

---

## 免费赞助

这套东西是白送的：**不收费、不锁功能、不塞广告**。如果它帮你省了时间、或者多赚了钱，
可以扫码请 Emperor 喝杯茶 —— 完全自愿，不打赏也照样用、照样更新。

<p align="center">
  <img src="assets/sponsor-qr.png" alt="免费赞助 · Emperor、| 说事-不闲聊" width="280">
</p>

<p align="center"><sub>扫码可备注一句你在做什么类目，方便后续针对性更新</sub></p>
