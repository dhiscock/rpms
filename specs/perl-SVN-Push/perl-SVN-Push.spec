# $Id$

# Authority: dries
# Upstream: Gerald Richter <richter$ecos,de>

%define real_name SVN-Push
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)
%define perl_archlib %(eval "`perl -V:archlib`"; echo $archlib)
%define perl_privlib %(eval "`perl -V:privlib`"; echo $privlib)

Summary: Push Repository to Remote Subversion Repository
Name: perl-SVN-Push
Version: 0.02
Release: 1
License: Artistic
Group: Applications/CPAN
URL: http://search.cpan.org/dist/SVN-Push/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/G/GR/GRICHTER/SVN-Push-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl, subversion-perl

%description
SVN::Push is a module which let you push the content of a repoitory
or a parts of a repository to another subversion repository, using the
Ra layer. This means you can access the repositories by URL, so
it works also with remote repositories. It's also possible to specify
the revisions to push, so you need not to copy all revision and can
instead just push a cumulated revision, where necessary.

svnpush is a command line frontend for SVN::Push.

svndumpload is a command line tool which is able to replicate
a full repository to another by doing incremental dumps and loads.
It checks the revsion of the destination repsitory and
dumps only changes. One or both repositories could
be on a remote machine, in which case ssh access is necessary.
The main adavatage of svndumpload over svnpush is that it preserves
copy history.

svnsetuuid is a command line tool to set the uuid of a repostory.
This is necessary in case you want later on your working copy
with svn switch --relocate, in which case both repositories need to
have the same uuid.

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
%doc README CHANGES
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_bindir}/*
%{perl_vendorlib}/SVN/Push.pm
%exclude %{perl_archlib}/perllocal.pod
%exclude %{perl_vendorarch}/auto/*/*/.packlist

%changelog
* Thu Jul 22 2004 Dries Verachtert <dries@ulyssis.org> - 0.02-1
- Initial package.
