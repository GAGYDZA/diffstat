Summary:	Provides diff file statistics
Summary(de):	Liefert diff-Datei-Statistiken
Summary(fr):	Fournit des statistiques sur les diff�rences de fichiers
Summary(pl):	Umo�liwia robienie statystyk plik�w diff
Summary(tr):	diff dosyas� istatistik bilgileri ��kar�r
Name:		diffstat
Version:	1.28
Release:	1
Copyright:	distributable
Group:		Utilities/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Narz�dzia/Tekst
Source0:	ftp://ftp.clark.net/pub/dickey/diffstat/%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
'diffstat' provides a number of statistics on a patch generated by
diff, including number of additions, number of removals, and total
number of changes. It can be useful, for example, to find out what
changes have been made to a program, just by feeding the update patch
to diffstat.

%description -l de
'diffstat' stellt eine Reihe von statistischen Informationen f�r mit
Patch erzeugte Diffs bereit, u.a. die Zahl der Einf�gungen, der
Streichungen sowie die Gesamtzahl der �nderungen. So ist es m�glich,
die �nderungen an einem Programm zu ermitteln, indem man das
Update-Patch durch diffstat durchlaufen l��t.

%description -l fr
� diffstat � offre de nombreuses statistiques sur un patch g�n�r� par
diff, cela comprend le nombre d'ajouts, de suppressions et le nombre
total de modifications. Il peut �tre utile, par exemple, de retrouver
les modifications faites � un programme en fournissant uniquement le
patch de mise � jour � diffstat.

%description -l pl
Diffstat umo�liwia prowadzenie statystyk pliku (�atki) generowanego
przez diff. Pakiet ten mo�e by� u�yteczny, na przyk�ad w poszukiwaniu
zmian, kt�re zosta�y dokonane w jakim� programie.

%description -l tr
diffstat program�, diff taraf�ndan �retilen bir yama �zerinden toplama
say�s�, ��karma say�s�, toplam de�i�iklik say�s� gibi baz�
istatistiksel bilgiler ��kart�r.

%prep
%setup -q

%build

%configure
%{__make} CPPFLAGS="$RPM_OPT_FLAGS -w" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install diffstat $RPM_BUILD_ROOT%{_bindir}
install diffstat.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,CHANGES}.gz
%attr(755,root,root) %{_bindir}/*

%{_mandir}/man1/*
