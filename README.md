# 🧠 RAG Assistant (Retrieval-Augmented Generation)

RAG-система для ответов на вопросы по документации с использованием LangGraph, embeddings и LLM.

---

## 🚀 О проекте

В проекте реализован ассистент, который:

* принимает вопрос пользователя
* ищет релевантные документы (retrieval)
* проверяет качество найденного контекста
* при необходимости переписывает запрос (query rewrite)
* генерирует ответ на основе найденной информации

Основная цель — уменьшение галлюцинаций и повышение точности ответов за счёт retrieval.

---

## 🏗 Архитектура

```text
User Question
      ↓
generate_query_or_respond
      ↓
retrieve (vector search)
      ↓
grade_documents
   ├── good → generate_answer
   └── bad  → rewrite_question → повтор
      ↓
generate_answer
      ↓
Final Answer + Sources
```

Особенность:

* добавлен механизм **query rewriting**
* ограничено количество rewrite (защита от бесконечного цикла)

---

## ⚙️ Используемые технологии

* Python
* LangChain / LangGraph
* FAISS / InMemory Vector Store
* sentence-transformers / OpenAI embeddings
* Hugging Face / LLM API

---

## 📂 Структура проекта

```text
Rag-Assistence/
├── src/
│   ├── graph.py                 # построение графа
│   ├── state.py                 # состояние графа (messages + rewrite_count)
│   ├── retriever_tool.py        # поиск документов
│   ├── generation/
│   │   ├── grade.py             # оценка релевантности
│   │   ├── rewrite.py           # переписывание запроса
│   │   └── generation_answer.py # генерация ответа
│   ├── processing/
│   │   ├── chunking.py          # разбиение документов
│   │   └── vectorstore.py       # создание векторного индекса
│   └── response/
│       └── generater.py         # основной LLM вызов
├── config.py
├── main.py
└── README.md
```

---

## ▶️ Запуск

```bash
pip install -r requirements.txt
```

```bash
python main.py
```

Пример:

```python
result = app.invoke({
    "messages": [("user", "What is reward hacking?")],
    "rewrite_count": 0
})
```

---

## 🧪 Реализованные фичи

* ✅ Chunking документов
* ✅ Embeddings + vector search
* ✅ Retrieval (top-k)
* ✅ Query rewriting
* ✅ Grading релевантности
* ✅ Ограничение rewrite (anti-loop)
* ✅ Генерация ответа с контекстом

---

## 📊 Ограничения текущей версии

* используется небольшой набор документов
* нет автоматической оценки (evaluation)
* индекс пересоздаётся при запуске
* нет reranker

---

## 🚀 Дальнейшие улучшения

* добавить FAISS/Chroma с сохранением индекса
* внедрить reranking
* провести эксперименты:

  * chunk size
  * top-k
  * embedding модели
* добавить evaluation (retrieval accuracy, hallucination rate)
* сделать UI (Streamlit)

---

## 📌 Вывод

Проект демонстрирует:

* построение RAG pipeline
* работу с retrieval и LLM
* понимание проблем (галлюцинации, нерелевантный контекст)
* базовые техники их решения (grading, rewriting)

---

## 📬 Контакты

GitHub: https://github.com/Stolide-anseed
