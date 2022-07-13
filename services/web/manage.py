# -*- coding: utf-8 -*-
"""Provide commands for starting the application, creating the database and seeding the database."""
from api import create_app, db
from api.blueprints.default.models import User
from dotenv import load_dotenv
from flask.cli import FlaskGroup

load_dotenv()

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('create_db')
def create_db():
    """Create the database."""
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    """Seed the database."""
    db.session.add(User(
        email='lyle@notreal.com',
    ))
    db.session.add(User(
        email='michael@notreal.com',
    ))
    db.session.commit()


if __name__ == '__main__':
    cli()
