Logit
-------

Logit is an easy to use logging wrapper for command line applications.  Logit executes the command passed to it and writes a timestamp, the command executed and its output to a log file.  Logit is useful when you require dead simple timestamp logging added over the output from a command line application. Built using Python 3.4.3, should be compatible with earlier Python 3 releases, definitely compatible wth Python 3.5.1 as well.

## Execute Logit

````shell
python3 logit.py "echo test" -l /custom/log/path.log
cat /custom/log/path.log
````

The default log path ~/logit.log is used if logit is called without any argument.

````shell
python3 logit.py "curl -ks https://bitpay.com/api/rates | python -m json.tool"
````

## Comands
+ Specify log filename "--log" or "-l"
+ Silence logit feedback output "--silent" or "-s"



## Example

````shell
$ ./logit.py "echo test" -l test.log
Executing 'echo test'
Saving output to log test.log
$ cat test.log
2016-01-16 22:35:27.375387 - Executing 'echo test'
test
````


## Crontab

````shell
0 6 * * * python3 logit.py "brew cask update" -l brewupdates.log

````


## Add symlink to bin for easier use

````shell
ln -s path/to/logit.py /usr/local/bin/logit
````

Logit is Open Sourced under an MIT License.