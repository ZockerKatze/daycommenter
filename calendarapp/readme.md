# CalendarApp

A simple Qt5-based Calendar application with note-taking functionality.

## Features
- Interactive calendar view
- Add and edit notes for specific dates
- Save notes persistently in JSON format
- Simple and clean UI built with Qt Widgets

## Prerequisites
Before you begin, make sure you have the following dependencies installed:

- **Qt5 Framework** (including `qtbase5-dev` and `qttools5-dev-tools`)
- **qmake** (build tool for Qt projects)
- **g++** (C++ compiler)

You can install them on Debian-based systems with:
```sh
sudo apt update && sudo apt install qtbase5-dev qttools5-dev-tools g++
```
For Arch-based systems:
```sh
sudo pacman -S qt5-base qt5-tools
```
For Fedora:
```sh
sudo dnf install qt5-qtbase-devel qt5-qttools-devel gcc-c++
```

## Installation & Compilation
Follow these simple steps to build and run the application:

### 1. Clone the repository
```sh
git clone https://github.com/ZockerKatze/daycommenter/
cd daycommenter/calendarapp/
```

### 2. Run `qmake`
```sh
qmake calendarApp.pro
```
This will generate the `Makefile` needed for compilation.

### 3. Compile the application
```sh
make
```
After this step, the executable file will be generated.

### 4. Run the application
```sh
./calendarApp
```

## Uninstallation
To remove the compiled binaries:
```sh
make clean
```

## Troubleshooting
- **`qmake` not found?** Run `which qmake`. If it's missing, install the required Qt5 development packages.
- **Permissions error?** Try running `chmod +x calendarApp` before execution.
- **Errors related to missing Qt modules?** Ensure you have the correct Qt5 libraries installed by running `qmake -v` to check.

## Contributing
Pull requests and improvements are welcome! Feel free to fork the project and submit changes.

---

