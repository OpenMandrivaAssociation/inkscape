%define Werror_cflags %nil

%define	name	inkscape
%define version 0.47
%define pre	%nil
#define rel	0.%pre.1
%define rel	1
%define release %mkrel %{rel}

Name:		inkscape
Summary:	A vector-based drawing program using SVG
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Graphics
URL:		http://inkscape.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}%{pre}.tar.bz2
Source1:	%{name}-icons.tar.bz2
# Fedora patches
Patch2: 	inkscape-0.46-cxxinclude.patch
# use uniconvertor to import coreldraw cdr files (not applied yet)
Patch6:		inkscape-0.46-uniconv.patch
# Fix build with poppler 0.12.2
Patch7:		inkscape-poppler-0.12.2.patch
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
BuildRequires:	imagemagick-devel
BuildRequires:	gsl-devel
Requires: python-pyxml, python-lxml
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
#Suggests:	uniconvertor

%description
Inkscape is a SVG based generic vector-drawing program.

Inkscape uses W3C SVG as its native file format. It is therefore a very useful
tool for web designers and as an interchange format for desktop publishing.

%prep
%setup -q -a1 -n %name-%version%pre
%patch2 -p1 -b .cxxinclude
# disabled for now, it does not seem to work
# once this is working again, also the suggests on uniconvertor
# should be uncommented
#%patch6 -p1 -b .uniconv
%patch7 -p1 -b .poppler0.12.2

%build
intltoolize --force
aclocal
automake
autoconf
CPPFLAGS="`Magick++-config --cppflags`"
export CPPFLAGS
%configure2_5x \
	--with-python \
	--with-perl \
    	--enable-inkboard \
    	--disable-mmx
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# Menu support
sed -i -e s/inkscape.png/inkscape/ %{buildroot}%{_datadir}/applications/*

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

# icons
install -D -m 644 %{name}-48.png %{buildroot}/%_liconsdir/%{name}.png
install -D -m 644 %{name}-32.png %{buildroot}/%_iconsdir/%{name}.png
install -D -m 644 %{name}-16.png %{buildroot}/%_miconsdir/%{name}.png

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
%{_datadir}/pixmaps/*
%{_datadir}/inkscape/
#%{_libdir}/inkscape
%{_mandir}/man1/*
%{_mandir}/*/man1/*
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
