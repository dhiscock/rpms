# $Id$

# Authority: dries
# Upstream: Mark Fowler <mark$twoshortplanks,com>

%define real_name Test-Builder-Tester
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Test testsuites that have been built with Test::Builder
Name: perl-Test-Builder-Tester
Version: 1.00
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Builder-Tester/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/M/MA/MARKF/Test-Builder-Tester-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
Test testsuites that have been built with Test::Builder.

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
%doc CHANGES
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Test/Builder/Tester.pm
%{perl_vendorlib}/Test/Builder/Tester/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.00-1
- Initial package.
