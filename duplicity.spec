Summary:	Utility for encrypted, bandwidth-efficient backups using the rsync algorithm
Name:		duplicity
Version:	0.6.22
Release:	3
License:	GPL v2
Group:		Applications/Archiving
Source0:	http://savannah.nongnu.org/download/duplicity/%{name}-%{version}.tar.gz
# Source0-md5:	5b035359a6bb7b2f3f3b9829c6c071e1
URL:		http://www.nongnu.org/duplicity/
BuildRequires:	python-devel
BuildRequires:	librsync-devel
BuildRequires:	rpm-pythonprov
Requires:	python-paramiko
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Duplicity backs directories by producing encrypted tar-format volumes
and uploading them to a remote or local file server. Because duplicity
uses librsync, the incremental archives are space efficient and only
record the parts of files that have changed since the last backup.
Because duplicity uses GnuPG to encrypt and/or sign these archives,
they will be safe from spying and/or modification by the server.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/io

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG README-LOG README-REPO
%attr(755,root,root) %{_bindir}/duplicity
%attr(755,root,root) %{_bindir}/rdiffdir
%dir %{py_sitedir}/duplicity
%dir %{py_sitedir}/duplicity/backends
%attr(755,root,root) %{py_sitedir}/duplicity/_librsync.so
%{py_sitedir}/duplicity/*.py*
%{py_sitedir}/duplicity/backends/*.py*
%{_mandir}/man1/duplicity.1*
%{_mandir}/man1/rdiffdir.1*
