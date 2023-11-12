Name:           xdg-desktop-portal-hyprland
Version:        1.2.4
Release:        1
Summary:        xdg-desktop-portal backend for hyprland
License:        BSD-3-Clause AND HPND-sell-variant
Group:          Hyprland
URL:            https://github.com/hyprwm/%{name}
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(hyprland-protocols)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(sdbus-c++)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
 
Requires:       dbus-common
Requires:       dbus
# required for Screenshot portal implementation
Requires:       grim
Requires:       xdg-desktop-portal
# required for hyprland-share-picker
Requires:       slurp
Requires:       qt6-qtwayland
 
Enhances:       hyprland
Supplements:    hyprland
 
%description
%{summary}.
 
%prep
%autosetup -p1
 
%build
%meson
%meson_build
 
%install
%meson_install
 
%post
%systemd_user_post %{name}.service
 
%preun
%systemd_user_preun %{name}.service
 
%files
%license LICENSE
%doc README.md contrib/config.sample
%{_bindir}/hyprland-share-picker
%{_libexecdir}/%{name}
%{_datadir}/xdg-desktop-portal/portals/hyprland.portal
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.hyprland.service
%{_userunitdir}/%{name}.service
