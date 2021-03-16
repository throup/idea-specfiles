%define vendor    jetbrains
%define fullname  IntelliJ Idea
%define shortname idea
%define buildname intellij-community-%{shortname}

%global __python %{__python3}
%define debug_package %{nil}

Name:          idea-intellij-community-edition
Version:       203.7717.45
Release:       1%{?dist}
Summary:       IntelliJ Java IDE - Community Edition

Group:         Development
License:       Apache License
URL:           https://github.com/JetBrains/intellij-community/tree/%{shortname}/%{version}
Source0:       https://github.com/JetBrains/intellij-community/archive/%{shortname}/%{version}.tar.gz
%define suppl1 android-idea-%{version}
Source1:       https://github.com/JetBrains/android/archive/%{shortname}/%{version}.tar.gz#/%{suppl1}.tar.gz

BuildRequires: ant
BuildRequires: desktop-file-utils
BuildRequires: java-sdk-11
Requires:      java >= 1:11
Requires:      jre >= 1:11
Requires:      %{name}-core = %{version}
Requires:      %{name}-plugin-android = %{version}
Requires:      %{name}-plugin-android-gradle-dsl = %{version}

%description
IntelliJ Java IDE based upon the Jetbrains Idea platform.


%package core
Summary:       IntelliJ Java IDE - core files
Group:         Development
%description core
Core files for Jetbrains IntelliJ.

%package plugin-android
Summary:       IntelliJ Java IDE - Android plugin
Group:         Development
%description plugin-android
Android plugin for Jetbrains IntelliJ.

%package plugin-android-gradle-dsl
Summary:       IntelliJ Java IDE - Android Gradle DSL plugin
Group:         Development
%description plugin-android-gradle-dsl
Android Gradle DSL plugin for Jetbrains IntelliJ.


%prep
%setup -qn "%{buildname}-%{version}"
echo %{version} > build.txt
%setup -T -D -a 1 -qn "%{buildname}-%{version}"
mv %{suppl1} android

%build
# Needed because pre-33 systems default to Java 8 even if a later version is installed.
export JAVA_HOME=$(rpm -ql $(rpm -q --whatprovides java-11-headless) | grep "jre")
export ANT_OPTS="$ANT_OPTS -Dintellij.build.target.os=linux"
ant -Dintellij.build.target.os=linux

cat >%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{fullname}
GenericName=%{fullname}
Comment=Starts %{fullname}
Exec="%{_datadir}/%{shortname}/bin/%{shortname}.sh" %f
Icon=%{_datadir}/%{shortname}/bin/%{shortname}.png
Terminal=false
Type=Application
Categories=GTK;GNOME;Development;
StartupWMClass=%{vendor}-%{shortname}-ce
EOF

# Create the wrapper for /usr/bin
cat >%{name} <<EOF
#!/bin/sh
%{_datadir}/%{shortname}/bin/%{shortname}.sh $@
EOF

%install
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_datadir}/%{shortname}

cp -a out/idea-ce/dist.all/* \
      %{buildroot}%{_datadir}/%{shortname}/
cp -a out/idea-ce/dist.unix/* \
      %{buildroot}%{_datadir}/%{shortname}/

install -p -m0755 out/idea-ce/dist.unix/bin/fsnotifier64 \
                  %{buildroot}%{_datadir}/%{shortname}/bin/
install -p -m0755 out/idea-ce/dist.unix/bin/idea.sh \
                  %{buildroot}%{_datadir}/%{shortname}/bin/
install -p -m0755 out/idea-ce/dist.unix/bin/inspect.sh \
                  %{buildroot}%{_datadir}/%{shortname}/bin/

install -p -m0755 %{name} \
                  %{buildroot}%{_bindir}/%{name}
desktop-file-install --dir %{buildroot}%{_datadir}/applications \
                     %{name}.desktop

# Remove unwanted files
rm %{buildroot}%{_datadir}/%{shortname}/Install-Linux-tar.txt

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files

%files plugin-android
%{_datadir}/%{shortname}/plugins/android

%files plugin-android-gradle-dsl
%{_datadir}/%{shortname}/plugins/android-gradle-dsl

%files core
%license %{_datadir}/%{shortname}/LICENSE.txt
%license %{_datadir}/%{shortname}/license
%doc %{_datadir}/%{shortname}/NOTICE.txt
%{_datadir}/%{shortname}/bin
%{_datadir}/%{shortname}/lib
%{_datadir}/%{shortname}/plugins
%{_datadir}/%{shortname}/redist
%{_datadir}/%{shortname}/brokenPlugins.db
%{_datadir}/%{shortname}/build.txt
%{_datadir}/%{shortname}/classpath.txt
%{_datadir}/%{shortname}/icons.db
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%exclude %{_datadir}/%{shortname}/plugins/android
%exclude %{_datadir}/%{shortname}/plugins/android-gradle-dsl

%changelog
* Tue Mar 16 2021 Chris Throup <chris@throup.eu>
- Split Android plugin into separate subpackage
* Mon Mar 15 2021 Chris Throup <chris@throup.eu>
- Under git control for release through COPR
* Fri Mar 12 2021 Chris Throup <chris@throup.eu>
- Tweaked for the modern world of Github
* Sat Dec  6 2014 Chris Throup <chris@throup.org.uk>
- Initial RPM release
