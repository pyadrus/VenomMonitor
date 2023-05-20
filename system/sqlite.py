import sqlite3

path_database = 'setting/database.db'


def writing_to_the_database_about_a_new_user(name_table, chat_id, chat_title, user_id, username, first_name, last_name,
                                             date_now):
    """Запись данных о новом пользователе"""
    # Записываем данные в базу данных
    conn = sqlite3.connect(path_database)
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
