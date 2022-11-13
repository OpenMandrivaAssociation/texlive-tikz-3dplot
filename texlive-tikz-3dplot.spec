Name:		texlive-tikz-3dplot
Version:	25087
Release:	1
Summary:	Coordinate transformation styles for 3d plotting in TikZ
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-3dplot
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-3dplot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-3dplot.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

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

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
