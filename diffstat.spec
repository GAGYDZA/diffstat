Summary:     Provides diff file statistics
Summary(de): Liefert diff-Datei-Statistiken
Summary(fr): Fournit des statistiques sur les diff�rences de fichiers.
Summary(pl): Umo�liwia robienie statystyk plik�w diff
Summary(tr): diff dosyas� istatistik bilgileri ��kar�r
Name:        diffstat
Version:     1.25
Release:     6
Source:      ftp.clark.net:/pub/dickey/diffstat/%{name}-%{version}.tgz
Group:       Utilities/Text
Copyright:   distributable
Buildroot:   /tmp/%{name}-%{version}-root

%description
'diffstat' provides a number of statistics on a patch generated by diff,
including number of additions, number of removals, and total number of
changes. It can be useful, for example, to find out what changes have been
made to a program, just by feeding the update patch to diffstat.

%description -l de
'diffstat' stellt eine Reihe von statistischen Informationen f�r mit 
Patch erzeugte Diffs bereit, u.a. die Zahl der Einf�gungen, der Streichungen
sowie die Gesamtzahl der �nderungen. So ist es m�glich, die �nderungen an 
einem Programm zu ermitteln, indem man das Update-Patch durch diffstat
durchlaufen l��t. 

%description -l fr
� diffstat � offre de nombreuses statistiques sur un patch g�n�r� par diff,
cela comprend le nombre d'ajouts, de suppressions et le nombre total de
modifications. Il peut �tre utile, par exemple, de retrouver les modifications
faites � un programme en fournissant uniquement le patch de mise � jour �
diffstat.

%description -l pl
Diffstat umo�liwia prowadzenie statystyk pliku (�atki) generowanego 
przez diff. Pakiet ten mo�e by� u�yteczny, na przyk�ad w poszukiwaniu 
zmian, kt�re zosta�y dokonane w jakim� programie. 

%description -l tr
diffstat program�, diff taraf�ndan �retilen bir yama �zerinden toplama
say�s�, ��karma say�s�, toplam de�i�iklik say�s� gibi baz� istatistiksel
bilgiler ��kart�r.

%prep
%setup -q

%build
./configure --prefix=/usr
make CPPFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}

install diffstat $RPM_BUILD_ROOT/usr/bin
install diffstat.1 $RPM_BUILD_ROOT/usr/man/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README CHANGES
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Thu Jul 23 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [1.25-6]
- added pl translation,
- added buildroot support,
- build from non root's account,
- minor changes.

* Mon Apr 27 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
