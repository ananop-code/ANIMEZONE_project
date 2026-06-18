import os
from flask import render_template, redirect, flash, session, request, url_for
from flask_login import login_user, logout_user, login_required
from ext import app, db
from forms import RegisterForm, AnimeForm, LoginForm
from models import Anime, Review, User


@app.route("/set_language/<lang>")
def set_language(lang):
    if lang in ["en", "ka", "ja"]:
        session["lang"] = lang
    return redirect(request.referrer or url_for("home"))


def get_current_lang():
    return session.get("lang", "en")


@app.route("/")
def home():
    animes = Anime.query.all()
    return render_template("index.html", animes=animes, lang=get_current_lang())


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, password=form.password.data)
        new_user.create()
        flash("Successfully registered! Now you can log in.")
        return redirect("/login")
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash("Welcome back to AnimeZone!")
            return redirect("/")
        else:
            flash("Invalid username or password.")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/add_anime", methods=["GET", "POST"])
@login_required
def add_anime():
    form = AnimeForm()
    if form.validate_on_submit():
        new_anime = Anime(
            title=form.title.data,
            release_year=form.release_year.data,
            description_en=form.description_en.data,
            description_ka=form.description_ka.data,
            description_ja=form.description_ja.data
        )
        img = form.image.data
        if img:
            new_anime.image = img.filename
            directory = os.path.join(app.root_path, "static", "images", img.filename)
            img.save(directory)

        new_anime.create()
        flash("Anime successfully added and will now appear on Home page!")
        return redirect("/")
    return render_template("add_anime.html", form=form)


@app.route("/update_anime/<int:anime_id>", methods=["GET", "POST"])
@login_required
def update_anime(anime_id):
    anime = Anime.query.get_or_404(anime_id)
    form = AnimeForm(
        title=anime.title,
        release_year=anime.release_year,
        description_en=anime.description_en,
        description_ka=anime.description_ka,
        description_ja=anime.description_ja
    )
    if form.validate_on_submit():
        anime.title = form.title.data
        anime.release_year = form.release_year.data
        anime.description_en = form.description_en.data
        anime.description_ka = form.description_ka.data
        anime.description_ja = form.description_ja.data

        image = form.image.data
        if image:
            directory = os.path.join(app.root_path, "static", "images", image.filename)
            image.save(directory)
            anime.image = image.filename

        anime.save()
        return redirect("/")
    return render_template("add_anime.html", form=form)


@app.route("/delete_anime/<int:anime_id>")
@login_required
def delete_anime(anime_id):
    anime = Anime.query.get_or_404(anime_id)
    anime.delete()
    return redirect("/")


@app.route("/anime/<int:anime_id>")
def view_anime_details(anime_id):
    anime = Anime.query.get_or_404(anime_id)
    reviews = Review.query.filter(Review.anime_id == anime_id).all()

    current_lang = get_current_lang()
    if current_lang == "ka":
        info = anime.description_ka
    elif current_lang == "ja":
        info = anime.description_ja
    else:
        info = anime.description_en

    return render_template("anime_details.html", anime=anime, reviews=reviews, info=info)


@app.route("/about")
def about():
    return render_template("about.html")