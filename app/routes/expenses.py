from flask import Blueprint, render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user

from app import db
from app.models import Expense, Trip, ExpenseCategory

expenses_bp = Blueprint('expenses', __name__)

@expenses_bp.route('/')
@login_required
def index():
    """List all expenses for the current user."""
    expenses = Expense.query.filter_by(user_id=current_user.id).all()
    return render_template('expenses/index.html', expenses=expenses) 