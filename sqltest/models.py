from sqltest import db, create_app
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(220), nullable=False)
    abc = db.Column(db.Numeric(10, 2), nullable=False)
    mode = db.Column(db.String(50), nullable=False)
    classifications = db.Column(db.String(80), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    contractor = db.relationship("Contractor", backref="project", lazy=True)

    def __repr__(self):
        return f"Project<'{self.key}', '{self.title}', {self.abc}>"


class Contractor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"), nullable=False)
    name = db.Column(db.String(50), nullable=True)
    amount = db.Column(db.Numeric(10, 2), nullable=True)

    def __repr__(self):
        return f"Contractor ('{self.name}')"


def main():
    app = create_app()
    app.app_context().push()


if __name__ == "__main__":
    main()
