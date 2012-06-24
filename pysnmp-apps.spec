
Summary:	SNMP applications in Python
Summary(pl):	Aplikacje SNMP napisane w Pythonie
Name:		pysnmp-apps
Version:	0.0.2
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pysnmp/%{name}-%{version}.tar.gz
# Source0-md5:	93b84380e3977aaacafc7a1e1cecccbd
URL:		http://pysnmp.sourceforge.net/
Patch0:		%{name}-setup.patch
BuildRequires:	rpm-pythonprov
BuildRequires:	python >= 2.2.1
%pyrequires_eq	python-modules
Requires:	python-pysnmp >= 3.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pysnmp-apps is a bunch of SNMP tools written on top of the PySNMP
package. Some of these tools mimic their famous Net-SNMP counterparts,
while others are designed toward easy integration with other Python
applications.

pysnmp-apps is written entirely in Python and only relies upon the
PySNMP package to run.

%description -l pl
pysnmp-apps to zestaw narz�dzi SNMP wykorzystuj�cych bibliotek�
PySNMP. Niekt�re z nich na�laduj� dzia�anie odpowiednik�w ze s�ynnego
pakietu Net-SNMP, podczas gdy inne s� zaprojektowane w celu �atwej
integracji z innymi aplikacjami Pythona.

pysnmp-apps jest napisany w ca�o�ci w Pythonie i zale�y tylko od
pakietu PySNMP.

%prep
%setup -q
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
   --optimize=2 \
   --root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" | xargs rm
ln -s %{_bindir}/pysnmpwalk $RPM_BUILD_ROOT%{_bindir}/pysnmpbulkwalk
ln -s %{_bindir}/pysnmpget $RPM_BUILD_ROOT%{_bindir}/pysnmpset

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/pysnmpap
