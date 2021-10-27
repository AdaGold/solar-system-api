# standard pytest file that holds test configurations & common test helper functions.
import pytest
from app import create_app
from app import db


@pytest.fixture
def app():
    app = create_app({"TESTING": True}) 
    # designates that the following code should have an application context. 
    with app.app_context():
        db.create_all() 
        # The lines after this statement will run after the test using the app has been completed.
        yield app 

    with app.app_context():
        db.drop_all() 


# client fixture will make a test client (object able to simulate a client making HTTP requests)
@pytest.fixture
def client(app):
	return app.test_client()


from app.models.planet import Planet

# @pytest.fixture
# def two_saved_books(app):
#     # Arrange
#     self_help_book = Book(title="The Ultimate Self Help Book", description="This will TOTALLY change ur lyfe!")
#     food_book = Book(title="Food Book", description="A book filled with pics of food and paragraphs that are too long to tell you how to make said food... so original.")

#     db.session.add_all([self_help_book, food_book])
#     # Alternatively, we could do
#     # db.session.add(ocean_book)
#     # db.session.add(mountain_book)
#     db.session.commit()
