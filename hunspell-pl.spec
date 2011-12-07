Name: hunspell-pl
Summary: Polish hunspell dictionaries
%define upstreamid 20090908
Version: 0.%{upstreamid}
Release: 1.1%{?dist}
Source: http://sjp.pl/slownik/ort/sjp-myspell-pl-%{upstreamid}.zip
Group: Applications/Text
URL: http://www.kurnik.pl/dictionary/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+ or GPL+ or MPLv1.1
BuildArch: noarch

Requires: hunspell

%description
Polish hunspell dictionaries.

%prep
%setup -q -c hunspell-pl

%build
unzip pl_PL.zip

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_pl_PL.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20090908-1.1
- Rebuilt for RHEL 6

* Tue Sep 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090908-1
- latest version

* Sat Aug 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090808-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090708-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090708-1
- latest version

* Mon Jun 08 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090608-1
- latest version

* Sun Apr 19 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090419-1
- latest version

* Sun Mar 15 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090315-1
- latest version

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090215-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 15 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090215-1
- latest version

* Wed Jan 14 2009 Caolan McNamara <caolanm@redhat.com> - 0.20090114-1
- latest version

* Sat Aug 23 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080823-1
- latest version

* Tue Jul 15 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080715-1
- latest version

* Sat Jun 14 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080614-1
- latest version

* Tue May 13 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080513-1
- latest version

* Mon Apr 07 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080407-1
- latest version

* Tue Mar 04 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080304-1
- source file name changed, update to latest version

* Wed Feb 13 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080213-1
- new version

* Wed Jan 09 2008 Caolan McNamara <caolanm@redhat.com> - 0.20080109-1
- new version

* Sat Dec 08 2007 Caolan McNamara <caolanm@redhat.com> - 0.20071208-1
- new version

* Thu Nov 15 2007 Caolan McNamara <caolanm@redhat.com> - 0.20071114-1
- new version

* Fri Oct 05 2007 Caolan McNamara <caolanm@redhat.com> - 0.20071004-1
- new version

* Mon Sep 03 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070903-1
- new version

* Thu Aug 09 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070803-1
- clarify that is tri-licensed

* Sun Jul 01 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070701-1
- latest version
- near daily updates => move to a pick it up the 1st of the month cycle

* Fri Jun 29 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070629-1
- latest version

* Fri Jun 22 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070622-1
- latest version
