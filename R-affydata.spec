%define		packname	affydata

Summary:	Affymetrix data for demonstration purpose
Name:		R-%{packname}
Version:	1.11.17
Release:	1
License:	GPL v2+
Group:		Applications/Engineering
Source0:	http://www.bioconductor.org/packages/2.11/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	05607d16af3f189340ef6c38c4ec3803
URL:		http://www.bioconductor.org/packages/2.11/data/experiment/html/affydata.html
BuildRequires:	/usr/bin/texi2dvi
BuildRequires:	R
BuildRequires:	R-affy >= 1.23.4
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-affy >= 1.23.4
Suggests:	R-hgu133acdf
Suggests:	R-hgu95av2cdf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Example data sets of a slightly large size. They represent 'real world
examples', unlike the artificial examples included in the package
affy.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL %{packname} -l $RPM_BUILD_ROOT%{_libdir}/R/library

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}/
%doc %{_libdir}/R/library/%{packname}/doc/
%doc %{_libdir}/R/library/%{packname}/html/
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/celfiles/
%{_libdir}/R/library/%{packname}/data/
%{_libdir}/R/library/%{packname}/extracelfiles/
