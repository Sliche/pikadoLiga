from pikadoLiga import mysql


class tim(object):
    def __init__(self):

        self.imeTima = basestring
        self.prviIgrac = basestring
        self.drugiIgrac = basestring
        self.points = int

    def napraviTim(self):

        conn = mysql.connect
        cur = conn.cursor()
        query = "INSERT INTO timovi (prvi_igrac, drugi_igrac, ime) VALUES (' " + self.prviIgrac + "', '" + self.drugiIgrac + "', '" + self.imeTima + "' )"


        cur.execute(query)
        conn.commit()
        return "success"




    def updateScore(self):

        conn = mysql.connect
        cur = conn.cursor()
        query = "update timovi set bodovi = bodovi + " + str(self.points) + " where ime='" + str(self.imeTima) + "'"



        cur.execute(query)
        conn.commit()
        return "success"

    def getTeamsByWins(self):
        conn = mysql.connect
        cur = conn.cursor()

        query = "select * from timovi order by pobede desc, bodovi desc"
        cur.execute(query)

        result = cur.fetchall()

        return result


    def dajMiSveTimove(self):
        conn = mysql.connect
        cur = conn.cursor()

        query = "select * from timovi"
        cur.execute(query)

        result = cur.fetchall()

        return result

    def incrementWins(self):

        conn = mysql.connect
        cur = conn.cursor()
        query = "update timovi set pobede = pobede + 1 where ime='" + str(self.imeTima) + "'"



        cur.execute(query)
        conn.commit()
        return "success"

    def incrementLosses(self):

        conn = mysql.connect
        cur = conn.cursor()
        query = "update timovi set porazi = porazi + 1 where ime='" + str(self.imeTima) + "'"



        cur.execute(query)
        conn.commit()
        return "success"

