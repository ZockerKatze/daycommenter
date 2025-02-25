#ifndef CALENDARAPP_H
#define CALENDARAPP_H

#include <QWidget>
#include <QCalendarWidget>
#include <QDate>
#include <QTextEdit>
#include <QPushButton>
#include <QDialog>

class CalendarApp : public QWidget {
    Q_OBJECT

public:
    explicit CalendarApp(QWidget* parent = nullptr);

private slots:
    void onDateSelected();
    void openNoteDialog();
    void saveNoteData(const QDate& date, const QString& text);
    void loadNoteData(const QDate& date, QTextEdit* noteText = nullptr);

private:
    QCalendarWidget* calendar;
    QDate selectedDate;
};

#endif // CALENDARAPP_H