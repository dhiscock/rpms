# $Id$

# Authority: dries
# Upstream: Adam Kennedy <cpan$ali,as>

%define real_name CSS-Tiny
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Read and write CSS files
Name: perl-CSS-Tiny
Version: 1.05
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/CSS-Tiny/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/CSS-Tiny-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
CSS::Tiny is a perl class to read and write .css stylesheets with as
little code as possible, reducing load time and memory overhead. CSS.pm
requires about 2.6 meg or ram to load, which is a large amount of
overhead if you only want to do trivial things. Memory usage is normally
scoffed at in Perl, but in my opinion should be at least kept in mind.

This module is primarily for reading and writing simple files, and
anything we write shouldn't need to have documentation/comments. If you
need something with more power, move up to CSS.pm. With the increasing
complexity of CSS, this is becoming more common, but many situations can
still live with simple CSS files.

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
%doc README Changes LICENSE
%doc %{_mandir}/man3/*
%{perl_vendorlib}/CSS/Tiny.pm
#%{perl_vendorlib}/CSS/Tiny/*
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 1.05-1
- Initial package.
