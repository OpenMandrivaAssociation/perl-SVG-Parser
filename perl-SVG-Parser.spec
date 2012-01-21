%define upstream_name	 SVG-Parser
%define upstream_version 1.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

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
