# Telegram Post Parser Bot 🤖
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-green.svg)](https://docs.aiogram.dev/)
[![Google Sheets API](https://img.shields.io/badge/Google%20Sheets-API-brightgreen.svg)](https://developers.google.com/sheets/api)
[![Regular Expressions](https://img.shields.io/badge/Regex-Python-orange.svg)](https://docs.python.org/3/library/re.html)

Автоматизированный бот для парсинга постов из Telegram-каналов и сохранения структурированной информации в Google Sheets.

## 📋 Описание проекта

Бот мониторит указанные Telegram-каналы, ловит посты с определёнными хэштегами, извлекает из них структурированные данные (имя, тип события, даты) и автоматически добавляет их в Google Таблицу. Идеально подходит для автоматизации учёта отпусков, больничных, командировок и других событий команды.

### 💡 Какую проблему решает

Ручное ведение таблицы отпусков/больничных занимает время и подвержено ошибкам. Этот бот:
- Автоматически ловит все посты с нужными хэштегами
- Извлекает даты и имена с помощью регулярных выражений
- Структурирует данные и сохраняет в таблицу
- Работает в фоновом режиме, пока запущен

## 🚀 Возможности

- ✅ Мониторинг нескольких Telegram-каналов одновременно
- ✅ Фильтрация постов по хэштегам (настраивается через `.env`)
- ✅ Извлечение имён, типов событий и дат из текста
- ✅ Поддержка различных форматов дат:
    - Одна дата: `23 июня`
    - Диапазон в одном месяце: `23–27 июля`
    - Диапазон через разные месяцы: `23 июня – 3 июля`
- ✅ Автоматическая запись в Google Sheets с накоплением данных

## 🛠 Технологии

- **Python 3.10+** — основной язык
- **aiogram 3.x** — асинхронный фреймворк для Telegram Bot API
- **gspread** — работа с Google Sheets API
- **google-auth** — авторизация через сервисный аккаунт Google
- **pydantic-settings** — валидация и загрузка конфигурации из `.env`
- **re (regular expressions)** — парсинг текста и извлечение данных

## ⚙️ Установка и запуск

### 1. Клонирование репозитория

git clone https://github.com/trcnko/telegram-post-parser.git cd telegram-post-parser

### 2. Создание виртуального окружения

python3 -m venv venv
source venv/bin/activate  # Linux/macOS
## или
venv\Scripts\activate     # Windows

### 3. Установка зависимостей
pip install -r requirements.txt

### 4. Настройка Google Sheets API
Создай проект в Google Cloud Console
Включи Google Sheets API и Google Drive API
Создай сервисный аккаунт и скачай credentials.json
Поделись таблицей с email из credentials.json (права "Редактор")
Положи credentials.json в корень проекта

### 5. Настройка конфигурации
BOT_TOKEN=твой_токен_бота_от_BotFather
GOOGLE_SHEET_ID=ID_таблицы_из_URL
CREDENTIALS_FILE=credentials.json
SHEET_NAME=Название листа
TARGET_HASHTAGS=#отпуск,#выходной,#командировка

### 6. Запуск бота
python tg_bot.py


