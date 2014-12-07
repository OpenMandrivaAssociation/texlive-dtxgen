# revision 33681
# category Package
# catalog-ctan /support/dtxgen
# catalog-date 2014-04-25 13:42:50 +0200
# catalog-license gpl
# catalog-version 1.04
Name:		texlive-dtxgen
Version:	1.04
Release:	3
Summary:	Creates a template for a self-extracting .dtx file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/dtxgen
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxgen.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxgen.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-dtxgen.bin = %{EVRD}

%description
The bash script dtxgen creates a template for a self-extracting
.dtx file. It is useful for those who plan to create a new
Documented LaTeX Source (.dtx) file.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/dtxgen
%{_texmfdistdir}/scripts/dtxgen/dtxgen
%doc %{_texmfdistdir}/doc/support/dtxgen/README
%doc %{_texmfdistdir}/doc/support/dtxgen/dtxgen.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/dtxgen/dtxgen dtxgen
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
