SESSION = $USER

tmux -2 new-session -d -s $SESSION

tmux new-window -t $SESSION:1 -n 'Logs'
tmux split-window -h
tmux select-pane -t 0

tmux send-keys "tail -f  'first.log' C-m
tmux select-pane -t 1

tmux send-keys "tail -f 'second.log' C-m



