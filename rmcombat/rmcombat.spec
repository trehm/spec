%define _htmlconfdir %{_localstatedir}/www/html
%define _imagedir %{_localstatedir}/www/html/images
%define _dbdir %{_localstatedir}/www/html/db


Name:		RMcombat
Version:	0.51
Release:	1
Summary:	PHP based Rolemaster combat generator

Group:		Web
License:	GPL
#URL:		
Source0:	%{name}-%{version}.%{release}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
#BuildRequires:	
Requires:	httpd php

%description
PHP-based combat generator for Rolemaster

%prep
%setup -q


#%build
#%%configure
#make %{?_smp_mflags}


%install
#rm -rf $RPM_BUILD_ROOT
rm -rf %{buildroot}
#make install DESTDIR=%{buildroot}
%{__mkdir_p} %{buildroot}%{_htmlconfdir}
%{__mkdir_p} %{buildroot}%{_imagedir}
%{__mkdir_p} %{buildroot}%{_dbdir}

install -m 644 crit.txt %{buildroot}%{_htmlconfdir}/crit.txt
install -m 644 index.php %{buildroot}%{_htmlconfdir}/index.php
install -m 444 README %{buildroot}%{_htmlconfdir}/README
install -m 444 images/battleaxe.gif %{buildroot}%{_imagedir}/battleaxe.gif
install -m 444 images/bola.gif %{buildroot}%{_imagedir}/bola.gif
install -m 444 images/broadsword.gif %{buildroot}%{_imagedir}/broadsword.gif
install -m 444 images/club.gif %{buildroot}%{_imagedir}/club.gif
install -m 444 images/compositebow.gif %{buildroot}%{_imagedir}/compositebow.gif
install -m 444 images/dagger.gif %{buildroot}%{_imagedir}/dagger.gif
install -m 444 images/falchion.gif %{buildroot}%{_imagedir}/falchion.gif
install -m 444 images/fall-huge.gif %{buildroot}%{_imagedir}/fall-huge.gif
install -m 444 images/fall-large.gif %{buildroot}%{_imagedir}/fall-large.gif
install -m 444 images/fall-medium.gif %{buildroot}%{_imagedir}/fall-medium.gif
install -m 444 images/fall-small.gif %{buildroot}%{_imagedir}/fall-small.gif
install -m 444 images/flail.gif %{buildroot}%{_imagedir}/flail.gif
install -m 444 images/handaxe.gif %{buildroot}%{_imagedir}/handaxe.gif
install -m 444 images/heavycrossbow.gif %{buildroot}%{_imagedir}/heavycrossbow.gif
install -m 444 images/javelin.gif %{buildroot}%{_imagedir}/javelin.gif
install -m 444 images/lance.gif %{buildroot}%{_imagedir}/lance.gif
install -m 444 images/lightcrossbow.gif %{buildroot}%{_imagedir}/lightcrossbow.gif
install -m 444 images/longbow.gif %{buildroot}%{_imagedir}/longbow.gif
install -m 444 images/mace.gif %{buildroot}%{_imagedir}/mace.gif
install -m 444 images/maingauche.gif %{buildroot}%{_imagedir}/maingauche.gif
install -m 444 images/mastrike1.gif %{buildroot}%{_imagedir}/mastrike1.gif
install -m 444 images/mastrike2.gif %{buildroot}%{_imagedir}/mastrike2.gif
install -m 444 images/morningstar.gif %{buildroot}%{_imagedir}/morningstar.gif
install -m 444 images/polearm.gif %{buildroot}%{_imagedir}/polearm.gif
install -m 444 images/quarterstaff.gif %{buildroot}%{_imagedir}/quarterstaff.gif
install -m 444 images/rapier.gif %{buildroot}%{_imagedir}/rapier.gif
install -m 444 images/scimitar.gif %{buildroot}%{_imagedir}/scimitar.gif
install -m 444 images/shortbow.gif %{buildroot}%{_imagedir}/shortbow.gif
install -m 444 images/shortsword.gif %{buildroot}%{_imagedir}/shortsword.gif
install -m 444 images/sling.gif %{buildroot}%{_imagedir}/sling.gif
install -m 444 images/spear.gif %{buildroot}%{_imagedir}/spear.gif
install -m 444 images/two-handedsword.gif %{buildroot}%{_imagedir}/two-handedsword.gif
install -m 444 images/warhammer.gif %{buildroot}%{_imagedir}/warhammer.gif
install -m 444 images/warmattock.gif %{buildroot}%{_imagedir}/warmattock.gif
install -m 444 images/whip.gif %{buildroot}%{_imagedir}/whip.gif
install -m 444 db/battleaxe.csv %{buildroot}%{_dbdir}/battleaxe.csv
install -m 444 db/beak-huge.csv %{buildroot}%{_dbdir}/beak-huge.csv
install -m 444 db/beak-large.csv %{buildroot}%{_dbdir}/beak-large.csv
install -m 444 db/beak-medium.csv %{buildroot}%{_dbdir}/beak-medium.csv
install -m 444 db/beak-small.csv %{buildroot}%{_dbdir}/beak-small.csv
install -m 444 db/bite-huge.csv %{buildroot}%{_dbdir}/bite-huge.csv
install -m 444 db/bite-large.csv %{buildroot}%{_dbdir}/bite-large.csv
install -m 444 db/bite-medium.csv %{buildroot}%{_dbdir}/bite-medium.csv
install -m 444 db/bite-small.csv %{buildroot}%{_dbdir}/bite-small.csv
install -m 444 db/bola.csv %{buildroot}%{_dbdir}/bola.csv
install -m 444 db/brawling.csv %{buildroot}%{_dbdir}/brawling.csv
install -m 444 db/brawling-huge.csv %{buildroot}%{_dbdir}/brawling-huge.csv
install -m 444 db/brawling-large.csv %{buildroot}%{_dbdir}/brawling-large.csv
install -m 444 db/brawling-medium.csv %{buildroot}%{_dbdir}/brawling-medium.csv
install -m 444 db/brawling-small.csv %{buildroot}%{_dbdir}/brawling-small.csv
install -m 444 db/broadsword.csv %{buildroot}%{_dbdir}/broadsword.csv
install -m 444 db/claw-huge.csv %{buildroot}%{_dbdir}/claw-huge.csv
install -m 444 db/claw-large.csv %{buildroot}%{_dbdir}/claw-large.csv
install -m 444 db/claw-medium.csv %{buildroot}%{_dbdir}/claw-medium.csv
install -m 444 db/claw-small.csv %{buildroot}%{_dbdir}/claw-small.csv
install -m 444 db/club.csv %{buildroot}%{_dbdir}/club.csv
install -m 444 db/compositebow.csv %{buildroot}%{_dbdir}/compositebow.csv
install -m 444 db/dagger.csv %{buildroot}%{_dbdir}/dagger.csv
install -m 444 db/falchion.csv %{buildroot}%{_dbdir}/falchion.csv
install -m 444 db/fall-huge.csv %{buildroot}%{_dbdir}/fall-huge.csv
install -m 444 db/fall-large.csv %{buildroot}%{_dbdir}/fall-large.csv
install -m 444 db/fall-medium.csv %{buildroot}%{_dbdir}/fall-medium.csv
install -m 444 db/fall-small.csv %{buildroot}%{_dbdir}/fall-small.csv
install -m 444 db/flail.csv %{buildroot}%{_dbdir}/flail.csv
install -m 444 db/fumble.csv %{buildroot}%{_dbdir}/fumble.csv
install -m 444 db/grapple.csv %{buildroot}%{_dbdir}/grapple.csv
install -m 444 db/grapple-huge.csv %{buildroot}%{_dbdir}/grapple-huge.csv
install -m 444 db/grapple-large.csv %{buildroot}%{_dbdir}/grapple-large.csv
install -m 444 db/grapple-medium.csv %{buildroot}%{_dbdir}/grapple-medium.csv
install -m 444 db/grapple-small.csv %{buildroot}%{_dbdir}/grapple-small.csv
install -m 444 db/handaxe.csv %{buildroot}%{_dbdir}/handaxe.csv
install -m 444 db/handcrossbow.csv %{buildroot}%{_dbdir}/handcrossbow.csv
install -m 444 db/heavycrossbow.csv %{buildroot}%{_dbdir}/heavycrossbow.csv
install -m 444 db/horn-huge.csv %{buildroot}%{_dbdir}/horn-huge.csv
install -m 444 db/horn-large.csv %{buildroot}%{_dbdir}/horn-large.csv
install -m 444 db/horn-medium.csv %{buildroot}%{_dbdir}/horn-medium.csv
install -m 444 db/horn-small.csv %{buildroot}%{_dbdir}/horn-small.csv
install -m 444 db/javelin.csv %{buildroot}%{_dbdir}/javelin.csv
install -m 444 db/krush.csv %{buildroot}%{_dbdir}/krush.csv
install -m 444 db/lance.csv %{buildroot}%{_dbdir}/lance.csv
install -m 444 db/large.csv %{buildroot}%{_dbdir}/large.csv
install -m 444 db/lightcrossbow.csv %{buildroot}%{_dbdir}/lightcrossbow.csv
install -m 444 db/longbow.csv %{buildroot}%{_dbdir}/longbow.csv
install -m 444 db/mace.csv %{buildroot}%{_dbdir}/mace.csv
install -m 444 db/maingauche.csv %{buildroot}%{_dbdir}/maingauche.csv
install -m 444 db/martialartsstrikesrank1.csv %{buildroot}%{_dbdir}/martialartsstrikesrank1.csv
install -m 444 db/martialartsstrikesrank2.csv %{buildroot}%{_dbdir}/martialartsstrikesrank2.csv
install -m 444 db/martialartsstrikesrank3.csv %{buildroot}%{_dbdir}/martialartsstrikesrank3.csv
install -m 444 db/martialartsstrikesrank4.csv %{buildroot}%{_dbdir}/martialartsstrikesrank4.csv
install -m 444 db/martialartssweepsrank1.csv %{buildroot}%{_dbdir}/martialartssweepsrank1.csv
install -m 444 db/martialartssweepsrank2.csv %{buildroot}%{_dbdir}/martialartssweepsrank2.csv
install -m 444 db/martialartssweepsrank3.csv %{buildroot}%{_dbdir}/martialartssweepsrank3.csv
install -m 444 db/martialartssweepsrank4.csv %{buildroot}%{_dbdir}/martialartssweepsrank4.csv
install -m 444 db/mastrike.csv %{buildroot}%{_dbdir}/mastrike.csv
install -m 444 db/masweep.csv %{buildroot}%{_dbdir}/masweep.csv
install -m 444 db/morningstar.csv %{buildroot}%{_dbdir}/morningstar.csv
install -m 444 db/polearm.csv %{buildroot}%{_dbdir}/polearm.csv
install -m 444 db/puncture.csv %{buildroot}%{_dbdir}/puncture.csv
install -m 444 db/quarterstaff.csv %{buildroot}%{_dbdir}/quarterstaff.csv
install -m 444 db/ram-huge.csv %{buildroot}%{_dbdir}/ram-huge.csv
install -m 444 db/ram-large.csv %{buildroot}%{_dbdir}/ram-large.csv
install -m 444 db/ram-medium.csv %{buildroot}%{_dbdir}/ram-medium.csv
install -m 444 db/ram-small.csv %{buildroot}%{_dbdir}/ram-small.csv
install -m 444 db/rapier.csv %{buildroot}%{_dbdir}/rapier.csv
install -m 444 db/scimitar.csv %{buildroot}%{_dbdir}/scimitar.csv
install -m 444 db/shortbow.csv %{buildroot}%{_dbdir}/shortbow.csv
install -m 444 db/shortsword.csv %{buildroot}%{_dbdir}/shortsword.csv
install -m 444 db/slash.csv %{buildroot}%{_dbdir}/slash.csv
install -m 444 db/sling.csv %{buildroot}%{_dbdir}/sling.csv
install -m 444 db/spear.csv %{buildroot}%{_dbdir}/spear.csv
install -m 444 db/stinger-huge.csv %{buildroot}%{_dbdir}/stinger-huge.csv
install -m 444 db/stinger-large.csv %{buildroot}%{_dbdir}/stinger-large.csv
install -m 444 db/stinger-medium.csv %{buildroot}%{_dbdir}/stinger-medium.csv
install -m 444 db/stinger-small.csv %{buildroot}%{_dbdir}/stinger-small.csv
install -m 444 db/super-large.csv %{buildroot}%{_dbdir}/super-large.csv
install -m 444 db/superlarge.csv %{buildroot}%{_dbdir}/superlarge.csv
install -m 444 db/tiny.csv %{buildroot}%{_dbdir}/tiny.csv
install -m 444 db/tiny-first.csv %{buildroot}%{_dbdir}/tiny-first.csv
install -m 444 db/tiny-fourth.csv %{buildroot}%{_dbdir}/tiny-fourth.csv
install -m 444 db/tiny-second.csv %{buildroot}%{_dbdir}/tiny-second.csv
install -m 444 db/tiny-third.csv %{buildroot}%{_dbdir}/tiny-third.csv
install -m 444 db/two-handedsword.csv %{buildroot}%{_dbdir}/two-handedsword.csv
install -m 444 db/unbalance.csv %{buildroot}%{_dbdir}/unbalance.csv
install -m 444 db/warhammer.csv %{buildroot}%{_dbdir}/warhammer.csv
install -m 444 db/warmattock.csv %{buildroot}%{_dbdir}/warmattock.csv
install -m 444 db/whip.csv %{buildroot}%{_dbdir}/whip.csv

%clean
#rm -rf $RPM_BUILD_ROOT
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %{_htmlconfdir}/
%{_htmlconfdir}/crit.txt
%{_htmlconfdir}/index.php
%{_htmlconfdir}/README
%{_imagedir}/battleaxe.gif
%{_imagedir}/bola.gif
%{_imagedir}/broadsword.gif
%{_imagedir}/club.gif
%{_imagedir}/compositebow.gif
%{_imagedir}/dagger.gif
%{_imagedir}/falchion.gif
%{_imagedir}/fall-huge.gif
%{_imagedir}/fall-large.gif
%{_imagedir}/fall-medium.gif
%{_imagedir}/fall-small.gif
%{_imagedir}/flail.gif
%{_imagedir}/handaxe.gif
%{_imagedir}/heavycrossbow.gif
%{_imagedir}/javelin.gif
%{_imagedir}/lance.gif
%{_imagedir}/lightcrossbow.gif
%{_imagedir}/longbow.gif
%{_imagedir}/mace.gif
%{_imagedir}/maingauche.gif
%{_imagedir}/mastrike1.gif
%{_imagedir}/mastrike2.gif
%{_imagedir}/morningstar.gif
%{_imagedir}/polearm.gif
%{_imagedir}/quarterstaff.gif
%{_imagedir}/rapier.gif
%{_imagedir}/scimitar.gif
%{_imagedir}/shortbow.gif
%{_imagedir}/shortsword.gif
%{_imagedir}/sling.gif
%{_imagedir}/spear.gif
%{_imagedir}/two-handedsword.gif
%{_imagedir}/warhammer.gif
%{_imagedir}/warmattock.gif
%{_imagedir}/whip.gif

%{_dbdir}/battleaxe.csv
%{_dbdir}/beak-huge.csv
%{_dbdir}/beak-large.csv
%{_dbdir}/beak-medium.csv
%{_dbdir}/beak-small.csv
%{_dbdir}/bite-huge.csv
%{_dbdir}/bite-large.csv
%{_dbdir}/bite-medium.csv
%{_dbdir}/bite-small.csv
%{_dbdir}/bola.csv
%{_dbdir}/brawling.csv
%{_dbdir}/brawling-huge.csv
%{_dbdir}/brawling-large.csv
%{_dbdir}/brawling-medium.csv
%{_dbdir}/brawling-small.csv
%{_dbdir}/broadsword.csv
%{_dbdir}/claw-huge.csv
%{_dbdir}/claw-large.csv
%{_dbdir}/claw-medium.csv
%{_dbdir}/claw-small.csv
%{_dbdir}/club.csv
%{_dbdir}/compositebow.csv
%{_dbdir}/dagger.csv
%{_dbdir}/falchion.csv
%{_dbdir}/fall-huge.csv
%{_dbdir}/fall-large.csv
%{_dbdir}/fall-medium.csv
%{_dbdir}/fall-small.csv
%{_dbdir}/flail.csv
%{_dbdir}/fumble.csv
%{_dbdir}/grapple.csv
%{_dbdir}/grapple-huge.csv
%{_dbdir}/grapple-large.csv
%{_dbdir}/grapple-medium.csv
%{_dbdir}/grapple-small.csv
%{_dbdir}/handaxe.csv
%{_dbdir}/handcrossbow.csv
%{_dbdir}/heavycrossbow.csv
%{_dbdir}/horn-huge.csv
%{_dbdir}/horn-large.csv
%{_dbdir}/horn-medium.csv
%{_dbdir}/horn-small.csv
%{_dbdir}/javelin.csv
%{_dbdir}/krush.csv
%{_dbdir}/lance.csv
%{_dbdir}/large.csv
%{_dbdir}/lightcrossbow.csv
%{_dbdir}/longbow.csv
%{_dbdir}/mace.csv
%{_dbdir}/maingauche.csv
%{_dbdir}/martialartsstrikesrank1.csv
%{_dbdir}/martialartsstrikesrank2.csv
%{_dbdir}/martialartsstrikesrank3.csv
%{_dbdir}/martialartsstrikesrank4.csv
%{_dbdir}/martialartssweepsrank1.csv
%{_dbdir}/martialartssweepsrank2.csv
%{_dbdir}/martialartssweepsrank3.csv
%{_dbdir}/martialartssweepsrank4.csv
%{_dbdir}/mastrike.csv
%{_dbdir}/masweep.csv
%{_dbdir}/morningstar.csv
%{_dbdir}/polearm.csv
%{_dbdir}/puncture.csv
%{_dbdir}/quarterstaff.csv
%{_dbdir}/ram-huge.csv
%{_dbdir}/ram-large.csv
%{_dbdir}/ram-medium.csv
%{_dbdir}/ram-small.csv
%{_dbdir}/rapier.csv
%{_dbdir}/scimitar.csv
%{_dbdir}/shortbow.csv
%{_dbdir}/shortsword.csv
%{_dbdir}/slash.csv
%{_dbdir}/sling.csv
%{_dbdir}/spear.csv
%{_dbdir}/stinger-huge.csv
%{_dbdir}/stinger-large.csv
%{_dbdir}/stinger-medium.csv
%{_dbdir}/stinger-small.csv
%{_dbdir}/super-large.csv
%{_dbdir}/superlarge.csv
%{_dbdir}/tiny.csv
%{_dbdir}/tiny-first.csv
%{_dbdir}/tiny-fourth.csv
%{_dbdir}/tiny-second.csv
%{_dbdir}/tiny-third.csv
%{_dbdir}/two-handedsword.csv
%{_dbdir}/unbalance.csv
%{_dbdir}/warhammer.csv
%{_dbdir}/warmattock.csv
%{_dbdir}/whip.csv

%doc



%changelog
* Wed Oct 2 2013 Tym Rehm
- Initial Build
