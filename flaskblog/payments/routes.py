from flask import Blueprint, render_template, url_for, flash, redirect, request, abort, current_app
from flaskblog import db
from flaskblog.payments.forms import ChargeForm
from flaskblog.models import Post
from flask_login import current_user, login_required
import stripe

payments = Blueprint('payments', __name__)

stripe_keys = {
    'secret_key': 'sk_test_AhwMz618zRWBywhvWbZC7uTy',
    'publishable_key': 'pk_test_WgHIhNXTUZnIkc7UJjJgHVJU'
    # 'secret_key': current_app.config['STRIPE_SECRET_KEY'],
    # 'publishable_key': current_app.config['STRIPE_PUBLISHABLE_KEY']
}

stripe.api_key = stripe_keys['secret_key']

@login_required
@payments.route('/charge', methods=['GET', 'POST'])
def charge():
    # Amount in cents
    form = ChargeForm()
    email = current_user.email

    customer = stripe.Customer.create(
        email = email,
        card=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='usd',
        description="Website Payment"
    )

    return render_template('charge.html', amount=amount)