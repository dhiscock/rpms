# $Id$

# Authority: dries
# Upstream: Jean-Michel Hiver <jhiver$mkdoc,com>

%define real_name MKDoc-XML
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: MKDoc XML Toolkit
Name: perl-MKDoc-XML
Version: 0.72
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MKDoc-XML/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/J/JH/JHIVER/MKDoc-XML-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Typically, in MKDoc the stripper is used to remove unwanted presentational
markup while the tagger adds structural markup such as an abbr tag or automatically
hyperlinks expressions so that MKDoc users don't have to know about a tag syntax.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" destdir=%{buildroot}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README Changes
%doc %{_mandir}/man3/*
%{perl_vendorlib}/MKDoc/XML.pm
%{perl_vendorlib}/MKDoc/XML/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.72-1
- Initial package.
