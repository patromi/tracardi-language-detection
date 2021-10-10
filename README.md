# Language detection Plugin

The purpose of this plugin is  detect language from given string with meaningcloud API

# Configuration

This node requires configuration. You need have a account in meaningcloud to provide your API https://www.meaningcloud.com/

## Message configuration

* string: None, - Enter your message
* key: None, - Enter your Key you can find this on https://www.meaningcloud.com/developer/account/subscriptions
* timeout: 15


## Example of action configuration

```json
{'key': '71d83e0a2ee2b68d57bf2f8fe752d73b',
    'string': """Welcome aboard
        Please pay attention as we demonstrate
        The safety features of this aircraft"""
        }
```



# Input payload

This node does not process input payload.

# Output

This node returns json with yours datas.
