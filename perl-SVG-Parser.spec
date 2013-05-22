%define upstream_name	 SVG-Parser
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:	Perl XML Parser for Scalable Vector Graphics (SVG) documents
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/SVG/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Module::Build)
BuildRequires:	perl(SVG)
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(XML::SAX)
BuildRequires:	perl(XML::SAX::Expat)
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
SVG::Parser is an XML parser for SVG Documents. It takes XML as input and
produces an SVG object as its output. SVG::Parser supports both XML::SAX and
XML::Parser (Expat) parsers, with SAX preferred by default.
Only one of these needs to be installed for SVG::Parser to function.

A list of preferred parsers may be specified in the import list.
SVG::Parser will use the first parser that successfully loads.
Some basic measures are taken to provide cross-compatibility.
Applications requiring more advanced parser features should use
the relevant parser module directly; see SVG::Parser::Expat and 
SVG::Parser::SAX.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%check
./Build test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README examples
%{perl_vendorlib}/SVG
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-4mdv2012.0
+ Revision: 765667
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.30.0-2
+ Revision: 667306
- mass rebuild

* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 1.30.0-1mdv2011.0
+ Revision: 410219
- adding missing buildrequires:
- rebuild using %%perl_convert_version

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.03-2mdv2009.0
+ Revision: 265436
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.03-1mdv2009.0
+ Revision: 195143
- switch to Module::Build

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.01-2mdv2008.1
+ Revision: 180559
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Feb 05 2007 Pascal Terjan <pterjan@mandriva.org> 1.01-1mdv2007.0
+ Revision: 116537
- fix Requires and BuildRequires
- fix file listed twice
- shorten summary and other lines too long
- fix typo in description
- Import perl-SVG-Parser

* Mon Feb 05 2007 Raphaël Gertz <rapsys@free.fr> 1.01-0.1mdv2007.0
- first mdk release

