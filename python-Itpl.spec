%define oname   Itpl
%define name    python-%oname
%define version 0
%define release 10


Summary:       String interpolation (variable expansion) for Python
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       http://www.lfw.org/python/Itpl.py
License:       Public Domain
Group:         Development/Python
Url:           http://www.python.org/peps/pep-0215.html
BuildRequires: python-devel
BuildArch:     noarch

%description
This is a python module for interpolating strings (that is,
for expanding variables within strings), as described in
PEP 215. This module may become part of the standard library,
or the functionality may be built into Python in the future.

%install
install -m644 -D %SOURCE0 $RPM_BUILD_ROOT/%{_libdir}/python%{py_ver}/site-packages/%oname.py
cd $RPM_BUILD_ROOT/%{_libdir}/python%{py_ver}/site-packages/
python -c "import Itpl"

%files
%defattr(-,root,root)
%py_platsitedir/Itpl.py*




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0-8mdv2010.0
+ Revision: 430847
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0-7mdv2009.0
+ Revision: 259649
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0-6mdv2009.0
+ Revision: 247490
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0-4mdv2008.1
+ Revision: 136450
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 31 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0-4mdv2007.0
+ Revision: 115770
- Rebuild against new python
- Import python-Itpl

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0-3mdk
- Rebuild for new python

