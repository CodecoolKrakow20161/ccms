from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.mod_courses.models import Course
from app.mod_courses.forms import CourseForm

# Define the blueprint: 'courses', set its url prefix: app.url/courses
mod_courses = Blueprint('courses', __name__, url_prefix='/courses')


# Set the route and accepted methods
@mod_courses.route('/', methods=['GET'])
def index():
    courses = Course.query.all()
    return render_template('courses/index.html', courses=courses)


@mod_courses.route('/new', methods=['GET', 'POST'])
def new():
    form = CourseForm(request.form)
    if request.method == "POST" and form.validate():
        course = Course(name=form.name.data)

        db.session.add(course)
        db.session.commit()

        return redirect(url_for('courses.index'))

    return render_template('courses/new.html', form=form)


@mod_courses.route('/edit/<int:course_id>', methods=['GET', 'POST'])
def edit(course_id):
    course = Course.query.get(course_id)
    form = CourseForm(formdata=request.form, obj=course)
    if request.method == "POST" and form.validate():
        course.name = form.name.data
        db.session.commit()

        return redirect(url_for('courses.index'))

    return render_template('courses/edit.html', form=form, course=course)


@mod_courses.route('/delete/<int:course_id>', methods=['GET'])
def delete(course_id):
    course = Course.query.get(course_id)

    db.session.delete(course)
    db.session.commit()

    return redirect(url_for('courses.index'))
