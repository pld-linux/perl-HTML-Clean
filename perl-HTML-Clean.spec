%include	/usr/lib/rpm/macros.perl
Summary:	Perl HTML-Clean module
Summary(pl):	Modu³ Perla HTML-Clean
Name:		perl-HTML-Clean
Version:	0.8
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-Clean-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTML::Clean module cleans and optimizes HTML documents.

%description -l pl
Modu³ HTML::Clean czy¶ci i optymalizuje dokumenty HTML.

%prep
%setup -q -n HTML-Clean-%{version}

%build
perl Makefile.PL

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*

%{perl_sitelib}/HTML/*.pm
%{perl_sitearch}/auto/HTML/Clean

%{_mandir}/man[13]/*
