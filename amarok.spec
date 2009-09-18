%define libname_orig lib%{name}
%define libname %mklibname %{name} 0
%define develname %mklibname -d %{name}

# Needed to obsolete old amarok2 packages
%define libname_orig2 libamarok2
%define libname2 %mklibname amarok2 0
%define develname2 %mklibname -d amarok2


Name: amarok
Summary: A powerful media player for KDE4
Version: 2.1.85
Release: %mkrel  5
Epoch: 3
License: GPL
Url: http://amarok.kde.org/
Group: Sound
Source0: %{name}-%{version}.tar.bz2
Patch0:  amarok-2.0.96-fix-initial-preference.patch
Patch1:  amarok-2.1.85-taglib-fix-build.patch
# Those patches are provided by Amarok TEAM
# patches in the form amarok-version-r<relnum> are referent to the KDE
# commit numbered as <relnum>
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: taglib-devel >= 1.6-3
BuildRequires: cmake >= 2.4.5
BuildRequires: libnjb-devel
BuildRequires: libifp-devel
BuildRequires: libmtp-devel >= 0.3.0
BuildRequires: loudmouth-devel
BuildRequires: mysql-static-devel
BuildRequires: glib2-devel
BuildRequires: libvisual-devel
BuildRequires: kdelibs4-devel >= 4.0.85
BuildRequires: kdebase4-workspace-devel >= 4.0.85
BuildRequires: kdemultimedia4-devel >= 4.0.85
BuildRequires: libgpod-devel >= 0.7.0
BuildRequires: curl-devel
BuildRequires: libmp4v2-devel
BuildRequires: taglib-extras-devel >= 1.0.0-1
BuildRequires: qtscriptgenerator
BuildRequires: liblastfm-devel
Requires: %name-scripts
Requires: %name-utils
Requires: mysql-common
Requires: qtscriptbindings
Conflicts: %{libname2}-devel < 1:2.0.0-1.svn743954.3
Conflicts: %{develname} < 3:1.94-3
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

%files -f build/%name.lang 
%defattr(-,root,root) 
%{_kde_bindir}/amarok
%{_kde_bindir}/amarok_afttagger
%{_kde_bindir}/amarokmp3tunesharmonydaemon
%{_kde_bindir}/amarokpkg
%{_kde_datadir}/applications/kde4/amarok.desktop
%{_kde_datadir}/config/amarok.knsrc
%{_kde_datadir}/config/amarok_homerc
%{_kde_datadir}/config.kcfg/amarokconfig.kcfg
%{_kde_appsdir}/desktoptheme/*
%dir %{_kde_appsdir}/amarok
%{_kde_appsdir}/amarok/*
%{_kde_libdir}/kde4/*
#%{_kde_libdir}/libamarok_service_liblastfm.so
%{_kde_appsdir}/solid/actions/amarok-play-audiocd.desktop
%{_kde_datadir}/config/amarokapplets.knsrc
%{_kde_datadir}/kde4/services/*
%{_kde_datadir}/kde4/servicetypes/*
%{_kde_libdir}/strigi/strigita_audible.so
%{_kde_libdir}/strigi/strigita_mp4.so
%{_kde_iconsdir}/*/*/*/amarok.*
%exclude %{_kde_appsdir}/amarok/scripts/

#--------------------------------------------------------------------

%package utils
Summary: Utilities for amarok
Group: Graphical desktop/KDE

%description utils
Utilities for amarok


%files utils
%defattr(-,root,root)
%{_kde_bindir}/amarokcollectionscanner

#--------------------------------------------------------------------

%package scripts
Summary: Scripts for amarok
Group: Graphical desktop/KDE
Requires: %name = %epoch:%version-%release
Obsoletes: amarok2-scripts <= 2:2.0.0-0.svn794807.1
Obsoletes: %{_lib}amarok0-scripts < 2:2.0.0-0.svn794807.4
Obsoletes: %{_lib}amarok20-scripts < 2:2.0.0-0.svn794807.1

%description scripts
This package includes python scripts for amarok.

%files scripts
%defattr(-,root,root)
%dir %{_kde_appsdir}/amarok/scripts/
%{_kde_appsdir}/amarok/scripts/*
#%{_kde_libdir}/kde4/plugins/script/*

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
%defattr(-,root,root)
%_kde_libdir/libamaroklib.so.%libamaroklib_major
%_kde_libdir/libamaroklib.so.%libamaroklib_major.0.0

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
%defattr(-,root,root)
%_kde_libdir/libamarokpud.so.%libamarokpud_major
%_kde_libdir/libamarokpud.so.%libamarokpud_major.0.0

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
%defattr(-,root,root)
%_kde_libdir/libamarokocsclient.so.%libamarokocsclient_major
%_kde_libdir/libamarokocsclient.so.%libamarokocsclient_major.3.0

#------------------------------------------------

%package -n %{develname}
Summary: Headers of %name for development
Group: Development/C
Requires: %libamarokpud = %epoch:%{version}-%{release}
Provides: %{name}-devel = %epoch:%{version}-%{release}
Provides: %{libname_orig}-devel = %epoch:%{version}-%{release}
Obsoletes: %{mklibname -d amarok2 0} < 2:2.0.0-0.svn794807.2
Obsoletes: %{develname2} <= 2:2.0.0-0.svn794807.1

%description -n %{develname}
Headers of %{name} for development.

%files -n %{develname}
%defattr(-,root,root)
%{_kde_libdir}/libamaroklib.so
%{_kde_libdir}/libamarokpud.so
%{_kde_libdir}/libamarokocsclient.so
%{_kde_datadir}/dbus-1/interfaces/*

#--------------------------------------------------------------------

%prep
%setup -q 
%patch0 -p0
%patch1 -p1

%build
%cmake_kde4 -DLOCALE_INSTALL_DIR=%{_datadir}/locale -DLIB_INSTALL_DIR=%{_libdir}

%make

%install
rm -rf %buildroot
cd build
%{makeinstall_std}
%find_lang %{name} amarokcollectionscanner_qt amarok_scriptengine_qscript amarokpkg

%clean
rm -rf %buildroot
