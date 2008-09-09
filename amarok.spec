%define libname_orig lib%{name}
%define libname %mklibname %{name} 0
%define develname %mklibname -d %{name}

# Needed to obsolete old amarok2 packages
%define libname_orig2 libamarok2
%define libname2 %mklibname amarok2 0
%define develname2 %mklibname -d amarok2

%define svn 857904

Name: amarok
Summary: A powerful media player for KDE4
Version: 1.90
Release: %mkrel 0.%svn.2
Epoch: 3
License: GPL
Url: http://amarok.kde.org/
Group: Sound
Source0: %{name}-%{version}.%svn.tar.bz2
Source1: amarok-1.90-po-files.tar.bz2
Patch0:  amarok-1.90-add-po-support.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: taglib-devel
BuildRequires: cmake >= 2.4.5
BuildRequires: libnjb-devel
BuildRequires: libifp-devel
BuildRequires: libmtp-devel >= 0.3.0
BuildRequires: loudmouth-devel
BuildRequires: mysql-devel
BuildRequires: glib2-devel
BuildRequires: libvisual-devel
BuildRequires: kdelibs4-devel >= 4.0.85
BuildRequires: kdebase4-workspace-devel >= 4.0.85
BuildRequires: kdemultimedia4-devel >= 4.0.85
BuildRequires: libgpod-devel
BuildRequires: curl-devel
BuildRequires: libmp4v2-devel
Requires: %name-scripts
Conflicts: %{libname2}-devel < 1:2.0.0-1.svn743954.3
Obsoletes: amarok2 < 2:2.0.0-0.svn794807.2
Obsoletes: amarok2-engine-phonon < 2:2.0.0-0.svn794807.2
Obsoletes: amarok2-engine-xine < 2:2.0.0-0.svn794807.2
Obsoletes: amarok2-engine-void < 2:2.0.0-0.svn794807.2
Obsoletes: amarok-engine-void < 1:1.4.9
Obsoletes: amarok-engine-xine < 1:1.4.9
Obsoletes: amarok-engine-yauap < 1:1.4.9
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

%if %mdkversion < 200900
%post
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%files -f build/%name.lang 
%defattr(-,root,root) 
%{_kde_bindir}/amarok
%{_kde_bindir}/amarok_afttagger
%{_kde_bindir}/amarokcollectionscanner
%{_kde_bindir}/amarokmp3tunesharmonydaemon
%{_kde_datadir}/applications/kde4/amarok.desktop
%{_kde_datadir}/config/amarok.knsrc
%{_kde_datadir}/config.kcfg/amarok.kcfg
%{_kde_appsdir}/desktoptheme/*
%dir %{_kde_appsdir}/amarok
%{_kde_appsdir}/amarok/*
%{_kde_libdir}/kde4/*
%{_kde_datadir}/kde4/services/*
%{_kde_datadir}/kde4/servicetypes/*
%{_kde_libdir}/strigi/strigita_audible.so
%{_kde_libdir}/strigi/strigita_mp4.so
%{_kde_iconsdir}/*/*/*/amarok.*
%exclude %{_kde_appsdir}/amarok/scripts/

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
%{_kde_libdir}/kde4/plugins/script/*

#------------------------------------------------

%define libamarok_taglib_major 1
%define libamarok_taglib %mklibname amarok_taglib %libamarok_taglib_major

%package -n %libamarok_taglib
Summary: Amarok 2 core library
Group: System/Libraries
Conflicts:   %{libname2} < 2.0.0-1.svn710748.1

%description -n %libamarok_taglib
Amarok 2 core library.

%if %mdkversion < 200900
%post -n %libamarok_taglib -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libamarok_taglib -p /sbin/ldconfig
%endif

%files -n %libamarok_taglib
%defattr(-,root,root)
%_kde_libdir/libamarok_taglib.so.%libamarok_taglib_major
%_kde_libdir/libamarok_taglib.so.%libamarok_taglib_major.0.0

#------------------------------------------------

%define libamaroklib_major 1
%define libamaroklib %mklibname amaroklib %libamaroklib_major

%package -n %libamaroklib
Summary: Amarok 2 core library
Group: System/Libraries
Obsoletes: %{libname2} < 2:2.0.0-0.svn794807.1

%description -n %libamaroklib
Amarok 2 core library.

%if %mdkversion < 200900
%post -n %libamaroklib -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libamaroklib -p /sbin/ldconfig
%endif

%files -n %libamaroklib
%defattr(-,root,root)
%_kde_libdir/libamaroklib.so.%libamaroklib_major
%_kde_libdir/libamaroklib.so.%libamaroklib_major.0.0

#------------------------------------------------

%define libamarokplasma_major 2
%define libamarokplasma %mklibname amarokplasma %libamarokplasma_major

%package -n %libamarokplasma
Summary: Amarok 2 core library
Group: System/Libraries
Conflicts: %{libname2} < 2:2.0.0-0.svn794807.1

%description -n %libamarokplasma
Amarok 2 core library.

%if %mdkversion < 200900
%post -n %libamarokplasma -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libamarokplasma -p /sbin/ldconfig
%endif

%files -n %libamarokplasma
%defattr(-,root,root)
%_kde_libdir/libamarokplasma.so.%libamarokplasma_major
%_kde_libdir/libamarokplasma.so.%libamarokplasma_major.0.0

#------------------------------------------------

%define libamarokpud_major 1
%define libamarokpud %mklibname amarokpud %libamarokpud_major

%package -n %libamarokpud
Summary: Amarok 2 core library
Group: System/Libraries
Conflicts: %{libname2} < 2:2.0.0-0.svn794807.1

%description -n %libamarokpud
Amarok 2 core library.

%if %mdkversion < 200900
%post -n %libamarokpud -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libamarokpud -p /sbin/ldconfig
%endif

%files -n %libamarokpud
%defattr(-,root,root)
%_kde_libdir/libamarokpud.so.%libamarokpud_major
%_kde_libdir/libamarokpud.so.%libamarokpud_major.0.0

#------------------------------------------------

%package -n %{develname}
Summary: Headers of %name for development
Group: Development/C
Requires: %libamarok_taglib = %epoch:%{version}-%{release}
Requires: %libamaroklib = %epoch:%{version}-%{release}
Requires: %libamarokpud = %epoch:%{version}-%{release}
Requires: %libamarokplasma = %epoch:%{version}-%{release}
Provides: %{name}-devel = %epoch:%{version}-%{release}
Provides: %{libname_orig}-devel = %epoch:%{version}-%{release}
Obsoletes: %{mklibname -d amarok2 0} < 2:2.0.0-0.svn794807.2
Obsoletes: %{develname2} <= 2:2.0.0-0.svn794807.1

%description -n %{develname}
Headers of %{name} for development.

%files -n %{develname}
%defattr(-,root,root)
%{_kde_libdir}/*.so
%{_kde_datadir}/dbus-1/interfaces/*

#--------------------------------------------------------------------

%prep
%setup -q -a 1
%patch0 -p0

%build
%cmake_kde4 -DLOCALE_INSTALL_DIR=%{_datadir}/locale -DLIB_INSTALL_DIR=%{_libdir}

%make

%install
rm -rf %buildroot
cd build
%{makeinstall_std}
%find_lang %{name}

%clean
rm -rf %buildroot
