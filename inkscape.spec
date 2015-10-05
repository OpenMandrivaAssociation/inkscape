%define Werror_cflags %nil

Summary:	A vector-based drawing program using SVG
Name:		inkscape
Version:	0.91
Release:	7
License:	GPLv2+
Group:		Graphics
Url:		http://inkscape.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
Source100:	inkscape.rpmlintrc

BuildRequires:	desktop-file-utils
BuildRequires:	gdk-pixbuf2.0
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	boost-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(bdw-gc) >= 6.4
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libwpg-0.3)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(loudmouth-1.0)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(popt)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(poppler-cairo)
BuildRequires:	pkgconfig(freetype2)

Requires(post,postun):	desktop-file-utils
Requires:	gdk-pixbuf2.0
Requires:	pstoedit
Requires:	python-lxml
Suggests:	uniconvertor

%description
Inkscape is a generic SVG-based vector-drawing program.

Inkscape uses the W3C SVG (= "Scalable Vector Graphics") standard as its
native file format. Therefore, it is a very useful tool for web designers
and can be used as an interchange format for desktop publishing.

%prep
%setup -q -a1
%apply_patches

%build
export CC=gcc
export CXX=g++
export CXXFLAGS="%optflags -fpermissive"
%configure \
    --enable-lcms           \
    --enable-poppler-cairo

%make

%install
%makeinstall_std

perl -i -lne 'print unless m{^\[Drawing Shortcut Group\]}..1' %{buildroot}%{_datadir}/applications/*

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
