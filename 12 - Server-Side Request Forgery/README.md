# Server-Side Request Forgery 
## Intro to Microservices

Many development teams have moved from monolithic web apps to smaller "micro" web services.  

![image](https://user-images.githubusercontent.com/99839823/222589799-18527f6a-b236-4e2d-9654-bb79e8195965.png)

Microservices privde the basic required functionality without dependencies.  

Microservices are often run in containers and must intercommunicate. Containers and their IPs are ephemeral, so they often use DNS for discover. 

Microservices modules expose their functionality by APIs. When an API is running over HTTP or HTTPS, it is called a web service. The two most common types of web services are SOAP and RESTful.  

An API gateway is used to provide a single entry point for the microservices. 

![image](https://user-images.githubusercontent.com/99839823/222592086-d1a0cb1c-2842-4e40-9b0a-321496fbc23f.png)

The microservices usually don't have their own security controls implemented, so bypassing the API gateway can subvert these controls. 

### References: 
https://en.wikipedia.org/wiki/Microservices  
https://en.wikipedia.org/wiki/SOAP  
https://en.wikipedia.org/wiki/Representational_state_transfer#Applied_to_web_services  
https://microservices.io/patterns/apigateway.html  

## Web Service URL Formats

URLs are often parsed with regular expressions. For example, an API gateway might be configured to send any URI that starts with /user to a specific service. 
### References:
https://bestbuyapis.github.io/api-documentation/#create-your-first-query  
https://www.troyhunt.com/your-api-versioning-is-wrong-which-is/  
https://haveibeenpwned.com/API/v3#Authorisation  
https://docs.github.com/en/rest/overview/resources-in-the-rest-api  
https://apiguide.readthedocs.io/en/latest/build_and_publish/use_RESTful_urls.html  

## API Discovery via Verb Tampering   

RESTful APIs often tie functionality to HTTP request methods, or verbs. So a service might have the same URL perform different actions based on the HTTP request's method.

**HTTP Methods**  
- GET: Retrieves data or object
- POST: Creates data or object
- PUT or PATCH: Updates the data of an existing object
- DELETE: Deletes an object

This is all application specific. A RESTful web service might not perform according to the REST standard. 

Regular enumeration tools normally send GET requests. These tools might miss endpoints that do not respond to GET requests. 

### Initial Enumeration

Start with sending an HTTP request to the API gateway with *curl* 
```bash
curl -i http://apigateway:8000
```

The server responds with kong/2.2.1. Looking at google we can see that the admin API runs on port 8001.  

A connnection to this is refused. We'll come back to it later. 

Lets use feroxbuster to enumerate endpoints running on port 8000
```bash
feroxbuster -u http://apigateway:8000 -w /usr/share/wordlists/dirbuster/directory-list-1.0.txt
```

I copy and pasted the results into a text file and used the command below to clean it up.

```bash
sort endpoints.txt | cut -d" " -f1 | cut -d "/" -f2 > endpoints_sorted.txt
```

I get these results in Burp Suite intruder. Sort by status code. There are four 401 forbidden results. 

Look through all the results. There is an X-Powered-By header that indicates it is a Directus application. 

There seems to be three disctinct endpoints: files, users, and render.

### Advanced Enumeration with Verb Tampering
See `route_buster.py`

We get a different result by fuzzing both get and post requests.

Extra mile: put and patch methods are added to the script, the /users/invite endpoint needs an email to make a valid request.
### References:
https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods  
https://konghq.com/kong/  
https://docs.konghq.com/gateway-oss/2.3.x/admin-api/  
https://directus.io/

## Intro to SSRF
SSRF occurs when an attacker can force an application or server to request data or a resource. 
SSRF can be especially effective against microservices, due to bypassing the security controls of a reverse proxy or an API gateway. 

### SSRF Discovery

Always check *url* parameters in an API or web form for an SSRF vulnerability. 