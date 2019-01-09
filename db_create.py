from app import db
from app.models import Mantan, User

# drop all of the existing database tables
db.drop_all()

db.create_all()
# create the database and the database table

#admin
admin_user = User('akhi@gmail.com', plaintext_password='123456', role='admin')
db.session.add(admin_user)

#insert nama mantan
mantan1 = Mantan('Raisa', 'Terlalu sibuk', 1, False)
mantan2 = Mantan('Irta', 'sibuk manggung bersama Qasima', 1, False )
mantan3 = Mantan('Cita citata', 'tidak direstui :v', 1, False)
db.session.add(mantan1)
db.session.add(mantan2)
db.session.add(mantan3)

'''
##### IF will insert user ####
#insert user

user1 = User('akhisyababahmad@gmail.com', 'aaaaaa')
db.session.add(user1)

'''

# commit the changes
db.session.commit()
