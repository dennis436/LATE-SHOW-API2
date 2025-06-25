from server.models import db

class Appearance(db.Model):
    __tablename__ = 'appearances'

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)

    guest_id = db.Column(db.Integer, db.ForeignKey("guests.id"), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey("episodes.id"), nullable=False)

    guest = db.relationship("Guest", back_populates="appearances")
    episode = db.relationship("Episode", back_populates="appearances")

    # validation to ensure rating is 1-5 (we’ll add this in controller/serializer logic)
