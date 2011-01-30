Summary:	Helper library for dumb speech synthesizers
Summary(pl.UTF-8):	Biblioteka pomocnicza dla głupich syntezatorów mowy
Name:		libdumbtts
Version:	0.3.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.tts.polip.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	7eff56583b94837c89f38cc5cb05a0b5
Patch0:		%{name}-Makefile.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libdumbtts is helper library for dumb speech synthesizer drivers.
Developed for Ivona synthesizer and speech-dispatcher, but may be
usable with other synthesizer and application.

%description -l pl.UTF-8
libdumbtts to biblioteka pomocnicza dla driverów "głupich"
syntezatorów mowy. Opracowana dla syntezatora Ivona oraz
speech-dispatchera, ale może być przydatna dla innych syntezatorów
i aplikacji.

%package devel
Summary:	Header files for libdumbtts library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdumbtts
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libdumbtts library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdumbtts.

%prep
%setup -q
%patch0 -p1

%build
%{__make} -C src \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/dumbtts

%{__make} -C src install \
	LIBDIR=%{_libdir} \
	DESTDIR=$RPM_BUILD_ROOT

# Propably junk - removing
rm -rf $RPM_BUILD_ROOT%{_datadir}/dumbtts/pl.conf~

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%doc %lang(pl) README_pl
%attr(755,root,root) %{_libdir}/libdumbtts.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdumbtts.so.?
%dir %{_datadir}/dumbtts
%dir %{_sysconfdir}/dumbtts
%{_datadir}/dumbtts/*.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdumbtts.so
%{_includedir}/*
