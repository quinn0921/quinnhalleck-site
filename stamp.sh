#!/bin/sh
# Bump cache-buster on css/js references. Run before committing.
V=$(date +%Y%m%d%H%M)
sed -i -E "s#(styles\.css|data\.js)(\?v=[0-9]+)?\"#\1?v=$V\"#g" index.html about.html 404.html
