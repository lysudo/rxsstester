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
	usage: getparams [OPTIONS]
	OPTIONS: 
		-f <targetfile> ,contains line separated urls/endpoits
		-o <outputfile> ,write to specific file 
		--silent ,don't show results
```
    
2- rxsstester.py ,which sends all the collected parameters to single or multiple endpoints seprated by **newline**
```
    usage: rxsstester [OPTIONS]

    OPTIONS: 
	    -f / --targetsfile <file> : line separated file contains target endpoits
	    --url : a singl endpoint to test against
	    -p / --paramsfile <file> : line separated file contains list of parameters to test
	    -o <outputfile> ,write to specific file 
	    --silent : sshh ,don't show results
```

**NOTE**: all endpoints should start with proper url schema i.e `http` or `https`


3- install.sh ,which for lazy people like me , it simply makes sympolic links for the above files in `/usr/local/bin/` 

let's say you are in the recon phase and got an intersting endpoint , then what's best than trying all params that the program have been used ? so you do `cat alive_domains | waybackurls | tee -a urls` , **NOW THE TOOL COMES IN HANDY**:

1- use `getparams` to get all the params ,**hence the name :')** ,`getparams -f urls.txt` and it will list all the params ! if you want to save the output then simply use the option `-o <outputfile>` OR just pipe it to `tee` i.e `getparams -f urls.txt | tee params.txt` 

2- start testing for reflections in all endpoints using all params we collected , so let's say you have file called `alive.txt` which have all alive domains/endpoints ,and the previous file `params.txt` , then simply do `rxsstester -f alive.txt -p params.txt` and if you want to test only one domain/endpoit then simply do `rxxtester --url <url> -p <params>
