from flask import render_template, redirect, url_for, flash
from app import app, db
from app.models import Volunteer, Donation, Distribution
from app.forms import VolunteerForm, DonationForm, DistributionForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register_volunteer', methods=['GET', 'POST'])
def register_volunteer():
    form = VolunteerForm()
    if form.validate_on_submit():
        volunteer = Volunteer(name=form.name.data, email=form.email.data,
                              phone=form.phone.data, availability=form.availability.data)
        db.session.add(volunteer)
        db.session.commit()
        flash('Volunteer registered successfully!')
        return redirect(url_for('index'))
    return render_template('register_volunteer.html', form=form)

@app.route('/register_donation', methods=['GET', 'POST'])
def register_donation():
    form = DonationForm()
    if form.validate_on_submit():
        donation = Donation(item_name=form.item_name.data, quantity=form.quantity.data,
                            expiration_date=form.expiration_date.data)
        db.session.add(donation)
        db.session.commit()
        flash('Donation registered successfully!')
        return redirect(url_for('index'))
    return render_template('register_donation.html', form=form)

@app.route('/distribution', methods=['GET', 'POST'])
def distribution():
    form = DistributionForm()
    if form.validate_on_submit():
        distribution = Distribution(recipient_name=form.recipient_name.data,
                                    item_name=form.item_name.data, quantity=form.quantity.data,
                                    distribution_date=form.distribution_date.data)
        db.session.add(distribution)
        db.session.commit()
        flash('Distribution registered successfully!')
        return redirect(url_for('index'))
    return render_template('distribution.html', form=form)
