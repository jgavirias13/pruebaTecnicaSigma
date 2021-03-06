from app.ext import db

class BaseModel:
  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()
  
  @classmethod
  def get_all(cls):
    return cls.query.all()

  @classmethod
  def get_by_id(cls, id):
    return cls.query.get(id)