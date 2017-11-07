# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import FreeWorkshopForm, UpcomingWorkshopForm
from .. import db
from ..models import FreeWorkshop, UpcomingWorkshop

def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

# FreeWorkshop Views

@admin.route('/workshops', methods=['GET', 'POST'])
@login_required
def list_freeworkshop():
    """
    List all Free Workshop
    """
    check_admin()

    freeworkshops = FreeWorkshop.query.all()

    return render_template('admin/workshops/freeworkshops.html',
                           freeworkshops=freeworkshops, title="FreeWorkshops")

@admin.route('/workshops/add', methods=['GET', 'POST'])
@login_required
def add_freeworkshop():
    """
    Add a FreeWorkshop to the database
    """
    check_admin()

    add_freeworkshop = True

    form = FreeWorkshopForm()
    if form.validate_on_submit():
        freeworkshop = FreeWorkshop(colname=form.colname.data,
                                seminardate=form.seminardate.data,
                                hodname=form.hodname.data,
                                contact=form.contact.data,
                                expectations=form.expectations.data,
                                mailsenddate=form.mailsenddate.data,
                                followup_date1=form.followup_date1.data,
                                remark1=form.remark1.data,
                                followup_date2=form.followup_date2.data, 
                                remark2=form.remark2.data)
        try:
            # add freeworkshop to the database
            db.session.add(freeworkshop)
            db.session.commit()
            flash('You have successfully added a new freeworkshop.')
        except:
            # in case freeworkshop name already exists
            flash('Error: freeworkshop name already exists.')

        # redirect to freeworkshop page
        return redirect(url_for('admin.list_freeworkshop'))

    # load freeworkshop template
    return render_template('admin/workshops/freeworkshop.html', action="Add",
                           add_freeworkshop=add_freeworkshop, form=form,
                           title="Add Free Workshop")

@admin.route('/workshops/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_freeworkshop(id):
    """
    Edit a freeworkshop
    """
    check_admin()

    add_freeworkshop = False

    freeworkshop = FreeWorkshop.query.get_or_404(id)
    form = FreeWorkshopForm(obj=freeworkshop)
    if form.validate_on_submit():
        freeworkshop.colname = form.colname.data
        freeworkshop.seminardate = form.seminardate.data
        freeworkshop.hodname = form.hodname.data
        freeworkshop.contact = form.contact.data
        freeworkshop.expectations = form.expectations.data
        freeworkshop.mailsenddate = form.mailsenddate.data
        freeworkshop.followup_date1 = form.followup_date1.data
        freeworkshop.remark1 = form.remark1.data
        freeworkshop.followup_date2 = form.followup_date2.data
        freeworkshop.remark2 = form.remark2.data
        db.session.commit()
        flash('You have successfully edited the freeworkshop.')

        # redirect to the freeworkshop page
        return redirect(url_for('admin.list_freeworkshop'))

    form.remark2.data = freeworkshop.remark2
    form.followup_date2.data = freeworkshop.followup_date2
    form.remark1.data = freeworkshop.remark1
    form.followup_date1.data = freeworkshop.followup_date1
    form.mailsenddate.data = freeworkshop.mailsenddate
    form.expectations.data = freeworkshop.expectations
    form.contact.data = freeworkshop.contact
    form.hodname.data = freeworkshop.hodname
    form.seminardate.data = freeworkshop.seminardate
    form.colname.data = freeworkshop.colname
    return render_template('admin/workshops/freeworkshop.html', action="Edit",
                           add_freeworkshop=add_freeworkshop, form=form,
                           freeworkshop=freeworkshop, title="Edit Freeworkshop")

@admin.route('/workshops/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_freeworkshop(id):
    """
    Delete a freeworkshop from the database
    """
    check_admin()

    freeworkshop = FreeWorkshop.query.get_or_404(id)
    db.session.delete(freeworkshop)
    db.session.commit()
    flash('You have successfully deleted the freeworkshop.')

    # redirect to the freeworkshop page
    return redirect(url_for('admin.list_freeworkshop'))

    return render_template(title="Delete FreeWorkshop")

@admin.route('/workshop', methods=['GET', 'POST'])
@login_required
def list_upcomingworkshop():
    """
    List all upcoming Workshop
    """
    check_admin()

    upcomingworkshops = UpcomingWorkshop.query.all()

    return render_template('admin/workshop/upcomingworkshops.html',
                           upcomingworkshops=upcomingworkshops, title="UpcomingWorkshops")

@admin.route('/workshop/add', methods=['GET', 'POST'])
@login_required
def add_upcomingworkshop():
    """
    Add a UpcomingWorkshop to the database
    """
    check_admin()

    add_upcomingworkshop = True

    form = UpcomingWorkshopForm()
    if form.validate_on_submit():
        upcomingworkshop = UpcomingWorkshop(colname=form.colname.data,
                                seminardate=form.seminardate.data,
                                hodname=form.hodname.data,
                                contact=form.contact.data,
                                expectations=form.expectations.data,
                                mailsenddate=form.mailsenddate.data,
                                followup1=form.followup1.data,
                                followup2=form.followup2.data, 
                                confirmation=form.confirmation.data)
        try:
            # add upcomingworkshop to the database
            db.session.add(upcomingworkshop)
            db.session.commit()
            flash('You have successfully added a new upcomingworkshop.')
        except:
            # in case upcomingworkshop name already exists
            flash('Error: upcomingworkshop name already exists.')

        # redirect to upcomingworkshop page
        return redirect(url_for('admin.list_upcomingworkshop'))

    # load freeworkshop template
    return render_template('admin/workshop/upcomingworkshop.html', action="Add",
                           add_upcomingworkshop=add_upcomingworkshop, form=form,
                           title="Add  UpcomingWorkshop")

@admin.route('/workshop/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_upcomingworkshop(id):
    """
    Edit a upcomingworkshop
    """
    check_admin()

    add_upcomingworkshop = False

    upcomingworkshop = UpcomingWorkshop.query.get_or_404(id)
    form = UpcomingWorkshopForm(obj=upcomingworkshop)
    if form.validate_on_submit():
        upcomingworkshop.colname = form.colname.data
        upcomingworkshop.seminardate = form.seminardate.data
        upcomingworkshop.hodname = form.hodname.data
        upcomingworkshop.contact = form.contact.data
        upcomingworkshop.expectations = form.expectations.data
        upcomingworkshop.mailsenddate = form.mailsenddate.data
        upcomingworkshop.followup1 = form.followup1.data
        upcomingworkshop.followup2 = form.followup2.data
        upcomingworkshop.confirmation = form.confirmation.data
        db.session.commit()
        flash('You have successfully edited the upcomingworkshop.')

        # redirect to the upcomingworkshop page
        return redirect(url_for('admin.list_upcomingworkshop'))

    form.confirmation.data = upcomingworkshop.confirmation
    form.followup2.data = upcomingworkshop.followup2
    form.followup1.data = upcomingworkshop.followup1
    form.mailsenddate.data = upcomingworkshop.mailsenddate
    form.expectations.data = upcomingworkshop.expectations
    form.contact.data = upcomingworkshop.contact
    form.hodname.data = upcomingworkshop.hodname
    form.seminardate.data = upcomingworkshop.seminardate
    form.colname.data = upcomingworkshop.colname
    return render_template('admin/workshop/upcomingworkshop.html', action="Edit",
                           add_upcomingworkshop=add_upcomingworkshop, form=form,
                           upcomingworkshop=upcomingworkshop, title="Edit Upcoming workshop")


@admin.route('/workshop/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_upcomingworkshop(id):
    """
    Delete a upcomingworkshop from the database
    """
    check_admin()

    upcomingworkshop = UpcomingWorkshop.query.get_or_404(id)
    db.session.delete(upcomingworkshop)
    db.session.commit()
    flash('You have successfully deleted the upcomingworkshop.')

    # redirect to the upcomingworkshop page
    return redirect(url_for('admin.list_upcomingworkshop'))

    return render_template(title="Delete upcomingWorkshop")