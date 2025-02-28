## Question
The Request Management App is used to view all pending requests for each user. It’s a pretty basic website, though I heard they were working on something new.
Anyway, did you know that one of the disgruntled employees shared some company secrets on the Requests Management App, but it’s status was set denied before I could see it. Please find out what it was and spill the tea!

## Solution
I started by looking for anything interesting on the application initiallty, but could not find any information. Then I went to networks and towards `buildManifest.js`.

```js
self.__BUILD_MANIFEST=function(e,r,s){return{__rewrites:{afterFiles:[],beforeFiles:[],fallback:[]},__routerFilterStatic:{numItems:0,errorRate:1e-4,numBits:0,numHashes:null,bitArray:[]},__routerFilterDynamic:{numItems:0,errorRate:1e-4,numBits:e,numHashes:null,bitArray:[]},"/":["static/chunks/pages/index-6413244cd5618b98.js"],"/_error":["static/chunks/pages/_error-fde50cb7f1ab27e0.js"],"/v2-testing":["static/chunks/pages/v2-testing-fb612b495bb99203.js"],sortedPages:["/","/_app","/_error","/v2-testing"]}}(0,0,0),self.__BUILD_MANIFEST_CB&&self.__BUILD_MANIFEST_CB();
```

Inside is the `/v2-testing` endpoint, which reveals a new page with a filter.
Writing the query as `admin' OR 1=1`, it reveals all the entries in the table and we get the flag.
![image](https://github.com/user-attachments/assets/a3e4ecbf-8da1-463b-9b52-043a2b165420)

flag: `KashiCTF{s4m3_old_c0rp0_l1f3_xPZDbQxY}`
