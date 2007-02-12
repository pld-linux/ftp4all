Summary:	Free, open source FTP server implementation
Summary(pl.UTF-8):   Darmowa implementacja serwera FTP
Name:		ftp4all
Version:	3.012
Release:	4
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.ftp4all.de/v3/archives/ftpd-%{version}.tar.gz
# Source0-md5:	a1bdeb4080d3900099e07aebd5fdd460
Source1:	http://www.ftp4all.de/v3/f4awebsite.tar.gz
# Source1-md5:	34b5c4712b8ed23af5beea1074f71fd7
Patch0:		ftpd-opt.patch
Patch1:		ftpd-endian.patch
Patch2:		ftpd-configure.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
# this isn't ,,standard FTP''. Don't treat it as system FTP server
# and don't put Provides:ftpserver etc here ! --misiek

%description
FTP4ALL was designed to require no superuser privileges. The
advantages are that FTP4ALL cannot be exploited to gain root access on
a machine. And second, any user on a UNIX box can run this server.

However, FTP4ALL is not designed to replace wu-ftpd or any other
system-level FTP server, for it does not use the default user database
(/etc/passwd or NIS or whatever), or the UNIX file and directory
permissions. Instead, FTP4ALL sets up its own user and group database
and file and directory permission system.

Those and other features like user upload and download ratios, IP
checks, bandwidth limit, transfer statistics make FTP4ALL a good
choice for running a private, specialised FTP site. There is no binary
distribution, the only one is the source distribution. So you must
have a C compiler (gcc preferred) and related tools to compile
FTP4ALL.

%description -l pl.UTF-8
FTP4ALL został zaprojektowany tak by nie wymagać praw
superużytkownika. Główną zaletą takiego podejścia jest uniemożliwienie
wykorzystania potencjalnych błędów do zdobycia uprawnień roota.
Ponadto każdy użytkownik może uruchamiać ten serwer.

Jednak FTP4ALL nie jest zaprojektowany by zastąpić wu-ftpd czy dowolny
inny systemowy serwer FTP, a to dlatego, że nie używa on standardowej
bazy użytkowników (/etc/passwd lub NIS), ani UNIXowych praw dostępu do
plików.

Te i inne możliwości jak ratio dla upload i download per użytkownik,
dostęp na poziomie IP, limity pasma, statystyki transferów sprawiają
że FTP4ALL to dobry wybór dla prywatnych, specjalistycznych serwerów
FTP.

%prep
%setup -q -n ftpd-%{version} -a1
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
echo "y" | \
CFLAGS="%{rpmcflags}" \
LIBDIR="%{_libdir}" \
SLIBDIR="/%{_lib}" \
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}}

install bin/* $RPM_BUILD_ROOT%{_bindir}

cp -a standard	$RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README f4adp frames
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
