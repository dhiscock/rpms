# $Id$

# Authority: dries
# Upstream: Flávio Soibelmann Glock <fglock$pucrs,br>

%define real_name DateTime-Event-Random
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: DateTime extension for creating random datetimes
Name: perl-DateTime-Event-Random
Version: 0.03
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DateTime-Event-Random/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/F/FG/FGLOCK/DateTime-Event-Random-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module creates DateTime::* objects with random values.

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
%{perl_vendorlib}/DateTime/Event/Random.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
