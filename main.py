from sqlalchemy import insert, select, or_, and_
from sqlalchemy.engine.base import Connection
from sqlalchemy.sql.elements import Null
from models import User, Address
from connect_to_db import engine, Base

Base.metadata.create_all(engine)

def insert_one_user():
    stmt = ''                 #пишется какое-нить выражение
    stmt = insert(User).values(
        name="Johnny",
        fullname="John Carter"
    )
    with engine.connect() as conn:
        conn.execute(stmt)

def insert_many_users(values):
    stmt = insert(User)
    with engine.connect() as conn:
        conn.execute(stmt, values)

def select_users():
    stmt = (
        select(User)
        .where(
            (
                (User.id >= 2) & (User.id <= 2) |
                User.name.in_(['Peter','Johnny'])
            )
        )
    )
    with engine.connect() as conn:
        return list(conn.execute(stmt))

def add_columns():
    stmt = "ALTER TABLE user_account ADD COLUMN age Integer"
    with engine.connect() as conn:
        conn.execute(stmt)

def select_null_ages_users():
    stmt = "UPDATE user_account SET age = 35 WHERE name = 'Johnny'"
    with engine.connect() as conn:
        conn.execute(stmt)

def select_three_mans():
    stmt = (
        select(User)
        .where(
            (User.sex == 'male') & (User.name.like('L%') | User.name.like('H%'))
        )
        .order_by(User.age.desc()).limit(3)
    )
    with engine.connect() as conn:
        return list(conn.execute(stmt))

def delete_extra_rows():
    stmt = "DELETE FROM user_account WHERE id >= 14"
    with engine.connect() as conn:
         conn.execute(stmt)

#for row in select_users():
#    print(row)

#insert_one_user()
values = [
    {'name': 'Leslie', 'fullname': "Leslie Nilson", 'sex': 'male', 'age': '75'},
    {'name': 'Lindon', 'fullname': "Lindon Jonson", 'sex': 'male', 'age': '80'},
    {'name': 'Henry', 'fullname': "Henry Smith", 'sex': 'male', 'age': '78'},
    {'name': 'Stiven', 'fullname': "Stiven Hawking", 'sex': 'male', 'age': '50'},
    {'name': 'Albert', 'fullname': "Albert Einstein", 'sex': 'male', 'age': '56'}
]

#insert_many_users(values)
#add_columns()

#select_null_ages_users()
delete_extra_rows()
print(select_three_mans())