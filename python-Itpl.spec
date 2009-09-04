%define oname   Itpl
%define name    python-%oname
%define version 0
%define release %mkrel 8


Summary:       String interpolation (variable expansion) for Python
Name:          %{name}
Version:       %{version}
Release:       %{release}
Source0:       http://www.lfw.org/python/Itpl.py
License:       Public Domain
Group:         Development/Python
BuildRoot:     %{_tmppath}/%{name}-buildroot
Url:           http://www.python.org/peps/pep-0215.html
BuildRequires: python-devel
BuildArch:     noarch

%description
This is a python module for interpolating strings (that is,
for expanding variables within strings), as described in
PEP 215. This module may become part of the standard library,
or the functionality may be built into Python in the future.

%install
rm -rf $RPM_BUILD_ROOT
install -m644 -D %SOURCE0 $RPM_BUILD_ROOT/%{_libdir}/python%pyver/site-packages/%oname.py
cd $RPM_BUILD_ROOT/%{_libdir}/python%pyver/site-packages/
python -c "import Itpl"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%py_platsitedir/Itpl.py*


