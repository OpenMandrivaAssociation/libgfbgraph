%define api_version 0.2
%define lib_major   0
%define lib_name    %mklibname gfbgraph %{api_version} %{lib_major}
%define gi_name     %mklibname gfbgraph-gir %{api_version}
%define develname   %mklibname -d gfbgraph

%define url_ver     %(echo %{version}|cut -d. -f1,2)

Summary:	GLib/GObject wrapper for the Facebook Graph API
Name:		gfbgraph
Version:	0.2.5
Release:	3
Epoch:  1
Group:		System/Libraries
License:	LGPLv2
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(glib-2.0) >= 2.16.0
BuildRequires:	pkgconfig(gobject-2.0) >= 2.16.0
BuildRequires:	pkgconfig(libxml-2.0) >= 2.4.16
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.6.4
BuildRequires:	pkgconfig(rest-0.7)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(goa-1.0)
BuildRequires:	gtk-doc
BuildRequires:	intltool

%description
GLib/GObject wrapper for the Facebook Graph API that integrates with
GNOME Online Accounts.


%package -n %{lib_name}
Summary:  %{summary}
Group: %{group}

%description -n %{lib_name}
GLib/GObject wrapper for the Facebook Graph API that integrates with
GNOME Online Accounts.

%package -n %develname
Summary: Support files necessary to compile applications with %{name}
Group: Development/C
Requires: %{lib_name}
Provides: %{name}-%{api_version}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %develname
Libraries, headers, and support files necessary to compile
applications using %{name}.

%package -n %{gi_name}
Summary:	GObject Introspection interface library for %{name}
Group:		System/Libraries
Requires:	%{lib_name}

%description -n %{gi_name}
GObject Introspection interface library for %{name}.

%prep
%setup -q

%build
#./autogen.sh
%configure --enable-gtk-doc --disable-static --enable-introspection
%make_build

%install
%make_install

# remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_datadir}/../doc/lib%{name}
rm -f %{buildroot}%{_libdir}/*.la

%files -n %{lib_name}
%doc AUTHORS COPYING README NEWS
%{_libdir}/lib%{name}*-%{api_version}.so.%{lib_major}*

%files -n %develname
%doc %{_datadir}/gtk-doc/html/%{name}*
%{_datadir}/gir-1.0/GFBGraph-%{api_version}.gir
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*

%files -n %{gi_name}
%{_libdir}/girepository-1.0/GFBGraph-%{api_version}.typelib
