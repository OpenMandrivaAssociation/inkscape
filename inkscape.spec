%define Werror_cflags %nil

Summary:	A vector-based drawing program using SVG
Name:		inkscape
Version:	0.48.4
Release:	4
License:	GPLv2+
Group:		Graphics
Url:		http://inkscape.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
Patch1:		inkscape-automake-1.13.patch
Patch2:		inkscape-0.48.4-spuriouscomma.patch
 
##Fix crash in Open/Save dialogue
#Patch5:		inkscape-0.48.3-gtkfiledialog.patch

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
BuildRequires:	pkgconfig(gnome-vfs-2.0)
BuildRequires:	pkgconfig(gsl)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(gtkspell-2.0)
BuildRequires:	pkgconfig(ImageMagick)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(libgnomeprintui-2.2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libwpg-0.2)
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
Requires:	gnome-vfs2
Requires:	pstoedit
Requires:	python-pyxml
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
# required for patch3
autoreconf -fi


%build
export CXXFLAGS="%optflags -fpermissive"
%configure2_5x \
	--with-python \
	--with-perl \
	--with-gnome-vfs        \
        --with-xft              \
        --enable-lcms           \
        --enable-poppler-cairo
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

