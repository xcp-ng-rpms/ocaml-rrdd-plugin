%global package_speccommit 4035dee79e55154d8fdc4325961ce1926318cbcc
%global package_srccommit v1.9.1

Name:           ocaml-rrdd-plugin
Version: 1.9.1
Release: 2.2%{?xsrel}%{?dist}
Summary:        Plugin library for the XenServer RRD daemon
License:        LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception
URL:            https://github.com/xapi-project/ocaml-rrdd-plugin/
Source0: ocaml-rrdd-plugin-1.9.1.tar.gz
BuildRequires:  ocaml-ocamldoc
BuildRequires:  xs-opam-repo
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  forkexecd-devel
BuildRequires:  ocaml-rrd-transport-devel

%description
Plugin library for the XenServer RRD daemon.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       xs-opam-repo
Requires:       forkexecd-devel%{?_isa}
Requires:       ocaml-xcp-idl-devel%{?_isa}
Requires:       ocaml-rrd-transport-devel%{?_isa}


# XCP-ng patches
Patch1000: ocaml-rrdd-plugin-1.9.1-check-page-count-before-writing-payload.backport.patch

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%global ocaml_dir    %{_opamroot}/ocaml-system
%global ocaml_libdir %{ocaml_dir}/lib
%global ocaml_docdir %{ocaml_dir}/doc
%global build_ocaml_dir %{buildroot}%{ocaml_dir}
%global build_ocaml_libdir %{buildroot}%{ocaml_libdir}
%global build_ocaml_docdir %{buildroot}%{ocaml_docdir}

%prep
%autosetup -p1

%build
make

%install
mkdir -p %{buildroot}/%{_bindir}
make install DESTDIR=%{buildroot}

# this is to make opam happy
mkdir -p %{build_ocaml_libdir}/xapi-rrdd-plugin
touch %{build_ocaml_libdir}/xapi-rrdd-plugin/opam.config

%files
%defattr(-,root,root)
%doc LICENSE
%{ocaml_libdir}/rrdd-plugin
%exclude %{ocaml_libdir}/rrdd-plugin/*.a
%exclude %{ocaml_libdir}/rrdd-plugin/*.cmx
%exclude %{ocaml_libdir}/rrdd-plugin/*.cmxa
%exclude %{ocaml_libdir}/rrdd-plugin/*.cmxs
%exclude %{ocaml_libdir}/rrdd-plugin/*.mli
%exclude %{ocaml_libdir}/rrdd-plugin/*.cmt
%exclude %{ocaml_libdir}/rrdd-plugin/*.cmti

%files devel
%defattr(-,root,root)
%{ocaml_docdir}/*
%{ocaml_libdir}/rrdd-plugin/*.a
%{ocaml_libdir}/rrdd-plugin/*.cmx
%{ocaml_libdir}/rrdd-plugin/*.cmxa
%{ocaml_libdir}/rrdd-plugin/*.cmxs
%{ocaml_libdir}/rrdd-plugin/*.mli

%{ocaml_libdir}/xapi-rrdd-plugin

%changelog
* Thu Apr 27 2023 Benjamin Reis <benjamin.reis@vates.fr> - 1.9.1-2.2
- Add ocaml-rrdd-plugin-1.9.1-check-page-count-before-writing-payload.backport.patch
- This fixes gpumon's "not enough memory" warnings in xcp-rrdd-plugins.log

* Fri Apr 14 2023 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.9.1-2.1
- Sync with hotfix XS82ECU1027
- *** Upstream changelog ***
- * Mon Feb 27 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 1.9.1-2
- - Change license to match the one in the source repo
- * Mon Feb 20 2023 Pau Ruiz Safont <pau.ruizsafont@cloud.com> - 1.9.1-1
- - Same as 1.9.0, koji tooling needed an annotated tag to build

* Wed Oct 12 2022 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.9.0-5.3
- Rebuild for security update synced from XS82ECU1019$

* Wed Aug 17 2022 Gael Duperrey <gduperrey@vates.fr> - 1.9.0-5.2
- Rebuild for updated xapi from XS82ECU1011

* Mon Dec 20 2021 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.9.0-5.1
- Sync with CH 8.2.1
- *** Upstream changelog ***
- * Mon Sep 27 2021 Pau Ruiz Safont <pau.safont@citrix.com> - 1.9.0-5
- - Bump package after xs-opam update
- * Tue Jul 13 2021 Edwin Török <edvin.torok@citrix.com> - 1.9.0-4
- - bump packages after xs-opam update
- * Thu Sep 02 2021 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.9.0-3.3
- - Rebuild for message-switch 1.23.1 from XS82E031

* Tue May 18 2021 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.9.0-3.2
- Rebuild for XS82E002 (updated xs-opam-repo, ocaml-xcp-idl, etc.)

* Thu Nov 05 2020 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.9.0-3.1
- Rebuild for xs-opam-src 6.35.1 from XS82E002

* Fri Aug 23 2019 Edwin Török <edvin.torok@citrix.com> - 1.9.0-2
- bump packages after xs-opam update

* Mon Jul 29 2019 Christian Lindig <christian.lindig@citrix.com> - 1.9.0-1
- Factor out local reporter to allow avoiding the libxenctrl dependency
- Change rpc -> rpclib in opam file

* Tue Jan 29 2019 Christian Lindig <christian.lindig@citrix.com> - 1.8.0-1
- CA-309024 improve SIGTERM signal handling
- CA-309024 Use signal numbers from Sys module

* Wed Jan 23 2019 Christian Lindig <christian.lindig@citrix.com> - 1.7.0-1
- Prepare for Dune 1.6

* Fri Jan 11 2019 Christian Lindig <christian.lindig@citrix.com> - 1.6.0-1
- Use xapi-rrd; rrd is being deprecated.
- Use OCaml 4.07 for travis

* Tue Dec 04 2018 Christian Lindig <christian.lindig@citrix.com> - 1.5.0-1
- Moved from jbuilder to dune and deprecated xcp in favour of xapi-idl.

* Thu Nov 01 2018 Christian Lindig <christian.lindig@citrix.com> - 1.4.0-1
- Update opam files for Opam 2

* Fri May 04 2018 Christian Lindig <christian.lindig@citrix.com> - 1.3.0-1
- CP-26583: Remove API call labels for PPX port of Rrdd
- CP-26583: Remove rpc <-> string conversion for PPX port
- Strip whitespace

* Wed Apr 04 2018 Marcello Seri <marcello.seri@citrix.com> - 1.2.0-6
- Update SPEC file to get rid of rpmbuild warnings

* Tue Feb 13 2018 Christian Lindig <christian.lindig@citrix.com> - 1.2.0-1
- jbuilder runtest: the test was failing to run

* Wed Dec 13 2017 Marcello Seri <marcello.seri@citrix.com> - 1.1.0-1
- Port to jbuilder
- Xstringext -> Astring
- Stdext -> Xapi_stdext submodules

* Mon Mar 13 2017 Marcello Seri <marcello.seri@citrix.com> - 1.0.1-2
- Update OCaml dependencies and build/install script after xs-opam-repo split

* Thu Jun 23 2016 Jon Ludlam <jonathan.ludlam@citrix.com> - 1.0.1-1
- Update to 1.0.1

* Mon Apr 25 2016 Euan Harris <euan.harris@citrix.com> - 1.0.0-1
- Update to 1.0.0

* Tue Jul 8 2014 John Else <john.else@citrix.com> - 0.5.0-1
- Initial package
