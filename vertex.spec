Summary:	Vertex - polygon based modeller
Summary(pl.UTF-8):	Vertex - modeler oparty o wielokąty
Name:		vertex
Version:	0.1.16
Release:	1
License:	GPL v2
Group:		X11/Graphics
Source0:	http://wolfsinger.com/~wolfpack/packages/%{name}-%{version}.tar.bz2
# Source0-md5:	6adc3b3f06d5d63b48002a62173f6fe5
URL:		http://freecode.com/projects/vertex
BuildRequires:	gtkglarea1-devel
BuildRequires:	imlib-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Vertex is a polygon based modeller geared towards making highly
efficient 3D objects for games and other live-end requirements. It
uses the V3D object model format to maximize efficiency with OpenGL
rendering.

%description -l pl.UTF-8
Vertex to modeler oparty o wielokąty, którego celem jest tworzenie
wydajnych obiektów 3D do gier i innych zastosowań. Używa formatu
modeli obiektów V3D, aby uzyskać największą wydajność renderowania z
użyciem OpenGL.

%prep
%setup -q

%build
./configure Linux
%{__make} \
	CC="%{__cc}"\
	CPP="%{__cxx}" \
	CFLAGS="%{rpmcflags} -Wall -fomit-frame-pointer -ffast-math -DHAVE_IMLIB `gtk-config --cflags`" \
	LIB_DIRS=


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	DATA_DIR=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	ICONS_DIR=$RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/vertex
%{_datadir}/%{name}
%{_pixmapsdir}/vertex.xpm
%{_mandir}/man1/vertex.1*
