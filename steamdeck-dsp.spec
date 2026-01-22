# broken build system
%undefine _debugsource_packages

Name:		steamdeck-dsp
Version:	0.77
Release:	1
Source0:	https://steamdeck-packages.steamos.cloud/archlinux-mirror/sources/jupiter-main/steamdeck-dsp-%{version}-1.src.tar.gz
Summary:	DSP files needed for audio on Steam Deck hardware
URL:		https://github.com/steamdeck-dsp/steamdeck-dsp
License:	GPL
Group:		Hardware
BuildRequires:	faust
BuildRequires:	faust-tools
BuildRequires:	git-core
BuildRequires:	make
BuildRequires:	qmake5
BuildRequires:	boost-devel

%description
DSP files needed for audio on Steam Deck hardware

%prep
%autosetup -p1 -n %{name}
git clone --depth 1 valve-hardware-audio-processing src

%build
export PATH=%{_libdir}/qt5/bin:$PATH
cd src
make FAUSTINC="%{_includedir}/faust" FAUSTLIB="%{_datadir}/faust"

%install
cd src
mkdir -p %{buildroot}%{_sysconfdir}/wireplumber/
make install DEST_DIR="%{buildroot}"

%files
%{_userunitdir}/filter-chain.service.d
%{_unitdir}/wireplumber-sysconf.service
%{_unitdir}/pipewire-sysconf.service
%{_unitdir}/multi-user.target.wants/*.service
%{_unitdir}/user@.service.d/*
%{_prefix}/lib/systemd/user.conf.d/*
%{_prefix}/lib/firmware/amd/sof
%{_prefix}/lib/firmware/amd/sof-tplg
%{_prefix}/lib/lv2/*.lv2
%{_prefix}/lib/lv2/*.dsp
%{_datadir}/alsa/ucm2/conf.d/*
%{_datadir}/pipewire/hardware-profiles/*
%{_datadir}/wireplumber/hardware-profiles/*
%{_sysconfdir}/wireplumber/*
