%define debug_package %{nil}
%define repo github.com/elkowar/eww/
%define version 0.6.0

Name:          eww
Version:       %{version}
Release:       1%{?dist}
Summary:       ElKowars wacky widgets

License:       MIT
URL:           https://%{repo}
Source0:       https://%{repo}/archive/v%{version}.tar.gz

BuildRequires: cargo rustup gtk3-devel gtk-layer-shell-devel pango-devel gdk-pixbuf2-devel libdbusmenu-gtk3-devel cairo-devel glib2-devel libgcc glibc-devel
Requires:      gtk3 gtk-layer-shell pango gdk-pixbuf2 libdbusmenu-gtk3 cairo glib2 libgcc glibc

AutoReq:       no 
AutoReqProv:   no

%description
Elkowars Wacky Widgets is a standalone widget system made in Rust that allows you to implement your own, custom widgets in any window manager.

%prep
%setup -q
cargo fetch --target "%{_arch}-unknown-linux-gnu"

%build
cargo build --frozen --release

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 -T target/release/%{name} %{buildroot}%{_bindir}/%{name}
# todo handle license file

%files
%{_bindir}/%{name}


%changelog
* Thu Aug 08 2024 Andrea Cowley <azbuilds@exophoton.com>
- First COPR release