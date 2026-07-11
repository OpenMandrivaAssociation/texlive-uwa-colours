%global tl_name uwa-colours
%global tl_revision 60443

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.0
Release:	%{tl_revision}.1
Summary:	The colour palette of The University of Western Australia
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/uwa-colours
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-colours.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-colours.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-colours.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package uses the xcolor package to define macros for the colour
palette of The University of Western Australia.

