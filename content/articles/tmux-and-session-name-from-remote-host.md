Title: TMUX session name changes when ssh to remote host
Date: 06-10-2015 09:36:56 +1000
Category: Linux,tmux
Tags: linux,tmux
Author: LanoX
Image:
Email: lanox.post@gmail.com
Summary: Tmux session name chnages when ssh to remote host

Hi i came across where tmux changes session name automatically from /etc/bashrc from remote host.

Basically whenever  i ssh to virtualbox CentOS 7 my tmux session name will inherit the PS from /etc/bashrc.  
I have tested this by removing everything from /etc/bashrc, then ssh to remote host again and session name will remain the same.

I did notice that ```/etc/bashrc``` sets PS for various things including ```screen*```, which i am sure that is the PS that my tmux inherits.

 If i make any changes to  PROMPT line below and ssh to remote host my tmux session name will change depending on what i change to PROMPT line i made .

```
screen*)
      if [ -e /etc/sysconfig/bash-prompt-screen ]; then
          PROMPT_COMMAND=/etc/sysconfig/bash-prompt-screen
      else
          PROMPT_COMMAND='printf "\033k%s@%s:%s\033\\" "${USER}" "${HOSTNAME%%.*}" "${PWD/#$HOME/~}"'
      fi
      ;;
    *)
      [ -e /etc/sysconfig/bash-prompt-default ] && PROMPT_COMMAND=/etc/sysconfig/bash-prompt-default
      ;;
    esac
  fi
```
Another thing i have find out is if i am running tmux but my TERM is set to xterm-256color instead of screen-256color it will not use PS1 from /etc/bashrc/ which kind of makes sense as /etc/bashrc/ doesn't containing anything for xterm-256color.

So to get aournd this i have set ```export TERM=xterm-256color``` in my .zshrc.

The only reason this seems to work is due to /etc/bashrc not setting any PS prompts in /etc/bashrc on remote host.

Note: if you do this you will need to apply vim patch in this post [ADD LINK to VIM POST]


