from pikadoLiga import app
from flask import render_template
from flask import request
from flask import redirect
from modeli.timovi import tim
from modeli.mecevi import mec


# import templates


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/kola')
def rounds():

    rounds = []
    matchInstance = mec()
    matches = matchInstance.getAllMatches()
    for item in matches:

        if item["kolo"] in rounds:
            print ('yo')
        else:
            rounds.append(item["kolo"])


    return render_template('kola.html', matchesList=matches, kola=rounds)

@app.route('/kola', methods = ["POST"])
def kolaPost():

    matchInstance = mec()


    hostPoints = request.form['domaci']
    guestPoints = request.form['gosti']

    matchInstance.id = request.form['id']
    matchInstance.rezultat = str(hostPoints) + " : " + str(guestPoints)
    matchInstance.poeniDomacih = hostPoints
    matchInstance.poeniGostiju = guestPoints

    matchInstance.updateResults()

    host = matchInstance.getHostByMatchId()
    guest = matchInstance.getGuestByMatchId()





    teamInstance = tim()

    # update host points
    teamInstance.imeTima = host
    teamInstance.points = hostPoints
    teamInstance.updateScore()

    # update guest points
    teamInstance.imeTima = guest
    teamInstance.points = guestPoints
    teamInstance.updateScore()

    if (int(hostPoints) == 301):
        teamInstance.imeTima = host
        teamInstance.incrementWins()
        teamInstance.imeTima = guest
        teamInstance.incrementLosses()
    else:
        teamInstance.imeTima = guest
        teamInstance.incrementWins()
        teamInstance.imeTima = host
        teamInstance.incrementLosses()


    return "results updated"


@app.route('/svitimovi')
def test():

    jabuka = tim()
    listaTimova = jabuka.dajMiSveTimove()

    return render_template('home.html', listaTimova=listaTimova)

@app.route('/index')
def index():


    jabuka = tim()
    jabuka.imeTima = "Bora"
    jabuka.prviIgrac = "Borica"
    jabuka.drugiIgrac = "Borisa"
    jabuka.napraviTim()

    return "bruka"

@app.route('/register')
def register():


    return render_template('register.html')

@app.route('/register', methods = ["POST"])
def registerPost():

    teamName = request.form['teamName']
    firstPlayer = request.form['firstPlayer']
    secondPlayer = request.form['secondPlayer']

    teamInstance = tim()
    teamInstance.imeTima = teamName
    teamInstance.prviIgrac = firstPlayer
    teamInstance.drugiIgrac = secondPlayer
    teamInstance.napraviTim()

    return "team " + teamName + " successfully created!"


@app.route('/standings')
def standings():

    teams = tim()
    teamsList = teams.getTeamsByWins()

    return render_template('standings.html', listaTimova=teamsList)

@app.route('/round')
def round():


    teamInstance = tim()
    allTeams = teamInstance.dajMiSveTimove()

    list=[]
    for team in allTeams:
        print team
        list.append(team["ime"])


    matches = mec()
    matches.allTeams= list
    matches.createMatchesByRounds()


    return "matches created by rounds"