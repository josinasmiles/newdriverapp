from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "woManGiantBear_GOOD999"

@app.route("/")
def index():
    return render_template("index.htm")

@app.route("/login")
def login():
    flash("Please enter your name")
    return render_template("login.htm")

@app.route("/submit", methods=["POST","GET"])
def greet():
    flash("Hi "+ str(request.form['name_input']+" let's get started!"))
    request.form['name_input']
    return render_template("login0.htm")

@app.route("/nf1")
def nf1():
    return render_template("intro1.htm")

@app.route("/nf2")
def nf2():
    return render_template("intro2.htm")

@app.route("/mod1home")
def mod1home():
    return render_template("module1.htm")

@app.route("/mod1pg1")
def mod1pg1():
    return render_template("module1page1.htm")

@app.route("/mod1pg2")
def mod1pg2():
    return render_template("module1page2.htm")

@app.route("/mod1pg3")
def mod1pg3():
    return render_template("module1page3.htm")

@app.route("/mod1pg4")
def mod1pg4():
    return render_template("module1page4.htm")

@app.route("/mod1pg4b")
def mod1pg4b():
    return render_template("module1page4b.htm")

@app.route("/mod1pg5")
def mod1pg5():
    return render_template("module1page5.htm")

@app.route("/mod1pg5b")
def mod1pg5b():
    return render_template("module1page5b.htm")

@app.route("/mod1pg6")
def mod1pg6():
    return render_template("module1page6.htm")
@app.route("/mod1pg6b")
def mod1pg6b():
    return render_template("module1fyi.htm")

@app.route("/mod1pg10")
def mod1pg10():
    return render_template("module1quizhome.htm")

@app.route("/mod2home")
def mod2home():
    return render_template("module2.htm")

@app.route("/mod2pg1")
def mod2pg1():
    return render_template("module2page1.htm")

@app.route("/mod2pg2")
def mod2pg2():
    return render_template("module2page2.htm")

@app.route("/mod2pg3")
def mod2pg3():
    return render_template("module2page3.htm")
@app.route("/mod2pg3b")
def mod2pg3b():
    return render_template("module2page3b.htm")

@app.route("/mod2pg4")
def mod2pg4():
    return render_template("module2page4.htm")
@app.route("/mod2pg4b")
def mod2pg4b():
    return render_template("module2page4b.htm")

@app.route("/mod2pg5")
def mod2pg5():
    return render_template("module2page5.htm")
@app.route("/mod2pg5b")
def mod2pg5b():
    return render_template("module2page5b.htm")

@app.route("/mod2pg6")
def mod2pg6():
    return render_template("module2page6.htm")
@app.route("/mod2pg6b")
def mod2pg6b():
    return render_template("module2page6b.htm")

@app.route("/mod2pg7")
def mod2pg7():
    return render_template("module2page7.htm")

@app.route("/mod2pg8")
def mod2pg8():
    return render_template("module2page8.htm")
@app.route("/mod2pg8b")
def mod2pg8b():
    return render_template("module2page8b.htm")

@app.route("/mod2pg9")
def mod2pg9():
    return render_template("module2page9.htm")

@app.route("/mod2pg10")
def mod2pg10():
    return render_template("module2page10.htm")
@app.route("/mod2pg10b")
def mod2pg10b():
    return render_template("module2fyi.htm")

@app.route("/mod2pg11")
def mod2pg11():
    return render_template("module2quizhome.htm")

@app.route("/mod3home")
def mod3home():
    return render_template("module3.htm")

@app.route("/mod3pg1")
def mod3pg1():
    return render_template("module3page1.htm")

@app.route("/mod3pg2")
def mod3pg2():
    return render_template("module3page2.htm")
@app.route("/mod3pg2b")
def mod3pg2b():
    return render_template("module3page2b.htm")

@app.route("/mod3pg3")
def mod3pg3():
    return render_template("module3page3.htm")

@app.route("/mod3pg4")
def mod3pg4():
    return render_template("module3page4.htm")
@app.route("/mod3pg4b")
def mod3pg4b():
    return render_template("module3page4b.htm")

@app.route("/mod3pg5")
def mod3pg5():
    return render_template("module3page5.htm")

@app.route("/mod3pg6")
def mod3pg6():
    return render_template("module3page6.htm")
@app.route("/mod3pg6b")
def mod3pg6b():
    return render_template("module3fyi.htm")

@app.route("/mod3pg7")
def mod3pg7():
    return render_template("module3quizhome.htm")

@app.route("/mod4home")
def mod4home():
    return render_template("module4.htm")

@app.route("/mod4pg1")
def mod4pg1():
    return render_template("module4page1.htm")
@app.route("/mod4pg1b")
def mod4pg1b():
    return render_template("module4page1b.htm")

@app.route("/mod4pg2")
def mod4pg2():
    return render_template("module4page2.htm")
@app.route("/mod4pg2b")
def mod4pg2b():
    return render_template("module4page2b.htm")

@app.route("/mod4pg3")
def mod4pg3():
    return render_template("module4page3.htm")

@app.route("/mod4pg4")
def mod4pg4():
    return render_template("module4page4.htm")

@app.route("/mod4pg5")
def mod4pg5():
    return render_template("module4page5.htm")

@app.route("/mod4pg6")
def mod4pg6():
    return render_template("module4page6.htm")

@app.route("/mod4pg7")
def mod4pg7():
    return render_template("module4page7.htm")

@app.route("/mod4pg8")
def mod4pg8():
    return render_template("module4page8.htm")

@app.route("/mod4pg9")
def mod4pg9():
    return render_template("module4page9.htm")

@app.route("/mod4pg10")
def mod4pg10():
    return render_template("module4page10.htm")

@app.route("/mod4pg10b")
def mod4pg10b():
    return render_template("module4fyi.htm")

@app.route("/mod4pg11")
def mod4pg11():
    return render_template("module4quizhome.htm")

@app.route("/mod4pg12")
def mod4pg12():
    return render_template("finalexam.htm")

@app.route("/mod4pg13")
def mod4pg13():
    return render_template("certificate0.htm")


if __name__ == '__main__':
    app.run()
