# rxxtester
a simple program for testing reflected xss written in python ..
![My Image](/images/rxsstester.png)


# install

```
$ git clone git@github.com:at-r00t/rxsstester.git
$ cd rxsstester
$ sudo bash install.sh
```


# usage

the directory have three files :

1- getparams.py ,which collecting all GET parameters from a file containing list of endpoints separeted by **newline**
```
    getparams.py <file>
```
    
2- rxsstester.py ,which sends all the collected parameters to single or multiple endpoints seprated by **newline**
```
    for multiple endpoints:
    rxxstester.py <endpoints> <parameters>
    
    for single endpoint:
    rxxstester.py -url <endpoint> <parameter>
```

**NOTE**: all endpoints should start with proper url schema i.e `http` or `https`


3- install.sh ,which for lazy people like me , it simply makes sympolic links for the above files in `/usr/local/bin/` 

let's say you are in the recon phase and got an intersting endpoint , then what's best than trying all params that the program have been used ? so you do `cat alive_domains | waybackurls | tee -a urls` , **NOW THE TOOL COMES IN HANDY**:

1- use `getparams` to get all the params ,**hence the name :')** ,`getparams urls` and it will list all the params ! if you want to save the output then simply pipe it to `tee` i.e `getparams urls | tee params` 

2- start testing for reflections in all endpoints using all params we collected , so let's say you have file called `alive.txt` which have all alive domains/endpoints , then simply do `rxsstester alive.txt <params>` and if you want to test only one domain/endpoit then simply do `rxxtester -url <url> <params>
