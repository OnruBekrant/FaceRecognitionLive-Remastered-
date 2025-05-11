from app import db

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    face_encoding = db.Column(db.PickleType, nullable=False)  # Yüz vektörlerini saklamak için

    def __repr__(self):
        return f"<User {self.name}>"
