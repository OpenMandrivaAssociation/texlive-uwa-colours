Name:		texlive-uwa-colours
Version:	60443
Release:	2
Summary:	The colour palette of The University of Western Australia
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/uwa-colours
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-colours.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-colours.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uwa-colours.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package uses the xcolor package to define macros for the
colour palette of The University of Western Australia.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/uwa-colours
%{_texmfdistdir}/tex/latex/uwa-colours
%doc %{_texmfdistdir}/doc/latex/uwa-colours

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
