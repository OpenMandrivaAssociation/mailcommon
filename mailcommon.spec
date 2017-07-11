%define major 5
%define libname %mklibname KF5MailCommon %{major}
%define devname %mklibname KF5MailCommon -d

Name: mailcommon
Version:	17.04.3
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/applications/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for mail handling
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(KF5Libkdepim)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(Qt5UiTools)
BuildRequires: cmake(KF5MessageCore)
BuildRequires: cmake(KF5MailImporter)
BuildRequires: cmake(KF5Akonadi)
BuildRequires: sasl-devel
BuildRequires: boost-devel
BuildRequires: xsltproc

%description
KDE library for mail handling

%package -n %{libname}
Summary: KDE library for mail handling
Group: System/Libraries
Requires: %{name} = %{EVRD}

%description -n %{libname}
KDE library for mail handling

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libmailcommon

%files -f libmailcommon.lang
%{_sysconfdir}/xdg/mailcommon.categories
%{_sysconfdir}/xdg/mailcommon.renamecategories

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/qt5/plugins/designer/mailcommonwidgets.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
