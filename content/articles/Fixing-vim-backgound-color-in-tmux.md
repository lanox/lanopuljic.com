Title: Fixing backgound color in vim  256 colors when in tmux
Date: 06-10-2015 08:59:56 +1000
Category: Linux, MacOS X
Tags: linux,MacOS X, tmux, vim
Author: LanoX
Image:
Email: lanox.post@gmail.com
Summary: Fixing backgound color in vim to use 256 colors when in tmux

This post is meant to help me remmber the issue that i seem to come across when running tmux/vim and support for 256 colors. 

I cant take credit for this as google helped me find the soulution i am just posting it here so that i do not have to search for it when i needed it.

Also searching for things like this wasn't easy.

[PROBLEM]

This is what you would see if you applied the Zenburn color scheme to Vim running under the TERM=xterm-256color environment inside tmux or GNU screen, which itself was attached to the xterm-256color terminal:

INSERT PICTURE HERE

Here, the terminal’s background color bleeds into Vim’s and, depending on the contrast between those two colors, makes Vim use highly unpleasant.

Thankfully, you can fix this by running :set term=screen-256color inside Vim or by relaunching Vim under the TERM=screen-256color environment


[SOLUTION]

One by one, I applied the screen-256color value of each differing setting to a Vim session that was running inside my desired xterm-256color terminal and then pressed Control-L to make Vim redraw itself. Changing ```t_cl``` and ```t_me``` had no effect but, luckily, ```t_ut``` did the trick! :-)

This makes sense because, according to Vim documentation, not only does ```t_ut``` control whether Vim “uses the current background color” to clear the screen (also known as ```Background Color Erase```, or ```BCE``` for short) but it also takes effect only when its value is a non-empty string.

In this case, Vim used BCE in xterm-256color because, under that terminal, ```t_ut``` had value ```y:``` a non-empty string. Conversely, Vim ```did not``` use BCE in screen-256color because under that terminal, ```t_ut``` had no value.

Therefore, the solution is to simply ```clear``` Vim’s ```t_ut``` value if Vim happens to be running inside any 256-color terminal. You can automate this by adding the following snippet to your Vim configuration file:

```
if &term =~ '256color'
  " disable Background Color Erase (BCE) so that color schemes
  " render properly when inside 256-color tmux and GNU screen.
  " see also http://snk.tuxfamily.org/log/vim-256color-bce.html
  set t_ut=
endif
```
