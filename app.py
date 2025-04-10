from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# PostgreSQL Config (update these with your actual credentials)
db = psycopg2.connect(
    host="ep-fancy-moon-123456.us-east-2.aws.neon.tech",
    database="neondb",
    user="neondb_owner",
    password="npg_BlGDvtfmY60g",
    port=5432,
    sslmode= "require"
)
#postgresql://neondb_owner:npg_rwS1ARVDsBd5@ep-lingering-block-a1egan2n.ap-southeast-1.aws.neon.tech/neondb?sslmode=require

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT CONCAT(baddie, ' Ji '), VARUN, ASS, OVR FROM AJ_BADDIES ORDER BY OVR DESC")
    baddies = cursor.fetchall()
    return render_template('index.html', baddies=baddies)

@app.route('/add', methods=['GET', 'POST'])
def add_baddie():
    if request.method == 'POST':
        name = request.form['name']
        varun_score = int(request.form['varun'])
        ass_score = int(request.form['ass'])
        ovr = (varun_score + ass_score) / 2
        cursor.execute("INSERT INTO AJ_BADDIES (baddie, VARUN, ASS, OVR) VALUES (%s, %s, %s, %s)", 
                       (name, varun_score, ass_score, ovr))
        db.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/top10/varun')
def top10_varun():
    cursor.execute("SELECT CONCAT(baddie, ' Ji '), VARUN, ASS, OVR FROM AJ_BADDIES ORDER BY VARUN DESC")
    baddies = cursor.fetchall()
    return render_template('top10_varun.html', baddies=baddies)

@app.route('/top10/ashmit')
def top10_ashmit():
    cursor.execute("SELECT CONCAT(baddie, ' Ji '), VARUN, ASS, OVR FROM AJ_BADDIES ORDER BY ASS DESC")
    baddies = cursor.fetchall()
    return render_template('top10_ashmit.html', baddies=baddies)

@app.route('/10on10/varun')
def ten10_varun():
    cursor.execute("SELECT CONCAT(baddie, ' Ji '), VARUN, ASS, OVR FROM AJ_BADDIES WHERE VARUN = 10 ORDER BY OVR DESC")
    baddies = cursor.fetchall()
    return render_template('ten10_varun.html', baddies=baddies)

@app.route('/10on10/ashmit')
def ten10_ashmit():
    cursor.execute("SELECT CONCAT(baddie, ' Ji '), VARUN, ASS, OVR FROM AJ_BADDIES WHERE ASS = 10 ORDER BY OVR DESC")
    baddies = cursor.fetchall()
    return render_template('ten10_ashmit.html', baddies=baddies)

if __name__ == '__main__':
    app.run(debug=True)
