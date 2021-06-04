# Testing a Cold Start

Here is the data from some warm executions of the HelloWorld service which writes a message to blob...

__Dataset__: [0.281393, 0.211332, 0.168132, 0.165836, 0.181599, 0.259707, 0.158387, 0.189689, 0.147810, 0.161251, 0.159347, 0.147366, 0.179143, 0.180670, 0.154449, 0.153678, 0.172940, 0.219063] 18 samples
__Range__: 0.147366 - 0.281393
__Average__: 0.182877

Here is the data from some cold executions of the HelloWorld service which writes a message to blob...

__Dataset__: [0.565065, 0.506495, 0.581789, 0.572215, 0.598630, 0.734826, 0.610703, 0.591457, 0.548597, 0.570093, 0.674447, 0.597485, 0.579737, 0.572238, 0.577276, 0.632795, 0.526608, 0.560387] 18 samples
__Range__: 0.506495 - 0.734826
__Average__: 0.588935

As you can see, there is about a 400ms difference with a cold start.

## Raw Data: Warm

```bash
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.117780
       time_connect:  0.140887
    time_appconnect:  0.202079
   time_pretransfer:  0.202104
      time_redirect:  0.000000
 time_starttransfer:  0.281249
                    ----------
         time_total:  0.281393
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.045948
       time_connect:  0.072744
    time_appconnect:  0.126118
   time_pretransfer:  0.126144
      time_redirect:  0.000000
 time_starttransfer:  0.211140
                    ----------
         time_total:  0.211332
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.001517
       time_connect:  0.026143
    time_appconnect:  0.097869
   time_pretransfer:  0.097900
      time_redirect:  0.000000
 time_starttransfer:  0.167865
                    ----------
         time_total:  0.168132
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.001311
       time_connect:  0.026146
    time_appconnect:  0.099402
   time_pretransfer:  0.099436
      time_redirect:  0.000000
 time_starttransfer:  0.165683
                    ----------
         time_total:  0.165836
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.001684
       time_connect:  0.027022
    time_appconnect:  0.102755
   time_pretransfer:  0.102810
      time_redirect:  0.000000
 time_starttransfer:  0.181419
                    ----------
         time_total:  0.181599
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.111440
       time_connect:  0.138001
    time_appconnect:  0.194852
   time_pretransfer:  0.194881
      time_redirect:  0.000000
 time_starttransfer:  0.259575
                    ----------
         time_total:  0.259707
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.001464
       time_connect:  0.027035
    time_appconnect:  0.086778
   time_pretransfer:  0.086814
      time_redirect:  0.000000
 time_starttransfer:  0.158227
                    ----------
         time_total:  0.158387
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.001252
       time_connect:  0.025425
    time_appconnect:  0.096956
   time_pretransfer:  0.096991
      time_redirect:  0.000000
 time_starttransfer:  0.189334
                    ----------
         time_total:  0.189689
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.001749
       time_connect:  0.022939
    time_appconnect:  0.077964
   time_pretransfer:  0.077996
      time_redirect:  0.000000
 time_starttransfer:  0.147647
                    ----------
         time_total:  0.147810
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.001359
       time_connect:  0.024436
    time_appconnect:  0.085086
   time_pretransfer:  0.085114
      time_redirect:  0.000000
 time_starttransfer:  0.161058
                    ----------
         time_total:  0.161251
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.001361
       time_connect:  0.025914
    time_appconnect:  0.086465
   time_pretransfer:  0.086504
      time_redirect:  0.000000
 time_starttransfer:  0.159198
                    ----------
         time_total:  0.159347
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.001503
       time_connect:  0.025717
    time_appconnect:  0.086949
   time_pretransfer:  0.086983
      time_redirect:  0.000000
 time_starttransfer:  0.147215
                    ----------
         time_total:  0.147366
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.001323
       time_connect:  0.026112
    time_appconnect:  0.093090
   time_pretransfer:  0.093137
      time_redirect:  0.000000
 time_starttransfer:  0.178932
                    ----------
         time_total:  0.179143
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.001367
       time_connect:  0.026055
    time_appconnect:  0.105312
   time_pretransfer:  0.105345
      time_redirect:  0.000000
 time_starttransfer:  0.180494
                    ----------
         time_total:  0.180670
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.001356
       time_connect:  0.027083
    time_appconnect:  0.084101
   time_pretransfer:  0.084129
      time_redirect:  0.000000
 time_starttransfer:  0.154280
                    ----------
         time_total:  0.154449
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.001365
       time_connect:  0.028930
    time_appconnect:  0.082397
   time_pretransfer:  0.082425
      time_redirect:  0.000000
 time_starttransfer:  0.153513
                    ----------
         time_total:  0.153678
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.001638
       time_connect:  0.025189
    time_appconnect:  0.077216
   time_pretransfer:  0.077245
      time_redirect:  0.000000
 time_starttransfer:  0.172783
                    ----------
         time_total:  0.172940
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.042970
       time_connect:  0.069462
    time_appconnect:  0.128744
   time_pretransfer:  0.128775
      time_redirect:  0.000000
 time_starttransfer:  0.218887
                    ----------
         time_total:  0.219063
```

## Raw Data: Cold

```bash
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.118966
       time_connect:  0.142805
    time_appconnect:  0.198613
   time_pretransfer:  0.198655
      time_redirect:  0.000000
 time_starttransfer:  0.564891
                    ----------
         time_total:  0.565065
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.048531
       time_connect:  0.070554
    time_appconnect:  0.128920
   time_pretransfer:  0.128950
      time_redirect:  0.000000
 time_starttransfer:  0.504394
                    ----------
         time_total:  0.506495
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.116878
       time_connect:  0.143160
    time_appconnect:  0.201193
   time_pretransfer:  0.201222
      time_redirect:  0.000000
 time_starttransfer:  0.581560
                    ----------
         time_total:  0.581789
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.114666
       time_connect:  0.137797
    time_appconnect:  0.202203
   time_pretransfer:  0.202235
      time_redirect:  0.000000
 time_starttransfer:  0.572087
                    ----------
         time_total:  0.572215
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.113993
       time_connect:  0.140544
    time_appconnect:  0.201354
   time_pretransfer:  0.201383
      time_redirect:  0.000000
 time_starttransfer:  0.598384
                    ----------
         time_total:  0.598630
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.161789
       time_connect:  0.184579
    time_appconnect:  0.256234
   time_pretransfer:  0.256266
      time_redirect:  0.000000
 time_starttransfer:  0.734644
                    ----------
         time_total:  0.734826
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.107703
       time_connect:  0.134557
    time_appconnect:  0.206145
   time_pretransfer:  0.206175
      time_redirect:  0.000000
 time_starttransfer:  0.609259
                    ----------
         time_total:  0.610703
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.116293
       time_connect:  0.142051
    time_appconnect:  0.201556
   time_pretransfer:  0.201593
      time_redirect:  0.000000
 time_starttransfer:  0.588451
                    ----------
         time_total:  0.591457
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.116806
       time_connect:  0.141213
    time_appconnect:  0.206605
   time_pretransfer:  0.206634
      time_redirect:  0.000000
 time_starttransfer:  0.573446
                    ----------
         time_total:  0.574147
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.116272
       time_connect:  0.140152
    time_appconnect:  0.197579
   time_pretransfer:  0.197615
      time_redirect:  0.000000
 time_starttransfer:  0.548442
                    ----------
         time_total:  0.548597
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.108644
       time_connect:  0.128786
    time_appconnect:  0.185600
   time_pretransfer:  0.185628
      time_redirect:  0.000000
 time_starttransfer:  0.568629
                    ----------
         time_total:  0.570093
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.167173
       time_connect:  0.193240
    time_appconnect:  0.259841
   time_pretransfer:  0.259942
      time_redirect:  0.000000
 time_starttransfer:  0.672666
                    ----------
         time_total:  0.674447
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.108899
       time_connect:  0.135239
    time_appconnect:  0.215566
   time_pretransfer:  0.215604
      time_redirect:  0.000000
 time_starttransfer:  0.593861
                    ----------
         time_total:  0.597485
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.102216
       time_connect:  0.128868
    time_appconnect:  0.190465
   time_pretransfer:  0.190498
      time_redirect:  0.000000
 time_starttransfer:  0.579356
                    ----------
         time_total:  0.579737
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.113474
       time_connect:  0.137205
    time_appconnect:  0.192123
   time_pretransfer:  0.192153
      time_redirect:  0.000000
 time_starttransfer:  0.569311
                    ----------
         time_total:  0.572238
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.109096
       time_connect:  0.137578
    time_appconnect:  0.195274
   time_pretransfer:  0.195306
      time_redirect:  0.000000
 time_starttransfer:  0.574840
                    ----------
         time_total:  0.577276
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.162270
       time_connect:  0.189496
    time_appconnect:  0.249560
   time_pretransfer:  0.249590
      time_redirect:  0.000000
 time_starttransfer:  0.630554
                    ----------
         time_total:  0.632795
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.044839
       time_connect:  0.071172
    time_appconnect:  0.135795
   time_pretransfer:  0.135828
      time_redirect:  0.000000
 time_starttransfer:  0.523947
                    ----------
         time_total:  0.526608
plasne@cpe-172-72-161-174 cli-mac-func-proj % az functionapp restart --resource-group pelasne-func --name pelasne-func                       
plasne@cpe-172-72-161-174 cli-mac-func-proj % ./curltime.sh "https://pelasne-func.azurewebsites.net/api/HelloWorld?name=Peter&filename=peter"
      response_code:  200
    time_namelookup:  0.058389
       time_connect:  0.082046
    time_appconnect:  0.138850
   time_pretransfer:  0.138882
      time_redirect:  0.000000
 time_starttransfer:  0.557050
                    ----------
         time_total:  0.560387
```