%define Werror_cflags %nil

%define	name	inkscape
%define version 0.48.2
%define rel	2
%define release %mkrel %{rel}

Name:		inkscape
Summary:	A vector-based drawing program using SVG
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Graphics
URL:		http://inkscape.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  png-devel
BuildRequires:  libxml2-devel >= 2.6.0
BuildRequires:	libgc-devel >= 6.4
BuildRequires:	gtkmm2.4-devel
BuildRequires:	libxslt-devel >= 1.0.15
BuildRequires:	libgnomeprintui-devel
BuildRequires:	perl-XML-Parser
BuildRequires:	gtkspell-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	python-devel
BuildRequires:	perl
BuildRequires:  perl-devel
BuildRequires:  loudmouth-devel
BuildRequires:	expat-devel
BuildRequires:	desktop-file-utils
BuildRequires:	lcms-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	autoconf2.5 automake
BuildRequires:	intltool
BuildRequires:	boost-devel
BuildRequires:	libpoppler-glib-devel
BuildRequires:	cairo-devel
BuildRequires:	libwpg-devel
BuildRequires:	popt-devel
BuildRequires:	imagemagick-devel
BuildRequires:	gsl-devel
Requires: python-pyxml, python-lxml
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils

%description
Inkscape is a generic SVG-based vector-drawing program.

Inkscape uses the W3C SVG (= "Scalable Vector Graphics") standard as its
native file format. Therefore, it is a very useful tool for web designers
and can be used as an interchange format for desktop publishing.

%prep
%setup -q -a1 -n %name-%version
%apply_patches

%build
autoreconf -fi
%configure2_5x \
	--with-python \
	--with-perl
%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --vendor="" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/inkscape/
%{_mandir}/man1/*
%{_mandir}/*/man1/*
%{_iconsdir}/hicolor/*/apps/*
