import pytest
from app import create_app
from app import db
from flask.signals import request_finished
from app.models.planet import Planet

@pytest.fixture
def app():
    app = create_app(test_config=True)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def make_two_planets(app):
    # Arrange
    first_planet = Planet(name="Mercury",
                      description="powdery gray",
                      moon_number = 0)
    second_planet = Planet(name="Venus",
                         description="yellowish",
                         moon_number =0)

    db.session.add_all([first_planet, second_planet])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()