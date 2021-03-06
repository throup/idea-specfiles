%define vendor     jetbrains
%define fullname   IntelliJ Idea
%define shortname  idea
%define buildname  intellij-community-%{shortname}
%define uniquename io.github.jetbrains.intellij_idea

%global __python %{__python3}
%define debug_package %{nil}

Name:          idea-intellij-ce
Version:       212.4746.92
Release:       1%{?dist}
Summary:       IntelliJ Java IDE - Community Edition

# Original package name was a little long...
Provides:      idea-intellij-community-edition = %{version}
Obsoletes:     idea-intellij-community-edition < %{version}

Group:         Development
License:       Apache License
URL:           https://github.com/JetBrains/intellij-community/tree/%{shortname}/%{version}
Source0:       https://github.com/JetBrains/intellij-community/archive/%{shortname}/%{version}.tar.gz

# This is an earlier version of the android project.
# At the time of writing, no unique version has been tagged for this release of IntelliJ, so we use the most recent
# previous tag.
%define androidversion 212.3116.43
%define suppl1 android-idea-%{androidversion}
Source1:       https://github.com/JetBrains/android/archive/%{shortname}/%{androidversion}.tar.gz#/%{suppl1}.tar.gz

# This is an earlier version of the library definition.
# At the time of writing, the current version points to an artifact which is not published publically.
Source2:       https://raw.githubusercontent.com/JetBrains/intellij-community/d8314c735234a95228e992df2ae3a12a417ccad0/.idea/libraries/Log4J.xml

BuildRequires: ant
BuildRequires: appstream
BuildRequires: desktop-file-utils
BuildRequires: java-sdk-11
Requires:      java-11
Requires:      jre-11
Requires:      %{name}-core = %{version}
Requires:      %{name}-plugin-android = %{version}
Requires:      %{name}-plugin-android-gradle-dsl = %{version}
Requires:      %{name}-plugin-ant = %{version}
Requires:      %{name}-plugin-bytecodeviewer = %{version}
Requires:      %{name}-plugin-completionmlranking = %{version}
Requires:      %{name}-plugin-configurationscript = %{version}
Requires:      %{name}-plugin-copyright = %{version}
Requires:      %{name}-plugin-coverage = %{version}
Requires:      %{name}-plugin-devkit = %{version}
Requires:      %{name}-plugin-eclipse = %{version}
Requires:      %{name}-plugin-editorconfig = %{version}
Requires:      %{name}-plugin-emojipicker = %{version}
Requires:      %{name}-plugin-externalsystem-dependencyupdater = %{version}
Requires:      %{name}-plugin-featurestrainer = %{version}
Requires:      %{name}-plugin-fileprediction = %{version}
Requires:      %{name}-plugin-git4idea = %{version}
Requires:      %{name}-plugin-github = %{version}
Requires:      %{name}-plugin-gradle = %{version}
Requires:      %{name}-plugin-gradle-dependencyupdater = %{version}
Requires:      %{name}-plugin-gradle-java = %{version}
Requires:      %{name}-plugin-gradle-java-maven = %{version}
Requires:      %{name}-plugin-grazie = %{version}
Requires:      %{name}-plugin-groovy = %{version}
Requires:      %{name}-plugin-hg4idea = %{version}
Requires:      %{name}-plugin-intellilang = %{version}
Requires:      %{name}-plugin-java = %{version}
Requires:      %{name}-plugin-java-decompiler = %{version}
Requires:      %{name}-plugin-javafx = %{version}
Requires:      %{name}-plugin-java-i18n = %{version}
Requires:      %{name}-plugin-java-ide-customization = %{version}
Requires:      %{name}-plugin-junit = %{version}
Requires:      %{name}-plugin-kotlin = %{version}
Requires:      %{name}-plugin-lombok = %{version}
Requires:      %{name}-plugin-markdown = %{version}
Requires:      %{name}-plugin-maven = %{version}
Requires:      %{name}-plugin-maven-model = %{version}
Requires:      %{name}-plugin-platform-images = %{version}
Requires:      %{name}-plugin-properties = %{version}
Requires:      %{name}-plugin-properties-resource-bundle-editor = %{version}
Requires:      %{name}-plugin-repository-search = %{version}
Requires:      %{name}-plugin-settings-repository = %{version}
Requires:      %{name}-plugin-sh = %{version}
Requires:      %{name}-plugin-smali = %{version}
Requires:      %{name}-plugin-stream-debugger = %{version}
Requires:      %{name}-plugin-svn4idea = %{version}
Requires:      %{name}-plugin-tasks = %{version}
Requires:      %{name}-plugin-terminal = %{version}
Requires:      %{name}-plugin-testng = %{version}
Requires:      %{name}-plugin-textmate = %{version}
Requires:      %{name}-plugin-uidesigner = %{version}
Requires:      %{name}-plugin-vcs-changereminder = %{version}
Requires:      %{name}-plugin-webp = %{version}
Requires:      %{name}-plugin-xpath = %{version}
Requires:      %{name}-plugin-xslt-debugger = %{version}
Requires:      %{name}-plugin-yaml = %{version}

%description
IntelliJ Java IDE based upon the Jetbrains Idea platform.


%package core
Summary:       IntelliJ Java IDE - core files
Group:         Development
%description core
Core files for Jetbrains IntelliJ.

%package plugin-ant
Summary:       IntelliJ Java IDE - Ant plugin
Group:         Development
Requires:      %{name}-core = %{version}
Requires:      mvn(ant:ant)
%description plugin-ant
Ant plugin for Jetbrains IntelliJ.

%package plugin-android
Summary:       IntelliJ Java IDE - Android plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-android
Android plugin for Jetbrains IntelliJ.

%package plugin-android-gradle-dsl
Summary:       IntelliJ Java IDE - Android Gradle DSL plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-android-gradle-dsl
Android Gradle DSL plugin for Jetbrains IntelliJ.

%package plugin-bytecodeviewer
Summary:       IntelliJ Java IDE - ByteCodeViewer plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-bytecodeviewer
ByteCodeViewer plugin for Jetbrains IntelliJ.

%package plugin-completionmlranking
Summary:       IntelliJ Java IDE - Machine Learning Code Completion plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-completionmlranking
The plugin improves code completion feature by reordering of elements in the completion popup by ranking more relevant items higher using machine learning.

To enable the feature for your programming language, check settings in Editor | General | Code Completion | "Machine Learning Assistant Code Completion" section.

%package plugin-configurationscript
Summary:       IntelliJ Java IDE - Configuration Script plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-configurationscript
Configuration Script plugin for Jetbrains IntelliJ.

%package plugin-copyright
Summary:       IntelliJ Java IDE - Copyright plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-copyright
Copyright plugin for Jetbrains IntelliJ.

%package plugin-coverage
Summary:       IntelliJ Java IDE - Coverage plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-coverage
Coverage plugin for Jetbrains IntelliJ.

%package plugin-devkit
Summary:       IntelliJ Java IDE - Devkit plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-devkit
Devkit plugin for Jetbrains IntelliJ.

%package plugin-eclipse
Summary:       IntelliJ Java IDE - Eclipse plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-eclipse
Eclipse plugin for Jetbrains IntelliJ.

%package plugin-editorconfig
Summary:       IntelliJ Java IDE - Editorconfig plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-editorconfig
Editorconfig plugin for Jetbrains IntelliJ.

%package plugin-emojipicker
Summary:       IntelliJ Java IDE - Emojipicker plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-emojipicker
Emojipicker plugin for Jetbrains IntelliJ.

%package plugin-externalsystem-dependencyupdater
Summary:       IntelliJ Java IDE - External System Dependency Updater plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-externalsystem-dependencyupdater
External System Dependency Updater plugin for Jetbrains IntelliJ.

%package plugin-git4idea
Summary:       IntelliJ Java IDE - Git plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-git4idea
Git plugin for Jetbrains IntelliJ.

%package plugin-github
Summary:       IntelliJ Java IDE - Github plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-github
Github plugin for Jetbrains IntelliJ.

%package plugin-gradle
Summary:       IntelliJ Java IDE - Gradle plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-gradle
Gradle plugin for Jetbrains IntelliJ.

%package plugin-gradle-dependencyupdater
Summary:       IntelliJ Java IDE - Gradle Dependency Updater plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-gradle-dependencyupdater
Gradle Dependency Updater plugin for Jetbrains IntelliJ.

%package plugin-gradle-java
Summary:       IntelliJ Java IDE - Gradle Java plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-gradle-java
Gradle Java plugin for Jetbrains IntelliJ.

%package plugin-gradle-java-maven
Summary:       IntelliJ Java IDE - Gradle Java Maven plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-gradle-java-maven
Gradle Java Maven plugin for Jetbrains IntelliJ.

%package plugin-grazie
Summary:       IntelliJ Java IDE - Grazie plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-grazie
Grazie plugin for Jetbrains IntelliJ.

%package plugin-groovy
Summary:       IntelliJ Java IDE - Groovy plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-groovy
Groovy plugin for Jetbrains IntelliJ.

%package plugin-java
Summary:       IntelliJ Java IDE - Java plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-java
Java plugin for Jetbrains IntelliJ.

%package plugin-java-decompiler
Summary:       IntelliJ Java IDE - Java Decompiler plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-java-decompiler
Java Decompiler plugin for Jetbrains IntelliJ.

%package plugin-javafx
Summary:       IntelliJ Java IDE - JavaFX plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-javafx
JavaFX plugin for Jetbrains IntelliJ.

%package plugin-java-i18n
Summary:       IntelliJ Java IDE - Java I18n plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-java-i18n
Java I18n plugin for Jetbrains IntelliJ.

%package plugin-java-ide-customization
Summary:       IntelliJ Java IDE - Java IDE Customization plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-java-ide-customization
Java IDE Customization plugin for Jetbrains IntelliJ.

%package plugin-junit
Summary:       IntelliJ Java IDE - Junit plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-junit
Junit plugin for Jetbrains IntelliJ.

%package plugin-markdown
Summary:       IntelliJ Java IDE - Markdown plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-markdown
Markdown plugin for Jetbrains IntelliJ.

%package plugin-maven
Summary:       IntelliJ Java IDE - Maven plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-maven
Maven plugin for Jetbrains IntelliJ.

%package plugin-maven-model
Summary:       IntelliJ Java IDE - Maven Model plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-maven-model
Maven Model plugin for Jetbrains IntelliJ.

%package plugin-intellilang
Summary:       IntelliJ Java IDE - Intellilang plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-intellilang
IntelliLang plugin for Jetbrains IntelliJ.

%package plugin-kotlin
Summary:       IntelliJ Java IDE - Kotlin plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-kotlin
Kotlin plugin for Jetbrains IntelliJ.

%package plugin-lombok
Summary:       IntelliJ Java IDE - Lombok plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-lombok
Lombok plugin for Jetbrains IntelliJ.

%package plugin-featurestrainer
Summary:       IntelliJ Java IDE - FeaturesTrainer plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-featurestrainer
FeaturesTrainer plugin for Jetbrains IntelliJ.

%package plugin-fileprediction
Summary:       IntelliJ Java IDE - FilePrediction plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-fileprediction
FilePrediction plugin for Jetbrains IntelliJ.

%package plugin-hg4idea
Summary:       IntelliJ Java IDE - Hg4idea plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-hg4idea
Hg4idea plugin for Jetbrains IntelliJ.

%package plugin-platform-images
Summary:       IntelliJ Java IDE - Platform-images plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-platform-images
Platform-images plugin for Jetbrains IntelliJ.

%package plugin-properties
Summary:       IntelliJ Java IDE - Properties plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-properties
Properties plugin for Jetbrains IntelliJ.

%package plugin-properties-resource-bundle-editor
Summary:       IntelliJ Java IDE - Properties-resource-bundle-editor plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-properties-resource-bundle-editor
Properties-resource-bundle-editor plugin for Jetbrains IntelliJ.

%package plugin-repository-search
Summary:       IntelliJ Java IDE - Repository-search plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-repository-search
Repository-search plugin for Jetbrains IntelliJ.

%package plugin-settings-repository
Summary:       IntelliJ Java IDE - Settings-repository plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-settings-repository
Settings-repository plugin for Jetbrains IntelliJ.

%package plugin-sh
Summary:       IntelliJ Java IDE - Sh plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-sh
Sh plugin for Jetbrains IntelliJ.

%package plugin-smali
Summary:       IntelliJ Java IDE - Smali plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-smali
Smali plugin for Jetbrains IntelliJ.

%package plugin-stream-debugger
Summary:       IntelliJ Java IDE - Stream-debugger plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-stream-debugger
Stream-debugger plugin for Jetbrains IntelliJ.

%package plugin-svn4idea
Summary:       IntelliJ Java IDE - Svn4idea plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-svn4idea
Svn4idea plugin for Jetbrains IntelliJ.

%package plugin-tasks
Summary:       IntelliJ Java IDE - Tasks plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-tasks
Tasks plugin for Jetbrains IntelliJ.

%package plugin-terminal
Summary:       IntelliJ Java IDE - Terminal plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-terminal
Terminal plugin for Jetbrains IntelliJ.

%package plugin-testng
Summary:       IntelliJ Java IDE - Testng plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-testng
Testng plugin for Jetbrains IntelliJ.

%package plugin-textmate
Summary:       IntelliJ Java IDE - Textmate plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-textmate
Textmate plugin for Jetbrains IntelliJ.

%package plugin-uidesigner
Summary:       IntelliJ Java IDE - UiDesigner plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-uidesigner
UiDesigner plugin for Jetbrains IntelliJ.

%package plugin-vcs-changereminder
Summary:       IntelliJ Java IDE - Vcs-changeReminder plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-vcs-changereminder
Vcs-changeReminder plugin for Jetbrains IntelliJ.

%package plugin-webp
Summary:       IntelliJ Java IDE - Webp plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-webp
Webp plugin for Jetbrains IntelliJ.

%package plugin-xpath
Summary:       IntelliJ Java IDE - Xpath plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-xpath
Xpath plugin for Jetbrains IntelliJ.

%package plugin-xslt-debugger
Summary:       IntelliJ Java IDE - XSLT Debugger plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-xslt-debugger
XSLT Debugger plugin for Jetbrains IntelliJ.

%package plugin-yaml
Summary:       IntelliJ Java IDE - YAML plugin
Group:         Development
Requires:      %{name}-core = %{version}
%description plugin-yaml
YAML plugin for Jetbrains IntelliJ.

%package release
Summary:       IntelliJ Java IDE - Community Edition - RELEASE version
Requires:      %{name} = %{version}
%description release
IntelliJ Java IDE based upon the Jetbrains Idea platform.
Meta-package to track the current RELEASE version


%prep
%setup -qn "%{buildname}-%{version}"
echo %{version} > build.txt
%setup -T -D -a 1 -qn "%{buildname}-%{version}"
mv %{suppl1} android
cp %_topdir/SOURCES/Log4J.xml .idea/libraries/

%build
# Needed because pre-33 systems default to Java 8 even if a later version is installed.
export JAVA_HOME=$(rpm -ql $(rpm -q --whatprovides java-11-headless) | grep "jre")
export ANT_OPTS="$ANT_OPTS -Dintellij.build.target.os=linux"
ant -Dintellij.build.target.os=linux

cat > %{uniquename}.metainfo.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="desktop-application">
    <id>%{uniquename}</id>

    <name>IntelliJ IDEA</name>
    <summary>IntelliJ Java IDE based upon the Jetbrains Idea platform.</summary>

    <metadata_license>FSFAP</metadata_license>
    <project_license>Apache-2.0</project_license>

    <description>
        <p>
            IntelliJ Java IDE based upon the Jetbrains Idea platform.
        </p>
    </description>

    <launchable type="desktop-id">%{uniquename}.desktop</launchable>
    <screenshots>
        <screenshot type="default">
            <image>https://www.jetbrains.com/idea/img/screenshots/idea_overview_5_1.png</image>
        </screenshot>
    </screenshots>

    <icon type="stock">%{uniquename}</icon>

    <categories>
        <category>Development</category>
        <category>IDE</category>
    </categories>

    <provides>
        <binary>%{name}</binary>
    </provides>
</component>
EOF

appstreamcli make-desktop-file %{uniquename}.metainfo.xml %{uniquename}.desktop
echo "StartupWMClass=%{vendor}-%{shortname}-ce" >> %{uniquename}.desktop

# Create the wrapper for /usr/bin
cat >%{name} <<EOF
#!/bin/sh
%{_datadir}/%{shortname}/bin/%{shortname}.sh $@
EOF

cat >%{name}.sh <<EOF
#!/bin/sh
export IDEA_JDK=/usr/lib/jvm/java-11
EOF

# Remove unwanted files
rm out/idea-ce/dist.unix/Install-Linux-tar.txt

# Removing bundled libs which are also provided by Fedora
rm -r out/idea-ce/dist.all/lib/ant
ln -s ../../ant out/idea-ce/dist.all/lib/

%install
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_datadir}/%{shortname} \
         %{buildroot}%{_datadir}/metainfo/ \
         %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/ \
         %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/ \
         %{buildroot}%{_sysconfdir}/profile.d

cp -a out/idea-ce/dist.all/* \
      %{buildroot}%{_datadir}/%{shortname}/
cp -a out/idea-ce/dist.unix/* \
      %{buildroot}%{_datadir}/%{shortname}/

ln -s ../../../../%{shortname}/bin/idea.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{uniquename}.png
ln -s ../../../../%{shortname}/bin/idea.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{uniquename}.svg

install -p -m0755 out/idea-ce/dist.unix/bin/fsnotifier64 \
                  %{buildroot}%{_datadir}/%{shortname}/bin/
install -p -m0755 out/idea-ce/dist.unix/bin/idea.sh \
                  %{buildroot}%{_datadir}/%{shortname}/bin/
install -p -m0755 out/idea-ce/dist.unix/bin/inspect.sh \
                  %{buildroot}%{_datadir}/%{shortname}/bin/

install -p -m0755 %{name} \
                  %{buildroot}%{_bindir}/%{name}

install -p -m0755 %{name}.sh \
                  %{buildroot}%{_sysconfdir}/profile.d/%{name}.sh

desktop-file-install --dir %{buildroot}%{_datadir}/applications \
                     %{uniquename}.desktop

cp %{uniquename}.metainfo.xml %{buildroot}%{_datadir}/metainfo/


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{uniquename}.desktop

%files

%files plugin-ant
%{_datadir}/%{shortname}/lib/ant
%{_datadir}/%{shortname}/plugins/ant

%files plugin-android
%{_datadir}/%{shortname}/plugins/android

%files plugin-android-gradle-dsl
%{_datadir}/%{shortname}/plugins/android-gradle-dsl

%files plugin-bytecodeviewer
%{_datadir}/%{shortname}/plugins/ByteCodeViewer

%files plugin-completionmlranking
%{_datadir}/%{shortname}/plugins/completionMlRanking

%files plugin-configurationscript
%{_datadir}/%{shortname}/plugins/configurationScript

%files plugin-copyright
%{_datadir}/%{shortname}/plugins/copyright

%files plugin-coverage
%{_datadir}/%{shortname}/plugins/coverage

%files plugin-devkit
%{_datadir}/%{shortname}/plugins/devkit

%files plugin-eclipse
%{_datadir}/%{shortname}/plugins/eclipse

%files plugin-editorconfig
%{_datadir}/%{shortname}/plugins/editorconfig

%files plugin-emojipicker
%{_datadir}/%{shortname}/plugins/emojipicker

%files plugin-externalsystem-dependencyupdater
%{_datadir}/%{shortname}/plugins/externalSystem-dependencyUpdater

%files plugin-git4idea
%{_datadir}/%{shortname}/plugins/git4idea

%files plugin-github
%{_datadir}/%{shortname}/plugins/github

%files plugin-gradle
%{_datadir}/%{shortname}/plugins/gradle

%files plugin-gradle-dependencyupdater
%{_datadir}/%{shortname}/plugins/gradle-dependencyUpdater

%files plugin-gradle-java
%{_datadir}/%{shortname}/plugins/gradle-java

%files plugin-gradle-java-maven
%{_datadir}/%{shortname}/plugins/gradle-java-maven

%files plugin-grazie
%{_datadir}/%{shortname}/plugins/grazie

%files plugin-groovy
%{_datadir}/%{shortname}/plugins/Groovy

%files plugin-java
%{_datadir}/%{shortname}/plugins/java

%files plugin-java-decompiler
%{_datadir}/%{shortname}/plugins/java-decompiler

%files plugin-javafx
%{_datadir}/%{shortname}/plugins/javaFX

%files plugin-java-i18n
%{_datadir}/%{shortname}/plugins/java-i18n

%files plugin-java-ide-customization
%{_datadir}/%{shortname}/plugins/java-ide-customization

%files plugin-junit
%{_datadir}/%{shortname}/plugins/junit

%files plugin-markdown
%{_datadir}/%{shortname}/plugins/markdown

%files plugin-maven
%{_datadir}/%{shortname}/plugins/maven
%{_datadir}/%{shortname}/plugins/maven/lib/maven3/lib/jansi-native/linux64
%exclude %{_datadir}/%{shortname}/plugins/maven/lib/maven3/lib/jansi-native/windows32
%exclude %{_datadir}/%{shortname}/plugins/maven/lib/maven3/lib/jansi-native/windows64
%exclude %{_datadir}/%{shortname}/plugins/maven/lib/maven3/lib/jansi-native/osx
%exclude %{_datadir}/%{shortname}/plugins/maven/lib/maven3/lib/jansi-native/freebsd32
%exclude %{_datadir}/%{shortname}/plugins/maven/lib/maven3/lib/jansi-native/freebsd64

%files plugin-maven-model
%{_datadir}/%{shortname}/plugins/maven-model

%files plugin-intellilang
%{_datadir}/%{shortname}/plugins/IntelliLang

%files plugin-kotlin
%{_datadir}/%{shortname}/plugins/Kotlin

%files plugin-lombok
%{_datadir}/%{shortname}/plugins/lombok

%files plugin-featurestrainer
%{_datadir}/%{shortname}/plugins/featuresTrainer

%files plugin-fileprediction
%{_datadir}/%{shortname}/plugins/filePrediction

%files plugin-hg4idea
%{_datadir}/%{shortname}/plugins/hg4idea

%files plugin-platform-images
%{_datadir}/%{shortname}/plugins/platform-images

%files plugin-properties
%{_datadir}/%{shortname}/plugins/properties

%files plugin-properties-resource-bundle-editor
%{_datadir}/%{shortname}/plugins/properties-resource-bundle-editor

%files plugin-repository-search
%{_datadir}/%{shortname}/plugins/repository-search

%files plugin-settings-repository
%{_datadir}/%{shortname}/plugins/settings-repository

%files plugin-sh
%{_datadir}/%{shortname}/plugins/sh

%files plugin-smali
%{_datadir}/%{shortname}/plugins/smali

%files plugin-stream-debugger
%{_datadir}/%{shortname}/plugins/stream-debugger

%files plugin-svn4idea
%{_datadir}/%{shortname}/plugins/svn4idea

%files plugin-tasks
%{_datadir}/%{shortname}/plugins/tasks

%files plugin-terminal
%{_datadir}/%{shortname}/plugins/terminal

%files plugin-testng
%{_datadir}/%{shortname}/plugins/testng

%files plugin-textmate
%{_datadir}/%{shortname}/plugins/textmate

%files plugin-uidesigner
%{_datadir}/%{shortname}/plugins/uiDesigner

%files plugin-vcs-changereminder
%{_datadir}/%{shortname}/plugins/vcs-changeReminder

%files plugin-webp
%{_datadir}/%{shortname}/plugins/webp

%files plugin-xpath
%{_datadir}/%{shortname}/plugins/xpath

%files plugin-xslt-debugger
%{_datadir}/%{shortname}/plugins/xslt-debugger

%files plugin-yaml
%{_datadir}/%{shortname}/plugins/yaml

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
%{_datadir}/applications/%{uniquename}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{uniquename}.png
%{_datadir}/icons/hicolor/scalable/apps/%{uniquename}.svg
%{_sysconfdir}/profile.d/%{name}.sh
%exclude %{_datadir}/%{shortname}/lib/pty4j-native/linux/x86
%exclude %{_datadir}/%{shortname}/lib/pty4j-native/linux/aarch64
%exclude %{_datadir}/%{shortname}/lib/pty4j-native/linux/mips64el
%exclude %{_datadir}/%{shortname}/lib/pty4j-native/linux/ppc64le
%exclude %{_datadir}/%{shortname}/lib/ant
%exclude %{_datadir}/%{shortname}/plugins/ant
%exclude %{_datadir}/%{shortname}/plugins/android
%exclude %{_datadir}/%{shortname}/plugins/android-gradle-dsl
%exclude %{_datadir}/%{shortname}/plugins/ByteCodeViewer
%exclude %{_datadir}/%{shortname}/plugins/completionMlRanking
%exclude %{_datadir}/%{shortname}/plugins/configurationScript
%exclude %{_datadir}/%{shortname}/plugins/copyright
%exclude %{_datadir}/%{shortname}/plugins/coverage
%exclude %{_datadir}/%{shortname}/plugins/devkit
%exclude %{_datadir}/%{shortname}/plugins/eclipse
%exclude %{_datadir}/%{shortname}/plugins/editorconfig
%exclude %{_datadir}/%{shortname}/plugins/emojipicker
%exclude %{_datadir}/%{shortname}/plugins/externalSystem-dependencyUpdater
%exclude %{_datadir}/%{shortname}/plugins/git4idea
%exclude %{_datadir}/%{shortname}/plugins/github
%exclude %{_datadir}/%{shortname}/plugins/gradle
%exclude %{_datadir}/%{shortname}/plugins/gradle-dependencyUpdater
%exclude %{_datadir}/%{shortname}/plugins/gradle-java
%exclude %{_datadir}/%{shortname}/plugins/gradle-java-maven
%exclude %{_datadir}/%{shortname}/plugins/grazie
%exclude %{_datadir}/%{shortname}/plugins/Groovy
%exclude %{_datadir}/%{shortname}/plugins/java
%exclude %{_datadir}/%{shortname}/plugins/java-decompiler
%exclude %{_datadir}/%{shortname}/plugins/javaFX
%exclude %{_datadir}/%{shortname}/plugins/java-i18n
%exclude %{_datadir}/%{shortname}/plugins/java-ide-customization
%exclude %{_datadir}/%{shortname}/plugins/junit
%exclude %{_datadir}/%{shortname}/plugins/markdown
%exclude %{_datadir}/%{shortname}/plugins/maven
%exclude %{_datadir}/%{shortname}/plugins/maven-model
%exclude %{_datadir}/%{shortname}/plugins/IntelliLang
%exclude %{_datadir}/%{shortname}/plugins/Kotlin
%exclude %{_datadir}/%{shortname}/plugins/lombok
%exclude %{_datadir}/%{shortname}/plugins/featuresTrainer
%exclude %{_datadir}/%{shortname}/plugins/filePrediction
%exclude %{_datadir}/%{shortname}/plugins/hg4idea
%exclude %{_datadir}/%{shortname}/plugins/platform-images
%exclude %{_datadir}/%{shortname}/plugins/properties
%exclude %{_datadir}/%{shortname}/plugins/properties-resource-bundle-editor
%exclude %{_datadir}/%{shortname}/plugins/repository-search
%exclude %{_datadir}/%{shortname}/plugins/settings-repository
%exclude %{_datadir}/%{shortname}/plugins/sh
%exclude %{_datadir}/%{shortname}/plugins/smali
%exclude %{_datadir}/%{shortname}/plugins/stream-debugger
%exclude %{_datadir}/%{shortname}/plugins/svn4idea
%exclude %{_datadir}/%{shortname}/plugins/tasks
%exclude %{_datadir}/%{shortname}/plugins/terminal
%exclude %{_datadir}/%{shortname}/plugins/testng
%exclude %{_datadir}/%{shortname}/plugins/textmate
%exclude %{_datadir}/%{shortname}/plugins/uiDesigner
%exclude %{_datadir}/%{shortname}/plugins/vcs-changeReminder
%exclude %{_datadir}/%{shortname}/plugins/webp
%exclude %{_datadir}/%{shortname}/plugins/xpath
%exclude %{_datadir}/%{shortname}/plugins/xslt-debugger
%exclude %{_datadir}/%{shortname}/plugins/yaml

%files release
%{_datadir}/metainfo/%{uniquename}.metainfo.xml

%changelog
* Mon Aug 16 2021 Chris Throup <chris@throup.eu>
- New release version
* Mon Jul 5 2021 Chris Throup <chris@throup.eu>
- New release version
* Wed Jun 2 2021 Chris Throup <chris@throup.eu>
- New release version
* Sun May 2 2021 Chris Throup <chris@throup.eu>
- New release version
* Fri Apr 23 2021 Chris Throup <chris@throup.eu>
- New eap release
* Tue Apr 20 2021 Chris Throup <chris@throup.eu>
- Restore StartupWMClass in Desktop file
* Thu Apr 8 2021 Chris Throup <chris@throup.eu>
- New RELEASE version
* Sat Apr 3 2021 Chris Throup <chris@throup.eu>
- Moved metapackage into the same SPEC as the build
* Fri Mar 26 2021 Chris Throup <chris@throup.eu>
- Improvements for release version packaging
* Thu Mar 25 2021 Chris Throup <chris@throup.eu>
- Improvements for release version packaging
* Fri Mar 19 2021 Chris Throup <chris@throup.eu>
- Split remaining plugins into separate subpackages
* Thu Mar 18 2021 Chris Throup <chris@throup.eu>
- Split additional plugins into separate subpackages
* Wed Mar 17 2021 Chris Throup <chris@throup.eu>
- Split additional plugins into separate subpackages
* Tue Mar 16 2021 Chris Throup <chris@throup.eu>
- Split Android plugin into separate subpackage
* Mon Mar 15 2021 Chris Throup <chris@throup.eu>
- Under git control for release through COPR
* Fri Mar 12 2021 Chris Throup <chris@throup.eu>
- Tweaked for the modern world of Github
* Sat Dec  6 2014 Chris Throup <chris@throup.org.uk>
- Initial RPM release
