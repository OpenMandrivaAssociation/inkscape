%define Werror_cflags %nil

Name:		inkscape
Summary:	A vector-based drawing program using SVG
Version:	0.48.3.1
Release:	4
License:	GPLv2+
Group:		Graphics
URL:		http://inkscape.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
Patch0:		inkscape-0.48.1-libpng15.patch
Patch3:		inkscape-0.48.2-poppler020.patch
#Fix crash in Open/Save dialogue
Patch5:		inkscape-0.48.3-gtkfiledialog.patch

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	boost-devel
BuildRequires:	expat-devel
BuildRequires:	pkgconfig(bdw-gc) >= 6.4
BuildRequires:	python-devel
BuildRequires:  perl-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(lcms)
BuildRequires:	pkgconfig(libgnomeprintui-2.2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:	pkgconfig(libwpg-0.2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:  pkgconfig(loudmouth-1.0)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(popt)
BuildRequires:	gdk-pixbuf2.0

Requires: python-pyxml
Requires: python-lxml
Requires: pstoedit
Requires: gnome-vfs2
Requires: gdk-pixbuf2.0
Requires(post,postun):	desktop-file-utils
Suggests:	uniconvertor

%description
Inkscape is a generic SVG-based vector-drawing program.

Inkscape uses the W3C SVG (= "Scalable Vector Graphics") standard as its
native file format. Therefore, it is a very useful tool for web designers
and can be used as an interchange format for desktop publishing.

%prep
%setup -q -a1
%apply_patches

# required for patch3
autoreconf

%build
export CXXFLAGS="%optflags -fpermissive"
autoreconf -fi
%configure2_5x \
	--with-python \
	--with-perl
%make

%install
%makeinstall_std

desktop-file-install --vendor="" \
	--add-category="X-MandrivaLinux-CrossDesktop" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/inkscape/
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/*
%{_mandir}/*/man1/*



%changelog
* Mon May 14 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.48.3.1-1
+ Revision: 798843
- new version 0.48.3.1
- cleaned up spec

  + Alexander Khrukin <akhrukin@mandriva.org>
    - new mandriva packaging policy

* Mon Oct 24 2011 Alexander Barakin <abarakin@mandriva.org> 0.48.2-4
+ Revision: 705894
- pstoedit requirment add. see #57740

* Thu Oct 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.48.2-3
+ Revision: 703259
- fix build against libpng-1.5.x (mageia)
- attempt to relink against libpng15.so.15

* Sat Jul 09 2011 Funda Wang <fwang@mandriva.org> 0.48.2-1
+ Revision: 689403
- New version 0.48.2
- drop merged patches

* Mon May 02 2011 Funda Wang <fwang@mandriva.org> 0.48.1-3
+ Revision: 662297
- add fedora patches to build with latest wpd

* Fri Mar 11 2011 Funda Wang <fwang@mandriva.org> 0.48.1-2
+ Revision: 643737
- rebuild for new poppler

* Sun Feb 06 2011 Funda Wang <fwang@mandriva.org> 0.48.1-1
+ Revision: 636421
- New version 0.48.1

* Thu Dec 30 2010 Funda Wang <fwang@mandriva.org> 0.48.0-3mdv2011.0
+ Revision: 626335
- add upstream fix for poppler 0.16.0
- rebuild for new poppler

* Sun Aug 22 2010 Funda Wang <fwang@mandriva.org> 0.48.0-2mdv2011.0
+ Revision: 571802
- rebuild for new poppler

* Sat Aug 14 2010 Funda Wang <fwang@mandriva.org> 0.48.0-1mdv2011.0
+ Revision: 569765
- New version 0.48.0
  * no other distroare using unviconvertor
  * cxxinclude patch not needed
  * poppler patch merged already

* Thu Aug 05 2010 Funda Wang <fwang@mandriva.org> 0.47-5mdv2011.0
+ Revision: 566256
- rebuild for new poppler

* Sat Jul 17 2010 Funda Wang <fwang@mandriva.org> 0.47-4mdv2011.0
+ Revision: 554585
- rebuild
- build with popt
- rebuild for new imagemagick

  + Shlomi Fish <shlomif@mandriva.org>
    - Revise the description to make it better English

* Thu Jan 14 2010 Funda Wang <fwang@mandriva.org> 0.47-2mdv2010.1
+ Revision: 491146
- rebuild for new imagemagick

* Thu Nov 26 2009 Pascal Terjan <pterjan@mandriva.org> 0.47-1mdv2010.1
+ Revision: 470389
- Add a patch fixing build against poppler 0.12.2
- Update to 0.47 final

* Sun Nov 08 2009 Lev Givon <lev@mandriva.org> 0.47-0.pre4.1mdv2010.1
+ Revision: 463125
- Update to 0.47pre4.

* Tue Oct 06 2009 Lev Givon <lev@mandriva.org> 0.47-0.pre3.1mdv2010.0
+ Revision: 454410
- Update to 0.47pre3.

* Thu Sep 03 2009 Pascal Terjan <pterjan@mandriva.org> 0.47-0.pre2.1mdv2010.0
+ Revision: 428248
- Update to 0.47 pre2

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Rebuild against new perl

* Tue May 19 2009 Götz Waschk <waschk@mandriva.org> 0.46-12mdv2010.0
+ Revision: 377635
- fix build with gcc 4.4
- remove old configure options
- fix adjustments with current gtk

* Tue May 19 2009 Götz Waschk <waschk@mandriva.org> 0.46-11mdv2010.0
+ Revision: 377606
- fix makefile
- rebuild for new poppler

* Wed Jan 28 2009 Götz Waschk <waschk@mandriva.org> 0.46-10mdv2009.1
+ Revision: 335033
- rebuild for new libmagick

* Wed Jan 14 2009 Jérôme Soyer <saispo@mandriva.org> 0.46-9mdv2009.1
+ Revision: 329551
- Rebuild with python2.6

* Sun Sep 28 2008 Frederik Himpe <fhimpe@mandriva.org> 0.46-8mdv2009.0
+ Revision: 289079
- Fix perl support build with perl 5.10
- Fix build with libmagick++
- Add mime type for compressed svg files to desktop files and don't
  add extension to icon name

* Fri Sep 26 2008 Oden Eriksson <oeriksson@mandriva.com> 0.46-7mdv2009.0
+ Revision: 288617
- rebuild against the correct version of the libgc library

* Thu Sep 11 2008 Frederik Himpe <fhimpe@mandriva.org> 0.46-6mdv2009.0
+ Revision: 283941
- Add patches from Debian and Fedora
  * fixing build with poppler 0.8.3 and gtk+ 2.13 and include fixes
  * fixing crash with zh_CN locale when using gtk+ file chooser
  * fixing gtk+ file dialog not showing last used directory

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu May 01 2008 Funda Wang <fwang@mandriva.org> 0.46-5mdv2009.0
+ Revision: 199793
- rebuild

* Wed Apr 23 2008 Giuseppe Ghibò <ghibo@mandriva.com> 0.46-4mdv2009.0
+ Revision: 196789
- Add support for ImageMagick in BuildRequires. Sound inkscape configure detect
  is broken with Magick++.h, so need to pass through CPPFLAGS.

* Tue Apr 22 2008 Lev Givon <lev@mandriva.org> 0.46-3mdv2009.0
+ Revision: 196597
- lxml is needed to run Inkscape extensions.

* Sun Apr 20 2008 Pascal Terjan <pterjan@mandriva.org> 0.46-2mdv2009.0
+ Revision: 195955
- Add more missing buildrequires to get all features

* Sun Apr 20 2008 Pascal Terjan <pterjan@mandriva.org> 0.46-1mdv2009.0
+ Revision: 195913
- BuildRequires boost-devel
- Update to 0.46

* Thu Feb 07 2008 Funda Wang <fwang@mandriva.org> 0.45.1-5mdv2008.1
+ Revision: 163569
- add ubuntu patch to have it built against latest glib
- drop old menu

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 17 2007 Pascal Terjan <pterjan@mandriva.org> 0.45.1-4mdv2008.0
+ Revision: 89124
- Update BuildRequires as liblcms was renamed to lcms
- Drop icon extension in .desktop
- Have inkscape in the main part of the menu under KDE
- Fix build with new intltool
- Fix build with new sigc++

* Tue Jul 03 2007 Michael Scherer <misc@mandriva.org> 0.45.1-3mdv2008.0
+ Revision: 47534
- rebuild for new glib

* Fri Jun 22 2007 Marcelo Ricardo Leitner <mrl@mandriva.com> 0.45.1-2mdv2008.0
+ Revision: 43219
- Added autotools patch: update to work with current autotools scheme.
- Rebuild against new glib

* Tue May 15 2007 Funda Wang <fwang@mandriva.org> 0.45.1-1mdv2008.0
+ Revision: 26827
- Patch1 merged upsream.
- New upstream version


* Sat Mar 24 2007 Pascal Terjan <pterjan@mandriva.org> 0.45-2mdv2007.1
+ Revision: 148707
- Add patch from MDKSA-2007:069

* Mon Feb 05 2007 Pascal Terjan <pterjan@mandriva.org> 0.45-1mdv2007.1
+ Revision: 116515
- 0.45
- fix build with new GCC

* Tue Oct 24 2006 Pascal Terjan <pterjan@mandriva.org> 0.44.1-1mdv2007.0
+ Revision: 71737
- Buildrequires intltool
- 0.44.1
- Fix building with new automake
- Import inkscape

* Thu Aug 24 2006 Götz Waschk <waschk@mandriva.org> 0.44-4mdv2007.0
- fix buildrequires
- rebuild for new cairomm

* Sat Aug 12 2006 Anssi Hannula <anssi@mandriva.org> 0.44-3mdv2007.0
- add BuildRequires: dbus-devel

* Sat Jul 15 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.44-2
- add BuildRequires: liblcms-devel

* Sat Jun 24 2006 Pascal Terjan <pterjan@mandriva.org>  0.44-1mdv2007.0
- 0.44
- Use XDG menu
- Drop P0 and P1 (fixed upstream)
- Remove --with-perl this is an experimental and broken currently useless
  build option

* Mon Jun 05 2006 Pascal Terjan <pterjan@mandriva.org>  0.43-5mdv2007.0
- BuildRequires expat-devel

* Sat Jun 03 2006 Pascal Terjan <pterjan@mandriva.org>  0.43-4mdv2007.0
- BuildRequires gnome-vfs-devel
- fix for gcc 4.1 (P0)
- apply upstream patch to not use freetype internals (P1)

* Thu Feb 09 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.43-3mdk
- require python-pyxml (#20099)

* Wed Jan 25 2006 Pascal Terjan <pterjan@mandriva.org>  0.43-2mdk
- Rebuild for new perl

* Mon Nov 21 2005 Michael Scherer <misc@mandriva.org> 0.43-1mdk
- New release 0.43
- activation of inkboard

* Tue Jul 26 2005 Pascal Terjan <pterjan@mandriva.org> 0.42-1mdk
- 0.42
- Drop P0, included upstream

* Thu Jul 07 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 0.41-5mdk
- work around weird problem when linking against popt (lib64)
- %%mkrel
- drop COPYING (package is GPL..)

* Fri May 20 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.41-4mdk
- Rebuild for new perl

* Tue Apr 05 2005 Pascal Terjan <pterjan@mandrake.org> 0.41-3mdk
- BuildRequires perl-devel for EXTERN.h

* Tue Mar 01 2005 Abel Cheung <deaddog@mandrake.org> 0.41-2mdk
- Fixes done by Tom Ph <tpgww@onepost.net>:
  o Patch (missing gnomeprint fn) from CVS
  o Add back gnomeprint support
  o Extra icons, menu icon
  o Requires, BuildRequires

* Sat Feb 26 2005 Abel Cheung <deaddog@mandrake.org> 0.41-1mdk
- New release
- Drop gnomeprint support (compile error)

* Thu Dec 02 2004 Abel Cheung <deaddog@mandrake.org> 0.40-2mdk
- Update BuildRequires

* Tue Nov 30 2004 Jerome Soyer <saispo@mandrake.org> 0.40-1mdk
- New release 0.40

* Tue Sep 21 2004 Jerome Soyer <saispo@mandrake.org> 0.39-4mdk
- Update BuildRequires

* Tue Sep 21 2004 Jerome Soyer <saispo@mandrake.org> 0.39-3mdk
- Added Autotrace and Frontline function

* Mon Aug 30 2004 Jerome Soyer <saispo@mandrake.org> 0.39-2mdk
- fix BuildRequires

* Thu Jul 22 2004 Michael Scherer <misc@mandrake.org> 0.39-1mdk
- New release 0.39
- remove patch 0, integrated upstream

* Sun Jun 20 2004 Abel Cheung <deaddog@deaddog.org> 0.38.1-4mdk
- Patch0: fix build against new gcc (CVS)

* Thu Jun 03 2004 Michael Scherer <misc@mandrake.org> 0.38.1-3mdk 
- [DIRM]

* Fri Apr 23 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.38.1-2mdk
- fix deps

* Tue Apr 13 2004 Michael Scherer <misc@mandrake.org> 0.38.1-1mdk
- New release 0.38.1
- [DIRM]

