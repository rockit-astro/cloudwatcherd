Name:      observatory-cloudwatcher-server
Version:   20230602
Release:   0
Url:       https://github.com/warwick-one-metre/cloudwatcherd
Summary:   Weather station daemon for the Warwick telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-pyserial python3-warwick-observatory-common python3-warwick-observatory-cloudwatcher

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/cloudwatcherd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/cloudwatcherd@.service %{buildroot}%{_unitdir}

%files
%defattr(0755,root,root,-)
%{_bindir}/cloudwatcherd
%defattr(0644,root,root,-)
%{_unitdir}/cloudwatcherd@.service

%changelog
