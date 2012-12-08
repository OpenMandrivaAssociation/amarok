%define libname_orig lib%{name}
%define libname %mklibname %{name} 0
%define develname %mklibname -d %{name}

# Needed to obsolete old amarok2 packages
%define libname_orig2 libamarok2
%define libname2 %mklibname amarok2 0
%define develname2 %mklibname -d amarok2

Name:		amarok
Summary:	A powerful media player for KDE4
Version:	2.6.0
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
BuildRequires:	pkgconfig(libmygpo-qt)
Suggests:	%{name}-scripts = %{EVRD}
Requires:	mysql-common-core
Requires:	qtscriptbindings
Requires:	kde4-audiocd
Obsoletes:	%{_lib}amarokqtjson1 < %{epoch}:%{version}
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
%cmake_kde4

%make

%install
%makeinstall_std -C build

%find_lang %{name} --with-kde --all-name



%changelog
* Fri Aug 17 2012 Crispin Boylan <crisb@mandriva.org> 3:2.6.0-1
+ Revision: 815219
- Apply upstream patch to fix lastfm 1.0 compat
- New release

* Fri Jun 08 2012 Bernhard Rosenkraenzer <bero@bero.eu> 3:2.5.90-1
+ Revision: 803455
- Update to 2.5.90
- Build for ffmpeg 0.11.x

* Thu Mar 29 2012 Andrey Bondrov <abondrov@mandriva.org> 3:2.5.0-2
+ Revision: 788241
- Add patch0 from upstream to fix Amarok bug 290123 (broken context view), spec cleanup

* Thu Jan 05 2012 Crispin Boylan <crisb@mandriva.org> 3:2.5.0-1
+ Revision: 757934
- New release

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New version 2.4.90

* Fri Nov 25 2011 Crispin Boylan <crisb@mandriva.org> 3:2.4.3-3
+ Revision: 733462
- Rebuild for new kde

* Fri Nov 18 2011 Crispin Boylan <crisb@mandriva.org> 3:2.4.3-2
+ Revision: 731564
- Bump release
- Fix find_lang again
- Fix find_lang
- Use with-kde for help files
- Remove obsolete(?) with-html on find_lang
- New release

  + Götz Waschk <waschk@mandriva.org>
    - rebuild for new libmtp

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Clean spec file layout

* Fri May 20 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 3:2.4.1-3
+ Revision: 676249
- Rebuild

* Tue May 10 2011 Per Øyvind Karlsen <peroyvind@mandriva.org> 3:2.4.1-2
+ Revision: 673173
- cleanups
- update license
- use %%{EVRD} in dependency
- name -scripts package noarch
- merge -utils package into main package as the two-way dependency makes them
  useless without eachother and -utils package's only pulling in one additional,
  minor library dependency anyways..
- untangle a dependency loop

* Sun May 08 2011 Funda Wang <fwang@mandriva.org> 3:2.4.1-1
+ Revision: 672504
- new version 2.4.1

* Wed Mar 30 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.4.0.90-3
+ Revision: 649053
- We do noxt need a %%clean section either
- We do not use %%mkrel anymore
- Remove patch5, it will not be needed with next mysql rpm

* Sun Mar 20 2011 Funda Wang <fwang@mandriva.org> 3:2.4.0.90-2
+ Revision: 647124
- change plugin version per requested by upstream

* Sun Mar 20 2011 Funda Wang <fwang@mandriva.org> 3:2.4.0.90-1
+ Revision: 647104
- update file list
- 2.4.1 beta1

* Thu Mar 17 2011 Oden Eriksson <oeriksson@mandriva.com> 3:2.4.0-2
+ Revision: 645739
- relink against libmysqlclient.so.18

* Sun Jan 16 2011 Funda Wang <fwang@mandriva.org> 3:2.4.0-1
+ Revision: 631140
- New version 2.4.0
- fix link against mysql 5.5

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against mysql-5.5.8 libs, again

* Tue Dec 28 2010 Oden Eriksson <oeriksson@mandriva.com> 3:2.3.90-2mdv2011.0
+ Revision: 625724
- fix deps
- rebuilt against mysql-5.5.8 libs

  + Funda Wang <fwang@mandriva.org>
    - New version 2.3.90
    - disable patch 3 for now (do not know where it comes from)

* Tue Sep 21 2010 Funda Wang <fwang@mandriva.org> 3:2.3.2-1mdv2011.0
+ Revision: 580329
- new version 2.3.2

* Tue Aug 17 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.3.1.90-1mdv2011.0
+ Revision: 571067
- Fix file list
- New version 2.3.2 Beta1

* Tue Jun 01 2010 Funda Wang <fwang@mandriva.org> 3:2.3.1-1mdv2010.1
+ Revision: 546820
- New version 2.3.1 final

* Thu Apr 29 2010 Christophe Fergeau <cfergeau@mandriva.com> 3:2.3.0.90-3mdv2010.1
+ Revision: 540854
- rebuild so that shared libraries are properly stripped again

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 3:2.3.0.90-2mdv2010.1
+ Revision: 540398
- rebuild so that shared libraries are properly stripped again

* Tue Apr 27 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.3.0.90-1mdv2010.1
+ Revision: 539499
- New version 2.3.1 beta1 :
       - Remove Merged patches
       - Rediff mdv patches

* Wed Apr 07 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.3.0-4mdv2010.1
+ Revision: 532521
- Rebuild against new openssl

* Fri Apr 02 2010 Colin Guthrie <cguthrie@mandriva.org> 3:2.3.0-3mdv2010.1
+ Revision: 530784
- Add upstream patches relating to volume changes
- Add fix for iPhone/iPodTouch permissions problems
- Adapt to a git-based patch structure to ease forward-porting and backporting

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - versionnate requires

* Tue Mar 16 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.3.0-1mdv2010.1
+ Revision: 520677
- Remove merged patch
- New version 2.3.0
- Add strueg patch fixing amarok crash

* Mon Mar 08 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.2.2.90-5mdv2010.1
+ Revision: 516005
- Git snapshot fix amarok start
  Rediff patches

* Fri Feb 26 2010 Oden Eriksson <oeriksson@mandriva.com> 3:2.2.2.90-4mdv2010.1
+ Revision: 511551
- rebuilt against openssl-0.9.8m

* Wed Feb 17 2010 Oden Eriksson <oeriksson@mandriva.com> 3:2.2.2.90-3mdv2010.1
+ Revision: 507014
- rebuild

* Wed Feb 17 2010 Funda Wang <fwang@mandriva.org> 3:2.2.2.90-2mdv2010.1
+ Revision: 506923
- rebuild

* Sun Feb 14 2010 Funda Wang <fwang@mandriva.org> 3:2.2.2.90-1mdv2010.1
+ Revision: 505928
- New version 2.2.2.90
- rediff CD-title patch, appendAndPlay patch
- drop upstream patches

* Tue Feb 09 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.2.2-3mdv2010.1
+ Revision: 503226
- Backport patches, now amarok solid action works

* Fri Jan 15 2010 Funda Wang <fwang@mandriva.org> 3:2.2.2-2mdv2010.1
+ Revision: 491599
- add missing requires
- renew tarball with latest released file
- rediff CD title patch
- fix lib ext

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Update to amarok 2.2.2
    - Clean spec file

* Wed Dec 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.2.1.90-1mdv2010.1
+ Revision: 479213
- Update to amarok 2.2.2 beta1
  Remove patch 101 : Merged upstream

* Sun Nov 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.2.1-1mdv2010.1
+ Revision: 469061
- Use a clever name for patches even if they come GIT
- Update to amarok 2.2.1
  Remove merged patches
  Rediff patches

  + Funda Wang <fwang@mandriva.org>
    - add upstream patch to have it build

* Sat Oct 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.2.0-10mdv2010.0
+ Revision: 459139
- Obsoletes kde3-amarok-scripts
- Obsolete for mdv >= 2010.0

* Thu Oct 22 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.2.0-9mdv2010.0
+ Revision: 458978
- Add obsolete for 2009.0 -> 2010.0 upgrade

* Sun Oct 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.2.0-8mdv2010.0
+ Revision: 458109
- Add patch from upstream to fix splashscreen with lastfm
  Disable patch5
- Disable lastfm by default ( but still can be enabled manually )
- Apply lyrics patch

* Thu Oct 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.2.0-5mdv2010.0
+ Revision: 457486
- Fix audio cd support

* Wed Oct 07 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 3:2.2.0-4mdv2010.0
+ Revision: 455757
- rebuild for new curl SSL backend

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Add the bugreport

* Thu Oct 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.2.0-3mdv2010.0
+ Revision: 452353
- Fix file list
- Remove the solid action as it does not work for now

* Thu Oct 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.2.0-2mdv2010.0
+ Revision: 452245
- Remove not userfriendly servicemenu

* Thu Oct 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.2.0-1mdv2010.0
+ Revision: 452237
- Time to release amarok
- Fix Requires for audiocd support
- Move dbus interfaces in amarok packages, as this is needed for ServiceMenus
- Fix  typo
- Amarok 2.2.0 requires at least kde 4.2
- Update to amarok 2.2.0 final

* Tue Sep 29 2009 Anssi Hannula <anssi@mandriva.org> 3:2.1.90-2mdv2010.0
+ Revision: 450956
- require mysql-common-core instead of full mysql-common on 2010.0+

* Wed Sep 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.1.90-1mdv2010.0
+ Revision: 447776
- Fix patch
- Update to Rc1

* Fri Sep 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.1.85-5mdv2010.0
+ Revision: 444485
- Version BuildRequires
  Fix build against new taglib ( from git )
- Rebuild
- Remove conflict
- Rebuild

  + Raphaël Gertz <rapsys@mandriva.org>
    - Rebuild for taglib-extras

* Wed Sep 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.1.85-1mdv2010.0
+ Revision: 443529
- This is release time, Enjoy
- Update to amarok 2.2beta2

* Fri Sep 04 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.1.80-1mdv2010.0
+ Revision: 429960
- Fix file list
- Update to amarok 2.2 beta1

* Wed Aug 19 2009 Raphaël Gertz <rapsys@mandriva.org> 3:2.1.1-3mdv2010.0
+ Revision: 418248
- Rebuild for libjpeg7

* Sun Aug 16 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.1.1-2mdv2010.0
+ Revision: 416917
- Rebuild against new libjpeg

* Wed Jun 17 2009 Helio Chissini de Castro <helio@mandriva.com> 3:2.1.1-1mdv2010.0
+ Revision: 386779
- Amarok bugfix update release 2.1.1

* Mon Jun 01 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.1-1mdv2010.0
+ Revision: 382022
- Update to version 2.1

* Wed May 13 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.0.96-3mdv2010.0
+ Revision: 375584
- Fix initial preference

* Mon May 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.0.96-2mdv2010.0
+ Revision: 374677
- Fix Requires (Bug #50813)

* Mon May 11 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.0.96-1mdv2010.0
+ Revision: 374300
- Update to amarok 2.0 beta2

* Wed Apr 29 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.0.90-1mdv2010.0
+ Revision: 369147
- Update to amarok 2.1 Beta1
  Create amarok-utils as asked by upstream devs

* Tue Apr 07 2009 Helio Chissini de Castro <helio@mandriva.com> 3:2.0.2-2mdv2009.1
+ Revision: 365064
- Try fix lastfm audio scrobbler. Fix bug https://qa.mandriva.com/show_bug.cgi?id=49595

* Mon Mar 02 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.0.2-1mdv2009.1
+ Revision: 347495
- Add back mysql compile fix
- Update to amarok 2.0.2

* Sat Jan 24 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.0.1.1-5mdv2009.1
+ Revision: 333341
- Add upstream patch  to fix build with new libgpod
- Rebuild

* Sun Jan 18 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.0.1.1-3mdv2009.1
+ Revision: 330917
- Better fix for mysql link

* Thu Jan 15 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.0.1.1-2mdv2009.1
+ Revision: 329958
- Fix link again
- Bump release
- Add mysql patch ( to make the collection working again)
  Remove verbose
- Move it on its own package ( next commit)

* Wed Jan 14 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.0.1.1-1mdv2009.1
+ Revision: 329533
- Fix build
- some more fixes for new libmp4
- Fix build with new libmp4v2
- Update to amarok 2.0.1.1
- Update to amarok 2.0.1

  + Funda Wang <fwang@mandriva.org>
    - po related files are not needed any more

* Fri Dec 05 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:2.0-1mdv2009.1
+ Revision: 310909
- Update to Final 2.0 Version
  Add 2 official patches to fix regressions

* Sun Nov 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.98-1mdv2009.1
+ Revision: 305963
- Update to amarok 2.0 Rc1

* Sun Nov 02 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.94-3mdv2009.1
+ Revision: 299199
- Fix File list and conflicts

* Sat Nov 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.94-2mdv2009.1
+ Revision: 299175
- Sorry i forgot to add back codeina support

* Sat Nov 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.94-1mdv2009.1
+ Revision: 299153
- Update tp amarok beta3
- Fix amarok_service_gstreamer_codec.desktop
- Update to amarok 1.92.

* Sun Oct 12 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.90-0.870288.1mdv2009.1
+ Revision: 292842
- New svn snaphsot
  Remove merged patches
  Rediff amarok-1.90-gstreamer-codec-install.patch patch
  Update translations

* Fri Oct 03 2008 Helio Chissini de Castro <helio@mandriva.com> 3:1.90-0.866096.6mdv2009.0
+ Revision: 291031
- Fix codeina

* Thu Oct 02 2008 Gustavo Pichorim Boiko <boiko@mandriva.com> 3:1.90-0.866096.5mdv2009.0
+ Revision: 290900
- Fix a crash when right-clicking an empty space of the collection panel (#44483)
- Fix a crash when running with --nofork and a path (upstream r867005)
- Don't fetch again covers explicitelly deleted by the user (upstream r866607)
- Fix a crash when playing a podcast without the artist tag (upstream r866155)

* Tue Sep 30 2008 Helio Chissini de Castro <helio@mandriva.com> 3:1.90-0.866096.4mdv2009.0
+ Revision: 290035
- Fix first playlist crash with non selected item
- Added missing requires for mysql-common, otherwise mysql embedded can't create the database

* Sun Sep 28 2008 Anssi Hannula <anssi@mandriva.org> 3:1.90-0.864324.2mdv2009.0
+ Revision: 289020
- fix obsoletes to account for backported amarok 1.4.9.1 on 2008.1

* Wed Sep 24 2008 Helio Chissini de Castro <helio@mandriva.com> 3:1.90-0.864324.1mdv2009.0
+ Revision: 287853
- Mysql embedded in the new database.

* Fri Sep 19 2008 Helio Chissini de Castro <helio@mandriva.com> 3:1.90-0.862469.6mdv2009.0
+ Revision: 285875
- Update to current post beta1 revision 862469

* Thu Sep 11 2008 Helio Chissini de Castro <helio@mandriva.com> 3:1.90-0.860031.4mdv2009.0
+ Revision: 283939
- Codeina support for Amarok. First attempt.
- We don't need xine devel anymore
- Rebuild to generate debug package ( missing ? )

* Sun Sep 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.90-0.857904.1mdv2009.0
+ Revision: 282046
- New snapshot

* Mon Sep 01 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.90-0.855557.1mdv2009.0
+ Revision: 278239
- New snasphot
- New SVN Snapshot

* Tue Aug 26 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.90-0.852485.1mdv2009.0
+ Revision: 276095
- New snapshot
- New snapshot

  + Funda Wang <fwang@mandriva.org>
    - raise BR of libmtp

* Sat Aug 23 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.90-0.851157.1mdv2009.0
+ Revision: 275280
- New snapshot

* Thu Aug 21 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.90-0.850252.1mdv2009.0
+ Revision: 274658
- Fix file list
- Fix file list
- New snapshot
  Pacakge amarok with locales
  Fix lib install path ( upstream )

* Wed Aug 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.87-0.849644.1mdv2009.0
+ Revision: 274106
- Fix File list
- New snapshot

* Tue Aug 19 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.87-0.849304.1mdv2009.0
+ Revision: 273731
- Update amarok snapshot
- Fix major of libamarokplasma
- New snapshot

* Sun Aug 17 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.87-0.848422.1mdv2009.0
+ Revision: 273066
- Use better tarball
- New snapshot

* Sun Aug 17 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.87-0.848114.2mdv2009.0
+ Revision: 272909
- Fix previous patch
- Add patch0 to try to fix crash when opening settings

* Sun Aug 17 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.87-0.848114.1mdv2009.0
+ Revision: 272844
- New snapshot

* Fri Aug 15 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.87-0.847430.1mdv2009.0
+ Revision: 272394
- Fix file list
- Fix file list
- Fix file list
- New snapshot
- New snapshot

* Sun Jul 27 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 3:1.87-0.838427.1mdv2009.0
+ Revision: 250685
- Updat to new snapshot
- Remove unneeded Requires

* Wed Jul 23 2008 Colin Guthrie <cguthrie@mandriva.org> 3:1.86-1mdv2009.0
+ Revision: 242070
- Add more BuildRequires to enable some new features.
- New version: Alpha2 (1.86)

* Wed Jul 09 2008 Helio Chissini de Castro <helio@mandriva.com> 3:1.83-2mdv2009.0
+ Revision: 233166
- Small cleanup.
- Removed postgres buildreq. No postgres anymore
- Scripts not depend and use ruby or python anymore
- Added loudmouth buildreq

* Wed Jul 09 2008 Helio Chissini de Castro <helio@mandriva.com> 3:1.83-1mdv2009.0
+ Revision: 233158
- First official alpha from amarok.
- Raised epoch to upgrade to a proper version

* Mon Jul 07 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:2.0.0-0.svn829031.2mdv2009.0
+ Revision: 232409
- New snapshot (fixes bedi bug)

* Fri Jun 27 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:2.0.0-0.svn825117.2mdv2009.0
+ Revision: 229591
- those macros are only needed for mdv < 200900

* Fri Jun 27 2008 Helio Chissini de Castro <helio@mandriva.com> 2:2.0.0-0.svn825117.1mdv2009.0
+ Revision: 229578
- new amarok library - pud
- Update for current svn snapshot rev825117
- Update with 820386 snapshot

* Tue Jun 10 2008 Helio Chissini de Castro <helio@mandriva.com> 2:2.0.0-0.svn819178.1mdv2009.0
+ Revision: 217747
- New svn snapshot

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 21 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:2.0.0-0.svn794807.7mdv2009.0
+ Revision: 209659
- Change conflicts
- Build with MySQL and PostgreSQL support

* Wed May 14 2008 Anssi Hannula <anssi@mandriva.org> 2:2.0.0-0.svn794807.6mdv2009.0
+ Revision: 207233
- obsolete dropped engine packages for smooth upgrade

* Wed May 14 2008 Anssi Hannula <anssi@mandriva.org> 2:2.0.0-0.svn794807.5mdv2009.0
+ Revision: 207101
- add missing buildrequires on kdebase4-workspace-devel (also fixes
  conflicts with kdebase4-workspace)

* Tue May 13 2008 Anssi Hannula <anssi@mandriva.org> 2:2.0.0-0.svn794807.4mdv2009.0
+ Revision: 206541
- Drop libamarok0-scripts subpackage. In addition to being empty, it used
  to contain non-versioned plugin libs that can be put in amarok-scripts
  directly.

* Mon May 12 2008 Anssi Hannula <anssi@mandriva.org> 2:2.0.0-0.svn794807.3mdv2009.0
+ Revision: 206472
- fix some conflicts and obsoletes

* Sat Apr 12 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:2.0.0-0.svn794807.2mdv2009.0
+ Revision: 192628
- Fix conflicts
- Change spec file name
  Obsolete old packages
- Use new kde4 amarok by default

  + Helio Chissini de Castro <helio@mandriva.com>
    - No more separated engines. Phonon is more than enough :-)

* Sun Mar 09 2008 Funda Wang <fwang@mandriva.org> 1:2.0.0-1.svn763708.4mdv2008.1
+ Revision: 182420
- rebuild for qt4 changes

  + Thierry Vignaud <tv@mandriva.org>
    - fix gstreamer0.10-devel BR for x86_64

* Sun Jan 20 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:2.0.0-1.svn763708.3mdv2008.1
+ Revision: 155406
- Fix File list
- New snapshot

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Dec 02 2007 Funda Wang <fwang@mandriva.org> 1:2.0.0-1.svn743954.3mdv2008.1
+ Revision: 114447
- fix upgrading by obsoletes old libname
- move strigi.so into main package
- adopt to new devel policy

* Sun Dec 02 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:2.0.0-1.svn743954.2mdv2008.1
+ Revision: 114411
- New snapshot

* Sat Dec 01 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1:2.0.0-1.svn738067.2mdv2008.1
+ Revision: 114310
- rebuild due to unresolved symbols

* Sat Nov 17 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:2.0.0-1.svn738067.1mdv2008.1
+ Revision: 109673
- New snapshot

* Sat Oct 27 2007 Funda Wang <fwang@mandriva.org> 1:2.0.0-1.svn730005.1mdv2008.1
+ Revision: 102640
- New snapshot at svn730005

* Sat Oct 20 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:2.0.0-1.svn727155.5mdv2008.1
+ Revision: 100524
- Fix BuildRequires
- New svn snapshot

* Thu Sep 27 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1:2.0.0-1.svn711995.5mdv2008.0
+ Revision: 93401
- Rebuild against latest kde4 packages

* Thu Sep 13 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:2.0.0-1.svn711995.4mdv2008.0
+ Revision: 85160
- Kill Require on libamarok

* Thu Sep 13 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:2.0.0-1.svn711995.3mdv2008.0
+ Revision: 84933
- New snashot because of new kdelibs
- Add conflicts to make update easier
- Upload again as Library rpm have not been uploaded properly

* Wed Sep 12 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:2.0.0-1.svn710748.1mdv2008.0
+ Revision: 84781
- New snapshot
- New snapshot
- New svn snapshot
- Change spec according to new Kde layout

* Sat Jun 16 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:2.0.0-1.svn676332.1mdv2008.0
+ Revision: 40409
- Fix File list
- New svn snapshot
- Fix File List
- New svn snapshot (20070508)

* Mon Apr 30 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:2.0.0-0.svn20070430.1mdv2008.0
+ Revision: 19404
- Remove Patch100: Ruby check is now fixed upstream
- Fix file list
- Fix BuildRequires
- New svn snapshot

* Sun Apr 22 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:2.0.0-0.svn20070418.2mdv2008.0
+ Revision: 17032
- Fix Buildrequires
- Remove redundant buildRequire

* Sun Apr 22 2007 Laurent Montel <lmontel@mandriva.org> 1:2.0.0-0.svn20070418.1mdv2008.0
+ Revision: 16848
- Move file into good package
- Cleanup
  Fix for x86_64

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New svn snapshot

* Tue Apr 17 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:2.0.0-0.svn20070407.3mdv2008.0
+ Revision: 13528
- Add njb support
- Fix Build on x86_64
- Add BR
- Clean Spec
- Import amarok2

