Date: 2012-10-25
Title: MOSH: How I learned to stop worrying and love VPN
Tags: mosh, ssh, vpn
slug: mosh-vpn

# Keep your remote secure connection snappy on the go.

In this, the first entry of the People's Front of Python, I will explain the setup I use for maintaining access to my servers over the VPN in general and, specially, under changing network conditions.

As the title indicates, the main component to achieve a snappy and resilient connection is
[mosh](http://mosh.mit.edu). Mosh is a project of the Massachusetts Institute of Technology that implements a remote terminal over a secure UDP connection with the server. It is designed to be tolerant to connectivity loss while, at the same time, providing smart feedback for your actions, i.e., if you time faster than the connection can get the data through, you see immediately what you type underlined (the underline is removed when the data reaches the remote system).


# Why would I want to use that?

I'm glad that you asked! You're probably thinking: "Here comes a hipster with a shiny new tool when I can currently achieve connectivity loss tolerance by starting a screen/tmux session once I ssh to the server...". Well, you got it, you are right! Errmm... I mean... No, it is not that! What I propose is to keep using ssh and screen (out of habit I've always used screen, I guess I should give tmux a go), but to access both of them in a more convenient way. I'll explain:

Have you ever...
* Found yourself cursing because you had to change from a wired connection to a wireless to attend some meeting or go to the bus and weren't in mood to detach, disconnect, ssh and reattach?
* Used cat on a log that was too big for the network and found yourself begging for mercy to the gods of the internet that your Ctrl-C was allowed to go through to put 'cat' out of its misery?
* Wished that you did not have for the network connection to get feedback on your actions?

If the answer to any of those is a heartily and resounding *YES*, please, keep reading. Otherwise... Me from the past envies you in a non completely healthy way.

# Requirements

You can pull all the requirements into your computer by just installing mosh on both the client and the remote hosts. You can do so by executing(with administrative rights):

* Fedora/RHEL/RHEL derivatives `yum install mosh`

* Debian (on stable you need to have the backports repository enabled) `apt-get install mosh`
* Gentoo `emerge net-misc/mosh`

# Configuration

For a basic use, there is no more configuration needed, you can just execute on the client: `mosh user@remote-ip` and mosh will use ssh to spawn it's server, get the UDP encrypted session key, and connect to the mosh server on the remote.

I recommend though, to spend a bit more time and set up ssh in a nice way to have a more seamless connection. To do that:

    ssh-keygen
    ssh user@remote-ip 'mkdir ~/.ssh; echo '`cat ~/.ssh/id_rsa.pub`' >> ~/.ssh/authorized_keys'
    cat >> ~/.ssh/config << EOF
    Host myremote
        Hostname remote-ip
        User     user
    EOF

Now you can just do: `mosh myremote` and you will be automatically logged in.

# How do I use it?

Usually I run a GNU screen(alright, fine, I'll admit I use byobu on my client not to setup my .screenrc) instance on my client in which I have named tabs for each of the remotes I usually need to work on that will always be accessible as long as the connection allows. If I need several terminals in any of those tabs it gets a little bit more complicated and I generally use a [nested GNU Screen session](https://wiki.archlinux.org/index.php/GNU_Screen#Nested_Screen_Sessions).

Thanks to this, when I leave the office on Thursday to work from home on Friday, the only menial task I have on Friday morning is to connect to the VPN and *all my screen tabs come back to responsiveness without any interaction from my part*.

