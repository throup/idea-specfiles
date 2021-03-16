%define vendor    jetbrains
%define fullname  IntelliJ Idea
%define shortname idea
%define buildname intellij-ce-eap

%global __python %{__python3}
%define debug_package %{nil}

Name:          idea-intellij-ce-eap
Version:       211.6432.7
Release:       2%{?dist}
Summary:       IntelliJ Java IDE - Community Edition - EAP version

Group:         Development
License:       Apache License

Requires:      idea-intellij-community-edition = %{version}

%description
IntelliJ Java IDE based upon the Jetbrains Idea platform.
Meta-package to track the current EAP version

%prep

%build

%install

%post

%check

%files

%changelog
* Mon Mar 15 2021 Chris Throup <chris@throup.eu>
- Initial RPM release
