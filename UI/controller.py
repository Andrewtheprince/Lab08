from dbm import error

import flet as ft

from model.nerc import Nerc


class Controller:
    def __init__(self, view, model):
        self._view = view
        self._model = model
        self._idMap = {}
        self.fillIDMap()

    def handleWorstCase(self, e):
        self._view._txtOut.controls.clear()
        nercSelezionato = self._ddNerc.id
        maxAnniSelezionati = self._view._txtYears.value
        maxHoursSelezionate = self._view._txtHours.value
        if maxAnniSelezionati.isdigit():
            maxAnniSelezionati = int(maxAnniSelezionati)
        else:
            self._view.create_alert("Devi inserire un valore numerico nel campo 'Max Years'")
            self._view._txtYears.clean()
            return
        if maxHoursSelezionate.isdigit():
            maxHoursSelezionate = int(maxHoursSelezionate)
        else:
            self._view.create_alert("Devi inserire un valore numerico nel campo 'Max Hours'")
            self._view._txtHours.clean()
            return
        worstCase = self._model.worstCase(nercSelezionato, maxAnniSelezionati, maxHoursSelezionate)
        peopleAffected = 0
        hoursOutage = 0
        for event in worstCase:
            peopleAffected += event.customers_affected
            hoursOutage += (event.date_event_finished-event.date_event_began).total_seconds()
        self._view._txtOut.controls.append(ft.Text(f"Tot People Affected: {peopleAffected}"))
        self._view._txtOut.controls.append(ft.Text(f"Tot Hours of outage: {hoursOutage/3600}"))
        for event in worstCase:
            self._view._txtOut.controls.append(ft.Text(event))
        self._view.update_page()

    def fillDD(self):
        nercList = self._model.listNerc
        for n in nercList:
            self._view._ddNerc.options.append(ft.dropdown.Option(key=n.value, data=n, on_click=self._choiceDDNerc))
        self._view.update_page()

    def _choiceDDNerc(self, e):
        self._ddNerc = e.control.data

    def fillIDMap(self):
        values = self._model.listNerc
        for v in values:
            self._idMap[v.value] = v
