Summary:	Vertex - polygon based modeller
Summary(pl):	Vertex
Name:		vertex
Version:	0.1.14
Release:	2
Copyright:	GPL
Group:		X11/Graphics
Source0:	ftp://wolfpack.twu.net/users/wolfpack/%{name}-%{version}.tar.bz2
#BuildRequires:	
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr

%description
Vertex is a polygon based modeller geared towards making highly efficient 3D objects for games and other live-end requirements. It uses the V3D object model format to maximize efficiency with OpenGL rendering.
%description -l pl

%prep
%setup -q

#%patch

%build
./configure Linux
%{__make} CC=gcc CXX=g++ INC_DIRS="-I%{_includedir}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	DATA_DIR=$RPM_BUILD_ROOT%{_datadir}/%{name} \
	ICONS_DIR=$RPM_BUILD_ROOT%{_datadir}/icons \
	install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(755,root,root) %{_bindir}/vertex
%dir %{_datadir}/%{name}/help/*
%dir %{_datadir}/%{name}/images/*
%dir %{_datadir}/%{name}/plugins/
%dir %{_datadir}/%{name}/preset_models/*
%dir %{_datadir}/%{name}/preset_primitives/*
%dir %{_datadir}/icons/*
%dir %{_mandir}/man1/*
