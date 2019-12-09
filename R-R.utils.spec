#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-R.utils
Version  : 2.9.2
Release  : 25
URL      : https://cran.r-project.org/src/contrib/R.utils_2.9.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/R.utils_2.9.2.tar.gz
Summary  : Various Programming Utilities
Group    : Development/Tools
License  : LGPL-2.1
Requires: R-R.methodsS3
Requires: R-R.oo
BuildRequires : R-R.methodsS3
BuildRequires : R-R.oo
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n R.utils

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1575907294

%install
export SOURCE_DATE_EPOCH=1575907294
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R.utils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R.utils
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library R.utils
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc R.utils || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/R.utils/DESCRIPTION
/usr/lib64/R/library/R.utils/INDEX
/usr/lib64/R/library/R.utils/Meta/Rd.rds
/usr/lib64/R/library/R.utils/Meta/features.rds
/usr/lib64/R/library/R.utils/Meta/hsearch.rds
/usr/lib64/R/library/R.utils/Meta/links.rds
/usr/lib64/R/library/R.utils/Meta/nsInfo.rds
/usr/lib64/R/library/R.utils/Meta/package.rds
/usr/lib64/R/library/R.utils/NAMESPACE
/usr/lib64/R/library/R.utils/NEWS
/usr/lib64/R/library/R.utils/R/R.utils
/usr/lib64/R/library/R.utils/R/R.utils.rdb
/usr/lib64/R/library/R.utils/R/R.utils.rdx
/usr/lib64/R/library/R.utils/WORDLIST
/usr/lib64/R/library/R.utils/data-ex/HISTORY.LNK
/usr/lib64/R/library/R.utils/data-ex/NEWS.LNK
/usr/lib64/R/library/R.utils/data-ex/exampleVComments.R
/usr/lib64/R/library/R.utils/data-ex/lnkFileWith10BitsInFlag.lnk
/usr/lib64/R/library/R.utils/help/AnIndex
/usr/lib64/R/library/R.utils/help/R.utils.rdb
/usr/lib64/R/library/R.utils/help/R.utils.rdx
/usr/lib64/R/library/R.utils/help/aliases.rds
/usr/lib64/R/library/R.utils/help/paths.rds
/usr/lib64/R/library/R.utils/html/00Index.html
/usr/lib64/R/library/R.utils/html/R.css
/usr/lib64/R/library/R.utils/tests/Arguments-FILES.R
/usr/lib64/R/library/R.utils/tests/FileProgressBar.R
/usr/lib64/R/library/R.utils/tests/GString.R
/usr/lib64/R/library/R.utils/tests/Java.R
/usr/lib64/R/library/R.utils/tests/MultiVerbose.R
/usr/lib64/R/library/R.utils/tests/NullVerbose.R
/usr/lib64/R/library/R.utils/tests/Options.R
/usr/lib64/R/library/R.utils/tests/ProgressBar.R
/usr/lib64/R/library/R.utils/tests/Settings.R
/usr/lib64/R/library/R.utils/tests/System.R
/usr/lib64/R/library/R.utils/tests/TextStatusBar.R
/usr/lib64/R/library/R.utils/tests/VComments.R
/usr/lib64/R/library/R.utils/tests/Verbose.R
/usr/lib64/R/library/R.utils/tests/absolute-relative-paths.R
/usr/lib64/R/library/R.utils/tests/attachLocally.R
/usr/lib64/R/library/R.utils/tests/callHooks.R
/usr/lib64/R/library/R.utils/tests/capitalize.R
/usr/lib64/R/library/R.utils/tests/captureOutput.R
/usr/lib64/R/library/R.utils/tests/cmdArgs.R
/usr/lib64/R/library/R.utils/tests/colClasses.R
/usr/lib64/R/library/R.utils/tests/commandArgs.R
/usr/lib64/R/library/R.utils/tests/compressFile.R
/usr/lib64/R/library/R.utils/tests/compressPDF.R
/usr/lib64/R/library/R.utils/tests/copyRenameFile.R
/usr/lib64/R/library/R.utils/tests/countLines.R
/usr/lib64/R/library/R.utils/tests/cout.R
/usr/lib64/R/library/R.utils/tests/createFileAtomically.R
/usr/lib64/R/library/R.utils/tests/createLink.R
/usr/lib64/R/library/R.utils/tests/dataFrame.R
/usr/lib64/R/library/R.utils/tests/dimNA.R
/usr/lib64/R/library/R.utils/tests/displayCode.R
/usr/lib64/R/library/R.utils/tests/doCall.R
/usr/lib64/R/library/R.utils/tests/eget.R
/usr/lib64/R/library/R.utils/tests/egsub.R
/usr/lib64/R/library/R.utils/tests/env.R
/usr/lib64/R/library/R.utils/tests/extract.array.R
/usr/lib64/R/library/R.utils/tests/fileAccess.R
/usr/lib64/R/library/R.utils/tests/filePath.R
/usr/lib64/R/library/R.utils/tests/findFiles.R
/usr/lib64/R/library/R.utils/tests/findSourceTraceback.R
/usr/lib64/R/library/R.utils/tests/gcDLLs.R
/usr/lib64/R/library/R.utils/tests/gcat.R
/usr/lib64/R/library/R.utils/tests/getOption.R
/usr/lib64/R/library/R.utils/tests/getParent.R
/usr/lib64/R/library/R.utils/tests/hpaste.R
/usr/lib64/R/library/R.utils/tests/insert.R
/usr/lib64/R/library/R.utils/tests/intToHex.R
/usr/lib64/R/library/R.utils/tests/isPackageLoaded.R
/usr/lib64/R/library/R.utils/tests/isReplicated.R
/usr/lib64/R/library/R.utils/tests/isUrl.R
/usr/lib64/R/library/R.utils/tests/isZero.R
/usr/lib64/R/library/R.utils/tests/listDirectory.R
/usr/lib64/R/library/R.utils/tests/loadObject.R
/usr/lib64/R/library/R.utils/tests/loadToEnv.R
/usr/lib64/R/library/R.utils/tests/mkdirs.R
/usr/lib64/R/library/R.utils/tests/mout.R
/usr/lib64/R/library/R.utils/tests/mpager.R
/usr/lib64/R/library/R.utils/tests/nullfile.R
/usr/lib64/R/library/R.utils/tests/parseRepos.R
/usr/lib64/R/library/R.utils/tests/pushBackupFile.R
/usr/lib64/R/library/R.utils/tests/pushTemporaryFile.R
/usr/lib64/R/library/R.utils/tests/queryRCmdCheck.R
/usr/lib64/R/library/R.utils/tests/readBinFragments.R
/usr/lib64/R/library/R.utils/tests/readWindowsShellLink.R
/usr/lib64/R/library/R.utils/tests/readWindowsShortcut.R
/usr/lib64/R/library/R.utils/tests/resample.R
/usr/lib64/R/library/R.utils/tests/seqToHumanReadable.R
/usr/lib64/R/library/R.utils/tests/seqToIntervals.R
/usr/lib64/R/library/R.utils/tests/sourceDirectory.R
/usr/lib64/R/library/R.utils/tests/sourceTo.R
/usr/lib64/R/library/R.utils/tests/splitByPattern.R
/usr/lib64/R/library/R.utils/tests/subplots.R
/usr/lib64/R/library/R.utils/tests/symlinks,dirs.R
/usr/lib64/R/library/R.utils/tests/symlinks,files.R
/usr/lib64/R/library/R.utils/tests/systemR.R
/usr/lib64/R/library/R.utils/tests/tempvar.R
/usr/lib64/R/library/R.utils/tests/tmpfile.R
/usr/lib64/R/library/R.utils/tests/toCamelCase.R
/usr/lib64/R/library/R.utils/tests/touchFile.R
/usr/lib64/R/library/R.utils/tests/use.R
/usr/lib64/R/library/R.utils/tests/useRepos.R
/usr/lib64/R/library/R.utils/tests/whichVector.R
/usr/lib64/R/library/R.utils/tests/withCapture.R
/usr/lib64/R/library/R.utils/tests/withLocale.R
/usr/lib64/R/library/R.utils/tests/withOptions.R
/usr/lib64/R/library/R.utils/tests/withRepos.R
/usr/lib64/R/library/R.utils/tests/withSeed.R
/usr/lib64/R/library/R.utils/tests/withSink.R
/usr/lib64/R/library/R.utils/tests/withTimeout.R
/usr/lib64/R/library/R.utils/tests/wrap.array.R
/usr/lib64/R/library/R.utils/tests/writeDataFrame.R
/usr/lib64/R/library/R.utils/tests/zzz_finalizer_crash.R
