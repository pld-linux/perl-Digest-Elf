%include	/usr/lib/rpm/macros.perl
%define		pdir	Digest
%define		pnam	Elf
Summary:	Digest::Elf Perl module - implementation of the ElfHash algorithm
Summary(pl):	Modu³ perla Digest::Elf - implementacja algorytmu ElfHash
Name:		perl-Digest-Elf
Version:	1.3
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1690451386d40ac0e433534ae747d31c
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Digest::Elf provides an implimentation of the ElfHash algorithm.
ElfHash generates resonably unique values from a string in a
reasonably short period of time. The actual algorith is culled from a
Dr. Dobbs Journal article, they culled it probably from the source for
the GNU C complier.

%description -l pl
Modu³ Digest::Elf jest implementacj± algorytmu ElfHash. Algorytm ten
generuje w miarê unikalne warto¶ci dla ³añcuchów znaków w przyzwoitym
czasie. W³a¶ciwy algorytm jest ¶ci±gniêty z artyku³u z Dr. Dobbs
Journal, gdzie zosta³ ¶ci±gniêty prawdopodobnie ze ¼róde³ kompilatora
C z GNU.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Digest/Elf.pm
%dir %{perl_vendorarch}/auto/Digest/Elf
%{perl_vendorarch}/auto/Digest/Elf/Elf.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Digest/Elf/Elf.so
%{_mandir}/man3/*
