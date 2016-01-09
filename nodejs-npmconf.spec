%define		pkg	npmconf
Summary:	The config thing npm uses
Name:		nodejs-%{pkg}
Version:	1.1.2
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/%{pkg}/-/%{pkg}-%{version}.tgz
# Source0-md5:	fa32a3cff8ffa6cf8151130699549500
URL:		https://github.com/isaacs/npmconf
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
Requires:	nodejs-config-chain < 1.2.0
Requires:	nodejs-config-chain >= 1.1.8
Requires:	nodejs-inherits < 2.1.1
Requires:	nodejs-inherits >= 2.0.0
Requires:	nodejs-ini < 2.0.0
Requires:	nodejs-ini >= 1.1.0
Requires:	nodejs-mkdirp < 0.4.0
Requires:	nodejs-mkdirp >= 0.3.3
Requires:	nodejs-nopt < 4
Requires:	nodejs-nopt >= 2
Requires:	nodejs-once < 1.4.0
Requires:	nodejs-once >= 1.3.0
Requires:	nodejs-osenv < 1
Requires:	nodejs-osenv >= 0.1.0
Requires:	nodejs-semver < 3
Requires:	nodejs-semver >= 2
Requires:	nodejs-uid-number = 0.0.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The config thing npm uses.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -a package.json %{pkg}.js config-defs.js $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{nodejs_libdir}/%{pkg}
