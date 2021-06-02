# Blob Bindings

There are a few interesting things about using an output blob binding.

## Binding Variables

The `path` must be hardcoded with Python, but it can include expressions (<https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-expressions-patterns>). Generally those must be determined from the trigger. In the case of an HttpTrigger, you can use variables that are set by querystring parameter or a JSON body. For instance, in this example...

```json
{
  "scriptFile": "__init__.py",
  "bindings": [
    {
      "name": "outputblob",
      "type": "blob",
      "dataType": "string",
      "path": "output/{filename}.txt",
      "connection": "AzureStorageConnectionAppSetting",
      "direction": "out"
    }
  ]
}
```

...`{filename}` can be set either by...

```bash
curl "http://localhost:7071/api/HelloWorld?name=Peter&filename=peter"
```

...or...

```bash
curl -X POST -d '{ "name": "Jason", "filename": "jason" }' "http://localhost:7071/api/HelloWorld"
```

## HttpTrigger

On a somewhat related note, while the binding type schema says it should be "HttpTrigger", it needs to be "httpTrigger" or it will not work.

```json
{
  "bindings": [
    {
      "type": "httpTrigger",
    },
  ]
}
```