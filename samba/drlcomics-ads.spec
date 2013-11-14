Name:		drlcomics-ads
Version:	0.1
Release:	8
Summary:	Configuration file for ADS authenication with DRLCOMICS

Group:		System
License:	GPL
#URL:		
Source0:	%{name}-%{version}.%{release}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	nscd
Requires:	ntp
Requires:	samba-winbind
Requires:	pam_krb5

%description
Custom configuration to set authenication with Active Directory

%prep
%setup -q


#%build
#%%configure
#make %{?_smp_mflags}


%install
rm -rf %{buildroot}
#make install DESTDIR=%{buildroot}
%{__mkdir_p} %{buildroot}

%clean
rm -rf %{buildroot}

%post
authconfig --enablemkhomedir --enableshadow --enablecache --enablewinbind \
--enablewinbindauth --winbindtemplatehomedir=/home/%U --enablewinbindusedefaultdomain \
--smbrealm=DRLCOMICS.LOCAL --smbservers=dc01.drlcomics.local,dc02.drlcomics.local --smbsecurity=ads \
--smbworkgroup=DRLCOMICS --winbindtemplateshell=/bin/bash --smbidmaprange=16777216-33554431 \
--disablefingerprint \
--updateall

cd /etc/init.d;chkconfig --level 345 ntpd on
cd /usr/sbin/;ntpdate -s  0.centos.pool.ntp.org

cd /usr/bin;net join -w DRLCOMICS -S dc01.drlcomics.local -U Administrator

sed -i 's/^;require_membership_of/require_membership_of/g' \
/etc/security/pam_winbind.conf
sed -i 's/require_membership_of\ =/require_membership_of\ =\ linuxusers/g' \
/etc/security/pam_winbind.conf
sed -i '/## Same\ thing\ without\ a\ password/a %linuxusers\tALL=\(ALL\)\tNOPASSWD:\ ALL' /etc/sudoers

%files
%defattr(-,root,root,-)

%doc



%changelog
* Thu Oct 31 2013 Tym Rehm
- Add group to sudoers file

* Wed Oct 2 2013 Tym Rehm
- Initial Build
