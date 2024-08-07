%define debug_package %{nil}
%define repo gitlab.gnome.org/GNOME/evolution-etesync/
%define version 1.1.1

Name:          evolution-etesync
Version:       %{version}
Release:       1%{?dist}
Summary:       EteSync (end-to-end encrypted sync) plugin for Evolution

License:       LGPL
URL:           https://%{repo}
Source0:       https://%{repo}/-/archive/%{version}/%{name}-%{version}.tar.gz

Requires: libgee json-glib evolution-data-server evolution libetebase
BuildRequires: cmake meson vala intltool evolution-data-server-devel evolution-devel libetebase

AutoReq:       no 
AutoReqProv:   no

%description
EteSync 2.0 (end-to-end encrypted sync) plugin for Evolution

%package langpacks
Summary: Translations for %{name}
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description langpacks
This package contains translations for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wno-deprecated-declarations"
%cmake
%cmake_build

%install
%cmake_install

%find_lang %{name}

%ldconfig_scriptlets


%files
%{_libdir}/evolution-etesync/libevolution-etesync.so
%{_libdir}/evolution-data-server/addressbook-backends/libebookbackendetesync.so
%{_libdir}/evolution-data-server/calendar-backends/libecalbackendetesync.so
%{_libdir}/evolution-data-server/credential-modules/module-etesync-credentials.so
%{_libdir}/evolution-data-server/registry-modules/module-etesync-backend.so
%{_libdir}/evolution/modules/module-etesync-configuration.so
%{_datadir}/metainfo/org.gnome.Evolution-etesync.metainfo.xml

%files langpacks -f %{name}.lang

%changelog
* Tue Aug 06 2024 Andrea Cowley <azbuilds@exophoton.com>
- Forked from daftaupe's repo as it appears to no longer be updated/maintained

* Fri Jul 09 2021 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 1.1.0-1
- Update to version 1.1.0

* Sun May 02 2021 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.99.1-2
- Bump release number

* Wed Nov 25 2020 Tom Hacohen <tom@etesync.com> 0.99.1-1
- Update to the now merged master branch

* Tue Nov 10 2020 Tom Hacohen <tom@etesync.com> 0.99-2
- Fix building on 32bit distros

* Fri Nov 06 2020 Tom Hacohen <tom@etesync.com> 0.99-1
- Update to EteSync 2.0

* Thu Aug 20 2020 Pierre-Alain TORET <pierre-alain.toret@protonmail.com> 0.1-1
- First release