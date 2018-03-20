#!/usr/bin/python
import os
import stat

# typically this would be versioned so it doesn't clobber old ones
package = '/opt/clover/archive/package'

# this is what we run, it points at the current archived version
pointer = '/opt/clover/package'

# create the package
def write_file(fname, installed):
    if installed:
        with open(fname, 'w') as f:
            f.write("""#!/usr/bin/env bash
                echo 'package installed'""")
    else:
        with open(fname, 'w') as f:
            f.write("""#!/usr/bin/env bash
                echo 'no package installed'""")

try:
    # remove old symlink
    try:
        os.remove(pointer)
    except OSError:
        pass

    # place package
    write_file(package, installed=True)

    # chmod +x
    st = os.stat(package)
    os.chmod(package, st.st_mode | stat.S_IEXEC)

    # add new symlink
    os.symlink(package, pointer)

except Exception as ex:
    print(ex)
    write_file(package, installed=False)
