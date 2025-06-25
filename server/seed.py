from server.app import create_app
from server.models import db
from server.models.user import User
from server.models.guest import Guest
from server.models.episode import Episode
from server.models.appearance import Appearance

app = create_app()

with app.app_context():
    print(" Seeding database...")

    # Delete existing data
    Appearance.query.delete()
    Guest.query.delete()
    Episode.query.delete()
    User.query.delete()

    # Seed data
    user1 = User(username="admin", password_hash="hashed_pw", role="admin")
    user2 = User(username="host", password_hash="hashed_pw", role="host")

    guest1 = Guest(name="Rihanna", occupation="Singer")
    guest2 = Guest(name="Chris Hemsworth", occupation="Actor")

    episode1 = Episode(date="2024-01-01", number=1)
    episode2 = Episode(date="2024-01-02", number=2)

    appearance1 = Appearance(rating=5, guest=guest1, episode=episode1)
    appearance2 = Appearance(rating=4, guest=guest2, episode=episode2)

    db.session.add_all([user1, user2, guest1, guest2, episode1, episode2, appearance1, appearance2])
    db.session.commit()

    print(" Done seeding!")
