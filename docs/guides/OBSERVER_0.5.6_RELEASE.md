# Observer 0.5.6 and Targeting Pod Display 0.1.16

## Install

Close Nuclear Option completely. Back up both current DLLs and configs, then replace Observer.dll and TargetingPodDisplay.dll under BepInEx/plugins with exactly one copy of this matched pair. Do not leave old duplicate DLLs or copy example configs over your settings. Confirm Observer 0.5.6 and Targeting Pod Display 0.1.16 in the next startup log. A process already disabled by the old render failure needs a game restart.

This is a source/build/test-verified candidate, not a live-game-verified release. Game 0.34.6 and the previously supported exact reference/loader identities remain required. TGP 0.1.16 adds this Observer binary's exact version/hash pair; older pairs stay recognized, and unknown rebuilds remain refused. The shared settings menu expects this new matched TGP version.

## Settings panel initialization

The reported message was “Observer could not establish a modal raycast shield; panel left closed.” Inspection of the supplied Unity assemblies confirmed two relevant setup assumptions in 0.5.5:

- Its Image alpha of .001 converts to byte alpha zero in uGUI's Color32 mesh colors.
- GraphicRaycaster rejects graphics with depth -1. ForceUpdateCanvases invokes managed rebuild callbacks and does not itself perform the native render/depth work needed by a newly created canvas.

The shield now uses byte alpha 1 with transparent-mesh culling disabled. Opening starts a short pending phase. The actual settings window stays closed until the canvas has valid depth and the owned shield is the first raycast hit at both screen center and the current pointer. A later frame alone never counts as proof.

Native context/focus loss, EventSystem replacement, new mouse/text activity and a two-second unscaled readiness timeout cancel pending setup without saving as if a panel had opened. A competing first hit still refuses. Once open, losing ownership still closes the panel. Failure notices/logs now distinguish missing canvas depth/culling from raycast ownership and identify a competing top hit.

Pause with Esc in a supported offline cockpit, close the game's own Settings if open, release mouse buttons and press your Observer Panel binding (default F8). Keep menu weapon safety enabled. ConfigurationManager is optional; close it before using this menu. The menu remains usable with Observer viewing disabled.

## Missile fullscreen candidate correction and diagnostics

The supplied log separately confirmed a “Fullscreen output ownership changed” exception during the render callback, which disabled Observer until restart. The old message combined several checks, so it does not establish which output property changed in that run.

The candidate allows tiny finite camera-aspect round-off and handles a window resize between LateUpdate and the render callback without treating it as an external ownership change. Target texture, viewport, display and material aspect changes remain guarded. New diagnostics identify the exact failing output property and its expected/actual state if it happens again. This addresses reproducible adapter cases; the user's actual live failure still requires retesting.

Existing missile-camera opt-ins and safety behavior remain. Enable Observer only if you want missile observation, select a live missile (Next defaults to F10), show PiP (F9), then try fullscreen (F11). Auto-show own launches affects future new launches only. Flight Hold's airspeed/stall/overspeed checks remain unchanged and can still refuse fullscreen when automatic Hold is requested in unsafe flight conditions.

## Retained settings and controls

The shared Observer/TGP settings and special-input editor from [0.5.5](OBSERVER_0.5.5_RELEASE.md) remain: select an action, Bind, then Key only or a special mouse/Ctrl/Shift/Alt input with Alone/Combine. Existing saved settings and modifier companions remain. Clear unbinds; Cancel preserves. Native and other-mod actions may still share recognized overlapping inputs.

If Panel is unbound, use optional ConfigurationManager or close the game and restore `Panel = F8` under `[Keys]` in `BepInEx/config/io.github.nuclearoption.observer.cfg`.

Run [the paired smoke checklist](OBSERVER_0.5.6_SMOKE_TEST.md). If the panel or missile camera still fails, preserve the new complete BepInEx LogOutput.log, the screenshot, current Observer/TGP config files and the steps just before it happened. Do not delete your configs as a troubleshooting step.

## Verification limits

The source contains a new production-ModalSurface boundary harness, deferred-session lifecycle tests, first-hit/center/cursor proof tests and camera output adapter regressions. The original 0.5.5 ModalSurface fails the new depth-readiness reproduction. Executable/static tests and both production builds are run again for this pair, and the exact packaged binaries are hashed. These checks do not exercise Unity's actual native renderer, game input, the installed mod set, or GPU/hardware behavior. Those remain unvalidated until the live smoke test.
