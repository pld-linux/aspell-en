Summary:	English dictionary for aspell
Summary(pl):	Angielski s�ownik dla aspella
Name:		aspell-en
Version:	0.51
%define	subv	0
Release:	2
Epoch:		2
License:	Custom
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/en/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	8f1eab27d02e44b15c833d5a7b24f9cd
URL:		http://wordlist.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
English dictionary (i.e. word list) for aspell.

%description -l pl
Angielski s�ownik (lista s��w) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Copyright doc/{ChangeLog,SCOWL-README}
%{_libdir}/aspell/*
%{_datadir}/aspell/*
