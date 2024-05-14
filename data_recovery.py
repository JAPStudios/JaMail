def recover_data_from_corrupted_db(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('PRAGMA integrity_check;')
    result = cursor.fetchone()[0]
    if result == 'ok':
        cursor.execute('SELECT * FROM table_name;')
        data = cursor.fetchall()
        conn.close()
        return data
    else:
        conn.close()
        return None
recovered_data = recover_data_from_corrupted_db('corrupted.db')
print(recovered_data)