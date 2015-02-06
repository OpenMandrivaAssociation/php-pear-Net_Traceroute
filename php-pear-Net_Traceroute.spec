%define		_class		Net
%define		_subclass	Traceroute
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	0.21.3
Release:	3
Summary:	Execute traceroute
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Net_Traceroute/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
OS independent wrapper class for executing traceroute calls.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Sun Dec 18 2011 Oden Eriksson <oeriksson@mandriva.com> 0.21.3-1mdv2012.0
+ Revision: 743438
- 0.21.3
- fix major breakage by careless packager
- mass rebuild
- the mass rebuild of 2010.1 packages
- 0.21.2 (fixes CVE-2009-4025)

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.21.1-5mdv2010.1
+ Revision: 468723
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.21.1-4mdv2010.0
+ Revision: 441494
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.21.1-3mdv2009.1
+ Revision: 322502
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.21.1-2mdv2009.0
+ Revision: 236997
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 0.21.1-1mdv2008.0
+ Revision: 15706
- 0.21.1


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.21-7mdv2007.0
+ Revision: 82417
- Import php-pear-Net_Traceroute

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.21-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.21-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.21-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.21-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.21-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.21-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.21-1mdk
- initial Mandriva package (PLD import)

