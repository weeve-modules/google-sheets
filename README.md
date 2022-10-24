# Google Sheets

|                |                                       |
| -------------- | ------------------------------------- |
| Name           | Google Sheets                           |
| Version        | v1.0.0                                |
| DockerHub | [weevenetwork/google-sheets](https://hub.docker.com/r/weevenetwork/google-sheets) |
| Authors        | Jakub Grzelak                    |

- [Google Sheets](#google-sheets)
  - [Description](#description)
  - [Enabling APIs and downloading credentials from Google Cloud](#enabling-apis-and-downloading-credentials-from-google-cloud)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

## Description

Write data to a selected Google Sheet. This module will require enabling Google Drive API and Google Sheets API in Google Cloud Console. Additionally, a Service Account will need to be created within Google Cloud to enable authentication of the user. Later, module settings referring to the credentials should be provided from the JSON file generated in Google Cloud Console. See the next section on setting up your Google Cloud.

## Enabling APIs and downloading credentials from Google Cloud

To connect Google Sheets with this module, the users have to download their credentials in a JSON file. Go to [Google Cloud Platform](https://console.cloud.google.com/getting-started) and then:

* Click on `Select a Project`
* Click on `New Project`
* Write the name of your new project and click on `Create`
* Go to the new project that you have just created
* In the left panel of your project select `APIs & Services` and then select `Library`
* Search for `Google Drive API` and enable it
* Once it is enabled, click on `Create Credentials` on the upper-right corner
* Set API to `Google Drive API`, set accessed data to `Application data` and answer `No, I'm not using them` to the question on using the API with Compute Engine, Kubernetes etc.
* Then, choose a name of your service account and `Create and Continue`
* Select the Role as `Project > Editor`
* After this, open the left panel again, click on `APIs & Services` and select `Credentials`
* In the `Service Account` section click on your **client email**
* Go to the `Keys` section and click on `Add Key > Create new key`
* A JSON file with your credentials will be downloaded to your computer. IMPORTANT: Contents of this JSON file need to be provided as the module settings on the weeve IoT Platform when creating an edge application. Names of the module settings should match those in the JSON file.
* Go to the `APIs & Services` again and search for `Google Sheets API` in the `Library`
* Enable `Google Sheets API` as you previously did for `Google Drive API`

## Environment Variables

### Module Specific

The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables     | type     | Description                                              |
| -------------------- | ------------------------- | -------- | -------------------------------------------------------- |
| Project ID    | PROJECT_ID         | string   | ID of a project in Google Cloud from JSON file.            |
| Private Key ID    | PRIVATE_KEY_ID         | string  | ID of a private key from JSON file.            |
| Private Key    | PRIVATE_KEY         | string  | Private key from JSON file.            |
| Client Email    | CLIENT_EMAIL         | string  | Email of a client set up in Google Cloud from JSON file.            |
| Client ID    | CLIENT_ID         | string  | Client ID set up in Google Cloud from JSON file.            |
| Spreadsheet Title    | SPREADSHEET_TITLE         | string  | Title of the selected spreadsheet.            |
| Worksheet Title    | WORKSHEET_TITLE         | string  | Title of the selected worksheet (page) in the spreadsheet.            |
| Column Headers    | COLUMN_HEADERS         | bool  | Whether the spreadsheet has defined column headers in the first row. If yes, then the module will match data labels with headers when writing data to the spreadsheet.            |


### Set by the weeve Agent on the edge-node

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)  |
| INGRESS_HOST          | string | Host to which data will be received            |
| INGRESS_PORT          | string | Port to which data will be received            |

## Dependencies

```txt
bottle
gspread
oauth2client
```

## Input

Input to this module is:

* JSON body single object, example:

```json
{
   "temperature": 12,
   "device": "Konin-1"
}
```

* batch of JSON body objects, example:

```json
[
    {
        "temperature": 12,
        "device": "Konin-1"
    },
    {
        "temperature": 15,
        "device": "Konin-1"
    }
]
```

## Output

New records written to a selected spreadsheet in Google Sheets.
