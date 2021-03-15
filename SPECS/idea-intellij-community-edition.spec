%define vendor    jetbrains
%define fullname  IntelliJ Idea
%define shortname idea
%define buildname intellij-community-%{shortname}

%global __python %{__python3}
%define debug_package %{nil}

Name:          idea-intellij-community-edition
Version:       203.7148.57
Release:       8
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

%description
IntelliJ Java IDE based upon the Jetbrains Idea platform.

%prep
%setup -qn "%{buildname}-%{version}"
echo %{version} > build.txt
%setup -T -D -a 1 -n "%{buildname}-%{version}"
mv %{suppl1} android

%build
#export ANT_OPTS="-Xmx4G -Dintellij.build.dev.mode=false -Dintellij.build.target.os=linux"
# This may not be the best way... but this ensures that the Java 11 compiler is used.
# Needed because pre-33 systems default to Java 8 even if a later version is installed.
export JAVA_HOME=$(rpm -ql $(rpm -q --whatprovides java-11-headless) | grep "jre")
export ANT_OPTS="$ANT_OPTS -Dintellij.build.target.os=linux"
ant -Dintellij.build.target.os=linux
#ant -f python/build.xml -Dintellij.build.target.os=linux -Didea.path=`pwd`/out/artifacts/ -Didea.build.number=%{version} plugin

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

#rm out/idea-ce/dist.unix/bin/fsnotifier

cp -a out/idea-ce/dist.all/* \
      %{buildroot}%{_datadir}/%{shortname}/
cp -a out/idea-ce/dist.unix/* \
      %{buildroot}%{_datadir}/%{shortname}/

#cp -a python/distCE/zip/python \
#      %{buildroot}%{_datadir}/%{shortname}/plugins/


#install -p -m0755 out/idea-ce/dist.unix/bin/fsnotifier \
#                  %{buildroot}%{_datadir}/%{shortname}/bin/
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


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%doc %{_datadir}/%{shortname}/license
%doc %{_datadir}/%{shortname}/NOTICE.txt
%doc %{_datadir}/%{shortname}/build.txt
%doc %{_datadir}/%{shortname}/Install-Linux-tar.txt
%{_datadir}/%{shortname}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Mar 15 2021 Chris Throup <chris@throup.eu>
- Under git control for release through COPR
* Fri Mar 12 2021 Chris Throup <chris@throup.eu>
- Tweaked for the modern world of Github
* Sat Dec  6 2014 Chris Throup <chris@throup.org.uk>
- Initial RPM release
