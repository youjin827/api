db = {
    "user": "root",
    "password": "dbwls2477",
    "host": "localhost",
    "port": 3306,
    "database": "minister"
}
DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@
{db['host']}:{db['port']}/{db['database']}?charset=utf8"