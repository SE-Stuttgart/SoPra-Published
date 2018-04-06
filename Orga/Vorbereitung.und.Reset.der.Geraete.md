# Vorbereitung der Android Geräte

## Allgemeines Vorgehen

Um nach einem Reset des Geräts 
- den kompletten **Setup Wizard** nicht durchlaufen zu müssen, kann in den *build-properties* (`/system/build.prop`) folgende Einstellung dafür verwendet werden:
    ```
    ro.setupwizard.mode=DISABLED
    ```
- die Anmeldung in einem WLAN-Netzwerk optional gemacht werden:
    ```
    ro.setupwizard.wifi_required=false
    ```

Um die Datei editieren zu können muss aber ein angepasster Recovery Modus installiert werden.

Source: http://forum.xda-developers.com/showthread.php?t=1909602

## HTC Nexus 9

## OnePlus 5

Following steps copied from https://twrp.me/devices/oneplus5.html

- You will need the **platform-tools** from the Android SDK on your computer. 
  Find the SDK Only section on the page linked and install the SDK and download only the platform-tools to get adb and fastboot binaries.
- Windows users will need proper drivers installed on your computer. 
  You can try the Naked ADB drivers or the Universal ADB drivers if you don't already have a working driver installed
- On your device, go into *Settings -> About* and find the Build Number and tap on it 7 times to enable developer settings. 
  Press back and go into **Developer Options** and enable **USB debugging**. From your computer, open a **command prompt** and type:
 `adb reboot bootloader`
- You should now be in **fastboot mode**. 
- Unlock bootloader: `fastboot oem unlock`
- [Download](https://eu.dl.twrp.me/cheeseburger/) the correct image file and copy the file into the same folder as your adb and fastboot binaries. Rename the image to `twrp.img` and type:
- `fastboot flash recovery twrp.img`
- Choose recovery mode and select with Power button
- Press **power and volume Down** until twrp starts (**Note many devices will replace your custom recovery automatically during first boot. To prevent this, use Google to find the proper key combo to enter recovery. After typing fastboot reboot, hold the key combo and boot to TWRP. Once TWRP is booted, TWRP will patch the stock ROM to prevent the stock ROM from replacing TWRP. If you don't follow this step, you will have to repeat the install.**)
- Im TWRP Recovery Modus: Mount -> `System` auswählen
- Ändern der *build-properties* (`/system/build.prop`): `adb shell` und dort dann `echo "ro.setupwizard.mode=DISABLED" >> /system/build.prop` eingeben
- Reboot -> System
- On your device, go into *Settings -> About* and find the Build Number and tap on it 7 times to enable developer settings. 
- Press back and go into **Developer Options** and enable **USB debugging**. 
- Press back and go into **Security and Fingerprint** and enable **Untrusted Sources**.
- From your computer, open a **command prompt** `adb reboot recovery`
- Backup inkl. System und Daten erstellen (um gerade gemachte Einstellungen zu sichern)

# Installation von benötigten Apps
- Reset
- `adb install appname.apk`
- `adb reboot recovery`
- Danach wieder Backup erstellen

# Reset (Restore Backup) nach Benutzung

- Gerät herunterfahren
- Gerät im Recovery-Modus (Nexus 5: Power+Volume Down+Volume Up halten, Recovery auswählen, Power drücken, kurz warten, Power+Volume Down drücken) wieder starten
- Im TWRP Recovery `Restore` auswählen