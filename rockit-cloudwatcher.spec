Name:      rockit-cloudwatcher
Version:   %{_version}
Release:   1%{dist}
Summary:   Weather station
Url:       https://github.com/rockit-astro/cloudwatcherd
License:   GPL-3.0
BuildArch: noarch

%description


%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/etc/bash_completion.d
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/cloudwatcherd/

%{__install} %{_sourcedir}/cloudwatcher %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/cloudwatcherd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/cloudwatcherd@.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/completion/cloudwatcher %{buildroot}/etc/bash_completion.d/cloudwatcher

%{__install} %{_sourcedir}/config/10-halfmetre-cloudwatcher.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/config/halfmetre.json %{buildroot}%{_sysconfdir}/cloudwatcherd/
%{__install} %{_sourcedir}/config/warwick.json %{buildroot}%{_sysconfdir}/cloudwatcherd/

%package server
Summary:  Weather station server
Group:    Unspecified
Requires: python3-rockit-cloudwatcher
%description server

%files server
%defattr(0755,root,root,-)
%{_bindir}/cloudwatcherd
%defattr(0644,root,root,-)
%{_unitdir}/cloudwatcherd@.service

%package client
Summary:  Weather station client
Group:    Unspecified
Requires: python3-rockit-cloudwatcher
%description client

%files client
%defattr(0755,root,root,-)
%{_bindir}/cloudwatcher
/etc/bash_completion.d/cloudwatcher

%package data-lapalma
Summary: Weather station data for La Palma telescopes
Group:   Unspecified
%description data-lapalma

%files data-lapalma
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-halfmetre-cloudwatcher.rules
%{_sysconfdir}/cloudwatcherd/halfmetre.json

%package data-warwick
Summary: Weather station data for Windmill Hill observatory
Group:   Unspecified
%description data-warwick

%files data-warwick
%defattr(0644,root,root,-)
%{_sysconfdir}/cloudwatcherd/warwick.json

%changelog
