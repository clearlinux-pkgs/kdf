#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kdf
Version  : 22.04.0
Release  : 38
URL      : https://download.kde.org/stable/release-service/22.04.0/src/kdf-22.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.04.0/src/kdf-22.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.04.0/src/kdf-22.04.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0
Requires: kdf-bin = %{version}-%{release}
Requires: kdf-data = %{version}-%{release}
Requires: kdf-lib = %{version}-%{release}
Requires: kdf-license = %{version}-%{release}
Requires: kdf-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdoctools-dev

%description
No detailed description available

%package bin
Summary: bin components for the kdf package.
Group: Binaries
Requires: kdf-data = %{version}-%{release}
Requires: kdf-license = %{version}-%{release}

%description bin
bin components for the kdf package.


%package data
Summary: data components for the kdf package.
Group: Data

%description data
data components for the kdf package.


%package doc
Summary: doc components for the kdf package.
Group: Documentation

%description doc
doc components for the kdf package.


%package lib
Summary: lib components for the kdf package.
Group: Libraries
Requires: kdf-data = %{version}-%{release}
Requires: kdf-license = %{version}-%{release}

%description lib
lib components for the kdf package.


%package license
Summary: license components for the kdf package.
Group: Default

%description license
license components for the kdf package.


%package locales
Summary: locales components for the kdf package.
Group: Default

%description locales
locales components for the kdf package.


%prep
%setup -q -n kdf-22.04.0
cd %{_builddir}/kdf-22.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1650675960
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1650675960
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kdf
cp %{_builddir}/kdf-22.04.0/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kdf/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
cp %{_builddir}/kdf-22.04.0/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kdf/3e8971c6c5f16674958913a94a36b1ea7a00ac46
pushd clr-build
%make_install
popd
%find_lang kdf

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kdf
/usr/bin/kwikdisk

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kdf.desktop
/usr/share/applications/org.kde.kwikdisk.desktop
/usr/share/icons/hicolor/128x128/apps/kdf.png
/usr/share/icons/hicolor/128x128/apps/kwikdisk.png
/usr/share/icons/hicolor/16x16/apps/kcmdf.png
/usr/share/icons/hicolor/16x16/apps/kdf.png
/usr/share/icons/hicolor/16x16/apps/kwikdisk.png
/usr/share/icons/hicolor/22x22/apps/kcmdf.png
/usr/share/icons/hicolor/22x22/apps/kdf.png
/usr/share/icons/hicolor/22x22/apps/kwikdisk.png
/usr/share/icons/hicolor/32x32/apps/kcmdf.png
/usr/share/icons/hicolor/32x32/apps/kdf.png
/usr/share/icons/hicolor/32x32/apps/kwikdisk.png
/usr/share/icons/hicolor/48x48/apps/kdf.png
/usr/share/icons/hicolor/48x48/apps/kwikdisk.png
/usr/share/icons/hicolor/64x64/apps/kdf.png
/usr/share/icons/hicolor/64x64/apps/kwikdisk.png
/usr/share/kservices5/kcmdf.desktop
/usr/share/kxmlgui5/kdf/kdfui.rc
/usr/share/metainfo/org.kde.kdf.appdata.xml
/usr/share/qlogging-categories5/kdf.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/kcontrol/blockdevices/index.cache.bz2
/usr/share/doc/HTML/ca/kcontrol/blockdevices/index.docbook
/usr/share/doc/HTML/ca/kdf/index.cache.bz2
/usr/share/doc/HTML/ca/kdf/index.docbook
/usr/share/doc/HTML/de/kcontrol/blockdevices/index.cache.bz2
/usr/share/doc/HTML/de/kcontrol/blockdevices/index.docbook
/usr/share/doc/HTML/de/kdf/index.cache.bz2
/usr/share/doc/HTML/de/kdf/index.docbook
/usr/share/doc/HTML/de/kdf/kdf.png
/usr/share/doc/HTML/de/kdf/kdf_config.png
/usr/share/doc/HTML/en/kcontrol/blockdevices/index.cache.bz2
/usr/share/doc/HTML/en/kcontrol/blockdevices/index.docbook
/usr/share/doc/HTML/en/kdf/index.cache.bz2
/usr/share/doc/HTML/en/kdf/index.docbook
/usr/share/doc/HTML/en/kdf/kdf.png
/usr/share/doc/HTML/en/kdf/kdf_config.png
/usr/share/doc/HTML/es/kcontrol/blockdevices/index.cache.bz2
/usr/share/doc/HTML/es/kcontrol/blockdevices/index.docbook
/usr/share/doc/HTML/es/kdf/index.cache.bz2
/usr/share/doc/HTML/es/kdf/index.docbook
/usr/share/doc/HTML/et/kdf/index.cache.bz2
/usr/share/doc/HTML/et/kdf/index.docbook
/usr/share/doc/HTML/fr/kdf/index.cache.bz2
/usr/share/doc/HTML/fr/kdf/index.docbook
/usr/share/doc/HTML/fr/kdf/kdf.png
/usr/share/doc/HTML/fr/kdf/kdf_config.png
/usr/share/doc/HTML/gl/kdf/index.cache.bz2
/usr/share/doc/HTML/gl/kdf/index.docbook
/usr/share/doc/HTML/it/kcontrol/blockdevices/index.cache.bz2
/usr/share/doc/HTML/it/kcontrol/blockdevices/index.docbook
/usr/share/doc/HTML/it/kdf/index.cache.bz2
/usr/share/doc/HTML/it/kdf/index.docbook
/usr/share/doc/HTML/ko/kcontrol/blockdevices/index.cache.bz2
/usr/share/doc/HTML/ko/kcontrol/blockdevices/index.docbook
/usr/share/doc/HTML/nl/kcontrol/blockdevices/index.cache.bz2
/usr/share/doc/HTML/nl/kcontrol/blockdevices/index.docbook
/usr/share/doc/HTML/nl/kdf/index.cache.bz2
/usr/share/doc/HTML/nl/kdf/index.docbook
/usr/share/doc/HTML/nl/kdf/kdf.png
/usr/share/doc/HTML/nl/kdf/kdf_config.png
/usr/share/doc/HTML/pt/kcontrol/blockdevices/index.cache.bz2
/usr/share/doc/HTML/pt/kcontrol/blockdevices/index.docbook
/usr/share/doc/HTML/pt/kdf/index.cache.bz2
/usr/share/doc/HTML/pt/kdf/index.docbook
/usr/share/doc/HTML/pt_BR/kcontrol/blockdevices/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kcontrol/blockdevices/index.docbook
/usr/share/doc/HTML/pt_BR/kdf/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kdf/index.docbook
/usr/share/doc/HTML/pt_BR/kdf/kdf.png
/usr/share/doc/HTML/pt_BR/kdf/kdf_config.png
/usr/share/doc/HTML/ru/kcontrol/blockdevices/index.cache.bz2
/usr/share/doc/HTML/ru/kcontrol/blockdevices/index.docbook
/usr/share/doc/HTML/ru/kdf/index.cache.bz2
/usr/share/doc/HTML/ru/kdf/index.docbook
/usr/share/doc/HTML/sr/kcontrol/blockdevices/index.cache.bz2
/usr/share/doc/HTML/sr/kcontrol/blockdevices/index.docbook
/usr/share/doc/HTML/sr/kdf/index.cache.bz2
/usr/share/doc/HTML/sr/kdf/index.docbook
/usr/share/doc/HTML/sv/kcontrol/blockdevices/index.cache.bz2
/usr/share/doc/HTML/sv/kcontrol/blockdevices/index.docbook
/usr/share/doc/HTML/sv/kdf/index.cache.bz2
/usr/share/doc/HTML/sv/kdf/index.docbook
/usr/share/doc/HTML/sv/kdf/kdf.png
/usr/share/doc/HTML/sv/kdf/kdf_config.png
/usr/share/doc/HTML/uk/kcontrol/blockdevices/index.cache.bz2
/usr/share/doc/HTML/uk/kcontrol/blockdevices/index.docbook
/usr/share/doc/HTML/uk/kdf/index.cache.bz2
/usr/share/doc/HTML/uk/kdf/index.docbook
/usr/share/doc/HTML/uk/kdf/kdf.png
/usr/share/doc/HTML/uk/kdf/kdf_config.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkdfprivate.so.22
/usr/lib64/libkdfprivate.so.22.04.0
/usr/lib64/qt5/plugins/libkcm_kdf.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kdf/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kdf/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files locales -f kdf.lang
%defattr(-,root,root,-)

