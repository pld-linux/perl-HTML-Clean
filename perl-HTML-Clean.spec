%include	/usr/lib/rpm/macros.perl
%define		pdir	HTML
%define		pnam	Clean
Summary:	HTML::Clean Perl module
Summary(cs):	Modul HTML::Clean pro Perl
Summary(da):	Perlmodul HTML::Clean
Summary(de):	HTML::Clean Perl Modul
Summary(es):	Módulo de Perl HTML::Clean
Summary(fr):	Module Perl HTML::Clean
Summary(it):	Modulo di Perl HTML::Clean
Summary(ja):	HTML::Clean Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	HTML::Clean ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul HTML::Clean
Summary(pl):	Modu³ Perla HTML::Clean
Summary(pt):	Módulo de Perl HTML::Clean
Summary(pt_BR):	Módulo Perl HTML::Clean
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl HTML::Clean
Summary(sv):	HTML::Clean Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl HTML::Clean
Summary(zh_CN):	HTML::Clean Perl Ä£¿é
Name:		perl-HTML-Clean
Version:	0.8
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTML::Clean module cleans and optimizes HTML documents.

%description -l pl
Modu³ HTML::Clean czy¶ci i optymalizuje dokumenty HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/HTML/*.pm
%dir %{perl_sitelib}/auto/HTML
%dir %{perl_sitelib}/auto/HTML/Clean
%{perl_sitelib}/auto/HTML/Clean/autosplit.ix
%{_mandir}/man[13]/*
