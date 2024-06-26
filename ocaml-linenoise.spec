Name:           ocaml-linenoise
Version:        1.5
Release:        %autorelease
Summary:        Self-contained OCaml bindings to linenoise, easy high level readline functionality in OCaml

License:        BSD
URL:            https://github.com/ocaml-community/%{name}
Source0:        https://github.com/ocaml-community/%{name}/archive/v%{version}/linenoise-v%{version}.tar.gz

BuildRequires:  ocaml >= 4.08.1
BuildRequires:  ocaml-dune >= 2.7
BuildRequires:  ocaml-odoc

%description
Self-contained OCaml bindings to linenoise, easy high level readline functionality in OCaml

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%autosetup -n ocaml-linenoise-%{version} -p1

%build
%dune_build

%install
%dune_install

%check
%dune_check

%files -f .ofiles
%doc README.md CHANGES.md

%files devel -f .ofiles-devel

%changelog
%autochangelog
