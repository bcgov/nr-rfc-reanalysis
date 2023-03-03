# Setup

For development follow these instructions to build a jekyll env
https://stackoverflow.com/questions/37720892/you-dont-have-write-permissions-for-the-var-lib-gems-2-3-0-directory

Follow instructions, but do not run with version 3.2, instead use version 3.1.1
Apparently there is a problem with 3.2 (https://www.miskatonic.org/2023/01/02/ruby-jekyll/)

then getting this error:
/home/kjnether/.rbenv/versions/3.1.1/lib/ruby/gems/3.1.0/gems/ffi-1.15.5/lib/ffi.rb:5:in `require': libffi.so.8: cannot open shared object file: No such file or directory - /home/kjnether/.rbenv/versions/3.1.1/lib/ruby/gems/3.1.0/gems/ffi-1.15.5/lib/ffi_c.so (LoadError)

resolution: (note ffi version is listed in error, in this case version 1.15.5)
gem uninstall ffi
gem install ffi -v 1.15.5 -- --disable-system-libffi