%{?_javapackages_macros:%_javapackages_macros}
%define debug_package %{nil}

Name:     nailgun
Version:  0.9.1
Release:  1.2
Summary:  Framework for running Java from the cli without the JVM startup overhead

License:  ASL 2.0
URL:      http://martiansoftware.com/nailgun/
Source0:  https://github.com/martylamb/nailgun/archive/nailgun-all-%{version}.zip
Patch0:   remove-tools-jar-dependencies.patch

BuildRequires: java-devel
BuildRequires:  jpackage-utils
BuildRequires: maven-local
Requires: java
Requires:  jpackage-utils

%description
Nailgun is a client, protocol, and server for running Java programs from the 
command line without incurring the JVM startup overhead. Programs run in the 
server (which is implemented in Java), and are triggered by the client 
(written in C), which handles all I/O.

%package javadoc
Summary:        Javadocs for %{name}

BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-all-%{version}

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Sep 02 2013 Mat Booth <fedora@matbooth.co.uk> - 0.7.1-9
- Drop dep on ant-trax, rhbz #992319
- Adapt to newer guidelines
- Fix bogus changelog date

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon May  24 2010  <mmorsi@redhat.com> - 0.7.1-3
- added necessary missing java-devel >= 1:1.6.0 BR

* Tue Apr  27 2010  <mmorsi@redhat.com> - 0.7.1-2
- removed deprecated gcj bits
- removed empty debuginfo package
- marked javadoc package as noarch

* Tue Jan  20 2009  <mmorsi@redhat.com> - 0.7.1-1
- Initial build.
