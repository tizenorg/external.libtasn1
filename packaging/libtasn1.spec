Name:       libtasn1
Summary:    This is the ASN.1 library used in GNUTLS
Version:    2.7
Release:    1
Group:      System/Libraries
License:    LGPLv2.1+
URL:        http://www.gnu.org/software/gnutls/download.html
Source0:    http://www.gnu.org/software/gnutls/releases/libtasn1/%{name}-%{version}.tar.gz
Source1001: packaging/libtasn1.manifest 
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  bison


%description
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org



%package tools
Summary:    Some ASN.1 tools
License:    GPLv3+
Group:      Applications/Text
Requires:   %{name} = %{version}-%{release}

%description tools
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org

This package contains tools using the libtasn library.


%package devel
Summary:    Files for development of applications which will use libtasn1
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
This is the ASN.1 library used in GNUTLS.  More up to date information can
be found at http://www.gnu.org/software/gnutls and http://www.gnutls.org

This package contains files for development of applications which will
use libtasn1.



%prep
%setup -q -n %{name}-%{version}


%build
cp %{SOURCE1001} .

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install 


%remove_docs


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%manifest libtasn1.manifest
%defattr(-,root,root,-)
%{_libdir}/*.so.*


%files tools
%manifest libtasn1.manifest
%defattr(-,root,root,-)
%_bindir/asn1*

%files devel
%manifest libtasn1.manifest
%defattr(-,root,root,-)
%_libdir/*.so
%_libdir/pkgconfig/*.pc
%_includedir/*
