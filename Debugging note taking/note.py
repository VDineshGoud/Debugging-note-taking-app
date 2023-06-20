from flask import Flask, render_template, request, url_for
app = Flask(__name__)


notetaking = []
templist = []

@app.route("/", methods=['GET', 'POST'])
def main():
    global notetaking, templist 

    if request.method == "POST":
        requestform = request.form
        # print(webpage)
        notes = str(requestform['notes'])
        print(notes)
        templist.append(notes)
        [notetaking.append(x) for x in templist if x not in notetaking]

    return render_template("index.html", notetaking=notetaking)


# Running the app
if __name__ == '__main__':
    app.run(debug=True)