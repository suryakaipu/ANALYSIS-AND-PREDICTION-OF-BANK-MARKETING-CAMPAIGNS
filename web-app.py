import numpy as np
from flask import Flask, render_template, request
import pickle

# Initialize the flask App
app = Flask(__name__, template_folder='.')
model = pickle.load(open('model.pkl', 'rb'))


# default page of our web-app
@app.route('/')
def index():
    return render_template("home.html")


# To use the predict button in our web-app
@app.route('/predict', methods=['POST', 'GET'])
# For rendering results on HTML GUI
def predict():
    duration = request.values.get("duration")
    euribor = request.values.get("euribor")
    age = request.values.get("age")
    campaign = request.values.get("campaign")
    outcome = request.values.get("outcome")
    varrate = request.values.get("varrate")
    pdays = request.values.get("pdays")
    housing = request.values.get("housing")
    loan = request.values.get("loan")
    conf = request.values.get("conf")
    price = request.values.get("price")
    job = request.values.get("job")
    education = request.values.get("education")
    marital = request.values.get("marital")
    day = request.values.get("day")
    month = request.values.get("month")
    contact = request.values.get("contact")
    previous = request.values.get("previous")
    default = request.values.get("default")
    admin = 0
    blue = 0
    entre = 0
    hmaid = 0
    man = 0
    ret = 0
    self = 0
    ser = 0
    stu = 0
    tech = 0
    job_un = 0
    if job == "admin":
        admin = 1
    elif job == "blue":
        blue = 1
    elif job == "entrepreneur":
        entre = 1
    elif job == "housemaid":
        hmaid = 1
    elif job == "management":
        man = 1
    elif job == "retired":
        ret = 1
    elif job == "self":
        self = 1
    elif job == "services":
        ser = 1
    elif job == "student":
        stu = 1
    elif job == "technician":
        tech = 1
    elif job == "unemployed":
        job_un = 1
    div = 0
    mar = 0
    sin = 0
    if marital == "divorced":
        div = 1
    elif marital == "married":
        mar = 1
    elif marital == "single":
        sin = 1
    b4y = 0
    b6y = 0
    b9y = 0
    high = 0
    illi = 0
    prof = 0
    univ = 0
    if education == "4y":
        b4y = 1
    elif education == "6y":
        b6y = 1
    elif education == "9y":
        b9y = 1
    elif education == "hs":
        high = 1
    elif education == "illiterate":
        illi = 1
    elif education == "pc":
        prof = 1
    elif education == "ud":
        univ = 1
    default = 0
    hous = 0
    if housing == "yes":
        hous = 1
    loan_yes = 0
    if loan == "yes":
        loan_yes = 1
    cell = 0
    tele = 0
    if contact == "cellular":
        cell = 1
    elif contact == "telephone":
        tele = 1
    apr = 0
    aug = 0
    dec = 0
    jul = 0
    jun = 0
    mar = 0
    may = 0
    nov = 0
    octo = 0

    sept = 0
    if month == "apr":
        apr = 1
    elif month == "aug":
        aug = 1
    elif month == "dec":
        dec = 1
    elif month == "july":
        jul = 1
    elif month == "june":
        jun = 1
    elif month == "mar":
        mar = 1
    elif month == "may":
        may = 1
    elif month == "nov":
        nov = 1
    elif month == "oct":
        octo = 1
    elif month == "sept":
        sept = 1
    fri = 0
    mon = 0
    thu = 0
    tue = 0
    wed = 0
    if day == "fri":
        fri = 1
    elif day == "mon":
        mon = 1
    elif day == "thu":
        thu = 1
    elif day == "tue":
        tue = 1
    elif day == "wed":
        wed = 1
    fail = 0
    non = 0
    suc = 0
    if outcome == "success":
        suc = 1
    elif outcome == "failure":
        fail = 1
    elif outcome == "nonexistent":
        non = 1
    rowlist = []
    rowlist.append(age)
    rowlist.extend((admin, blue, entre, hmaid, man, ret, self, ser, stu, tech, job_un, div, mar, sin, b4y, b6y, b9y,
                    high, illi, prof, univ, default, hous, loan_yes, cell, tele, apr, aug, dec, jul, jun, mar, may, nov,
                    octo, sept, fri, mon, thu, tue, wed, duration, campaign, pdays, previous, fail, non, suc, varrate,
                    price, conf, euribor))
    rowlist1 = [float(x) for x in rowlist];

    # for x in rowlist:
    #     rowlist1.append(int(float(x)))
    row = [np.array(rowlist1)]
    # print(row)
    # output=duration+" "+euribor+" "+age+" "+campaign+" "+outcome+" "+varrate+" "+pdays+" "+housing+" "+loan+" "+conf+" "+price+" "+job+" "+education+" "+marital+" "+day+" "+month+" "+contact+" "+previous+" "+default
    prediction = model.predict(row)
    # output = round(prediction[0], 2)
    if prediction[0] == 1:
        output = "Cheers!!! The client will subscribe :)"
    else:
        output = "The client will not subscribe :("
    return render_template('home.html', prediction_text=output)


@app.errorhandler(500)
def internal_error(error):
    return "Please enter valid details!!!"


@app.errorhandler(404)
def not_found(error):
    return "Sorry!!!Try again :(", 404


if __name__ == '__main__':
    app.run(debug=True)
