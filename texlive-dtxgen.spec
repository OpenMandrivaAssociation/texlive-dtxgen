%global tl_name dtxgen
%global tl_revision 75946
%global tl_bin_links dtxgen:%{_texmfdistdir}/scripts/dtxgen/dtxgen

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.09
Release:	%{tl_revision}.1
Summary:	Creates a template for a self-extracting .dtx file
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/dtxgen
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxgen.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dtxgen.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(dtxgen.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
The bash script dtxgen creates a template for a self-extracting .dtx
file. It is useful for those who plan to create a new Documented LaTeX
Source (.dtx) file.

