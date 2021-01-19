%ifarch %{ix86}
%define _disable_lto 1
%endif
%define Werror_cflags %nil
%define beta %nil

Summary:	A vector-based drawing program using SVG
Name:		inkscape
Version:	1.0.2
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		http://inkscape.sourceforge.net/
Source0:	https://inkscape.org/gallery/item/21571/%{name}-%{version}.tar.xz
Source1:	%{name}-icons.tar.bz2
Source100:	inkscape.rpmlintrc
Patch0:		inkscape-1.0.1-compile.patch
BuildRequires:	desktop-file-utils
BuildRequires:	gdk-pixbuf2.0
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	boost-devel
BuildRequires:	boost-core-devel
BuildRequires:	boost-align-devel
BuildRequires:	perl-devel
BuildRequires:	pkgconfig(bdw-gc) >= 6.4
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	pkgconfig(harfbuzz)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(gmodule-2.0)
BuildRequires:	pkgconfig(libsoup-2.4) >= 2.42
BuildRequires:	pkgconfig(gtkmm-3.0) >= 3.22
BuildRequires:	pkgconfig(gdkmm-3.0) >= 3.22
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:	pkgconfig(gdk-3.0) >= 3.22
BuildRequires:	pkgconfig(gdl-3.0) >= 3.4
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
BuildRequires:	pkgconfig(poppler)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(atomic_ops)
BuildRequires:	cmake(double-conversion)
BuildRequires:	cmake ninja
BuildRequires:	potrace-devel

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
%autosetup -p1 -a1 -n %{name}-%{version}_2021-01-15_e86c870879
%cmake \
	-DBUILD_STATIC_LIBS:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DWITH_DBUS:BOOL=ON \
	-DWITH_IMAGE_MAGICK:BOOL=ON \
	-DWITH_OPENMP:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

perl -i -lne 'print unless m{^\[Drawing Shortcut Group\]}..1' %{buildroot}%{_datadir}/applications/*

desktop-file-install --vendor="" \
	--add-category="X-MandrivaLinux-CrossDesktop" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/inkscape/
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/*
%{_mandir}/*/man1/*
%{_datadir}/metainfo/org.inkscape.Inkscape.appdata.xml
%{_datadir}/bash-completion/completions/inkscape
