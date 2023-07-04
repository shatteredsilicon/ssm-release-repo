Name:           ssm-release
Version:        1.0
Release:        1%{?dist}
Summary:        Install the SSM repo

License:	AGPLv3
URL:            https://ssm-dev-el8.repo
Source0:        ssm-repo.tar
BuildArch:	noarch

%description
Install the SSM repository


%prep
%autosetup


%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/etc/yum.repos.d
mkdir -p ${RPM_BUILD_ROOT}/etc/pki/rpm-gpg
cp ssm-el8.repo ${RPM_BUILD_ROOT}/etc/yum.repos.d/ssm-el8.repo
cp RPM-GPG-KEY-SSM-EL8 ${RPM_BUILD_ROOT}/etc/pki/rpm-gpg/RPM-GPG-KEY-SSM-EL8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/etc/yum.repos.d/ssm-el8.repo
/etc/pki/rpm-gpg/RPM-GPG-KEY-SSM-EL8

%changelog
* Tue Jul  4 2023 SSM build <ssmbuild@normandy.shatteredsilicon.net>
- 
