%define major 6
%define libname %mklibname KPim6MailCommon
%define devname %mklibname KPim6MailCommon -d

Name: plasma6-mailcommon
Version:	24.01.80
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/mailcommon-%{version}.tar.xz
Summary: KDE library for mail handling
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6UiPlugin)
BuildRequires: cmake(Qt6UiTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6SyntaxHighlighting)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6AkonadiMime)
BuildRequires: cmake(KPim6MailImporter)
BuildRequires: cmake(KPim6MailTransport)
BuildRequires: cmake(KPim6MessageComposer)
BuildRequires: cmake(KPim6MessageCore)
BuildRequires: cmake(KPim6MessageViewer)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KPim6PimCommon)
BuildRequires: cmake(KPim6TemplateParser)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(Phonon4Qt6)
BuildRequires: cmake(QGpgme)
BuildRequires: cmake(Gpgmepp)
BuildRequires: sasl-devel
BuildRequires: boost-devel
BuildRequires: xsltproc
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt6-qttools-assistant

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
%autosetup -p1 -n mailcommon-%{version}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libmailcommon

%files -f libmailcommon.lang
%{_datadir}/qlogging-categories6/mailcommon.categories
%{_datadir}/qlogging-categories6/mailcommon.renamecategories

%files -n %{libname}
%{_libdir}/*.so.*
%{_libdir}/qt6/plugins/designer/mailcommon6widgets.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
