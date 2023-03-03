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
