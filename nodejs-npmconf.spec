%define		pkg	npmconf
Summary:	The config thing npm uses
Name:		nodejs-%{pkg}
Version:	0.0.23
Release:	1
License:	MIT
Group:		Development/Libraries
URL:		https://github.com/isaacs/npmconf
# download from https://github.com/isaacs/%{pkg}/tarball/%%{version}
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	4d759f24e286fcacb7b8c609ff73b280
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
Requires:	nodejs
Requires:	nodejs-config-chain >= 1.1.1
Requires:	nodejs-inherits >= 1.0.0
Requires:	nodejs-ini < 1.2.0
Requires:	nodejs-ini >= 1.1.0
Requires:	nodejs-mkdirp >= 0.3.3
Requires:	nodejs-nopt >= 2.0.0
Requires:	nodejs-once >= 1.1.1
Requires:	nodejs-osenv >= 0.0.3
Requires:	nodejs-semver < 1.2.0
Requires:	nodejs-semver >= 1.1.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The config thing npm uses.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{nodejs_libdir}/%{pkg}}
cp -a package.json *.js $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%dir %{nodejs_libdir}/%{pkg}
%{nodejs_libdir}/%{pkg}/package.json
%{nodejs_libdir}/%{pkg}/*.js
