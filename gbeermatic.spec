Summary:	Stupid games to help you get drunk in style
Summary(pl.UTF-8):   Głupie gierki pomagające upić się w stylu
Name:		gbeermatic
Version:	0.1
Release:	3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://earthworm.no-ip.com/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	20b14c49e83c9f845a1ce9c618958668
Patch0:		%{name}-desktop.patch
URL:		http://earthworm.no-ip.com/gbeermatic/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.10.40
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gBeermatic is a GTK+2 based drinking game program. It features film
questions, games, and other stupid stuff.

%description -l pl.UTF-8
gBeermatic jest grą bazującą na GTK+2, zawierającą pytania o filmach,
gierki i inne głupie rzeczy.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless in binary package
rm -rf $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/%{name}
