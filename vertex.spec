Summary:	Vertex - polygon based modeller
Summary(pl):	Vertex - modeler oparty o wielok�ty
Name:		vertex
Version:	0.1.14
Release:	2
License:	GPL
Group:		X11/Graphics
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
# Source0-md5:	6ea0f01bfa480f49ba08637a124fbd1f
URL:		http://wolfpack.twu.net/Vertex/
BuildRequires:	gtkglarea1-devel
BuildRequires:	imlib-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
Vertex is a polygon based modeller geared towards making highly
efficient 3D objects for games and other live-end requirements. It
uses the V3D object model format to maximize efficiency with OpenGL
rendering.

%description -l pl
Vertex to modeler oparty o wielok�ty, kt�rego celem jest tworzenie
wydajnych obiekt�w 3D do gier i innych zastosowa�. U�ywa formatu
modeli obiekt�w V3D, aby uzyska� najwi�ksz� wydajno�� renderowania z
u�yciem OpenGL.

%prep
%setup -q

%build
./configure Linux
%{__make} CC=%{__cc} CXX=%{__cxx}

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
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/help
%{_datadir}/%{name}/images
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/preset_models
%{_datadir}/%{name}/preset_primitives
%{_pixmapsdir}/*
%{_mandir}/man1/*
