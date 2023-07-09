# ERPNext Autocount Integration


## Autocount Integration for ERPNext based on Frappe Framework
Autocount ERPNext custom app is built based on [Autocount Accounting 2.0](https://www.autocountsoft.com/pro-accounting2.html) software. It is built to integrate with ERPNext, act as a connector that allows bidirectional data transfer between Autocount software and ERPNext. With Autocount ERPNext custom app, only one copy of Autocount software is required to install on the main computer, other computers in the same network can read or write data through ERPNext. More information can be found in the [Wiki section](https://github.com/msf4-0/ERPNext-Autocount-Integration/wiki).

![Autocount](https://user-images.githubusercontent.com/69132663/194541410-8b3abf2a-40b3-45bb-b28d-38791b56c686.png)

## Features
1. Stock and Sales categories with related doctypes for users to read or write records.
2. Automatic import data from Autocount 
3. Automatic export data to Autocount


## Installation

### Pre-requisites
1. Autocount Accounting 2.0

- Refers to: https://www.autocountsoft.com/pro-accounting2.html

2. MyAutocount API server and service.

- Download and installation guide is available at: https://github.com/msf4-0/MyAutocount

3. Installed ERPNext which runs on localhost. 

- Installation guide refers to: https://github.com/msf4-0/IRPS-Autocount-Integration

## Setup
By default, the IP address is set to docker localhost with port of `8888` (http://host.docker.internal:8888). If the app is not running on main computer which installs Autocount software, users must configure the settings before using.

1. Go to Autocount Settings.

![image](https://user-images.githubusercontent.com/69132663/194541671-63a472bd-c2ac-435b-b03e-876ed689cc2c.png)

2. Make change to IP address and port.

![image](https://user-images.githubusercontent.com/69132663/194541823-d99f47cc-6578-465f-81c4-e466e5f8af51.png)

- If Autocount is installed on the same computer, the IP address can be set to default: `host.docker.internal`. Otherwise, run `ipconfig` on the main computer, the IP address is the `IPv4 Address` under `Wireless LAN adapter Wi-Fi` section.

- The default port number is 8888. However, users can customize by modifying `settings.json` file of `MyAutocount` program. More information is available at: https://github.com/msf4-0/MyAutocount/wiki/Configuration

3. Press `Test Connection` button to test if the connection is working. Remember to press `Save` to save changes.

4. Restart Docker image by running `docker-compose -p project1 restart` if any issue occurred. 


## Compatibility
Autocount Accounting 2.0 software and MyAutocount API server service only support Windows. However, ERPNext supports all major platforms (Windows, MacOS and Linux) which are compatible with Docker. 


## Important Note
Autocount ERPNext custom app may not validate all data when being exported to Autocount software. The user must have basic knowledge of Autocount to avoid any error. 

## Author
1. [Timothy Wong](https://github.com/Tim1702)

## License
This software is licensed under the [GNU GPLv3 LICENSE](/LICENSE) © [Selangor Human Resource Development Centre](http://www.shrdc.org.my/). 2022.  All Rights Reserved.
