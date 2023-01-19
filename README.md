# Mordhau_oSDK_PluginFixer
A simple plugin fix for Mordhau SDK to convert 4.26 plugins into SDK compatible plugins

## Usage:
Drag your 4.26 plugin folders from "UE_4.26\Engine\Plugins\Marketplace" to "MORDHAUEditor\mordhau\Plugins"
Drag this file to "MORDHAUEditor\mordhau\Plugins" and run from this folder

## Method:
It will first grab the installed build ID from the local engine (MORDHAUEditor\InstalledBuild\Windows\Engine)
And run through the configuration files of every folder in the "MORDHAUEditor\mordhau\Plugins"
changing their build ID's to match.

## Credits:

Thank you to Leprechaun003 for the custom icon!

Thank you to Mano for prompting an update!

Thanks to mathewminer.com for this article:
https://matthewminer.com/2020/09/07/run-sourceless-plugins-in-a-custom-unreal-build
