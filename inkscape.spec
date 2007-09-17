%define	name	inkscape
%define version 0.45.1
%define	rel	4
%define release %mkrel %{rel}

Name:		inkscape
Summary:	A vector-based drawing program using SVG
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Graphics
URL:		http://inkscape.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}-icons.tar.bz2
Patch0:		inkscape-0.45-python_gcc412.patch
Patch1:		inkscape-0.45.1-autotools.patch
Patch2:		inkscape-0.45.1-sigc.patch
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
BuildRequires:	liblcms-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	autoconf2.5 automake
BuildRequires:	intltool
Requires: python-pyxml
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils

%description
Inkscape is a SVG based generic vector-drawing program.

Inkscape uses W3C SVG as its native file format. It is therefore a very useful
tool for web designers and as an interchange format for desktop publishing.

%prep
%setup -q -a1
%patch0 -p1
%patch1 -p1 -b .autotools
%patch2 -p0 -b .sigc

sed -i 's/gc_libs=""/gc_libs="-lpthread -ldl"/' configure

%build
intltoolize --force
aclocal
automake
autoconf
%configure2_5x \
	--disable-static \
	--with-python \
    	--enable-inkboard \
    	--disable-mmx \
	--with-gnome-print
#(peroyvind) for some weird reason -lpopt will be converted to /usr/lib/libpopt.so
# during build, hardcode real path in stead
perl -pi -e "s#-lpopt#%{_libdir}/libpopt.so#g" src/Makefile
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# Menu support
install -d %{buildroot}%{_menudir}/ 
cat > %{buildroot}%{_menudir}/%{name} << EOF
?package(%{name}): needs=x11 \
icon="%{name}.png" \
section="Multimedia/Graphics" \
title=Inkscape longtitle="Vector graphics editor" \
command="%{name}" \
xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-Mandriva-Multimedia-Graphics" \
  --add-category="X-MandrivaLinux-CrossDesktop" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

# icons
install -D -m 644 %{name}-48.png %{buildroot}/%_liconsdir/%{name}.png
install -D -m 644 %{name}-32.png %{buildroot}/%_iconsdir/%{name}.png
install -D -m 644 %{name}-16.png %{buildroot}/%_miconsdir/%{name}.png

# remove .la files
rm -f %{buildroot}/%{_libdir}/inkscape/plugins/*.la

%find_lang %{name}

%post
%update_menus
%update_desktop_database

%postun
%clean_menus
%clean_desktop_database

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

%{_menudir}/%{name}
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png


