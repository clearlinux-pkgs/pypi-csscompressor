#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-csscompressor
Version  : 0.9.5
Release  : 3
URL      : https://files.pythonhosted.org/packages/f1/2a/8c3ac3d8bc94e6de8d7ae270bb5bc437b210bb9d6d9e46630c98f4abd20c/csscompressor-0.9.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/f1/2a/8c3ac3d8bc94e6de8d7ae270bb5bc437b210bb9d6d9e46630c98f4abd20c/csscompressor-0.9.5.tar.gz
Summary  : A python port of YUI CSS Compressor
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-csscompressor-license = %{version}-%{release}
Requires: pypi-csscompressor-python = %{version}-%{release}
Requires: pypi-csscompressor-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
.. image:: https://travis-ci.org/sprymix/csscompressor.svg?branch=master
:target: https://travis-ci.org/sprymix/csscompressor

%package license
Summary: license components for the pypi-csscompressor package.
Group: Default

%description license
license components for the pypi-csscompressor package.


%package python
Summary: python components for the pypi-csscompressor package.
Group: Default
Requires: pypi-csscompressor-python3 = %{version}-%{release}

%description python
python components for the pypi-csscompressor package.


%package python3
Summary: python3 components for the pypi-csscompressor package.
Group: Default
Requires: python3-core
Provides: pypi(csscompressor)

%description python3
python3 components for the pypi-csscompressor package.


%prep
%setup -q -n csscompressor-0.9.5
cd %{_builddir}/csscompressor-0.9.5
pushd ..
cp -a csscompressor-0.9.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681786193
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-csscompressor
cp %{_builddir}/csscompressor-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-csscompressor/746e7948324fa1a0ab3f173558d50a5204b5374a || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-csscompressor/746e7948324fa1a0ab3f173558d50a5204b5374a

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
