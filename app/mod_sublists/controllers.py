from flask import Blueprint, render_template, request, redirect, url_for
from app import db

mod_sublists = Blueprint('sublists', __name__, url_prefix='/sublists')
