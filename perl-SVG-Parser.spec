%define modname	SVG-Parser
%define modver	1.03

Summary:	Perl XML Parser for Scalable Vector Graphics (SVG) documents
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	16
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/SVG/%{modname}-%{modver}.tar.bz2
Buildarch:	noarch
BuildRequires:	perl(Test)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(SVG)
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(XML::SAX)
BuildRequires:	perl(XML::SAX::Expat)

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
%setup -qn %{modname}-%{modver}

%build
%__perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot}

%check
./Build test

%files 
%doc README examples
%{perl_vendorlib}/SVG
%{_mandir}/man3/*

