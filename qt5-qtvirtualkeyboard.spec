%define beta rc2

Name:	qt5-qtvirtualkeyboard
Version: 5.9.0
Release: 0.%{beta}.1
%if "%{beta}" != "%{nil}"
Source0: http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/qtvirtualkeyboard-opensource-src-%{version}-%{beta}.tar.xz
%else
Source0: http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/qtvirtualkeyboard-opensource-src-%{version}.tar.xz
%endif
Summary: Qt Virtual Keyboard
URL: https://github.com/qtproject/qtvirtualkeyboard
License: LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-with-Qt-Company-Qt-exception-1.1
Group: System/Libraries
BuildRequires: qmake5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Svg)

%description
Qt text to virtualkeyboard library

%package examples
Summary: Examples for the Qt Virtual Keyboard
Group: Development/KDE and Qt

%description examples
Examples for the Qt Virtual Keyboard

%files examples
%{_libdir}/qt5/examples/virtualkeyboard

%prep
%if "%{beta}" != "%{nil}"
%setup -qn qtvirtualkeyboard-opensource-src-%{version}-%{beta}
%else
%setup -qn qtvirtualkeyboard-opensource-src-%{version}
%endif
%qmake_qt5 *.pro

%build
%make

%install
make install install_docs INSTALL_ROOT="%{buildroot}"

%files
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QVirtualKeyboardPlugin.cmake
%{_libdir}/qt5/plugins/platforminputcontexts/libqtvirtualkeyboardplugin.so
%{_libdir}/qt5/qml/QtQuick/VirtualKeyboard
