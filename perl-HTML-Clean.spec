#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	HTML
%define		pnam	Clean
%include	/usr/lib/rpm/macros.perl
Summary:	HTML::Clean - cleans up HTML code for web browsers, not humans
Summary(pl.UTF-8):	HTML::Clean - czyści kod w HTML-u z punktu widzenia serwerów WWW
Name:		perl-HTML-Clean
Version:	0.8
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ee562703b7700c7fd4173f355e83ec2c
URL:		http://search.cpan.org/dist/HTML-Clean/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HTML::Clean Perl module encapsulates a number of common techniques
for minimizing the size of HTML files. You can typically save between
10% and 50% of the size of a HTML file using these methods.

%description -l pl.UTF-8
Moduł Perla HTML::Clean zamyka w sobie kilka ogólnych technik
minimalizacji rozmiaru plików HTML. Zazwyczaj pozwala on zaoszczędzić
na rozmiarze pliku HTML od 10% do 50%.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/HTML/*.pm
%dir %{perl_vendorlib}/auto/HTML
%dir %{perl_vendorlib}/auto/HTML/Clean
%{perl_vendorlib}/auto/HTML/Clean/autosplit.ix
%{_mandir}/man[13]/*
