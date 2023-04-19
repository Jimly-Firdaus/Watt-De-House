import sqlite3


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

    def create_table(self, table_name, columns):
        columns_str = ", ".join(
            [f"{name} {data_type}" for name, data_type in columns.items()]
        )
        self.c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})")
        self.conn.commit()

    def insert_data(self, table_name, data):
        columns_str = ", ".join(data.keys())
        values_str = ", ".join(["?" for _ in data.values()])
        values = tuple(data.values())
        self.c.execute(
            f"INSERT OR REPLACE INTO {table_name} ({columns_str}) VALUES ({values_str})",
            tuple(data.values()),
        )
        self.conn.commit()

    def update_data(self, table_name, data, condition):
        set_str = ", ".join([f"{key} = ?" for key in data.keys()])
        condition_str = " AND ".join([f"{key} = ?" for key in condition.keys()])
        self.c.execute(
            f"UPDATE {table_name} SET {set_str} WHERE {condition_str}",
            tuple(data.values()) + tuple(condition.values()),
        )
        self.conn.commit()

    def delete_data(self, table_name, condition):
        condition_str = " AND ".join([f"{key} = ?" for key in condition.keys()])
        self.c.execute(
            f"DELETE FROM {table_name} WHERE {condition_str}", tuple(condition.values())
        )
        self.conn.commit()

    def get_data(self, table_name, columns="*", condition=None):
        columns_str = (
            ", ".join(columns) if isinstance(columns, (list, tuple)) else columns
        )
        if condition:
            condition_strs = []
            condition_values = []
            for key, value in condition.items():
                if isinstance(value, str) and value.startswith("SELECT"):
                    # Handle subqueries
                    condition_strs.append(f"{key} IN ({value})")
                else:
                    # Handle regular values
                    condition_strs.append(f"{key} = ?")
                    condition_values.append(value)
            condition_str = " AND ".join(condition_strs)
            self.c.execute(
                f"SELECT {columns_str} FROM {table_name} WHERE {condition_str}",
                tuple(condition_values),
            )
        else:
            self.c.execute(f"SELECT {columns_str} FROM {table_name}")
        return self.c.fetchall()

    def close(self):
        self.conn.close()
