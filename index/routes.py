from flask import render_template, redirect, url_for, flash, request
from index.forms import AddForm, LoginForm, SellForm
from index import app, db
from index.models import User, Medicine


@app.route('/', methods=['GET', 'POST'])
def login1():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'admin':
            flash("You've been logged in", 'success')
            return redirect(url_for('home'))
        else:
            flash('Wrong username or password', 'danger')
    return render_template('login1.html', form=form)


@app.route('/stock')
def stock():
    posts = Medicine.query.all()
    return render_template('stock.html', posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        medecine = Medicine(name=form.name.data, dose=form.dose.data, price=form.price.data, package=form.package.data,
                            company=form.company.data, purpose=form.purpose.data, description=form.description.data)
        db.session.add(medecine)
        db.session.commit()
        flash(f'{form.name.data} added to stock successfully', 'success')
        return redirect(url_for('add'))
    return render_template('add.html', form=form, legend='Add post')


@app.route('/home', methods=['GET', 'POST'])
def home():
    form = SellForm()
    form.medicine_name.choices = [(medicine.id, medicine.name) for medicine in Medicine.query.all()]
    quantity = form.quantity.data
    info = Medicine.query.filter_by(id=form.medicine_name.data).first()
    if info != None:
        price = info.price
        final_price = int(price)*int(quantity)
        form.price.data = final_price
        flash(f'{info.name} sold successfully, Total price: {form.price.data} ', 'success')



    return render_template('home.html', form=form, legend='Sell Medicine')


@app.route('/post/<int:medicine_id>')
def post(medicine_id):
    post = Medicine.query.get_or_404(medicine_id)
    return render_template('post.html', post=post)


@app.route('/post/<int:medicine_id>/update', methods=['GET', 'POST'])
def post_update(medicine_id):
    post = Medicine.query.get_or_404(medicine_id)
    form = AddForm()
    if form.validate_on_submit():
        post.name = form.name.data
        post.package = form.package.data
        post.purpose = form.purpose.data
        post.dose = form.dose.data
        post.company = form.company.data
        post.price = form.price.data
        db.session.commit()
        flash('Medicine has been updated.', 'success')
        return redirect(url_for('post', medicine_id=post.id))
    elif request.method == 'GET':
        form.name.data = post.name
        form.package.data = post.package
        form.purpose.data = post.purpose
        form.dose.data = post.dose
        form.company.data = post.company
        form.price.data = post.price
    return render_template('add.html', form=form, legend='Update medicine')


@app.route('/post/<int:medicine_id>/delete', methods=['POST'])
def delete_post(medicine_id):
    post = Medicine.query.get_or_404(medicine_id)
    db.session.delete(post)
    db.session.commit()
    flash('Medicine has been deleted', 'danger')
    return redirect(url_for('stock'))
