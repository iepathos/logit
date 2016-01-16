Logit is an easy to use Logging Wrapper for Commandline Applications
-----------------------

Built using Python 3.4.3, should be compatible with other Python 3 releases.

## Execute Logit

./logit.py "echo test" -l /custom/log/path.log

The default log path ~/logit.log is used if logit is called without any argument.

./logit.py "curl -ks https://bitpay.com/api/rates | python -m json.tool"


## Read Log
cat ~/logit.log
