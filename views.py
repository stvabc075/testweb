from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__,"views")

#default route
@views.route("/")
def home():
    return render_template("test.html", name="Tim")

#Profile route use a get requesto to get name
@views.route("/profile")
def test():
    args = request.args
    name = args.get('name')
    return render_template("test.html", name=name)

#will print json of given data
@views.route("/json")
def get_json():
    return jsonify({'name': 'tim', 'coolness': 10})


@views.route("/data")
def get_data():
    data = request.data
    return jsonify(data)

#redirect: uses that url to ho back to a certain function 
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))


#stv CV route
@views.route("/web")
def web():
    return render_template("web.html")
