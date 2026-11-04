# Controllable Targeting Pod

An unofficial **Nuclear Option** community mod with manual Scan, native target Follow, fullscreen, optional PiP and game-style IR.

**Experimental release:** Targeting Pod Display **0.1.17** + optional Observer **0.5.7**. Source/build/test verified; **not live-game, hardware or GPU verified**. Offline local cockpit only. Requires exact supported Nuclear Option **0.34.6** and official BepInEx **5.4.23.5 / 5.4.23.6** with bundled Harmony **2.9.0.0**. Game and loader binaries are not included.

## Downloads

- [Recommended matched runtime ZIP](docs/downloads/Observer-0.5.7_TGP-0.1.17-runtime.zip)
- [TargetingPodDisplay.dll](docs/downloads/TargetingPodDisplay.dll)
- [Observer.dll](docs/downloads/Observer.dll)
- [SHA-256 checksums](docs/downloads/SHA256SUMS.txt)
- [Build and test metadata](docs/downloads/BUILD_INFO.json)

For a file on GitHub, open it and use **Download raw file**. The Pages site provides direct download buttons after Pages is enabled.

## Install and first use

1. Close Nuclear Option and back up existing DLLs/configs.
2. Install the supported official BepInEx loader separately if needed.
3. Extract the ZIP and copy `TargetingPodDisplay.dll` into `BepInEx/plugins`. Add the matched `Observer.dll` for the shared settings menu and companion features. Keep exactly one copy of each DLL.
4. Launch the game. Confirm both expected versions in `BepInEx/LogOutput.log`.
5. In a supported offline cockpit, pause with **Esc**, then press **F8** (Observer's default Panel key). Choose **TGP → Settings**, enable TGP, and then assign **Fullscreen** and **ScanFollow** in **TGP → Bindings**.
6. Close the menu, release held controls, resume and test in a safe offline situation.

**TGP starts disabled and its view shortcuts start as `None`.** F6 is not a default. Observer is optional for core TGP: without it, edit `BepInEx/config/local.nuclearoption.targetingpoddisplay.cfg` with the game closed, or use optional ConfigurationManager. Preserve existing configs when updating; do not overwrite with examples.

Use your Fullscreen shortcut to enter/leave the TGP view. In Scan, move the mouse and use the wheel to zoom. Use the game's existing Select/Cancel actions for targets. ScanFollow lets you scan without clearing selections and return to native Follow. IR (GAME) is the game's presentation, not temperature-based thermal sensing. Selection is not seeker lock.

## Detailed guides

- [TGP installation, configuration and features](docs/guides/TARGETING_POD_DISPLAY.md)
- [Matched 0.5.7 / 0.1.17 release notes](docs/guides/OBSERVER_0.5.7_RELEASE.md)
- [Live-game smoke checklist](docs/guides/OBSERVER_0.5.7_SMOKE_TEST.md)
- [TGP smoke checklist](docs/guides/TARGETING_POD_SMOKE_TEST.md)

Flight Hold is an optional experimental Observer feature, disabled by default. An **AUTO HOLD INACTIVE / AIRCRAFT NOT STABILIZED** warning means exit missile fullscreen to fly. It is not a guaranteed autopilot.

## Website

The static site is in [`docs/`](docs/index.html), with all four supplied images labeled as an in-game screenshot, menu layout preview, or HUD illustration. There are no external scripts, analytics or build dependencies.

Enable **Settings → Pages → Deploy from a branch → main → /docs → Save**. The expected project URL is `https://akwaa2545-gif.github.io/Controllable-Targeting-Pod/`; availability must be checked after GitHub finishes deployment.

## Verify the website

Run `python3 -m unittest discover -s tests -v` to check local links, required release information, image paths and release SHA-256 values.

No software license has been selected in this repository. No permission beyond the owner's applicable rights is implied.
