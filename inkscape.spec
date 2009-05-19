%define Werror_cflags %nil

%define	name	inkscape
%define version 0.46
%define rel	12
%define release %mkrel %{rel}

Name:		inkscape
Summary:	A vector-based drawing program using SVG
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Graphics
URL:		http://inkscape.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:	%{name}-icons.tar.bz2
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=487623
Patch0:		inkscape-0.46-zh_CN-locale-crash.patch
# http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=488170
Patch1:		inkscape-0.46-poppler-0.8.3.patch
# Fedora patches
Patch2: 	inkscape-0.46-cxxinclude.patch
Patch3: 	inkscape-0.46-gtk2.13.3.patch
Patch4:		inkscape-0.46-gtkopen.patch
Patch5:		inkscape-0.46-desktop.patch
# use uniconvertor to import coreldraw cdr files (not applied yet)
Patch6:		inkscape-0.46-uniconv.patch
# Ubuntu patch, fixes libMagick++ detection
Patch7:		inkscape-0.46-imagemagick.patch
# Frugalware patch, fixes building perl support with perl 5.10
Patch8:		inkscape-0.46-perl-5.10.patch
Patch9:		inkscape-0.46-fix-makefile.patch
# Ubuntu patch, fix gtk adjustment bugs
Patch10:	102_gtk_zero_pagesize.dpatch
# Gentoo patch
Patch11:	inkscape-0.46-gcc4.4.patch
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
Requires: python-pyxml, python-lxml
Requires(post):	desktop-file-utils
Requires(postun): desktop-file-utils
#Suggests:	uniconvertor

%description
Inkscape is a SVG based generic vector-drawing program.

Inkscape uses W3C SVG as its native file format. It is therefore a very useful
tool for web designers and as an interchange format for desktop publishing.

%prep
%setup -q -a1
%patch0 -p1 -b .zh_CN-locale-crash
%patch1 -p1 -b .poppler
%patch2 -p1 -b .cxxinclude
%patch3 -p1 -b .gtk2.13.3
%patch4 -p0 -b .gtkopen
%patch5 -p1 -b .desktop
# disabled for now, it does not seem to work
# once this is working again, also the suggests on uniconvertor
# should be uncommented
#%patch6 -p1 -b .uniconv
%patch7 -p2 -b .imagemagick
%patch8 -p1 -b .perl5.10
%patch9 -p1
%patch10 -p1
%patch11 -p1 -b .gcc4.4

sed -i 's/gc_libs=""/gc_libs="-lpthread -ldl"/' configure
cd src/extension/script/CXX
ln -s ../CXX/ CXX

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
