#include "calendar.h"
#include <QApplication>
#include <QVBoxLayout>
#include <QColorDialog>
#include <QJsonDocument>
#include <QJsonObject>
#include <QFile>
#include <QDir>
#include <QMessageBox>
#include <QTextEdit>

CalendarApp::CalendarApp(QWidget* parent) : QWidget(parent) {
    setWindowTitle("Calendar");
    setMinimumSize(500, 400);

    QVBoxLayout* mainLayout = new QVBoxLayout(this);

    calendar = new QCalendarWidget(this);
    calendar->setGridVisible(true);
    calendar->setVerticalHeaderFormat(QCalendarWidget::NoVerticalHeader);
    mainLayout->addWidget(calendar);

    QPushButton* editButton = new QPushButton("Add/Edit Note", this);
    mainLayout->addWidget(editButton);

    connect(calendar, &QCalendarWidget::selectionChanged, this, &CalendarApp::onDateSelected);
    connect(editButton, &QPushButton::clicked, this, &CalendarApp::openNoteDialog);
}

void CalendarApp::onDateSelected() {
    selectedDate = calendar->selectedDate();
    loadNoteData(selectedDate);  // This will load the note for the selected date
}

void CalendarApp::openNoteDialog() {
    if (!selectedDate.isValid()) {
        QMessageBox::warning(this, "Warning", "Please select a date.");
        return;
    }

    QDialog noteDialog(this);
    noteDialog.setWindowTitle("Edit Note");
    noteDialog.setMinimumSize(300, 200);

    QVBoxLayout* layout = new QVBoxLayout(&noteDialog);
    QTextEdit* noteText = new QTextEdit(&noteDialog);
    QPushButton* colorButton = new QPushButton("Pick Color", &noteDialog);
    QPushButton* saveButton = new QPushButton("Save", &noteDialog);

    layout->addWidget(noteText);
    layout->addWidget(colorButton);
    layout->addWidget(saveButton);

    // Load the note when opening the dialog
    loadNoteData(selectedDate, noteText);

    connect(colorButton, &QPushButton::clicked, [&]() {
        QColor color = QColorDialog::getColor(Qt::white, this);
        if (color.isValid()) {
            noteText->setStyleSheet("background-color: " + color.name() + ";");
        }
    });

    connect(saveButton, &QPushButton::clicked, [&]() {
        saveNoteData(selectedDate, noteText->toPlainText());
        noteDialog.accept();
    });

    noteDialog.exec();
}

void CalendarApp::loadNoteData(const QDate& date, QTextEdit* noteText) {
    // Make sure the QTextEdit pointer is valid before accessing it
    if (!noteText) return;

    QDir dir("calendar_data");
    if (!dir.exists()) return;

    QFile file("calendar_data/" + date.toString("yyyy-MM") + ".json");
    if (!file.exists()) return;

    if (file.open(QIODevice::ReadOnly)) {
        QJsonDocument doc = QJsonDocument::fromJson(file.readAll());
        QJsonObject jsonData = doc.object();
        file.close();

        QString dayNote = jsonData.value(date.toString("dd")).toString();
        if (!dayNote.isEmpty()) {
            noteText->setPlainText(dayNote);  // Set the note in the QTextEdit
        }
    }
}

void CalendarApp::saveNoteData(const QDate& date, const QString& text) {
    if (!date.isValid()) return;  // Early return if the date is not valid

    QDir dir("calendar_data");
    if (!dir.exists()) dir.mkpath(".");

    QFile file("calendar_data/" + date.toString("yyyy-MM") + ".json");
    QJsonObject jsonData;

    if (file.open(QIODevice::ReadOnly)) {
        QJsonDocument doc = QJsonDocument::fromJson(file.readAll());
        jsonData = doc.object();
        file.close();
    }

    jsonData[date.toString("dd")] = text;

    if (file.open(QIODevice::WriteOnly)) {
        file.write(QJsonDocument(jsonData).toJson());
        file.close();
    }
}

int main(int argc, char* argv[]) {
    QApplication app(argc, argv);
    CalendarApp window;
    window.show();
    return app.exec();
}