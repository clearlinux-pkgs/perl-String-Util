#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-String-Util
Version  : 1.32
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/B/BA/BAKERSCOT/String-Util-1.32.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BA/BAKERSCOT/String-Util-1.32.tar.gz
Summary  : 'String processing utility functions'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-String-Util-license = %{version}-%{release}
Requires: perl-String-Util-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
NAME
String::Util -- String processing utility functions
DESCRIPTION
String::Util provides a collection of small, handy functions for
processing strings in various ways.

%package dev
Summary: dev components for the perl-String-Util package.
Group: Development
Provides: perl-String-Util-devel = %{version}-%{release}
Requires: perl-String-Util = %{version}-%{release}

%description dev
dev components for the perl-String-Util package.


%package license
Summary: license components for the perl-String-Util package.
Group: Default

%description license
license components for the perl-String-Util package.


%package perl
Summary: perl components for the perl-String-Util package.
Group: Default
Requires: perl-String-Util = %{version}-%{release}

%description perl
perl components for the perl-String-Util package.


%prep
%setup -q -n String-Util-1.32
cd %{_builddir}/String-Util-1.32

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-String-Util
cp %{_builddir}/String-Util-1.32/LICENSE %{buildroot}/usr/share/package-licenses/perl-String-Util/5a495047fa17d9b0c6f4e19c3061305ee5a8acdd
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/String::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-String-Util/5a495047fa17d9b0c6f4e19c3061305ee5a8acdd

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/String/Util.pm
