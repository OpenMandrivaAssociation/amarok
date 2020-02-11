Summary:	A powerful media player for KDE
Name:		amarok
Version:	2.9.20190508
Release:	2
Group:		Sound
License:	GPLv2+
Url:		http://amarok.kde.org/
Source0:	http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
Source1000:	amarok.rpmlintrc
#Patch0:		amarok-2.6.0-lastfm1.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(KF5Codecs)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5DBusAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5DNSSD)
BuildRequires:	cmake(KF5GlobalAccel)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5NewStuff)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5NotifyConfig)
BuildRequires:	cmake(KF5Package)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5TextEditor)
BuildRequires:	cmake(KF5ThreadWeaver)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavdevice)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(libpostproc)
BuildRequires:	pkgconfig(libofa)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libcrypto)
BuildRequires:	pkgconfig(libgcrypt)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(loudmouth-1.0)
BuildRequires:	pkgconfig(liblz4)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Script)
BuildRequires:	pkgconfig(Qt5QuickControls2)
BuildRequires:	pkgconfig(Qt5WebEngine)
BuildRequires:	pkgconfig(Qt5QuickWidgets)
BuildRequires:	pkgconfig(Qt5ScriptTools)
BuildRequires:	pkgconfig(Qt5Svg)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	cmake(KF5Parts)
BuildRequires:	cmake(Phonon4Qt5)
BuildRequires:	%{_lib}aio-devel
BuildRequires:	pkgconfig(lzo2)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	systemd-macros
# If you want ipod support
#BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	mariadb-static-devel
BuildRequires:	mariadb-server
BuildRequires:	gtest-devel
Requires:	mariadb-common

Obsoletes:	%{_lib}amarokqtjson1 < 3:2.7.0
%define	devname	%mklibname -d %{name}
Obsoletes:	%{devname} < 3:%{version}
Obsoletes:	%{name}-scripts < 3:%{version}
%define libamaroklib %mklibname amaroklib 1
Obsoletes:	%{libamaroklib} < 3:%{version}
%define libamarokcore %mklibname amarokcore 1
Obsoletes:	%{libamarokcore} < 3:%{version}
%define libamarokpud %mklibname amarokpud 1
Obsoletes:	%{libamarokpud} < 3:%{version}
%define libamarokocsclient %mklibname amarokocsclient 4
Obsoletes:	%{libamarokocsclient} < 3:%{version}
%define libamarokshared %mklibname amarokshared 1
Obsoletes:	%{libamarokshared} < 3:%{version}
%define libamaroksqlcollection %mklibname amarok-sqlcollection 1
Obsoletes:	%{libamaroksqlcollection} < 3:%{version}
%define libamaroktranscoding %mklibname amarok-transcoding 1
Obsoletes:	%{libamaroktranscoding} < 3:%{version}
%rename		amarok-utils

# Allow transcoding
Suggests:	ffmpeg

%description
Feature Overview

* Music Collection:
You have a huge music library and want to locate tracks quickly? Let amaroK's
powerful Collection take care of that! It's a database powered music store,
which keeps track of your complete music library, allowing you to find any
title in a matter of seconds.

* Intuitive User Interface:
You will be amazed to see how easy amaroK is to use! Simply drag-and-drop files
into the playlist. No hassle with complicated  buttons or tangled menus.
Listening to music has never been easier!

* Streaming Radio:
Web streams take radio to the next level: Listen to thousands of great radio
stations on the internet, for free! amaroK provides excellent streaming
support, with advanced features, such as displaying titles of the currently
playing songs.

* Context Browser:
This tool provides useful information on the music you are currently listening
to, and can make listening suggestions, based on your personal music taste. An
innovate and unique feature.

* Visualizations:
amaroK is compatible with XMMS visualization plugins. Allows you to use the
great number of stunning visualizations available on the net. 3d visualizations
with OpenGL are a great way to enhance your music experience.

%files
%{_bindir}/amarok
%{_bindir}/amarokpkg
%{_bindir}/amarokcollectionscanner
%{_bindir}/amarok_afttagger
# No separate libpackages necessary, those are more like modules
# than like libraries even if they're packaged in shared library
# format
%{_libdir}/libamarok-transcoding.so*
%{_libdir}/libampache_account_login.so
%{_libdir}/libamarokpud.so
%{_libdir}/libamarok-sqlcollection.so*
%{_libdir}/libamarokcore.so*
%{_libdir}/libamaroklib.so*
%{_libdir}/libamarokshared.so*
%{_libdir}/qt5/qml/org/kde/amarok
%{_libdir}/qt5/plugins/amarok_*.so
%{_libdir}/qt5/plugins/kcm_amarok_*.so
%{_datadir}/kconf_update/*
%{_datadir}/kpackage/amarok
%{_datadir}/kpackage/genericqml/org.kde.amarok*
%{_datadir}/dbus-1/interfaces/org.kde.amarok*
%{_datadir}/dbus-1/interfaces/org.freedesktop.MediaPlayer*
%{_datadir}/config.kcfg/*
%{_datadir}/solid/actions/amarok*.desktop
%{_datadir}/kservices5/amarok*
%{_datadir}/kservices5/ServiceMenus/*.desktop
%{_datadir}/kservicetypes5/amarok*.desktop
%{_datadir}/metainfo/org.kde.amarok.*
%{_datadir}/applications/org.kde.amarok*
%{_datadir}/icons/*/*/*/amarok.*
%{_datadir}/amarok
%{_datadir}/knotifications5/amarok.*
%{_sysconfdir}/xdg/amarok*

%prep
%autosetup -p1

%build
%cmake_kde5

%ninja_build

%install
%ninja_install -C build
