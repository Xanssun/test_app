import sqlite3

# Функция для установки соединения с базой данных
def connect_to_database():
    conn = sqlite3.connect('procedural_style/todo_list.db')
    return conn

# Функция для инициализации базы данных и таблицы
def initialize_database():
    with connect_to_database() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY,
                text TEXT
            )
        ''')

# Функция для выполнения SQL-запроса с параметрами
def execute_query(query, params=()):
    with connect_to_database() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()

# Функция для загрузки задач из базы данных в Listbox
def load_tasks():
    query = 'SELECT text FROM tasks'
    with connect_to_database() as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        tasks = cursor.fetchall()
    return [task[0] for task in tasks]

# Функция для добавления задачи в базу данных
def add_task(text):
    query = f"INSERT INTO tasks (text) VALUES ('{text}')"
    execute_query(query)

# Функция для редактирования задачи
def edit_task(text, new_value):
    query = F"UPDATE tasks SET text = ('{new_value}') WHERE text = ('{text}')"
    execute_query(query)

# Функция для удаления задачи из базы данных
def delete_task(text):
    query = F"DELETE FROM tasks WHERE text = ('{text}')"
    execute_query(query)
