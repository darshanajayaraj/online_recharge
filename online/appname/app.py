from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:kgisl@localhost/online'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

@app.route("/index")
def index():
	return render_template("index.html")
	
@app.route("/about")
def about():
	return render_template("about.html")
	
@app.route("/")
def login():
	return render_template("login.html")
	
@app.route("/bus")
def bus():
	return render_template("bus.html")
	
@app.route("/bus_list")
def bus_list():
	return render_template("bus-list.html")
	
@app.route("/contact")
def contact():
	return render_template("contact.html")
	
@app.route("/faq")
def faq():
	return render_template("faq.html")
	
@app.route("/icons")
def icons():
	return render_template("icons.html")
	
@app.route("/pay")
def pay():
	return render_template("pay.html")
	
@app.route("/plans")
def plans():
	return render_template("plans.html")
	
@app.route("/select_show")
def select_show():
	return render_template("select_show.html")
	
@app.route("/shortcodes")
def shortcodes():
	return render_template("shortcodes.html")
	

	
	
class register(db.Model):
	id=db.Column('student_id',db.Integer,primary_key=True)
	name=db.Column(db.String(50))
	email=db.Column(db.String(50))
	mobile=db.Column(db.String(50))
	password=db.Column(db.String(50))
	
	
	def __init__(self,name,email,mobile,password):
		self.name=name
		self.email=email
		self.mobile=mobile
		self.password=password
		
	@app.route("/register_db",methods=["GET","POST"])
	def register_db():
		if request.method == 'POST':
			if not request.form['name'] or not request.form['email'] or not request.form['mobile'] or not request.form['password']:
				flash("Error")
			else:
				student=register(request.form['name'],request.form['email'],request.form['mobile'],request.form['password'])
				db.session.add(student)
				db.session.commit()
			return redirect(url_for('login'))
		return render_template("login.html")




if __name__ == '__main__':
	db.create_all()
	app.run(debug = True)




