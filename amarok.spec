Summary:	A powerful media player for KDE
Name:		amarok
Version:	3.2.2
Release:	3
Group:		Sound
License:	GPLv2+
Url:		https://amarok.kde.org/
Source0:  https://download.kde.org/stable/amarok/%{version}/amarok-%{version}.tar.xz
# git Source0:	https://invent.kde.org/multimedia/amarok/-/archive/master/amarok-master.tar.bz2
Source1000:	amarok.rpmlintrc
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DNSSD)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6ThreadWeaver)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Wallet)
BuildRequires:	pkgconfig(taglib)
# Optional now, can be dropped anytime
BuildRequires:  pkgconfig(taglib-extras)
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
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Help)
BuildRequires:  cmake(Qt6Linguist)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6UiTools)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:	%{_lib}aio-devel
BuildRequires:	pkgconfig(lzo2)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	systemd-rpm-macros
# If you want ipod support
#BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	mariadb-static-devel
BuildRequires:	mariadb-server
BuildRequires:	gtest-devel
# Not yet ready for qt6
#BuildRequires:  %{_lib}lastfm-devel
Requires: mariadb
Requires:	mariadb-common

Requires: qt6-qtdeclarative
# Keep this one
Requires: phonon4qt6-gstreamer
Requires: plasma6-kio-extras
Requires: kf6-kirigami
Requires: plasma6-audiocd-kio

# Allow transcoding
Recommends:	ffmpeg

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

%files -f %{name}.lang
%{_bindir}/amarok
%{_bindir}/amarokcollectionscanner
%{_bindir}/amarok_afttagger
%{_libdir}/libamarok-transcoding.so*
%{_libdir}/libampache_account_login.so
%{_libdir}/libamarokpud.so
%{_libdir}/libamarok-sqlcollection.so*
%{_libdir}/libamarokcore.so*
%{_libdir}/libamaroklib.so*
%{_libdir}/libamarokshared.so*
%{_libdir}/qt6/plugins/amarok_collection-*
%{_libdir}/qt6/plugins/amarok_importer-*
%{_libdir}/qt6/plugins/amarok_service*
%{_libdir}/qt6/plugins/amarok_storage-mysqlestorage.so
%{_libdir}/qt6/plugins/amarok_storage-mysqlserverstorage.so
%{_libdir}/qt6/plugins/kcm_amarok*
%{_libdir}/qt6/qml/org/kde/amarok/
%{_datadir}/kio/servicemenus/amarok_append.desktop
%{_datadir}/knotifications6/amarok.notifyrc
%{_datadir}/kpackage/amarok/
%{_datadir}/kpackage/genericqml/org.kde.amarok.context/
%{_datadir}/dbus-1/interfaces/org.kde.amarok*
%{_datadir}/dbus-1/services/org.kde.amarok.service
%{_datadir}/config.kcfg/*
%{_datadir}/solid/actions/amarok*.desktop
%{_datadir}/metainfo/org.kde.amarok.*
%{_datadir}/applications/org.kde.amarok*
%{_datadir}/icons/*/*/*/amarok.*
%{_datadir}/amarok
%{_sysconfdir}/xdg/amarok*

%prep
%autosetup -p1 -n %{name}-%{version}

%cmake -DBUILD_WITH_QT6:BOOL=ON -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html
