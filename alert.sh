#!/bin/sh

if [ "$PAM_TYPE" != "close_session" ]; then
    host="`hostname`"
    subject="SSH Login: $SSH_CLIENT  from $PAM_RHOST on $host"
    echo  "$subject"  | python3 /opt/postaciselim/daraltici_alper.py 
fi

