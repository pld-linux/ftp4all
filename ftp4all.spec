Summary:	free, open source FTP server implementation
Summary(pl):	implementacja serwera FTP
Name:		ftp4all
Version:	3.012
Release:	3
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.ftp4all.de/v3/archives/ftpd-%{version}.tar.gz
Source1:	http://www.ftp4all.de/v3/f4awebsite.tar.gz
Patch0:		ftpd-opt.patch
Patch1:		ftpd-endian.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
# this isn't ,,standard ftp''. Don't treat it as system ftp server
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

%description -l pl
FTP4ALL zosta³ zaprojektowany tak by nie wymagaæ praw
superu¿ytkownika. G³ówn± zalet± takiego podej¶cia jest uniemo¿liwienie
wykorzystania potencjalnych b³êdów do zdobycia uprawnieñ roota.
Ponadto ka¿dy u¿ytkownik mo¿e uruchamiaæ ten serwer.

Jednak FTP4ALL nie jest zaprojektowany by zast±piæ wu-ftpd czy dowolny
inny systemowy serwer FTP, a to dlatego, ¿e nie u¿ywa on standardowej
bazy u¿ytkowników (/etc/passwd lub NIS), ani UNIXowych praw dostêpu do
plików.

Te i inne mo¿liwo¶ci jak ratio dla upload i download per u¿ytkownik,
dostêp na poziomie IP, limity pasma, statystyki transferów.

%prep
%setup -q -n ftpd-%{version} -a1
%patch0 -p1
%patch1 -p1

%build
%ifarch %{ix86}
echo "y" | CFLAGS="%{rpmcflags}" ./configure
%else
echo "y" | ./configure
%endif
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}}

install bin/* $RPM_BUILD_ROOT%{_bindir}

cp -ar standard	$RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README f4adp frames
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
