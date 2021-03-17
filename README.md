# idea-specfiles

SPEC files for unofficial RPM builds of IntelliJ IDEA Community Edition.
Currently a work in progress, finding an appropriate package structure.

*These are not the [official packages](https://www.jetbrains.com/idea) built by JetBrains.
They are compiled from the [publicly released source code](https://github.com/JetBrains/intellij-community).*

## Install on Fedora Linux

RPM packages are built in a Copr (community project): https://copr.fedorainfracloud.org/coprs/throup/idea-intellij-community-edition/

To enable this repository on Fedora:
```
dnf copr enable throup/idea-intellij-community-edition
```

The best way to install the IDE is to select the current RELEASE version, or be brave and install the EAP releases:
```
# for the stable RELEASE version:
dnf install idea-intellij-ce-release

# for the unstable EAP version:
dnf install idea-intellij-ce-eap
```

## Current build status
_Note:_ these badges show the current build status for the specific versions of the SPEC files found in the `main` branch of this repository.
See the [Copr project page](https://copr.fedorainfracloud.org/coprs/throup/idea-intellij-community-edition/) for the status of other builds.

| Intellij IDEA CE (latest build version) | Latest RELEASE version | Latest EAP version |
| --------------------------------------- | ---------------------- | ------------------ |
| [![Copr build status](https://copr.fedorainfracloud.org/coprs/throup/idea-intellij-community-edition/package/idea-intellij-community-edition/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/throup/idea-intellij-community-edition/package/idea-intellij-community-edition/) | [![Copr build status](https://copr.fedorainfracloud.org/coprs/throup/idea-intellij-community-edition/package/idea-intellij-ce-release/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/throup/idea-intellij-community-edition/package/idea-intellij-ce-release/) | [![Copr build status](https://copr.fedorainfracloud.org/coprs/throup/idea-intellij-community-edition/package/idea-intellij-ce-eap/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/throup/idea-intellij-community-edition/package/idea-intellij-ce-eap/) |

## Project aims
1. Make the open source, Community Edition of this IDE available as a native package for Fedora desktops.
2. Reduce the installation footprint by breaking the application into smaller, selectable packages.
3. Depend on existing packages in the Fedora infrastructure, instead of adding unneccessary copies of common libraries.
