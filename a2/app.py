# This file runs the application for creating and viewing Restaurant reviews


from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/')         # home page
def home():
        return render_template('index.html', template_folder = 'templates')

@app.route('/addReview')        # add review page
def addReview():
        return render_template('addReview.html', template_folder = 'templates')

@app.route('/addRev', methods = ['POST', 'GET'])        # add review function
def addRev():
    if request.method == 'POST':                        # verify request method
            try:
                usrnm = request.form['usrnm']           # get values from form
                rst   = request.form['rst']
                food  = request.form['food']
                svc   = request.form['srvc']
                amb   = request.form['amb']
                prc   = request.form['prc']
                ovll  = request.form['ovll']
                rev   = request.form['rvw']

                with sql.connect("reviewData.db") as con:       # establish connection to database
                        cur = con.cursor()
                        cur.execute("INSERT INTO Reviews (Username, Restaurant, Rating, Review) VALUES (?,?,?,?)", (usrnm,rst,ovll,rev,))       # insert data
                        cur.execute("INSERT INTO Ratings (Restaurant, Food, Svc, Ambience, Price, Overall) VALUES (?,?,?,?,?,?) ", (rst,food,svc,amb,prc,ovll,))
                        con.commit()    # commit to db

            except:
                con.rollback()          # error handling
                   
            finally:
                return showReviews(rst = rst)   # pass restaurant name to showReviews to display all reviews for restaurant
                con.close()                     # close connection     


@app.route('/getReviews')       # get reviews page
def getReviews():
        return render_template('getReviews.html', template_folder = 'templates')

@app.route('/searchResult', methods = ['POST', 'GET'])         # function to find reviews matching search criteria
def searchResult():
        if request.method == 'POST':
                try:
                        rst = request.form['rst']              # get search criteria
                finally:
                        return showReviews(rst = rst)           # return reviews matching

@app.route('/showReport')       # function to return top 10 overall restaurants
def showReport():                    
        con = sql.connect("reviewData.db")      # establish connection to db
        con.row_factory = sql.Row               # create rows
        
        cur = con.cursor()
        cur.execute("SELECT Restaurant, AVG(Food), AVG(Svc), AVG(Ambience), AVG(Price), AVG(Overall) FROM Ratings GROUP BY Restaurant ORDER BY AVG(Overall) DESC, Restaurant LIMIT 10")     #query for appropriate results

        rows = cur.fetchall();          # set rows
        return render_template('showReport.html', template_folder = 'templates', rows = rows)   # pass rows into showReport
    

@app.route('/showReviews')
def showReviews(rst):           # function to show reviews for a given restaurant "rst"

        con = sql.connect("reviewData.db")      # establish connection to db
        con.row_factory = sql.Row               # create rows

        cur = con.cursor()
        cur.execute("SELECT Username, Rating, Review FROM Reviews WHERE Restaurant = ?", (rst,))        # find matching reviews
                        
        rows = cur.fetchall();          # set rows
        return render_template("showReviews.html", template_folder = 'templates', rows = rows, rst = rst) # render results

if __name__ == '__main__':      # main
   app.run(debug = True)
