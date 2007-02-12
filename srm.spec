Summary:	srm - secure replacement for rm
Summary(pl.UTF-8):	srm - bezpieczny zamiennik dla rm
Name:		srm
Version:	1.2.8
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/srm/%{name}-%{version}.tar.gz
# Source0-md5:	66ba49b1864a7c69763210dbc3efee33
URL:		http://srm.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
srm is a secure replacement for rm. Unlike the standard rm, it
overwrites the data in the target files before unlinking them. This
prevents command-line recovery of the data by examining the raw block
device. It may also help frustrate physical examination of the disk,
although it's unlikely that it can completely prevent that type of
recovery. It is, essentially, a paper shredder for sensitive files.

%description -l pl.UTF-8
srm to bezpieczny zamiennik rm. W przeciwieństwie do zwykłego rm
nadpisuje dane w plikach docelowych przed ich usunięciem. Zapobiega to
odtworzeniu danych poprzez badanie surowego urządzenia blokowego. Może
także pomóc w udaremnieniu fizycznego badania dysku, ale jest mało
prawdopodobne, że zapobiegnie odtworzeniu w ten sposób. Jest to coś w
rodzaju niszczarki do dokumentów dla wrażliwych plików.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README Credits
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
