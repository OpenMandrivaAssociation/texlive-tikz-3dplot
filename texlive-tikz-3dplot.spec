%global tl_name tikz-3dplot
%global tl_revision 79461

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Coordinate transformation styles for 3d plotting in TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-3dplot
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-3dplot.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-3dplot.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides straightforward ways to define three-dimensional
coordinate frames through which to plot in TikZ. The user can specify
the orientation of the main coordinate frame, and use standard TikZ
commands and coordinates to render their tikzfigure. A secondary
coordinate frame is provided to allow rotations and translations with
respect to the main coordinate frame. In addition, the package can also
handle plotting user-specified functions in spherical polar coordinates,
where both the radius and fill color can be expressed as parametric
functions of polar angles.

