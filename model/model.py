from database.DAO import DAO


class Model:
    def __init__(self):
        self._solBest = []
        self._listNerc = None
        self._listEvents = None
        self.loadNerc()



    def worstCase(self, nerc, maxY, maxH):
        self.loadEvents(nerc)
        #mancano queste due funzioni
        #deve restituire una lista di eventi
        return self._listEvents

    def ricorsione(self, parziale, maxY, maxH, pos):
        # Mancano queste due funzioni
        pass

    def loadEvents(self, nerc):
        self._listEvents = DAO.getAllEvents(nerc)

    def loadNerc(self):
        self._listNerc = DAO.getAllNerc()


    @property
    def listNerc(self):
        return self._listNerc