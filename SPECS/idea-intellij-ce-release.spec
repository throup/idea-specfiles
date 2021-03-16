%define vendor    jetbrains
%define fullname  IntelliJ Idea
%define shortname idea
%define buildname intellij-ce-release

%global __python %{__python3}
%define debug_package %{nil}

Name:          idea-intellij-ce-release
Version:       203.7148.57
Release:       2%{?dist}
Summary:       IntelliJ Java IDE - Community Edition - RELEASE version

Group:         Development
License:       Apache License

Requires:      idea-intellij-community-edition = %{version}

%description
IntelliJ Java IDE based upon the Jetbrains Idea platform.
Meta-package to track the current RELEASE version

%prep

%build

%install

%post

%check

%files

%changelog
* Mon Mar 15 2021 Chris Throup <chris@throup.eu>
- Initial RPM release
