from flask import Flask, jsonify, request
from onyx_taxi_db import Driver, Client, Order, engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from sqlalchemy.orm import scoped_session
app = Flask(__name__)

Session = scoped_session(sessionmaker(autoflush=True, autocommit=False, bind=engine))

@contextmanager
def session_scope():
        session = Session()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

@app.route("/")
def hello_world():
    return "<p>Hello, world</p>"


@app.route("/drivers", methods=["POST"])
def post_driver():
    content = request.get_json()
    with session_scope() as session:

        new_driver = Driver(
            name=content["name"],
            car=content["car"]
        )
        session.add(new_driver)
    return jsonify(content)


if __name__ == "__main__":
    app.run()
