from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class PhoneSchedule(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  phone_number = db.Column(db.String(20), nullable=False)
  schedule = db.Column(db.String(100), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

  def to_json(self):
    return {
      'id': self.id,
      'name': self.name,
      'phone_number': self.phone_number,
      'schedule': self.schedule,
      'created_at': self.created_at.isoformat()
    }

class ContactClient(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  phone_number = db.Column(db.String(20), nullable=False)
  email = db.Column(db.String(100), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

  def to_json(self):
    return {
      'id': self.id,
      'name': self.name,
      'phone_number': self.phone_number,
      'email': self.email,
      'created_at': self.created_at.isoformat()
    }
                         

  