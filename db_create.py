from app import db
from app.models import Book, User

# drop all of the existing database tables
db.drop_all()

db.create_all()
# create the database and the database table

# admin
admin_user = User('admin@gmail.com', plaintext_password='123456', role='admin')
db.session.add(admin_user)

# insert book name
book1 = Book('Naruto', 'unpredictable', 1, False)
book2 = Book('Dragonball', 'great story', 1, False )
book3 = Book('One piece', 'impressive', 1, False)
db.session.add(book1)
db.session.add(book2)
db.session.add(book3)

'''
#insert user
user1 = User('akhisyababahmad@gmail.com', 'aaaaaa')
db.session.add(user1)
'''

# commit the changes
db.session.commit()
