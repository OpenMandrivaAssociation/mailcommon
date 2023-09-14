%define major 5
%define oldlibname %mklibname KF5MailCommon 5
%define libname %mklibname KPim5MailCommon
%define olddevname %mklibname KF5MailCommon -d
%define devname %mklibname KPim5MailCommon -d

Name: mailcommon
Version:	23.08.1
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Release:	1
Source0: http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Summary: KDE library for mail handling
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Test)
BuildRequires: cmake(Qt5UiTools)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ItemModels)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5WindowSystem)
BuildRequires: cmake(KF5XmlGui)
BuildRequires: cmake(KF5DBusAddons)
BuildRequires: cmake(KF5SyntaxHighlighting)
BuildRequires: cmake(KPim5Akonadi)
BuildRequires: cmake(KPim5AkonadiMime)
BuildRequires: cmake(KPim5MailImporter)
BuildRequires: cmake(KPim5MailTransport)
BuildRequires: cmake(KPim5MessageComposer)
BuildRequires: cmake(KPim5MessageCore)
BuildRequires: cmake(KPim5MessageViewer)
BuildRequires: cmake(KPim5Mime)
BuildRequires: cmake(KPim5PimCommon)
BuildRequires: cmake(KPim5TemplateParser)
BuildRequires: cmake(KPim5Libkdepim)
BuildRequires: cmake(Phonon4Qt5)
BuildRequires: cmake(KF5DesignerPlugin)
BuildRequires: cmake(QGpgme)
BuildRequires: cmake(Gpgmepp)
BuildRequires: sasl-devel
BuildRequires: boost-devel
BuildRequires: xsltproc
# For QCH format docs
BuildRequires: doxygen
BuildRequires: qt5-assistant

%description
KDE library for mail handling

%package -n %{libname}
Summary: KDE library for mail handling
Group: System/Libraries
Requires: %{name} = %{EVRD}
%rename %{oldlibname}

%description -n %{libname}
KDE library for mail handling

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
%rename %{olddevname}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang libmailcommon

%files -f libmailcommon.lang
%{_datadir}/qlogging-categories5/mailcommon.categories
%{_datadir}/qlogging-categories5/mailcommon.renamecategories

%files -n %{libname}
%{_libdir}/*.so.%{major}*
%{_libdir}/qt5/plugins/designer/mailcommon5widgets.so

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/*
%{_libdir}/qt5/mkspecs/modules/*.pri
%doc %{_docdir}/qt5/*.{tags,qch}
