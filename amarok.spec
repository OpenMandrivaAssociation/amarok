%define libname_orig lib%{name}
%define libname %mklibname %{name} 0
%define develname %mklibname -d %{name}

# Needed to obsolete old amarok2 packages
%define libname_orig2 libamarok2
%define libname2 %mklibname amarok2 0
%define develname2 %mklibname -d amarok2

Name:		amarok
Summary:	A powerful media player for KDE4
Version:	2.7.0
Release:	2
Epoch:		3
License:	GPLv2+
Url:		http://amarok.kde.org/
Group:		Sound
Source0:	http://fr2.rpmfind.net/linux/KDE/unstable/%{name}/%{version}/src/%{name}-%{version}.tar.bz2
Source1000:	amarok.rpmlintrc
Patch0:		amarok-2.6.0-lastfm1.patch
BuildRequires:	pkgconfig(taglib)
BuildRequires:	cmake
BuildRequires:	pkgconfig(libnjb)
BuildRequires:	libifp-devel
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(loudmouth-1.0)
BuildRequires:	mysql-static-devel
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(libvisual-0.4)
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	nepomuk-core-devel
BuildRequires:	pkgconfig(libgpod-1.0)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	libmp4v2-devel
BuildRequires:	pkgconfig(taglib-extras)
BuildRequires:	qtscriptgenerator
BuildRequires:	liblastfm-devel
BuildRequires:	pkgconfig(qca2)
BuildRequires:	pkgconfig(libofa)
BuildRequires:	ffmpeg-devel
BuildRequires:	libaio-devel
BuildRequires:	pkgconfig(libmygpo-qt) >= 1.0.6
BuildRequires:	clamz
BuildRequires:	gmock-devel	
Suggests:	%{name}-scripts = %{EVRD}
Requires:	mysql-common-core
Requires:	qtscriptbindings
Requires:	kde4-audiocd
Requires:	gstreamer0.10-tools
Obsoletes:	%{_lib}amarokqtjson1 < 3:2.7.0
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

%files -f %{name}.lang
%{_kde_bindir}/amarok
%{_kde_bindir}/amarokcollectionscanner
%{_kde_bindir}/amarok_afttagger
%{_kde_bindir}/amarokmp3tunesharmonydaemon
%{_kde_bindir}/amarokpkg
%{_kde_bindir}/amzdownloader
%{_kde_datadir}/applications/kde4/amarok.desktop
%{_kde_datadir}/applications/kde4/amarok_containers.desktop
%{_kde_datadir}/config/amarok.knsrc
%{_kde_datadir}/config/amarok_homerc
%{_kde_datadir}/config.kcfg/amarokconfig.kcfg
%{_kde_appsdir}/desktoptheme/*
%{_kde_appsdir}/solid/actions/amarok-play-audiocd.desktop
%{_kde_appsdir}/amarok
%{_kde_appsdir}/kconf_update/*
%{_kde_libdir}/kde4/*
%{_kde_libdir}/libampache_account_login.so
%{_kde_libdir}/libamarok_service_lastfm_shared.so
%{_kde_datadir}/config/amarokapplets.knsrc
%{_kde_datadir}/kde4/services/*
%{_kde_datadir}/kde4/servicetypes/*
%{_kde_iconsdir}/*/*/*/amarok.*
%{_kde_datadir}/dbus-1/interfaces/*
%exclude %{_kde_appsdir}/amarok/scripts/

#--------------------------------------------------------------------

%package scripts
Summary:	Scripts for amarok
Group:		Graphical desktop/KDE
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description scripts
This package includes python scripts for amarok.

%files scripts
%dir %{_kde_appsdir}/amarok/scripts/
%{_kde_appsdir}/amarok/scripts/*

#------------------------------------------------

%define libamaroklib_major 1
%define libamaroklib %mklibname amaroklib %{libamaroklib_major}

%package -n %{libamaroklib}
Summary:	Amarok 2 core library
Group:		System/Libraries

%description -n %{libamaroklib}
Amarok 2 core library.

%files -n %{libamaroklib}
%{_kde_libdir}/libamaroklib.so.%{libamaroklib_major}*

#------------------------------------------------

%define libamarokcore_major 1
%define libamarokcore %mklibname amarokcore %{libamarokcore_major}

%package -n %{libamarokcore}
Summary:	Amarok 2 core library
Group:		System/Libraries

%description -n %{libamarokcore}
Amarok 2 core library.

%files -n %{libamarokcore}
%{_kde_libdir}/libamarokcore.so.%{libamarokcore_major}*

#------------------------------------------------

%define libamarokpud_major 1
%define libamarokpud %mklibname amarokpud %{libamarokpud_major}

%package -n %{libamarokpud}
Summary:	Amarok 2 core library
Group:		System/Libraries

%description -n %{libamarokpud}
Amarok 2 core library.

%files -n %{libamarokpud}
%{_kde_libdir}/libamarokpud.so.%{libamarokpud_major}*

#------------------------------------------------

%define libamarokocsclient_major 4
%define libamarokocsclient %mklibname amarokocsclient %{libamarokocsclient_major}

%package -n %{libamarokocsclient}
Summary:	Amarok 2 core library
Group:		System/Libraries

%description -n %{libamarokocsclient}
Amarok 2 core library.

%files -n %{libamarokocsclient}
%{_kde_libdir}/libamarokocsclient.so.%{libamarokocsclient_major}*

#------------------------------------------------

%define libamaroksqlcollection_major 1
%define libamaroksqlcollection %mklibname amarok-sqlcollection %{libamaroksqlcollection_major}

%package -n %{libamaroksqlcollection}
Summary:	Amarok 2 core library
Group:		System/Libraries

%description -n %{libamaroksqlcollection}
Amarok 2 core library.

%files -n %{libamaroksqlcollection}
%{_kde_libdir}/libamarok-sqlcollection.so.%{libamaroksqlcollection_major}*

#------------------------------------------------

%define libamaroktranscoding_major 1
%define libamaroktranscoding %mklibname amarok-transcoding %{libamaroktranscoding_major}

%package -n %{libamaroktranscoding}
Summary:	Amarok 2 core library
Group:		System/Libraries

%description -n %{libamaroktranscoding}
Amarok 2 core library.

%files -n %{libamaroktranscoding}
%{_kde_libdir}/libamarok-transcoding.so.%{libamaroktranscoding_major}*

#------------------------------------------------

%package -n %{develname}
Summary:	Headers of %{name} for development
Group:		Development/C
Requires:	%{libamaroklib} = %{EVRD}
Requires:	%{libamarokcore} = %{EVRD}
Requires:	%{libamarokpud} = %{EVRD}
Requires:	%{libamarokocsclient} = %{EVRD}
Requires:	%{libamaroksqlcollection} = %{EVRD}
Requires:	%{libamaroktranscoding} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	%{libname_orig}-devel = %{EVRD}

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

%build
%cmake_kde4 -DKDE4_BUILD_TESTS=OFF

%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-kde --all-name


