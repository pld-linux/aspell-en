Summary:	English dictionary for aspell
Summary(pl.UTF-8):	Angielski słownik dla aspella
Name:		aspell-en
Version:	2016.01.19
%define	subv	0
Release:	1
Epoch:		2
License:	Custom
Group:		Applications/Text
Source0:	http://ftp.gnu.org/gnu/aspell/dict/en/aspell6-en-%{version}-%{subv}.tar.bz2
# Source0-md5:	18cf685153bea76566f63dc0ab45c391
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.60
BuildRequires:	which
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
English dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Angielski słownik (lista słów) dla aspella.

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
%{_libdir}/aspell/american*.alias
%{_libdir}/aspell/british*.alias
%{_libdir}/aspell/canadian*.alias
%{_libdir}/aspell/english*.alias
%{_libdir}/aspell/en*.multi
%{_libdir}/aspell/en*.rws
%{_datadir}/aspell/en*.dat
