import sqlite3

path_database = 'setting/database.db'


def delete_expired_users(chat_id, user_id):
    """Функция для удаления забаненных пользователей из базы данных через 24 часа"""
    conn = sqlite3.connect(path_database)  # Подключение к базе данных
    cursor = conn.cursor()
    # Создание таблицы, если она не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS baned_users (chat_id INT, user_id INT)''')
    # Вставка данных в таблицу
    cursor.execute("INSERT INTO warned_users VALUES (?, ?)", (chat_id, user_id))
    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()


def write_user_to_database(chat_id, user_id):
    """Функция для записи данных о предупрежденных пользователях в базу данных"""
    conn = sqlite3.connect(path_database)  # Подключение к базе данных
    cursor = conn.cursor()
    # Создание таблицы, если она не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS warned_users (chat_id INT, user_id INT)''')
    # Вставка данных в таблицу
    cursor.execute("INSERT INTO warned_users VALUES (?, ?)", (chat_id, user_id))
    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()


def writing_to_the_database_about_a_new_user(name_table, chat_id, chat_title, user_id, username, first_name, last_name,
                                             date_now):
    """Запись данных о новом пользователе"""
    conn = sqlite3.connect(path_database)  # Записываем данные в базу данных
    cursor = conn.cursor()
    cursor.execute(
        f"CREATE TABLE IF NOT EXISTS {name_table} (chat_id, chat_title, user_id, username, first_name, last_name, "
        "date_joined)"
    )
    cursor.execute(
        f"INSERT INTO {name_table} (chat_id, chat_title, user_id, username, first_name, last_name, date_joined) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)",
        (chat_id, chat_title, user_id, username, first_name, last_name, date_now)
    )
    conn.commit()
    conn.close()


def reading_data_from_the_database():
    conn = sqlite3.connect(path_database)
    cursor = conn.cursor()
    cursor.execute("SELECT chat_id, user_id FROM privileged_users")
    rows = cursor.fetchall()
    data_dict = {(row[0], row[1]): True for row in rows}
    cursor.close()
    conn.close()
    return data_dict


if __name__ == '__main__':
    reading_data_from_the_database()
