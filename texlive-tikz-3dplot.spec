# revision 23338
# category Package
# catalog-ctan /graphics/pgf/contrib/tikz-3dplot
# catalog-date 2011-06-27 20:46:44 +0200
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-tikz-3dplot
Version:	20110627
Release:	1
Summary:	Coordinate transformation styles for 3d plotting in TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-3dplot
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-3dplot.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-3dplot.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides straightforward ways to define three-
dimensional coordinate frames through which to plot in TikZ.
The user can specify the orientation of the main coordinate
frame, and use standard TikZ commands and coordinates to render
their tikzfigure. A secondary coordinate frame is provided to
allow rotations and translations with respect to the main
coordinate frame. In addition, the package can also handle
plotting user-specified functions in spherical polar
coordinates, where both the radius and fill color can be
expressed as parametric functions of polar angles.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tikz-3dplot/tikz-3dplot.sty
%doc %{_texmfdistdir}/doc/latex/tikz-3dplot/CHANGELOG
%doc %{_texmfdistdir}/doc/latex/tikz-3dplot/README
%doc %{_texmfdistdir}/doc/latex/tikz-3dplot/externalize_images.bat
%doc %{_texmfdistdir}/doc/latex/tikz-3dplot/tikz-3dplot_documentation.pdf
%doc %{_texmfdistdir}/doc/latex/tikz-3dplot/tikz-3dplot_documentation.tex
%doc %{_texmfdistdir}/doc/latex/tikz-3dplot/tikz-3dplot_documentation_figures.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
