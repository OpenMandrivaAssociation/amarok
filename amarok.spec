%define libname_orig lib%{name}
%define libname %mklibname %{name} 0
%define develname %mklibname -d %{name}

# Needed to obsolete old amarok2 packages
%define libname_orig2 libamarok2
%define libname2 %mklibname amarok2 0
%define develname2 %mklibname -d amarok2

Name: amarok
Summary: A powerful media player for KDE4
Version: 2.4.1
Release: 3
Epoch: 3
License: GPLv2+
Url: http://amarok.kde.org/
Group: Sound
Source0: http://fr2.rpmfind.net/linux/KDE/stable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
Patch0001: 0001-Fix-initial-preference-in-.desktop-from-2.1.90.patch
Patch0002: 0002-Remove-appendAndPlay-service-from-2.2.2.90.patch
Patch0003: 0003-Fix-CD-titleChanged-from-2.2.2.90.patch
Patch0004: 0004-Do-not-enable-Last.fm-by-default-from-2.2.0.patch
BuildRequires: taglib-devel >= 1.6-3
BuildRequires: cmake >= 2.4.5
BuildRequires: libnjb-devel
BuildRequires: libifp-devel
BuildRequires: libmtp-devel >= 0.3.0
BuildRequires: loudmouth-devel
BuildRequires: mysql-static-devel
BuildRequires: glib2-devel
BuildRequires: libvisual-devel
BuildRequires: kdelibs4-devel >= 2:4.2.0
BuildRequires: kdebase4-workspace-devel >= 4.2.0
BuildRequires: kdemultimedia4-devel >= 4.2.0
BuildRequires: libgpod-devel >= 0.7.0
BuildRequires: curl-devel
BuildRequires: libmp4v2-devel
BuildRequires: taglib-extras-devel >= 1.0.0-1
BuildRequires: qtscriptgenerator
BuildRequires: liblastfm-devel
BuildRequires: qca2-devel
BuildRequires: libofa-devel
BuildRequires: ffmpeg-devel
BuildRequires: libaio-devel
BuildRequires: libmygpo-qt-devel
Suggests:	%{name}-scripts = %{EVRD}
%if %{mdkversion} >= 201000
Requires: mysql-common-core
%else
Requires: mysql-common
%endif
Requires: qtscriptbindings
Requires: kde4-audiocd
Conflicts: %{libname2}-devel < 1:2.0.0-1.svn743954.3
Conflicts: %{develname} < 3:2.2.0-1
Obsoletes: amarok2 < 2:2.0.0-0.svn794807.2
Obsoletes: amarok2-engine-phonon < 2:2.0.0-0.svn794807.2
Obsoletes: amarok2-engine-xine < 2:2.0.0-0.svn794807.2
Obsoletes: amarok2-engine-void < 2:2.0.0-0.svn794807.2
Obsoletes: amarok-engine-void < 2:2.0.0
Obsoletes: amarok-engine-xine < 2:2.0.0
Obsoletes: amarok-engine-yauap < 2:2.0.0
Obsoletes: amarok-engine-arts                 <= 1.4-0.beta1_rc1.10mdk
Obsoletes: amarok-engine-gstreamer            <= 1.4-0.beta1_rc1.10mdk
Obsoletes: amarok-engine-akode                <= 1.4-0.beta2.3mdk
Obsoletes: amarok-engine-gstreamer0.10        <= 1.4-0.beta3.7mdk
Obsoletes: %{_lib}amarokqtjson1 < %{epoch}:%{version}
%if %mdkversion >= 201000
Obsoletes: kde3-amarok < 1:1.4.10-3
Obsoletes: kde3-amarok-engine-xine < 1:1.4.10-3
Obsoletes: kde3-amarok-engine-yauap < 1:1.4.10-3
Obsoletes: kde3-amarok-engine-void < 1:1.4.10-3
Obsoletes: kde3-amarok-engine < 1:1.4.10-3
%endif
%rename		amarok-utils

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

%files -f %name.lang 
%{_kde_bindir}/amarok
%{_kde_bindir}/amarokcollectionscanner
%{_kde_bindir}/amarok_afttagger
%{_kde_bindir}/amarokmp3tunesharmonydaemon
%{_kde_bindir}/amarokpkg
%{_kde_datadir}/applications/kde4/amarok.desktop
%{_kde_datadir}/applications/kde4/amarok_containers.desktop
%{_kde_datadir}/config/amarok.knsrc
%{_kde_datadir}/config/amarok_homerc
%{_kde_datadir}/config.kcfg/amarokconfig.kcfg
%{_kde_appsdir}/desktoptheme/*
%{_kde_appsdir}/solid/actions/amarok-play-audiocd.desktop
%{_kde_appsdir}/amarok
%{_kde_appsdir}/kconf_update/*
%{_kde_appsdir}/kconf_update/amarok.upd
%{_kde_libdir}/kde4/*
%{_kde_libdir}/libampache_account_login.so
%{_kde_datadir}/config/amarokapplets.knsrc
%{_kde_datadir}/kde4/services/*
%{_kde_datadir}/kde4/servicetypes/*
%{_kde_iconsdir}/*/*/*/amarok.*
%{_kde_datadir}/dbus-1/interfaces/*
%exclude %{_kde_appsdir}/amarok/scripts/

#--------------------------------------------------------------------

%package scripts
Summary: Scripts for amarok
Group: Graphical desktop/KDE
Requires: %{name} = %{EVRD}
Obsoletes: amarok2-scripts <= 2:2.0.0-0.svn794807.1
Obsoletes: %{_lib}amarok0-scripts < 2:2.0.0-0.svn794807.4
Obsoletes: %{_lib}amarok20-scripts < 2:2.0.0-0.svn794807.1
%if %mdkversion >= 201000
Obsoletes: kde3-amarok-scripts < 1:1.4.10-3
%endif
BuildArch:	noarch

%description scripts
This package includes python scripts for amarok.

%files scripts
%dir %{_kde_appsdir}/amarok/scripts/
%{_kde_appsdir}/amarok/scripts/*

#------------------------------------------------

%define libamaroklib_major 1
%define libamaroklib %mklibname amaroklib %libamaroklib_major

%package -n %libamaroklib
Summary: Amarok 2 core library
Group: System/Libraries
Obsoletes: %{libname2} < 2:2.0.0-0.svn794807.1

%description -n %libamaroklib
Amarok 2 core library.

%files -n %libamaroklib
%_kde_libdir/libamaroklib.so.%{libamaroklib_major}*

#------------------------------------------------

%define libamarokcore_major 1
%define libamarokcore %mklibname amarokcore %libamarokcore_major

%package -n %libamarokcore
Summary: Amarok 2 core library
Group: System/Libraries

%description -n %libamarokcore
Amarok 2 core library.

%files -n %libamarokcore
%_kde_libdir/libamarokcore.so.%{libamarokcore_major}*

#------------------------------------------------

%define libamarokpud_major 1
%define libamarokpud %mklibname amarokpud %libamarokpud_major

%package -n %libamarokpud
Summary: Amarok 2 core library
Group: System/Libraries
Conflicts: %{libname2} < 2:2.0.0-0.svn794807.1

%description -n %libamarokpud
Amarok 2 core library.

%files -n %libamarokpud
%_kde_libdir/libamarokpud.so.%{libamarokpud_major}*

#------------------------------------------------

%define libamarokocsclient_major 4
%define libamarokocsclient %mklibname amarokocsclient %libamarokocsclient_major

%package -n %libamarokocsclient
Summary: Amarok 2 core library
Group: System/Libraries
Conflicts: %{libname2} < 2:2.0.0-0.svn794807.1

%description -n %libamarokocsclient
Amarok 2 core library.

%files -n %libamarokocsclient
%_kde_libdir/libamarokocsclient.so.%{libamarokocsclient_major}*

#------------------------------------------------

%define libamaroksqlcollection_major 1
%define libamaroksqlcollection %mklibname amarok-sqlcollection %libamaroksqlcollection_major

%package -n %libamaroksqlcollection
Summary: Amarok 2 core library
Group: System/Libraries

%description -n %libamaroksqlcollection
Amarok 2 core library.

%files -n %libamaroksqlcollection
%_kde_libdir/libamarok-sqlcollection.so.%{libamaroksqlcollection_major}*

#------------------------------------------------

%define libamaroktranscoding_major 1
%define libamaroktranscoding %mklibname amarok-transcoding %libamaroktranscoding_major

%package -n %libamaroktranscoding
Summary: Amarok 2 core library
Group: System/Libraries

%description -n %libamaroktranscoding
Amarok 2 core library.

%files -n %libamaroktranscoding
%_kde_libdir/libamarok-transcoding.so.%{libamaroktranscoding_major}*

#------------------------------------------------

%package -n %{develname}
Summary: Headers of %name for development
Group: Development/C
Requires: %libamaroklib = %{EVRD}
Requires: %libamarokcore = %{EVRD}
Requires: %libamarokpud = %{EVRD}
Requires: %libamarokocsclient = %{EVRD}
Requires: %libamaroksqlcollection = %{EVRD}
Requires: %libamaroktranscoding = %{EVRD}
Provides: %{name}-devel = %{EVRD}
Provides: %{libname_orig}-devel = %{EVRD}
Obsoletes: %{mklibname -d amarok2 0} < 2:2.0.0-0.svn794807.2
Obsoletes: %{develname2} <= 2:2.0.0-0.svn794807.1

%description -n %{develname}
Headers of %{name} for development.

%files -n %{develname}
%{_kde_libdir}/libamaroklib.so
%{_kde_libdir}/libamarokcore.so
%{_kde_libdir}/libamarokpud.so
%{_kde_libdir}/libamarokocsclient.so
%{_kde_libdir}/libamarok-sqlcollection.so
%{_kde_libdir}/libamarok-transcoding.so

#--------------------------------------------------------------------

%prep
%setup -q
%patch0001 -p0 
%patch0002 -p0
%patch0004 -p0

%build
%cmake_kde4
%make

%install
%{makeinstall_std} -C build
%find_lang %{name} amarokcollectionscanner_qt amarok_scriptengine_qscript amarokpkg --with-html
