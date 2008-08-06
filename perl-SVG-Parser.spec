%define module	SVG-Parser
%define name	perl-%{module}
%define version 1.03
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl XML Parser for Scalable Vector Graphics (SVG) documents
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/SVG/%{module}-%{version}.tar.bz2
BuildRequires:	perl(XML::SAX)
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(SVG)
BuildRequires:	perl(Module::Build)
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

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


