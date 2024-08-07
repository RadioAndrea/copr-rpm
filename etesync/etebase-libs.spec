%define debug_package %{nil}
%define repo github.com/etesync/libetebase
%define upstreamname libetebase
%define version 0.5.6

Name:          etebase-libs
Version:       %{version}
Release:       1%{?dist}
Summary:       C and Rust client libraries for EteSync

License:       LGPLv2.1
URL:           https://%{repo}
Source0:       https://%{repo}/archive/v%{version}.tar.gz

BuildRequires: cargo openssl-devel

AutoReq:       no 
AutoReqProv:   no

%description
C and Rust client libraries for EteSync

%prep%define version 0.5.6
%setup -q -n libetebase-%{version}

%build
make build-release

%install
mkdir -p %{buildroot}%{_libdir}/pkconfig
mkdir -p %{buildroot}%{_includedir}
install -Dm644 target/etebase.pc -t %{buildroot}%{_libdir}/pkgconfig/
install -Dm644 EtebaseConfig.cmake -t %{buildroot}%{_libdir}/cmake/Etebase/
install -Dm644 target/etebase.h -t %{buildroot}%{_includedir}
install -Dm755 target/release/%{upstreamname}.so -t %{buildroot}%{_libdir}

%files
%{_libdir}/%{upstreamname}.so
%{_libdir}/pkgconfig/etebase.pc
%{_libdir}/cmake/Etebase/EtebaseConfig.cmake
%{_includedir}/etebase.h
%if ! 0%{?suse_version}
%{_libdir}/%{upstreamname}.so.0
%endif

%changelog
* Tue Aug 06 2024 Andrea Cowley <azbuilds@exophoton.com>
- Forked the repo as it appears to no longer be updated/maintained
* Thu Apr 01 2022 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.5.3-1
- Update to version 0.5.3
* Tue Mar 29 2022 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.5.2-1
- Update to version 0.5.2
* Fri Nov 06 2020 Tom Hacohen <tom@etesync.com> 0.3.1-2
- Include CMake config
* Fri Nov 06 2020 Tom Hacohen <tom@etesync.com> 0.3.1-1
- Change to libetebase
* Fri Jul 31 2020 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.1-1
- First release
