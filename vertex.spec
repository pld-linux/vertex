Summary:	Vertex - polygon based modeller
Summary(pl):	Vertex
Name:		vertex
Version:	0.1.14
Release:	1
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
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%post
%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
