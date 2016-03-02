# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	idna
Summary:	Internationalized Domain Names in Applications (IDNA)
Name:		python-%{module}
Version:	2.0
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/i/idna/%{module}-%{version}.tar.gz
# Source0-md5:	bd17a9d15e755375f48a62c13b25b801
URL:		https://pypi.python.org/pypi/idna
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.713
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library to support the Internationalised Domain Names in
Applications (IDNA) protocol as specified in RFC 5891. This version of
the protocol is often referred to as “IDNA2008” and can produce
different results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement
for the “encodings.idna” module that comes with the Python standard
library but currently only supports the older 2003 specification.

%package -n python3-%{module}
Summary:	Internationalized Domain Names in Applications (IDNA)
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
A library to support the Internationalised Domain Names in
Applications (IDNA) protocol as specified in RFC 5891. This version of
the protocol is often referred to as “IDNA2008” and can produce
different results from the earlier standard from 2003.

The library is also intended to act as a suitable drop-in replacement
for the “encodings.idna” module that comes with the Python standard
library but currently only supports the older 2003 specification.

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
%doc HISTORY.rst README.rst
%{py_sitescriptdir}/%{module}
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc HISTORY.rst README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
