%define Werror_cflags %nil

Name:		inkscape
Summary:	A vector-based drawing program using SVG
Version:	0.48.3.1
Release:	2
License:	GPLv2+
Group:		Graphics
URL:		http://inkscape.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
Patch0:		inkscape-0.48.1-libpng15.patch
Patch1:		inkscape-poppler20.patch
Patch2:		inkscape-0.48.2-types.patch

BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	boost-devel
BuildRequires:	expat-devel
BuildRequires:	gc-devel >= 6.4
BuildRequires:	python-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(lcms)
BuildRequires:	pkgconfig(libgnomeprintui-2.2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libwpg-0.2)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(loudmouth-1.0)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(popt)

Requires:	python-pyxml
Requires:	python-lxml
Requires:	pstoedit
Requires(post,postun):	desktop-file-utils

%description
Inkscape is a vector graphics editor, with capabilities similar to
Illustrator, CorelDraw, or Xara X, using the W3C standard Scalable Vector
Graphics (SVG) file format.  It is therefore a very useful tool for web
designers and as an interchange format for desktop publishing.

Inkscape supports many advanced SVG features (markers, clones, alpha
blending, etc.) and great care is taken in designing a streamlined
interface. It is very easy to edit nodes, perform complex path operations,
trace bitmaps and much more.

%prep
%setup -q -a1
%apply_patches
autoreconf -fi

%build
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
