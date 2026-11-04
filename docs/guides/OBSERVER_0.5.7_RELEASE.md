# Observer 0.5.7 and Targeting Pod Display 0.1.17

## Install and scope

Close Nuclear Option completely, back up both DLLs/configs, and replace Observer.dll and TargetingPodDisplay.dll with exactly one copy of this pair under BepInEx/plugins. Retain your existing configs. Confirm Observer 0.5.7 and Targeting Pod Display 0.1.17 in the next startup log.

This is a source/build/test-verified candidate, not a live-game-verified release. The previous settings-panel and fullscreen-output initialization corrections remain. Exact game 0.34.6 references and supported loader identities remain required; the text-rendering module is now explicitly checked for the warning's font/alignment types. No proprietary binaries are included.

TGP 0.1.17 adds the exact Observer 0.5.7 version/hash pair, retains previous known pairs, and exposes a narrowly verified same-camera view contract so Observer can recognize its fullscreen view. Sensor selection/Scan/Follow/IR behavior is unchanged; watched-view flight input behavior changes as described below.

## Requested fullscreen and Auto Hold behavior

Missile fullscreen viewing no longer depends on Auto Hold being able to engage. If Hold refuses an unsafe flight condition or releases, Hold still stops applying its commands, but the missile camera remains open while its own context/input/render ownership remains valid.

Whenever Hold is not enabled, available and active, a persistent high-contrast band says:

**AUTO HOLD INACTIVE**

**AIRCRAFT NOT STABILIZED**

**Exit fullscreen to fly.**

The warning does not expire with temporary notices. The status/return-key header moves below it, and lower-priority Hold details/transient notices yield space in small windows rather than covering it. The warning disappears only when Hold is effectively active or missile fullscreen ends.

The aircraft continues simulating without stabilization. The existing fullscreen neutral-input handling is not autopilot and does not mean normal pilot controls remain available while watching the missile. Exit fullscreen with its configured return shortcut, and release held controls if prompted, before flying normally.

## Safety and input behavior retained

Hold's airspeed, clearance, attitude, angular-rate, engine and other safety limits are not widened. A released Hold remains latched off until its existing trigger-cycle/rearm rules allow another attempt. The fallback fullscreen command keeps the latest finite throttle/custom setting captured when Hold releases instead of reverting to stale entry values. An invalid fallback input still fails closed.

Deliberate flight-control movement still exits fullscreen. Raw manual-input sensing uses a fresh baseline for each fullscreen lifetime, including when Hold is disabled, unavailable or already latched; late Hold engagement must not swallow that baseline. Disabled control maps do not turn synthetic zeros into a false manual movement. No Hold actuation is enabled merely to observe manual input.

Fullscreen also still exits for genuine target/context/owner/render/input failures. Hold refusal is not permission to bypass those checks. Notification failures cannot change otherwise valid camera/control ownership.

## Map, TGP and missile mouse/keyboard behavior

With automatic Flight Hold enabled, opening the maximized map clears the cached virtual-joystick offset before attempting Hold. Paired TGP fullscreen is now also a Hold trigger. Eligible supported forward flight attempts the existing current-course/speed/altitude stabilization. Clearing a cached mouse offset or applying neutral inputs alone will not level an already-banked aircraft when Hold cannot engage.

The normal mouse Pan View/Tilt View virtual-stick path no longer counts as aircraft steering or manual flight takeover in map/TGP while Auto Hold is enabled, or in Observer missile fullscreen regardless of Hold availability. The mouse can still operate the map or pod/camera. Keyboard and controller flight inputs remain meaningful:

- Map/TGP: keyboard/controller steering cancels Hold and directly steers while the view stays open. Releasing the keys must not replay a cached mouse turn.
- Missile fullscreen: keyboard/controller takeover exits to normal flight view. The persistent unstabilized warning still instructs you to leave fullscreen to fly.
- Auto Hold disabled: native map/TGP flight behavior is unchanged. The missile fullscreen mouse-steering exclusion still applies.

The implementation verifies that enabled Mouse mappings cannot directly contribute to Pitch/Roll/Yaw, then uses native Rewired keyboard/joystick aggregation. It does not subtract combined input values, remap controls, or interfere with another plugin's mouse-binding ownership. Enabled direct Mouse Pitch/Roll/Yaw bindings are explicitly unsupported: the affected view refuses/closes with a reason rather than accepting uncertain input or holding zero axes forever. Keep normal virtual-stick Pan/Tilt with keyboard/joystick flight bindings for this supported behavior.

Fresh source-proof waits can briefly delay entry after startup/reconfiguration. Retrying after a native input update may be necessary. During a temporary reproof wait, Hold commands are suspended and reported inactive/suspended while targets remain stored, then fresh verified input resumes without recapture. Permanent source/identity/guard failure refuses or closes the affected view. Native pilot-strength/G-LOC cutoff and non-steering throttle/auxiliary side effects remain intact.

This corrects cached mouse replay, input-source handling and TGP lifecycle integration in the source/adapters. It does not prove live aircraft stability and does not retune the existing controller or broaden its envelope.

## More useful diagnostics

Safety refusals identify the measured value, threshold and units where available: for example, airspeed, radar clearance, bank or angular rate. Fullscreen exits report the actual closure reason once rather than only disappearing. Hold release reports that fullscreen continues without stabilization. These messages help distinguish a Hold-envelope issue from a lost missile, input conflict or camera ownership change.

Run [the live smoke checklist](OBSERVER_0.5.7_SMOKE_TEST.md). Preserve the new full LogOutput.log if behavior differs, including the precise warning/closure reason and the action immediately before it. The earlier [0.5.6 guide](OBSERVER_0.5.6_RELEASE.md) and [0.5.5 settings workflow](OBSERVER_0.5.5_RELEASE.md) remain useful, but this document supersedes their statement that Hold refusal prevents fullscreen.

## Verification limits

The release is checked with production-policy/adapter code against authored engine/input boundaries, warning-renderer and composed-layout tests, static wiring checks, both production builds, and an independent rebuild from the packaged source. These checks do not run Unity, the game, its native input/Harmony hooks, the installed mod set, or GPU rendering. Actual in-game behavior and warning appearance still need verification.
