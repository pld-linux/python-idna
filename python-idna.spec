#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
# see python3-idna.spec
%bcond_with	python3 # CPython 3.x module

%define 	module	idna
Summary:	Internationalized Domain Names in Applications (IDNA) for Python 2
Summary(pl.UTF-8):	IDNA (Internationalized Domain Names in Applications) dla Pythona 2
Name:		python-%{module}
Version:	2.9
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://github.com/kjd/idna/releases
Source0:	https://github.com/kjd/idna/archive/v%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	117c8fbeabd36d7206121dec962ef011
URL:		https://github.com/kjd/idna
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library to support the Internationalised Domain Names in
Applications (IDNA) protocol as specified in RFC 5891. This version of
the protocol is often referred to as IDNA2008 and can produce
different results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement
for the encodings.idna module that comes with the Python standard
library but currently only supports the older 2003 specification.

%description -l pl.UTF-8
Biblioteka obsługująca protokół IDNA (International Domain Names in
Applications - międzynarodowe nazwy domen w aplikacjach) według
specyfikacji RFC 5891. Ta wersja protokołu jest często nazywana
IDNA2008 i może dawać inne wyniki, niż wcześniejszy standard z 2003
roku.

Ta biblioteka ma służyć także jako zamiennik modułu encodings.idna
dostarczanego z biblioteką standardową Pythona, ale obecnie
obsługująca tylko starszą specyfikację z 2003.

%package -n python3-%{module}
Summary:	Internationalized Domain Names in Applications (IDNA) for Python 3
Summary(pl.UTF-8):	IDNA (Internationalized Domain Names in Applications) dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
A library to support the Internationalised Domain Names in
Applications (IDNA) protocol as specified in RFC 5891. This version of
the protocol is often referred to as IDNA2008 and can produce
different results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement
for the encodings.idna module that comes with the Python standard
library but currently only supports the older 2003 specification.

%description -n python3-%{module} -l pl.UTF-8
Biblioteka obsługująca protokół IDNA (International Domain Names in
Applications - międzynarodowe nazwy domen w aplikacjach) według
specyfikacji RFC 5891. Ta wersja protokołu jest często nazywana
IDNA2008 i może dawać inne wyniki, niż wcześniejszy standard z 2003
roku.

Ta biblioteka ma służyć także jako zamiennik modułu encodings.idna
dostarczanego z biblioteką standardową Pythona, ale obecnie
obsługująca tylko starszą specyfikację z 2003.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc HISTORY.rst LICENSE.rst README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc HISTORY.rst LICENSE.rst README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
