%{?_javapackages_macros:%_javapackages_macros}
%define debug_package %{nil}

Name:     nailgun
Version:  0.7.1
Release:  9.0%{?dist}
Summary:  Framework for running Java from the cli without the JVM startup overhead

License:  ASL 2.0
URL:      http://martiansoftware.com/nailgun/
Source0:  http://downloads.sourceforge.net/project/nailgun/nailgun/0.7.1/nailgun-src-0.7.1.zip
Patch0:   remove-tools-jar-dependencies.patch

BuildRequires: java-devel
BuildRequires:  jpackage-utils
BuildRequires: ant
BuildRequires: ant-junit
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
%setup -q
%patch0 -p1

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

%build
ant

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_bindir}

cp dist/nailgun-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

cp ng $RPM_BUILD_ROOT%{_bindir}/ng

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_javadir}/nailgun.jar
%{_bindir}/ng
%doc LICENSE.txt README.txt

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

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
