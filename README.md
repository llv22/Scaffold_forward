<!-- markdownlint-disable MD029 -->
# README for Rebuttal

This is the project used by Orlando and Yue for collecting support data of EMNLP 2024. We cloned data from original [Scaffold](https://github.com/leixy20/Scaffold/tree/main) and added code to support call Qianwen.

## 1. Environment preparation

```bash
pip install -r requirements.txt
```

## 2. Scaffolding

preprocessing for data run

```bash
python image_processor.py --img_dir "<your folder input>"
```

The prompt refer to Line 109 and Line 122 in [call-api.py](call-api.py).

## 3, QuestionVL API

1. create .env on the root folder add

```txt
DASHSCOPE_API_KEY=<Your Key>
```

2. Sample code get_response() in qianwen.py

## Author

By Fan, Yue and Lei, Ding(Orlando), 2024@June.
