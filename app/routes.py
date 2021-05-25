from app import app, db
from app.models import Subscription, SubChange
from app.forms import SearchIDForm, AddSubscriptionForm, RenewSubscriptionForm, ResetAllSubscriptionsForm, DeleteSubscriptionForm, DeleteAllForm
from config import Config
from datetime import datetime
from flask import render_template, url_for, flash, redirect, jsonify

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchIDForm()
    if form.validate_on_submit():
        if form.name.data is not None:
            subs = Subscription.query.filter(Subscription.name.ilike(f'%{form.name.data}%'))
            if subs is None:
                flash('There are no subscriptions with this name. Please create a new subscription.')
                return redirect(url_for('add_subscription'))
            return render_template('subscriptions.html', subs=subs)
        else:    
            sub = Subscription.query.filter_by(sub_id=form.sub_id.data).first()
        if sub is None:
            flash('There is no subscription with this id. Please create a new subscription.')
            return redirect(url_for('add_subscription'))
        return redirect(url_for('subscription_info', sub_id=sub.sub_id))
    return render_template('index.html', form=form)

@app.route('/add_subscription', methods=['GET', 'POST'])
def add_subscription():
    form = AddSubscriptionForm()
    if form.validate_on_submit():
        subscription = Subscription(sub_id=form.sub_id.data, name=form.name.data, active_status=True)
        db.session.add(subscription)
        subChange = SubChange(sub_id=subscription.id, prev_name=subscription.name, new_name=subscription.name,
                                prev_status=subscription.active_status, new_status=subscription.active_status,
                                prev_sub_id=subscription.sub_id, new_sub_id=subscription.sub_id)
        db.session.add(subChange)
        db.session.commit()
        flash('Subscription added successfully.')
        return redirect(url_for('subscription_info', sub_id=subscription.sub_id))
    return render_template('add_subscription.html', form=form)

@app.route('/renew_subscription/<id>', methods=['GET', 'POST'])
def renew_subscription(id):
    form = RenewSubscriptionForm()
    sub = Subscription.query.filter_by(id=id).first()
    if form.validate_on_submit():
        change = SubChange(sub_id=sub.id, prev_name=sub.name, new_name=sub.name,
                                prev_status=sub.active_status, new_status=form.active_status.data,
                                prev_sub_id=sub.sub_id, new_sub_id=sub.sub_id)
        sub.active_status = form.active_status.data
        db.session.add(change)
        db.session.commit()
        flash(f'Subscription for {sub.name} has been updated!')
        return redirect(url_for('subscription_info', sub_id=sub.sub_id))
    return render_template('renew_subscription.html', form=form, title="Renew a subscription")

@app.route('/subscription_info/<sub_id>')
def subscription_info(sub_id):
    sub = Subscription.query.filter_by(sub_id=sub_id).first()
    return render_template('subscription_info.html', sub=sub)

@app.route('/subscriptions')
def subscriptions():
    subs = Subscription.query.all()
    return render_template('subscriptions.html', subs=subs)

@app.route('/reset_subscriptions', methods=['GET', 'POST'])
def reset_subscriptions():
    form = ResetAllSubscriptionsForm()
    if form.validate_on_submit():
        if form.reset.data == 'Reset':
            subs = Subscription.query.all()
            for sub in subs:
                if sub.active_status == True:
                    subChange = SubChange(sub_id=sub.id, prev_name=sub.name, new_name=sub.name,
                                prev_status=True, new_status=False,
                                prev_sub_id=sub.sub_id, new_sub_id=sub.sub_id)
                    sub.active_status = False
                    db.session.add(subChange)
            db.session.commit()
            flash('All subscriptions have been reset.')
            return redirect(url_for('index'))
        else:
            flash('The spelling may be off for "Reset"')
            return redirect(url_for('reset_subscriptions'))
    return render_template('renew_subscription.html', form=form, title="Reset Subscriptions")

@app.route('/changelog')
def changelog():
    changes = SubChange.query.all()
    return render_template('changes.html', changes=changes)

@app.route('/delete_subscription/<sub_id>', methods=['GET', 'POST'])
def delete_subscription(sub_id):
    form = DeleteSubscriptionForm()
    sub = Subscription.query.filter_by(sub_id=sub_id).first()
    if form.validate_on_submit():
        if form.delete.data == 'Delete':
            change = SubChange(sub_id=sub.id, prev_name=sub.name, new_name='', 
                                prev_status=sub.active_status, new_status=False,
                                prev_sub_id=sub.sub_id, new_sub_id='')
            db.session.add(change)
            db.session.delete(sub)
            db.session.commit()
            flash(f'Subscription successfully deleted for {sub.name}.')
            return redirect(url_for('index'))
    return render_template('delete_subscription.html', form=form, sub=sub, title="Delete Subscription")

@app.route('/delete_all', methods=['GET', 'POST'])
def delete_all():
    form = DeleteAllForm()
    if form.validate_on_submit():
        if form.delete.data == Config.SECRET_KEY:
            subs = Subscription.query.all()
            for sub in subs:
                db.session.delete(sub)
            changes = SubChange.query.all()
            for change in changes:
                db.session.delete(change)
            db.session.commit()
            flash('All entries in all databases have been cleared.')
            return redirect(url_for('index'))
    return render_template('delete_all.html', form=form, title="Delete All Data")