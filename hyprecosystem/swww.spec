%define debug_package %{nil}
%define repo github.com/LGFae/swww
%define version 0.9.5

Name:          swww
Version:       %{version}
Release:       1%{?dist}
Summary:       A Solution to your Wayland Wallpaper Woes 

License:       GPL-3.0
URL:           https://%{repo}
Source0:       https://%{repo}/archive/v%{version}.tar.gz

BuildRequires: cargo lz4-devel

AutoReq:       no 
AutoReqProv:   no

%description
A Solution to your Wayland Wallpaper Woes
Efficient animated wallpaper daemon for wayland, controlled at runtime

%prep
%setup -q

%build
cargo build --release

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
install -m 0755 target/release/%{name}-daemon %{buildroot}%{_bindir}/%{name}-daemon
install -m 0755 completions/%{name}.bash %{bash_completions_dir}/%{name}.bash
install -m 0755 completions/_%{name} %{zsh_completions_dir}/_%{name}
install -m 0755 completions/%{name}.fish %{fish_completions_dir}/%{name}.fish

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-daemon
%{bash_completions_dir}/%{name}.bash
%{zsh_completions_dir}/_%{name}
%{fish_completions_dir}/%{name}.fish


%changelog
* Tue Aug 06 2024 Andrea Cowley <azbuilds@exophoton.com>
- First COPR release