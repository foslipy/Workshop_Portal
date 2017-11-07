# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class FreeWorkshopForm(FlaskForm):
    """
    Form for admin to add or edit a FreeWorkshopList
    """
    colname = StringField('CollegeName', validators=[DataRequired()])
    seminardate = StringField('SeminarDate', validators=[DataRequired()])
    hodname = StringField('HODName', validators=[DataRequired()])
    contact = StringField('Contact', validators=[DataRequired()])
    expectations = StringField('Expectations', validators=[DataRequired()])
    mailsenddate = StringField('MailSendDate')
    followup_date1 = StringField('FolloupDate1')
    remark1 = StringField('Remark1')
    followup_date2 = StringField('FollowupDate2')
    remark2 = StringField('Remark2')
    submit = SubmitField('Submit')

class UpcomingWorkshopForm(FlaskForm):
    """
    Form for admin to add or edit a UpcomingWorkshopList
    """
    colname = StringField('CollegeName', validators=[DataRequired()])
    seminardate = StringField('SeminarDate', validators=[DataRequired()])
    hodname = StringField('HODName', validators=[DataRequired()])
    contact = StringField('Contact', validators=[DataRequired()])
    expectations = StringField('Expectations', validators=[DataRequired()])
    mailsenddate = StringField('MailSendDate')
    followup1 = StringField('Folloup1')
    followup2 = StringField('Followup2')
    confirmation = StringField('Confirmation')
    submit = SubmitField('Submit')


