# Setting up an environment file:

In your local repository, you should store the ChatGPT API key (since it can't be shared publicly) and whatever relevant path names you have to the shared Dropbox. The formatting within the file should be identical to this (in order for the code to be reproducible locally:

```
KEY="put_key_here"
ENDPOINT="https://daz-openai-canada.openai.azure.com/"
DATA_FIGURES="C:\Users\\fuem\Dropbox (Bank of Canada)\TT_trade_relationships\data\statscan_trade"
DATA_CONCORDANCE="C:\Users\\fuem\Dropbox (Bank of Canada)\TT_trade_relationships\data\concordance"
```

# Gitignore

A gitignore file is a plain text file that tells Git what kind of file extensions should be ignored when dealing with version control. These file extensions should be anything you don't want in the remote repo.

