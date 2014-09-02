# -*- coding: utf-8 -*-

"""
This program make work schedule from 08/01/2013 with these simple rules:
    - 3 workers (Jane, Jack, Joe)
    - 22 working days a month (even Satruday, Sunday)
    - every third weekend is free (Friday, Saturday)
    - if all the three people have to work, posssibly be that on Friday
    - the remaining 6-7 freedays should be distributed evenly,
      no 5 consecutive freedays next to each other, max 2
    - every day is a workday with minimum 2 people
    - dec. 24, 25, 26 and jan. 1 CLOSED
"""

import calendar
import datetime
from PySide.QtGui import QApplication, QMainWindow, QTableWidgetItem, QColor, QDialog, QFontDatabase, QMessageBox
from PySide.QtCore import Qt
import sys

import mainwindow
import helpwindow
import about


FRIDAY_RED = QColor(255, 155, 103)
FREE_GREEN = QColor(168, 255, 171)


def month_days_num(year, month):
    return calendar.monthrange(year, month)[1]


def get_next_month(year, month):
    """ http://stackoverflow.com/a/4131007/720077 """
    plus_year, new_month = divmod(month + 1, 12)
    if new_month == 0:
        new_month = 12
        plus_year -= 1
    return year + plus_year, new_month


class Employee(object):
    def __init__(self, name, first_free_day, working_days_num=22):
        self.name = name
        self.working_days_num = working_days_num
        self.first_free_day = first_free_day

    def count_free_days(self, year, month):
        """Count free weekend days (every third weekend), based on the fixed first schedule."""
        self.free_days = []
        if self.first_free_day.year == year and self.first_free_day.month == month:
            self.free_days.append(self.first_free_day.day)

        days_num = month_days_num(year, month)
        day = 1
        while day <= days_num:
            difference = datetime.date(year, month, day) - self.first_free_day
            if difference.days > 0 and (difference.days % 21 == 0 or difference.days % 21 == 1):
                self.free_days.append(day)
            day += 1

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name.encode('utf-8')


class Schedule(object):
    def __init__(self, year, month, employees):
        self.year, self.month = year, month
        self.month_days_num = month_days_num(year, month)
        self.employees = employees
        self.schedule = []

        for employee in self.employees:
            employee.count_free_days(self.year, self.month)
            self.schedule.append(self._init_schedule(employee.free_days))

        self._make_schedule()

    def is_friday(self, day):
        return calendar.weekday(self.year, self.month, day) == 4

    def _init_schedule(self, free_days):
        """Initialize schedule, mark every day as working days, except for free_days."""
        return [day not in free_days for day in xrange(1, self.month_days_num + 1)]

    def _make_schedule(self):
        """Remove free days from the initial schedule, based on these rules:
            - Everybody working on every friday if possible.
            - at least two people are working on the same day.
        """
        for ind, employee in enumerate(self.employees):
            remained = self.month_days_num - len(employee.free_days) - employee.working_days_num

            consecutive = 0
            for dayind in xrange(self.month_days_num):
                working = self.schedule[ind][dayind]
                if dayind + 1 in employee.free_days:
                    consecutive += 1
                elif consecutive >= 2:
                    consecutive = 0
                elif working and \
                        not self.is_friday(dayind+1) and \
                        dayind + 1 not in employee.free_days and \
                        sum([self.schedule[empind][dayind] for empind in xrange(3)]) > 2:
                    self.schedule[ind][dayind] = False
                    remained -= 1
                    consecutive += 1
                    if remained == 0:
                        break

        dayind = 0
        while dayind < self.month_days_num and remained > 0:
            if self.is_friday(dayind+1):
                self.schedule[2][dayind] = False
                remained -= 1
            dayind += 1


class TableWidgetCenteredItem(QTableWidgetItem):
    """
    Read only centered cells in QTableWidget.
    """
    def __init__(self, *args, **kwargs):
        super(TableWidgetCenteredItem, self).__init__(*args, **kwargs)
        self.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)


class AboutDialog(QDialog, about.Ui_About):
    """
    Dialog with my contact.
    """
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)


class HelpDialog(QDialog, helpwindow.Ui_Dialog):
    """
    A simple help dialog.
    """
    def __init__(self, *args, **kwargs):
        super(HelpDialog, self).__init__(*args, **kwargs)
        self.setupUi(self)


class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.dateEdit.setDate(datetime.datetime.now())

        self.pushButton.clicked.connect(self.fill_data)
        self.actionAbout.triggered.connect(self.about)
        self.actionHelp.triggered.connect(self.help)
        self.actionLoad.triggered.connect(self.notimplemented)
        self.actionSave.triggered.connect(self.notimplemented)
        self.actionExport.triggered.connect(self.notimplemented)

    def fill_data(self):
        date = self.dateEdit.date()
        year, month = date.year(), date.month()
        widgets_to_fill = ((self.first_month_table, self.first_month_label),
                           (self.second_month_table, self.second_month_label),
                           (self.third_month_table, self.third_month_label))

        for table, label in widgets_to_fill:
            self.fill_table(table, year, month)
            self._set_month_label(label, year, month)
            year, month = get_next_month(year, month)

    def fill_table(self, table_widget, year, month):
        schedule = Schedule(year, month, [Employee(u'Jack', datetime.date(2013, 8, 10)),
                                          Employee(u'Jane', datetime.date(2013, 8, 17)),
                                          Employee(u'Joe', datetime.date(2013, 8, 24))
                                          ]
                            )
        table_widget.setColumnCount(schedule.month_days_num)

        for row, sched in enumerate(schedule.schedule):
            for col, day in enumerate(sched):
                item = TableWidgetCenteredItem('X') if schedule.schedule[row][col] else TableWidgetCenteredItem()
                if schedule.is_friday(col+1):
                    item.setBackground(FRIDAY_RED)
                elif col+1 in schedule.employees[row].free_days:
                    item.setBackground(FREE_GREEN)
                table_widget.setItem(row, col, item)

    def _set_month_label(self, label_widget, year, month):
        label_widget.setText(unicode(year) + '. ' + calendar.month_name[month])

    def about(self):
        """Show about dialog."""
        about = AboutDialog(self)
        about.exec_()

    def help(self):
        """Show help dialog."""
        help = HelpDialog(self)
        help.show()

    def notimplemented(self):
        QMessageBox.information(self, u'Not implemented',
                                u'This function is not implemented!\n'
                                u'If you need it, you can hire me for developing it.\n'
                                u'Check About menu!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    QFontDatabase.addApplicationFont(':/font/general_foundicons.ttf')
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())
