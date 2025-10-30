# JMC Agent Version
%global major 1
%global minor 0
%global patchlevel 1

# Revision
%global revnum 3

# JMC release version tag containing the agent code
%global jmc_version 9.1.1-ga
%global tarball_name jmc-%{jmc_version}

%global releasestr %{revnum}

Name:     jmc-agent
Version:  %{major}.%{minor}.%{patchlevel}
Release:  %{releasestr}%{?dist}
Summary:  JDK Mission Control Agent
License:  UPL
URL:      http://openjdk.java.net/projects/jmc/agent/
Source0:  https://github.com/openjdk/jmc/archive/refs/tags/%{jmc_version}.tar.gz

BuildArch:  noarch

BuildRequires:  java-21-openjdk-devel
BuildRequires:  junit
BuildRequires:  maven-local
BuildRequires:  maven-shade-plugin
BuildRequires:  objectweb-asm >= 8.0.0-1

# On F35 onward, surefire requires Xmx1024m to avoid the VM from crashing during tests
Patch0:  0-increase-surefire-memory.patch

%description
The JMC agent allows users to add JFR instrumentation declaratively to a running program.
The agent can, for example, be used to add flight recorder events to third party code
for which the source is not available.

%package javadoc
Summary:  Javadoc for %{name}

%description javadoc
This package contains javadoc for %{summary}.

%prep
%setup -q -n %{tarball_name}/agent

%patch 0 -p1

cp ./license/* ./

%pom_remove_plugin :maven-failsafe-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :spotless-maven-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%license THIRDPARTYREADME.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt
%license THIRDPARTYREADME.txt
%doc README.md

%changelog
* Thu Oct 30 2025 aptmac <aptmac@ibm.com> - 1.0.1-2
- Update to use JMC 9.1.1-ga

* Thu Jan 06 2022 aptmac <almacdon@redhat.com> - 1.0.1-2
- Added build requires on jdk 11 and version requirement on objectweb-asm

* Mon Dec 06 2021 aptmac <almacdon@redhat.com> - 1.0.1-1
- Initial package
