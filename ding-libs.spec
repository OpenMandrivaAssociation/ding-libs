%define path_utils_version 0.2.1
%define dhash_version 0.4.3
%define collection_version 0.6.2
%define ref_array_version 0.1.4
%define ini_config_version 1.1.0
%define basicobjects_version 0.1.1

%define path_utils_major 1
%define path_utils_libname %mklibname path_utils %{path_utils_major}
%define path_utils_devname %mklibname path_utils -d

%define dhash_major 1
%define dhash_libname %mklibname dhash %{dhash_major}
%define dhash_devname %mklibname dhash -d

%define collection_major 4
%define collection_libname %mklibname collection %{collection_major}
%define collection_devname %mklibname collection -d

%define ref_array_major 1
%define ref_array_libname %mklibname ref_array %{ref_array_major}
%define ref_array_devname %mklibname ref_array -d

%define ini_config_major 5
%define ini_config_libname %mklibname ini_config %{ini_config_major}
%define ini_config_devname %mklibname ini_config -d

%define basicobjects_major 0
%define basicobjects_libname %mklibname basicobjects %{basicobjects_major}
%define basicobjects_devname %mklibname basicobjects -d

Summary:	"Ding is not GLib" assorted utility libraries
Name:		ding-libs
Version:	0.6.0
Release:	1
License:	LGPLv3+
Group:		Development/C
Url:		https://fedorahosted.org/sssd/
Source0:	http://fedorahosted.org/releases/d/i/ding-libs/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	doxygen
BuildRequires:	pkgconfig(check)

%description
A set of helpful libraries used by projects such as SSSD.

#----------------------------------------------------------------------------

%package -n %{path_utils_libname}
Summary:	Filesystem Path Utilities
Version:	%{path_utils_version}
Group:		Development/C

%description -n %{path_utils_libname}
Utility functions to manipulate filesystem pathnames.

%files -n %{path_utils_libname}
%{_libdir}/libpath_utils.so.%{path_utils_major}*

#----------------------------------------------------------------------------

%package -n %{path_utils_devname}
Summary:	Development files for libpath_utils
Version:	%{path_utils_version}
Group:		Development/C
Requires:	%{path_utils_libname} = %{path_utils_version}-%{release}
Provides:	path_utils-devel = %{path_utils_version}-%{release}

%description -n %{path_utils_devname}
Utility functions to manipulate filesystem pathnames.

%files -n %{path_utils_devname}
%doc path_utils/README.path_utils
%doc path_utils/doc/html/
%doc COPYING COPYING.LESSER
%{_libdir}/libpath_utils.so
%{_libdir}/pkgconfig/path_utils.pc
%{_includedir}/path_utils.h

#----------------------------------------------------------------------------

%package -n %{dhash_libname}
Summary:	Dynamic hash table
Version:	%{dhash_version}
Group:		Development/C

%description -n %{dhash_libname}
A hash table which will dynamically resize to achieve optimal storage & access
time properties.

%files -n %{dhash_libname}
%{_libdir}/libdhash.so.%{dhash_major}*

#----------------------------------------------------------------------------

%package -n %{dhash_devname}
Summary:	Development files for libdhash
Version:	%{dhash_version}
Group:		Development/C
Requires:	%{dhash_libname} = %{dhash_version}-%{release}
Provides:	dhash-devel = %{dhash_version}-%{release}

%description -n %{dhash_devname}
A hash table which will dynamically resize to achieve optimal storage & access
time properties.

%files -n %{dhash_devname}
%doc dhash/README.dhash
%doc COPYING COPYING.LESSER
%{_includedir}/dhash.h
%{_libdir}/libdhash.so
%{_libdir}/pkgconfig/dhash.pc

#----------------------------------------------------------------------------

%package -n %{collection_libname}
Summary:	Collection data-type for C
Version:	%{collection_version}
Group:		Development/C

%description -n %{collection_libname}
A data-type to collect data in a hierarchical structure for easy iteration
and serialization.

%files -n %{collection_libname}
%{_libdir}/libcollection.so.%{collection_major}*

#----------------------------------------------------------------------------

%package -n %{collection_devname}
Summary:	Development files for libcollection
Version:	%{collection_version}
Group:		Development/C
Requires:	%{collection_libname} = %{collection_version}-%{release}
Provides:	collection-devel = %{collection_version}-%{release}

%description -n %{collection_devname}
A data-type to collect data in a hierarchical structure for easy iteration
and serialization.

%files -n %{collection_devname}
%doc collection/doc/html/
%doc COPYING COPYING.LESSER
%{_includedir}/collection.h
%{_includedir}/collection_tools.h
%{_includedir}/collection_queue.h
%{_includedir}/collection_stack.h
%{_libdir}/libcollection.so
%{_libdir}/pkgconfig/collection.pc

#----------------------------------------------------------------------------

%package -n %{ref_array_libname}
Summary:	A refcounted array for C
Version:	%{ref_array_version}
Group:		Development/C

%description -n %{ref_array_libname}
A dynamically-growing, reference-counted array.

%files -n %{ref_array_libname}
%{_libdir}/libref_array.so.%{ref_array_major}*

#----------------------------------------------------------------------------

%package -n %{ref_array_devname}
Summary:	Development files for libref_array
Version:	%{ref_array_version}
Group:		Development/C
Requires:	%{ref_array_libname} = %{ref_array_version}-%{release}
Provides:	ref_array-devel = %{ref_array_version}-%{release}

%description -n %{ref_array_devname}
A dynamically-growing, reference-counted array.

%files -n %{ref_array_devname}
%doc refarray/README.ref_array
%doc refarray/doc/html/
%doc COPYING COPYING.LESSER
%{_includedir}/ref_array.h
%{_libdir}/libref_array.so
%{_libdir}/pkgconfig/ref_array.pc

#----------------------------------------------------------------------------

%package -n %{ini_config_libname}
Summary:	INI file parser for C
Version:	%{ini_config_version}
Group:		Development/C

%description -n %{ini_config_libname}
Library to process config files in INI format into a libcollection data
structure.

%files -n %{ini_config_libname}
%{_libdir}/libini_config.so.%{ini_config_major}*

#----------------------------------------------------------------------------

%package -n %{ini_config_devname}
Summary:	Development files for libini_config
Version:	%{ini_config_version}
Group:		Development/C
Requires:	%{ini_config_libname} = %{ini_config_version}-%{release}
Provides:	ini_config-devel = %{ini_config_version}-%{release}

%description -n %{ini_config_devname}
Library to process config files in INI format into a libcollection data
structure.

%files -n %{ini_config_devname}
%doc ini/doc/html/
%doc COPYING COPYING.LESSER
%{_includedir}/ini_config.h
%{_includedir}/ini_configmod.h
%{_includedir}/ini_comment.h
%{_includedir}/ini_configobj.h
%{_includedir}/ini_valueobj.h
%{_libdir}/libini_config.so
%{_libdir}/pkgconfig/ini_config.pc

#----------------------------------------------------------------------------

%package -n %{basicobjects_libname}
Summary:	Basic object types for C
Version:	%{basicobjects_version}
Group:		Development/C

%description -n %{basicobjects_libname}
Basic object types.

%files -n %{basicobjects_libname}
%{_libdir}/libbasicobjects.so.%{basicobjects_major}*

#----------------------------------------------------------------------------

%package -n %{basicobjects_devname}
Summary:	Development files for libbasicobjects
Version:	%{basicobjects_version}
Group:		Development/C
Requires:	%{basicobjects_libname} = %{basicobjects_version}-%{release}
Provides:	basicobjects-devel = %{basicobjects_version}-%{release}

%description -n %{basicobjects_devname}
Basic object types.

%files -n %{basicobjects_devname}
%doc COPYING COPYING.LESSER
%{_includedir}/simplebuffer.h
%{_libdir}/libbasicobjects.so
%{_libdir}/pkgconfig/basicobjects.pc

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure \
	--disable-static

%make
%make docs

%install
rm -fr dhash/examples/{.dirstamp,.deps/.dirstamp,dhash_example.o,dhash_test.o}
%makeinstall_std

# Remove the example files from the output directory
# We will copy them directly from the source directory
# for packaging
rm -f \
    %{buildroot}/usr/share/doc/ding-libs/README.* \
    %{buildroot}/usr/share/doc/ding-libs/examples/dhash_example.c \
    %{buildroot}/usr/share/doc/ding-libs/examples/dhash_test.c

# Remove document install script. RPM is handling this
rm -f */doc/html/installdox

find %{buildroot} -size 0 -delete

%check
%make check
