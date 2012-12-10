%define path_utils_version 0.2.1
%define dhash_version 0.4.2
%define collection_version 0.6.0
%define ref_array_version 0.1.1
%define ini_config_version 0.6.1

%define path_utils_libname %mklibname path_utils 1
%define path_utils_develname %mklibname path_utils -d
%define dhash_libname %mklibname dhash 1
%define dhash_develname %mklibname dhash -d
%define collection_libname %mklibname collection 2
%define collection_develname %mklibname collection -d
%define ref_array_libname %mklibname ref_array 1
%define ref_array_develname %mklibname ref_array -d
%define ini_config_libname %mklibname ini_config 2
%define ini_config_develname %mklibname ini_config -d

Name: ding-libs
Version: 0.1.2
Release: %mkrel 2
Summary: "Ding is not GLib" assorted utility libraries
Group: Development/C
License: LGPLv3+
URL: http://fedorahosted.org/sssd/
Source0: http://fedorahosted.org/releases/d/i/ding-libs/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}
BuildRequires: doxygen
BuildRequires: check-devel

%description
A set of helpful libraries used by projects such as SSSD.

%package -n %{path_utils_libname}
Summary: Filesystem Path Utilities
Group: Development/C
License: LGPLv3+
Version: %{path_utils_version}

%description -n %{path_utils_libname}
Utility functions to manipulate filesystem pathnames

%package -n %{path_utils_develname}
Summary: Development files for libpath_utils
Group: Development/C
Requires: %{path_utils_libname} = %{path_utils_version}-%{release}
Provides: path_utils-devel = %{path_utils_version}-%{release}
License: LGPLv3+
Version: %{path_utils_version}

%description -n %{path_utils_develname}
Utility functions to manipulate filesystem pathnames


%package -n %{dhash_libname}
Group: Development/C
Summary: Dynamic hash table
License: LGPLv3+
Version: %{dhash_version}

%description -n %{dhash_libname}
A hash table which will dynamically resize to achieve optimal storage & access
time properties

%package -n %{dhash_develname}
Summary: Development files for libdhash
Group: Development/C
Requires: %{dhash_libname} = %{dhash_version}-%{release}
Provides: dhash-devel = %{dhash_version}-%{release}
License: LGPLv3+
Version: %{dhash_version}

%description -n %{dhash_develname}
A hash table which will dynamically resize to achieve optimal storage & access
time properties

%package -n %{collection_libname}
Summary: Collection data-type for C
Group: Development/C
License: LGPLv3+
Version: %{collection_version}

%description -n %{collection_libname}
A data-type to collect data in a hierarchical structure for easy iteration
and serialization

%package -n %{collection_develname}
Summary: Development files for libcollection
Group: Development/C
License: LGPLv3+
Requires: %{collection_libname} = %{collection_version}-%{release}
Provides: collection-devel = %{collection_version}-%{release}
Version: %{collection_version}

%description -n %{collection_develname}
A data-type to collect data in a hierarchical structure for easy iteration
and serialization

%package -n %{ref_array_libname}
Summary: A refcounted array for C
Group: Development/C
License: LGPLv3+
Version: %{ref_array_version}

%description -n %{ref_array_libname}
A dynamically-growing, reference-counted array

%package -n %{ref_array_develname}
Summary: Development files for libref_array
Group: Development/C
Requires: %{ref_array_libname} = %{ref_array_version}-%{release}
Provides: ref_array-devel = %{ref_array_version}-%{release}
License: LGPLv3+
Version: %{ref_array_version}

%description -n %{ref_array_develname}
A dynamically-growing, reference-counted array

%package -n %{ini_config_libname}
Summary: INI file parser for C
Group: Development/C
License: LGPLv3+
Version: %{ini_config_version}

%description -n %{ini_config_libname}
Library to process config files in INI format into a libcollection data
structure

%package -n %{ini_config_develname}
Summary: Development files for libini_config
Group: Development/C
License: LGPLv3+
Requires: %{ini_config_libname} = %{ini_config_version}-%{release}
Provides: ini_config-devel = %{ini_config_version}-%{release}
Version: %{ini_config_version}

%description -n %{ini_config_develname}
Library to process config files in INI format into a libcollection data
structure

%prep
%setup -q

%build
%configure2_5x \
    --disable-static
%make
%make docs

%check
%make check

%install
rm -rf %{buildroot}

%makeinstall_std

# Remove .la files created by libtool
rm -f %{buildroot}/%{_libdir}/*.la

# Remove the example files from the output directory
# We will copy them directly from the source directory
# for packaging
rm -f \
    %{buildroot}/usr/share/doc/ding-libs/README.* \
    %{buildroot}/usr/share/doc/ding-libs/examples/dhash_example.c \
    %{buildroot}/usr/share/doc/ding-libs/examples/dhash_test.c

# Remove document install script. RPM is handling this
rm -f */doc/html/installdox

%clean
rm -rf %{buildroot}

%files -n %{path_utils_libname}
%defattr(-,root,root)
%doc COPYING COPYING.LESSER
%{_libdir}/libpath_utils.so.1
%{_libdir}/libpath_utils.so.1.0.0

%files -n %{path_utils_develname}
%defattr(-,root,root)
%{_includedir}/path_utils.h
%{_libdir}/libpath_utils.so
%{_libdir}/pkgconfig/path_utils.pc
%doc path_utils/README.path_utils
%doc path_utils/doc/html/

%files -n %{dhash_libname}
%defattr(-,root,root)
%doc COPYING COPYING.LESSER
%{_libdir}/libdhash.so.1
%{_libdir}/libdhash.so.1.0.0

%files -n %{dhash_develname}
%defattr(-,root,root)
%{_includedir}/dhash.h
%{_libdir}/libdhash.so
%{_libdir}/pkgconfig/dhash.pc
%doc dhash/README.dhash
%doc dhash/examples/

%files -n %{collection_libname}
%defattr(-,root,root)
%doc COPYING
%doc COPYING.LESSER
%{_libdir}/libcollection.so.2
%{_libdir}/libcollection.so.2.0.0

%files -n %{collection_develname}
%defattr(-,root,root)
%{_includedir}/collection.h
%{_includedir}/collection_tools.h
%{_includedir}/collection_queue.h
%{_includedir}/collection_stack.h
%{_libdir}/libcollection.so
%{_libdir}/pkgconfig/collection.pc
%doc collection/doc/html/

%files -n %{ref_array_libname}
%defattr(-,root,root)
%doc COPYING
%doc COPYING.LESSER
%{_libdir}/libref_array.so.1
%{_libdir}/libref_array.so.1.0.0

%files -n %{ref_array_develname}
%defattr(-,root,root)
%{_includedir}/ref_array.h
%{_libdir}/libref_array.so
%{_libdir}/pkgconfig/ref_array.pc
%doc refarray/README.ref_array
%doc refarray/doc/html/

%files -n %{ini_config_libname}
%defattr(-,root,root)
%doc COPYING
%doc COPYING.LESSER
%{_libdir}/libini_config.so.2
%{_libdir}/libini_config.so.2.0.0

%files -n %{ini_config_develname}
%defattr(-,root,root)
%{_includedir}/ini_config.h
%{_libdir}/libini_config.so
%{_libdir}/pkgconfig/ini_config.pc
%doc ini/doc/html/



%changelog
* Mon Oct 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.2-2mdv2011.0
+ Revision: 589349
- fix some dependencies

* Sat Oct 23 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.2-1mdv2011.0
+ Revision: 587732
- import ding-libs

