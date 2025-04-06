%ifarch %{ix86}
%define _disable_lto 1
%endif
%define Werror_cflags %nil
%define beta %nil

%define devname %mklibname -d -s 2geom

Summary:	A vector-based drawing program using SVG
Name:		inkscape
Version:	1.4.1
Release:	1
License:	GPLv2+
Group:		Graphics
Url:		https://inkscape.org/
Source0:	https://inkscape.org/gallery/item/55853/inkscape-%{version}.tar.xz
Source1:	%{name}-icons.tar.bz2
Source100:	inkscape.rpmlintrc

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
BuildRequires:	pkgconfig(gtksourceview-4)
BuildRequires:	pkgconfig(gspell-1)
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
BuildRequires:	pkgconfig(libunwind-llvm)
BuildRequires:	pkgconfig(GraphicsMagick)
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
Requires:	python3dist(numpy)
Requires:	python-tinycss2
Suggests:	uniconvertor

%patchlist
#inkscape-1.4-compile.patch
#inkscape-1.4-poppler-24.10.patch
#inkscape-1.4-poppler-24.11.patch
#inkscape-1.4-poppler-25.01.patch

%description
Inkscape is a generic SVG-based vector-drawing program.

Inkscape uses the W3C SVG (= "Scalable Vector Graphics") standard as its
native file format. Therefore, it is a very useful tool for web designers
and can be used as an interchange format for desktop publishing.

%package -n %{devname}
Summary:	Static library and header files for the 2geom library
Group:		Development/Libraries

%description -n %{devname}
Static library and header files for the 2geom library

%prep
%autosetup -p1 -a1 -n %{name}-%{version}_2025-03-30_93de688d07
CXXFLAGS="%{optflags} -std=gnu++20" %cmake \
	-DBUILD_STATIC_LIBS:BOOL=ON \
	-DBUILD_SHARED_LIBS:BOOL=OFF \
	-DWITH_DBUS:BOOL=ON \
	-DWITH_IMAGE_MAGICK:BOOL=ON \
	-DWITH_OPENMP:BOOL=ON \
	-G Ninja

%build
export CC=gcc
export CXX=g++
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

%files -n %{devname}
%{_libdir}/lib2geom.a
%{_libdir}/cmake/2Geom
%{_includedir}/2geom-*
%{_libdir}/pkgconfig/2geom.pc
