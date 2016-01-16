Logit
-------

Logit is an easy to use logging wrapper for command line applications.  Built using Python 3.4.3, should be compatible with other Python 3 releases, but not yet tested with.

## Execute Logit

./logit.py "echo test" -l /custom/log/path.log
cat /custom/log/path.log


The default log path ~/logit.log is used if logit is called without any argument.

./logit.py "curl -ks https://bitpay.com/api/rates | python -m json.tool"


## Read Log
cat ~/logit.log



## Example

````shell
$ ./logit.py "echo test" -l test.log
Executing 'echo test'
Saving output to log test.log
$ cat test.log
2016-01-16 22:35:27.375387 - Executing 'echo test'
test
````