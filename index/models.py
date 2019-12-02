from index import db


class Medicine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    dose = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(10), nullable=False)
    package = db.Column(db.String(50), nullable=False)
    company = db.Column(db.String(50), nullable=False)
    purpose = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"Medicine('{self.name}','{self.dose}','{self.price}','{self.package}','{self.company}'," \
               f"'{self.purpose}','{self.description}')"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.password}')"