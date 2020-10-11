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
            ("sho", "Shopping"),
            ("dir", "Direct Contracting"),
            ("eme", "Emergency Cases"),
            ("toc", "Take Over Contracts"),
            ("adj", "Adjacentt/Contigious Contract"),
            ("SSA", "Scientific, similarly or artistic work"),
            ("htc", "Highly Technical Consultant"),
            ("svp", "Small Value Procurement"),
            ("lea", "Lease of Real Property"),
        ],
    )
    proj_class = SelectField(
        "Class",
        choices=[
            ("goods", "Goods"),
            ("infrastructure", "Infrastructure"),
            ("consultancy", "Consultancy"),
        ],
    )
    submit = SubmitField("Submit")


class NewLot(FlaskForm):
    title = StringField("Lot Title", validators=[DataRequired()])
    abc = DecimalField("Budget Per Lot", validators=[InputRequired()])
    submit = SubmitField("Submit")
