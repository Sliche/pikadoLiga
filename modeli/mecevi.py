from pikadoLiga import mysql

class mec(object):
    def __init__(self):

        self.id =int
        self.poeniDomacih = int
        self.poeniGostiju = int
        self.domaci = basestring
        self.gosti = basestring
        self.kolo = basestring
        self.rezultat = str
        self.allTeams = list



    def getAllMatches(self):
        conn = mysql.connect
        cur = conn.cursor()

        query = "select * from mecevi order by kolo"
        cur.execute(query)

        result = cur.fetchall()

        return result


    # def napraviKola(self):

    def updateResults(self):

        conn = mysql.connect
        cur = conn.cursor()
        query = "update mecevi set poeniDomacih='" + str(self.poeniDomacih) + "', poeniGostiju='" + str(self.poeniGostiju) + "', rezultat='" + str(self.rezultat) + "' where id='" + str(self.id) + "'"



        cur.execute(query)
        conn.commit()
        return "success"

    def createMatch(self):

        conn = mysql.connect
        cur = conn.cursor()
        query = "insert into mecevi (domaci, gosti, kolo) values ('" + str(self.domaci) + "', '" + str(self.gosti) + "', '" + str(self.kolo) + "')"


        cur.execute(query)
        conn.commit()
        return "success"

    def getHostByMatchId(self):
        conn = mysql.connect
        cur = conn.cursor()
        query = "select domaci from mecevi where id='" + str(self.id) + "'"

        cur.execute(query)

        result = cur.fetchall()

        return result[0]["domaci"]

    def getGuestByMatchId(self):
        conn = mysql.connect
        cur = conn.cursor()
        query = "select gosti from mecevi where id='" + str(self.id) + "'"

        cur.execute(query)

        result = cur.fetchall()

        return result[0]["gosti"]

    def createMatchesByRounds(self):


        div1 = self.allTeams


        def create_schedule(list):
            """ Create a schedule for the teams in the list and return it"""
            s = []

            if len(list) % 2 == 1: list = list + ["BYE"]

            for i in range(len(list)-1):

                mid = len(list) / 2
                l1 = list[:mid]
                l2 = list[mid:]
                l2.reverse()

                # Switch sides after each round
                if(i % 2 == 1):
                    s = s + [ zip(l1, l2) ]
                else:
                    s = s + [ zip(l2, l1) ]

                list.insert(1, list.pop())

            return s

        matchInstance=mec()

        def makeRounds():
            i=1
            kolo=1
            brKola = len(div1) - 1
            for round in create_schedule(div1):
                for match in round:
                    if (i > len(div1)/2):
                        kolo=kolo+1
                        i=1

                    print (kolo)
                    i=i+1


                    matchInstance.domaci=match[0]
                    matchInstance.gosti=match[1]
                    matchInstance.kolo=kolo
                    matchInstance.createMatch()

                    print match[0] + " - " + match[1]
            print
        makeRounds()


        return "success"



