from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    IntegerField,
    DecimalField,
    DateField,
    SubmitField,
    SelectField,
)
from wtforms.validators import DataRequired, InputRequired


class ProjectAdd(FlaskForm):
    title = StringField("Project Title", validators=[DataRequired()])
    abc = DecimalField("Approved Budget for the Contract", validators=[InputRequired()])
    mode = SelectField(
        "Mode of Procurement",
        choices=[
            ("pbp", "Public Bidding"),
            ("svp", "Small Value Procurement"),
            ("amp", "Alternative Mode of Procurement"),
        ],
    )
    proj_class = SelectField(
        "Class",
        choices=[("inf", "Infrastructure"), ("gds", "Goods"), ("con", "Consultancy"),],
    )
    submit = SubmitField("Submit")
