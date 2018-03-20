#! /usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

package=/opt/clover/archive/package
pointer=/opt/clover/package

# nuke old stuff
rm -rf "$package"
rm -f "$pointer"
mkdir -p /opt/clover/archive/

# place 'old version' dummy
echo '#!/usr/bin/env bash' > "$package"
echo 'echo "not installed"' >> "$package"
chmod +x "$package"

# stage a symlink
ln -s "$package" "$pointer"

# clear the log
rm -f /var/tmp/stuff.log

# place the install script
cp $DIR/install_package.py /usr/local/bin/install_package.py
hash -r
