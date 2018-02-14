%define beta %{nil}

Name:	qt5-qtvirtualkeyboard
Version: 5.10.1
%if "%{beta}" != "%{nil}"
%define qttarballdir qtvirtualkeyboard-everywhere-src-%{version}-%{beta}
Source0: http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%(echo %{beta} |sed -e "s,1$,,")/submodules/%{qttarballdir}.tar.xz
Release: 0.%{beta}.1
%else
%define qttarballdir qtvirtualkeyboard-everywhere-src-%{version}
Source0: http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
Release: 1
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
%setup -qn %{qttarballdir}
%qmake_qt5 *.pro

%build
%make

%install
make install install_docs INSTALL_ROOT="%{buildroot}"

%files
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QVirtualKeyboardPlugin.cmake
%{_libdir}/qt5/plugins/platforminputcontexts/libqtvirtualkeyboardplugin.so
%{_libdir}/qt5/qml/QtQuick/VirtualKeyboard
