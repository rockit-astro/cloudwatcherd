Name:      observatory-cloudwatcher-data
Version:   20230602
Release:   0
Url:       https://github.com/warwick-one-metre/cloudwatcherd
Summary:   Weather station data for La Palma
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

%build
mkdir -p %{buildroot}%{_udevrulesdir}
mkdir -p %{buildroot}%{_sysconfdir}/cloudwatcherd/

%files
%defattr(0644,root,root,-)

%changelog
