Summary:	English dictionary for aspell
Summary(pl):	Angielski s�ownik dla aspella
Name:		aspell-en
Version:	6.0
%define	subv	0
Release:	1
Epoch:		2
License:	Custom
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-%{version}-%{subv}.tar.bz2
# Source0-md5:	16449e0a266e1ecc526b2f3cd39d4bc2
URL:		http://wordlist.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
English dictionary (i.e. word list) for aspell.

%description -l pl
Angielski s�ownik (lista s��w) dla aspella.

%prep
%setup -q -n aspell6-en-%{version}-%{subv}

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
%doc Copyright README doc/{ChangeLog,SCOWL-README,extra.txt}
%{_libdir}/aspell/*
%{_datadir}/aspell/*
