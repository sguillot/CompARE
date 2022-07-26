#/bin/sh

# version number
#VER=0.2

# Local folder where CompARE is installed:
LIB=$HOME/mylib
CompARE=$LIB/CompARE

echo ""
echo ">> -----------------------------------"
echo ">> creates a local copy of CompARE"
echo ">> Home path: $HOME"
echo ">> Local folder: $LIB"
echo ">> -----------------------------------"
echo ""

echo ">> Install the library CompARE"

echo ""
echo ">> mkdir -p $LIB"
mkdir -p $LIB

echo ""
echo ">> mkdir -p $CompARE"
mkdir -p $CompARE

echo ""
echo ">> cp -R data $CompARE"
cp -R data $CompARE

echo ""
echo ">> cp -R scripts $CompARE"
cp -R scripts $CompARE

echo ""
echo ">> cp README.md $CompARE"
cp README.md $CompARE

echo ""
echo ">> cp requirements $CompARE"
cp requirements.txt $CompARE



