Name:      observatory-cloudwatcher-client
Version:   20230602
Release:   0
Url:       https://github.com/warwick-one-metre/cloudwatcherd
Summary:   Weather station client for the Warwick telescopes.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3 python3-Pyro4 python3-warwick-observatory-common python3-warwick-observatory-cloudwatcher

%description

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/cloudwatcher %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/cloudwatcher %{buildroot}/etc/bash_completion.d/cloudwatcher

%files
%defattr(0755,root,root,-)
%{_bindir}/cloudwatcher
/etc/bash_completion.d/cloudwatcher

%changelog
