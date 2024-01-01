%define major 5
%define libname %mklibname Qt5VirtualKeyboard %{major}
%define develname %mklibname -d Qt5VirtualKeyboard
%define hunspelllib %mklibname Qt5HunspellInputMethod %{major}
%define hunspelldevel %mklibname -d Qt5HunspellInputMethod

%define beta %{nil}

Summary:	Qt Virtual Keyboard
Name:		qt5-qtvirtualkeyboard
Version:	5.15.12
%if "%{beta}" != "%{nil}"
%define qttarballdir qtvirtualkeyboard-everywhere-src-%{version}-%{beta}
Source0: http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
Release:	0.%{beta}.1
%else
%define qttarballdir qtvirtualkeyboard-everywhere-opensource-src-%{version}
Source0: http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
Release:	1
%endif
URL: https://github.com/qtproject/qtvirtualkeyboard
License: LGPL-2.1-with-Qt-Company-Qt-exception-1.1 or LGPL-3.0-with-Qt-Company-Qt-exception-1.1
Group: System/Libraries
# From KDE https://invent.kde.org/qt/qt/qtvirtualkeyboard -b kde/5.15
# [currently none required]
# OM specific
Patch2000:	qtvirtualkeyboard-5.15.0-hapticfeedback.patch
BuildRequires:	qmake5
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(hunspell)
BuildRequires:	qt5-qtdoc
BuildRequires:	qt5-qttools
BuildRequires:	qdoc5
BuildRequires:	qt5-doc
BuildRequires:	qt5-assistant
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1

%description
Qt text to virtualkeyboard library.

%package -n %{libname}
Summary:	The Qt Virtual Keyboard library
Group:		System/Libraries

%description -n %{libname}
The Qt Virtual Keyboard library.

%package -n %{develname}
Summary:	Development files for the Qt Virtual Keyboard library
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{develname}
Development files for the Qt Virtual Keyboard library.

%package -n %{hunspelllib}
Summary:	The Qt Hunspell input method library
Group:		System/Libraries

%description -n %{hunspelllib}
The Qt Hunspell input method library.

%package -n %{hunspelldevel}
Summary:	Development files for the Qt Hunspell input method library
Group:		Development/KDE and Qt
Requires:	%{hunspelllib} = %{EVRD}

%description -n %{hunspelldevel}
Development files for the Qt Hunspell input method library.

%package examples
Summary:	Examples for the Qt Virtual Keyboard
Group:		Development/KDE and Qt

%description examples
Examples for the Qt Virtual Keyboard.

%files examples
%{_libdir}/qt5/examples/virtualkeyboard

%prep
%autosetup -n %(echo %{qttarballdir}|sed -e 's,-opensource,,') -p1
%{_libdir}/qt5/bin/syncqt.pl -version %{version}
%qmake_qt5 *.pro

%build
%make_build
%make_build docs

%install
%make_install install_docs INSTALL_ROOT="%{buildroot}"

%files
%{_libdir}/qt5/plugins/platforminputcontexts/libqtvirtualkeyboardplugin.so
%{_libdir}/qt5/qml/QtQuick/VirtualKeyboard
%dir %{_libdir}/qt5/plugins/virtualkeyboard
# FIXME do we want to split language support into subpackages?
%{_libdir}/qt5/plugins/virtualkeyboard/*.so

%files -n %{libname}
%{_libdir}/libQt5VirtualKeyboard.so.%{major}*

%files -n %{develname}
%{_libdir}/libQt5VirtualKeyboard.so
%{_libdir}/libQt5VirtualKeyboard.prl
%{_libdir}/pkgconfig/Qt5VirtualKeyboard.pc
%{_libdir}/qt5/mkspecs/modules/qt_lib_virtualkeyboard*.pri
%{_libdir}/cmake/Qt5VirtualKeyboard
%{_includedir}/qt5/QtVirtualKeyboard
%{_libdir}/cmake/Qt5Gui/Qt5Gui_QVirtualKeyboardPlugin.cmake
%{_libdir}/cmake/Qt5HunspellInputMethod/Qt5HunspellInputMethodConfig.cmake
%{_libdir}/cmake/Qt5HunspellInputMethod/Qt5HunspellInputMethodConfigVersion.cmake
%doc %{_docdir}/qt5/qtvirtualkeyboard.qch
%doc %{_docdir}/qt5/qtvirtualkeyboard

%files -n %{hunspelllib}
%{_libdir}/libQt5HunspellInputMethod.so.%{major}*

%files -n %{hunspelldevel}
%{_libdir}/libQt5HunspellInputMethod.so
%{_libdir}/libQt5HunspellInputMethod.prl
%{_libdir}/qt5/mkspecs/modules/qt_lib_hunspellinputmethod*.pri
%{_includedir}/qt5/QtHunspellInputMethod
