# $Id$

# Authority: dries
# Upstream: Marc Lehmann <pcg$goof,com>

%define real_name Crypt-Twofish2
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Twofish encryption module
Name: perl-Crypt-Twofish2
Version: 1.0
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Crypt-Twofish2/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/Crypt-Twofish2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
This module implements the twofish cipher in a less braindamaged (read:
slow and ugly) way than the existing "Crypt::Twofish" module.

Although it is "Crypt::CBC" compliant you usually gain nothing by using
that module (except generality, which is often a good thing), since
"Crypt::Twofish2" can work in either ECB or CBC mode itself.
    
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
%doc README Changes COPYING
%doc %{_mandir}/man3/*
%{perl_vendorarch}/Crypt/Twofish2.pm
%{perl_vendorarch}/auto/Crypt/Twofish2/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.0-1
- Initial package.
