<div align="center">

# CONTROLLABLE TARGETING POD

### A closer view of Nuclear Option.

Manual sensor scanning · Native target following · Fullscreen & PiP · Game-style IR

**TGP 0.1.17** &nbsp; • &nbsp; **Nuclear Option 0.34.6** &nbsp; • &nbsp; **Experimental**

### [↓ Download TargetingPodDisplay.dll](https://raw.githubusercontent.com/akwaa2545-gif/Controllable-Targeting-Pod/main/docs/downloads/TargetingPodDisplay.dll)

[Install](#installation) &nbsp; / &nbsp; [Configure](#first-time-setup) &nbsp; / &nbsp; [Controls](#controls) &nbsp; / &nbsp; [Troubleshooting](#troubleshooting)

<img src="docs/assets/tgp-in-game.jpg" alt="In-game TGP view over an airfield with green Scan symbology, red hostile diamonds and white selection brackets" width="100%">

<sub>User-provided in-game screenshot. This image is not validation of the current experimental build.</sub>

</div>

> [!IMPORTANT]
> **TGP-only download.** This repository distributes `TargetingPodDisplay.dll` only. Observer is a separate, optional companion and is **not included**. The mod is build/test verified, but **not live-game, hardware or GPU verified**. Use an offline local cockpit and back up your existing files.

## What it does

| Sensor control | Viewing options | Display information |
| :--- | :--- | :--- |
| Move the pod in **Scan**, or **Follow** native selected targets | Direct **fullscreen**, optional **picture-in-picture** and cockpit display options | Green HUD symbology, known-contact markers and native selected-target information |
| Hold a valid terrain point with **AREA** ground stabilization | Switch the owned camera between **COLOR** and **IR (GAME)** | Keep camera view state within the same valid aircraft/session |

IR (GAME) uses the game's presentation, not temperature-based thermal sensing. Contact markers and selection brackets do not prove optical visibility or weapon lock. TGP by itself does not fly or stabilize the aircraft.

## Download

| File | Version | Purpose |
| :--- | :--- | :--- |
| **[TargetingPodDisplay.dll](https://raw.githubusercontent.com/akwaa2545-gif/Controllable-Targeting-Pod/main/docs/downloads/TargetingPodDisplay.dll)** | **0.1.17** | The standalone TGP mod |
| [SHA256SUMS.txt](docs/downloads/SHA256SUMS.txt) | Same DLL | Verify the download |
| [Build information](docs/downloads/BUILD_INFO.json) | Same DLL | Provenance and verification limits |

<details>
<summary><strong>Check the DLL's SHA-256</strong></summary>

Expected:

```text
5e8ca78f9a11c90539eef3193a637d4e864ca1b62f39a0012fe193be0403f7b5
```

In Windows PowerShell, from the folder containing your download:

```powershell
Get-FileHash .\TargetingPodDisplay.dll -Algorithm SHA256
```

The hash should match exactly. The filename alone does not identify a build.

</details>

## Requirements

| Component | Supported version / context |
| :--- | :--- |
| Game | **Nuclear Option 0.34.6** on Windows |
| Mod loader | Official **BepInEx 5.4.23.5 or 5.4.23.6**, including bundled **Harmony 2.9.0.0** |
| Session | **Offline, local cockpit** |
| Settings UI | Config file, or optional **ConfigurationManager** |
| Observer | **Not required** for core TGP; separate companion for the shared menu and paired features |

Exact game and loader identities are checked. Other/newer versions and modified dependency files are not automatically supported. Game, loader and companion binaries are not supplied here. See the [official BepInEx installation guide](https://docs.bepinex.dev/articles/user_guide/installation/index.html) if you need the loader.

## Installation

1. **Close Nuclear Option.** Back up an existing TGP DLL and its configuration.
2. **Download [TargetingPodDisplay.dll](https://raw.githubusercontent.com/akwaa2545-gif/Controllable-Targeting-Pod/main/docs/downloads/TargetingPodDisplay.dll).** No ZIP extraction or Observer installation is needed for core TGP.
3. **Copy the DLL** into your game's `BepInEx/plugins/TargetingPodDisplay/` folder. Create that subfolder if needed.
4. **Keep only one copy.** Remove older duplicate TGP DLLs from other plugin subfolders. Do not remove unrelated mods.
5. **Launch the game once.** Confirm **Targeting Pod Display 0.1.17** in `BepInEx/LogOutput.log`, then close the game before editing its config.

```text
Nuclear Option/
└── BepInEx/
    ├── plugins/
    │   └── TargetingPodDisplay/
    │       └── TargetingPodDisplay.dll
    └── config/
        └── local.nuclearoption.targetingpoddisplay.cfg
```

> [!NOTE]
> Installing the DLL is only the first step. **TGP starts disabled** and its view shortcuts start as **None**. Enable it and assign your controls below.

## First-time setup

### Standalone TGP

With the game closed, open:

```text
BepInEx/config/local.nuclearoption.targetingpoddisplay.cfg
```

1. Under `[General]`, set `Enabled = true`.
2. Under `[Keys]`, assign **Fullscreen** to an unused supported key. For example, `Fullscreen = F6` uses F6, but **F6 is only an example, not a default**. Check the game's and other mods' bindings first.
3. Assign **ScanFollow** to a different unused key if you want to keep selected targets while scanning. Optional **InfraredToggle** and **PiPToggle** also start unassigned.
4. Keep `ManualSensor = None` for the simple mouse-controlled setup. Keep `FullscreenMouseSlew = true` and `FullscreenWheelZoom = true` under `[Presentation]`.
5. Save, launch the game and enter a supported offline cockpit. Release held keys and briefly stop moving the mouse or scrolling before opening fullscreen.

Optional ConfigurationManager exposes the same settings and binding controls. Configure while paused. Preserve existing configs when updating; do not replace them with examples.

<details>
<summary><strong>Already using Observer? Optional shared settings menu</strong></summary>

The separately obtained, exact supported **Observer 0.5.7** binary can host a shared menu. In a supported offline cockpit, pause with **Esc**, then press **F8** (Observer's default Panel key). Choose **TGP → Settings** or **TGP → Bindings**.

Select an action, then **Bind**. Use **Key only**, or choose a special mouse/Ctrl/Shift/Alt input followed by **Alone** or **Combine**. Combine waits for an ordinary keyboard key. **Clear** unbinds; **Cancel** keeps the previous value. Release held controls before closing the menu.

F8 is **not** a standalone TGP key. Unknown or rebuilt Observer binaries can fail compatibility checks. The companion is not distributed in this repository.

<img src="docs/assets/settings-layout-preview.png" alt="Observer-hosted settings layout preview, explicitly labeled not an in-game screenshot" width="100%">

*Layout preview, not an in-game screenshot. Source-based approximation; appearance may differ. Requires the optional Observer companion.*

</details>

## Controls

| Action | Default | Use |
| :--- | :---: | :--- |
| **Fullscreen** | `None` | Open or close the TGP fullscreen view |
| **ScanFollow** | `None` | Switch mouse Scan and native selected-target Follow |
| **InfraredToggle** | `None` | Switch COLOR / IR (GAME) on the owned sensor camera |
| **PiPToggle** | `None` | Toggle and save the optional PiP display |
| **PiPZoomIn / PiPZoomOut** | `None` | Hold to zoom a visible PiP feed outside fullscreen |
| **ManualSensor** | `None` | Optional keyboard sensor-control path |

### A first flight

1. Press your assigned **Fullscreen** key. With no selected target, use the mouse to scan and the wheel to zoom.
2. Aim near a known hostile marker and use the game's existing **Select** binding. There is no new hardcoded mouse button for target selection.
3. Selected targets use native **Follow**, including group framing. Press **ScanFollow** to search without clearing those selections, then press it again to return to Follow.
4. Use the game's existing **Cancel** binding: tap removes the newest target; hold clears all.
5. Press your **Fullscreen** shortcut again, or **Escape**, to leave the view.

Shared bindings may also trigger native game/other-mod actions. Rebind while paused. Aircraft controls and firing remain live; TGP is not autopilot.

<details>
<summary><strong>Optional keyboard sensor controls</strong></summary>

Assign **ManualSensor**, then check all eight sensor keys against the game and other mods before setting `ConfirmNoOtherModUsesSensorKeys = true`.

| Initial sensor key | Action |
| :--- | :--- |
| Arrow keys | Slew |
| PageUp / PageDown | Zoom |
| Home | Recenter |
| End | Inertial direction hold |

This extra confirmation is not required for mouse scanning, ScanFollow or optional PiP zoom. These sensor keys do not assign a Fullscreen shortcut for you.

</details>

## Reading the display

| Indicator | Meaning |
| :--- | :--- |
| **SCAN / FOLLOW** | Camera mode; Follow is not seeker lock |
| **AREA** | A valid held ground point in Scan |
| **NO GROUND** | No supported terrain was acquired |
| **MASKED** | The remembered ground point is obstructed |
| **GIMBAL LIMIT** | A manual viewing stop or unreachable held reference |
| **Red diamond / white brackets** | Known hostile / native selected target |
| **Cyan square** | Known friendly contact, display-only |

Normal manual Scan reaches up to **135° left or right of the aircraft nose**, with the rear **90° sector blocked**. Ground hold is a geometric terrain reference, not moving-object image tracking. SEL range/grid and weapon advice refer to native selected targets, not necessarily the reticle point.

<details>
<summary><strong>HUD illustration</strong></summary>

<p align="center"><img src="docs/assets/tgp-hud-illustration.png" alt="TGP HUD illustration on a plain background, showing crosshair, brackets and range information" width="600"></p>

*HUD illustration without a game scene. Not a gameplay screenshot.*

</details>

## Troubleshooting

<details>
<summary><strong>Nothing happens when I press a key</strong></summary>

Check `Enabled = true`, your assigned Fullscreen key, the startup version and duplicate DLLs. Fullscreen is `None` by default. Use an offline local cockpit, release held inputs and read the precise refusal in `BepInEx/LogOutput.log`.

</details>

<details>
<summary><strong>F8 does not open a menu</strong></summary>

F8 belongs to the optional Observer companion. Standalone TGP uses its config or optional ConfigurationManager; no Observer DLL is included in this download.

</details>

<details>
<summary><strong>The mouse no longer scans, or the view closes</strong></summary>

Selected targets normally engage Follow. Use ScanFollow, or clear selections with native Cancel. UI/focus loss, unsupported input mappings, conflicting ownership or game/loader identities can refuse or release the view. Stop moving/scrolling briefly before entry and check the log reason.

</details>

<details>
<summary><strong>Pink/magenta or incorrect rendering</strong></summary>

Rendering is not live-game/GPU verified. Record the aircraft, game/loader version, installed mods, exact actions and relevant log messages. No verified shader fix is promised.

</details>

<details>
<summary><strong>Updating or uninstalling</strong></summary>

Close the game first. Back up and replace the TGP DLL once; preserve its config. To uninstall, remove only `TargetingPodDisplay.dll` from plugins and keep a config backup if you may reinstall. Do not delete unrelated files or the whole BepInEx folder.

</details>

## Documentation & feedback

- [Complete TGP reference](docs/guides/TARGETING_POD_DISPLAY.md)
- [TGP live-game smoke checklist](docs/guides/TARGETING_POD_SMOKE_TEST.md)
- [Optional Observer compatibility context](docs/guides/OBSERVER_0.5.7_RELEASE.md)
- [Report an issue](https://github.com/akwaa2545-gif/Controllable-Targeting-Pod/issues)

Before posting logs publicly, check for personal paths or other private information. Include the exact version, warning and steps needed to reproduce the issue.

<details>
<summary><strong>Maintainer: GitHub Pages and website checks</strong></summary>

The static site is in `docs/`. To enable it, choose **Settings → Pages → Deploy from a branch → main → /docs → Save**. Expected URL: `https://akwaa2545-gif.github.io/Controllable-Targeting-Pod/`. Check availability after deployment before sharing it as live.

Run `python3 -m unittest discover -s tests -v` to check local links, image paths, TGP-only distribution and the DLL hash.

</details>

---

<sub>Unofficial Nuclear Option community mod. No game or loader binaries are distributed. No software license has been selected in this repository.</sub>
