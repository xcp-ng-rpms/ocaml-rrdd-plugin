%define debug_package %{nil}

Name:           ocaml-rrdd-plugin
Version:        1.3.0
Release:        7%{?dist}
Summary:        Plugin library for the XenServer RRD daemon
License:        LGPL2.1 + OCaml linking exception
URL:            https://github.com/xapi-project/ocaml-rrdd-plugin/
Source0:        https://code.citrite.net/rest/archive/latest/projects/XSU/repos/%{name}/archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz
Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XSU/repos/ocaml-rrdd-plugin/archive?at=v1.3.0&format=tar.gz&prefix=ocaml-rrdd-plugin-1.3.0#/ocaml-rrdd-plugin-1.3.0.tar.gz) = 6b22047f1357f33e7b4467c4db900f2189c09134
BuildRequires:  ocaml-ocamldoc
BuildRequires:  xs-opam-repo
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  forkexecd-devel
BuildRequires:  ocaml-rrd-transport-devel

%global _use_internal_dependency_generator 0
%global __requires_exclude *caml*

%description
Plugin library for the XenServer RRD daemon.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       xs-opam-repo
Requires:       forkexecd-devel%{?_isa}
Requires:       ocaml-xcp-idl-devel%{?_isa}
Requires:       ocaml-rrd-transport-devel%{?_isa}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%global ocaml_dir    /usr/lib/opamroot/system
%global ocaml_libdir %{ocaml_dir}/lib
%global ocaml_docdir %{ocaml_dir}/doc
%global build_ocaml_dir %{buildroot}%{ocaml_dir}
%global build_ocaml_libdir %{buildroot}%{ocaml_libdir}
%global build_ocaml_docdir %{buildroot}%{ocaml_docdir}

%prep
%autosetup -p1

%build
eval $(opam config env --root=/usr/lib/opamroot)
make

%install
eval $(opam config env --root=/usr/lib/opamroot)
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{build_ocaml_libdir}
mkdir -p %{build_ocaml_docdir}

make install OPAM_PREFIX=%{build_ocaml_dir} OPAM_LIBDIR=%{build_ocaml_libdir}

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
