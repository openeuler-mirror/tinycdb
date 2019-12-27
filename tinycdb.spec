%global _description \
TinyCDB is a very fast and simple package for creating and reading constant data bases, \
a data structure introduced by Dan J. Bernstein in his cdb package. It may be used \
to speed up searches in a sequence of (key,value) pairs with very big number of records.

Name:           tinycdb
Version:        0.78
Release:        11
Summary:        A very fast and simple package for creating and reading constant databases
License:        Public Domain
URL:            http://www.corpit.ru/mjt/tinycdb.html
Source0:        http://www.corpit.ru/mjt/tinycdb/tinycdb-%{version}.tar.gz
Source1:        libcdb.pc

BuildRequires:  gcc
%description %_description

%package devel
Summary:        Development files for tinycdb
Requires:       tinycdb = %{version}-%{release}

%description devel  %_description

%package help
Summary:        Help documents for tinycdb
%description help
The tinycdb-help package contains manual pages for tinycdb

%prep
%autosetup -n %{name}-%{version} -p1
cp %{SOURCE1} debian/
sed -i -e 's\/lib\/%{_lib}\g' debian/libcdb.pc

%build
%make_build staticlib sharedlib cdb-shared CFLAGS="%{optflags}"

%install
install -d %{buildroot}%{_libdir}
%make_install prefix=%{_prefix} libdir=%{_libdir} mandir=%{_mandir} \
  install-sharedlib INSTALLPROG=cdb-shared CP="cp -p"
chmod +x %{buildroot}%{_libdir}/*.so.*
install -d %{buildroot}%{_libdir}/pkgconfig
cp -p debian/libcdb.pc %{buildroot}%{_libdir}/pkgconfig/libcdb.pc

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%files
%doc NEWS ChangeLog
%{_bindir}/cdb
%{_libdir}/*.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/lib*.a

%files help
%{_mandir}/man1/*.1*
%{_mandir}/man5/*.5*
%{_mandir}/man3/*.3*

%changelog
* Fri Nov 15 2019 sunguoshuai <sunguoshuai@huawei.com> - 0.78-11
- Package init
