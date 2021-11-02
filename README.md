# Timestamps

CLI tool to prefix lines of output with a timestamp.

Install by cloning / downloading, then from inside the directory:
    
`sudo pip3 install .`


## Invocation

Pipe input into `timestamps`, e.g.

`long-running-command | timestamps | tee output.txt`


## Arguments

```
usage: timestamps [-h] [-f [FORMAT]] [-t]

optional arguments:
  -h, --help            show this help message and exit
  -f [FORMAT], --format [FORMAT]
                        Timestamp format
  -t, --total           Display total time taken at the end
```
