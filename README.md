# rodrigoamaral.net

My personal website. Made with [Pelican](http://getpelican.com)

## Installing

Download project and submodules:

    $ git clone --recursive git@github.com:rodrigoamaral/rodrigoamaral.net.git

Install dependencies in a previously activated virtual environment:

    $ pip install -r requirements.txt

This site needs the `assets` Pelican plugin to allow using the [Webassets](https://github.com/miracle2k/webassets) module to manage assets such as CSS and JS files. The easiest way to make it available to this and to any other project using pelican-plugins, is to clone the entire repo into **the same directory level as the other projects** you may have:

    $ git clone --recursive https://github.com/getpelican/pelican-plugins

Check if it is working properly by building the HTML output and starting the development server (`Ctrl+C` to stop):

    $ make html
    $ pelican --listen --verbose

The site should now be available at `http://localhost:8000`.

## Configuring

TODO

## Publishing

Set environment variables with SSH access credentials to the hosting server:

    export RODRIGOAMARAL_NET_SSH_HOST="the_host_address"
    export RODRIGOAMARAL_NET_SSH_PORT="the_host_port"
    export RODRIGOAMARAL_NET_SSH_USER="the_username"
    export RODRIGOAMARAL_NET_SSH_TARGET_DIR="the/target/dir"