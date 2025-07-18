#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-String-Util
Version  : 1.35
Release  : 25
URL      : https://cpan.metacpan.org/authors/id/B/BA/BAKERSCOT/String-Util-1.35.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BA/BAKERSCOT/String-Util-1.35.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0 MIT
Requires: perl-String-Util-license = %{version}-%{release}
Requires: perl-String-Util-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
**String::Util** -- String processing utility functions
# DESCRIPTION
**String::Util** provides a collection of small, handy functions for processing
strings in various ways.

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
%setup -q -n String-Util-1.35
cd %{_builddir}/String-Util-1.35
pushd ..
cp -a String-Util-1.35 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-String-Util
cp %{_builddir}/String-Util-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-String-Util/d4b32db5bc71cc83a97f1577c1204fbdabf7cc73 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/String::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-String-Util/d4b32db5bc71cc83a97f1577c1204fbdabf7cc73

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
