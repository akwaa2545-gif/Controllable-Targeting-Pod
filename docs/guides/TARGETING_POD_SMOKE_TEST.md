# 0.1.17 runtime acceptance checklist — new changes not yet run

> **Current public distribution: TGP-only.** Download only TargetingPodDisplay.dll. Observer, paired ZIP bundles and example configs are not included. References to supplied packages/configs in historical sections below describe earlier development packages. Let the mod generate its config or preserve your existing one; follow the repository README for current installation.

For current binding, shared menu and overlap semantics, run [the 0.5.7 / 0.1.17 paired checklist](OBSERVER_0.5.7_SMOKE_TEST.md) first. Historical input/conflict expectations below are superseded by that checklist; retained camera/selection tests still apply.

## 0.1.10 Scan ground stabilization (runtime required)
1. Keep the current config and DLL backup. In ConfigurationManager, verify Presentation → ScanGroundStabilization appears enabled by default, with no AREA key or new target mode. Close the panel, release keys and enter no-target fullscreen Scan with the existing Fullscreen key. Point at terrain: expect stabilizer icon + AREA while the header remains SCAN / 0 SELECTED.
2. Fly laterally, climb and bank without moving the mouse. The same ground patch should remain centered. Confirm aircraft controls remain live and this is not autopilot. Slew slowly and quickly: aim must move smoothly from its current location, then hold the new patch when input stops. If normal terrain aim reports NO GROUND, check the log and compare aircraft: only verified own-aircraft geometry is skipped; a foreign overlap or nearer obstruction must still refuse stabilization. Repeat at narrow/wide FOV, keyboard slew if configured, fullscreen/PiP/cockpit output, and mouse wheel zoom.
3. Aim at sky, sea, aircraft/vehicles, buildings and unsupported scenery. Expect NO GROUND without an active icon, no click/selection/firing, and no acquisition through the nearer object. Aim back onto supported terrain to reacquire. Cross a hill/building/vehicle into the held point's line of sight: MASKED must not become a false AREA at the blocker or retarget foreground silently. Reappearance of the original point may restore it.
4. Move the held point out of the configured camera's near/far range or manual angular limits. Expect LIMIT/no active icon and a finite, safe view rather than a flipped/NaN camera. Slew/reset to acquire a new patch. Test near-vertical look, rearward native-to-Scan entry, rapid bank, terrain edges and colliders near the own aircraft.
5. Select one or several targets, enter explicit Scan, add contacts while holding ground, and return to Follow. Native group framing and locked mouse behavior must be unchanged. Hold Select while toggling ScanFollow: the final designation must resolve in the old view before mode transition. Native Cancel tap/hold and aftermath behavior remain unchanged; Follow/aftermath must never inherit AREA text.
6. Close/reopen fullscreen while holding ground, including while the aircraft moves and after a floating-origin shift. Expect the same global patch and zoom, subject to fresh LOS/range validation. Repeat native selection changes during the entry neutral wait. Change aircraft/TargetCam/scene or disable the plugin: no old point may be applied to a new owner. A new map datum must invalidate the reference.
7. Test optional InertialHold: DIRECTION is not AREA, and aircraft translation can sweep terrain in that deliberate legacy mode. Slew/recenter returns to ground acquisition. Toggle ScanGroundStabilization off/on in the panel: release old input ownership and show no stale icon; off restores legacy behavior. Try pause/map/chat/focus loss and repeated setting changes while keys are held.
8. Verify AREA/icon and loss text stay readable without covering mode/count, native blinking weapon advice, target markers or reticle at square/wide/asymmetric output sizes. Compare frame time and repeated-entry cleanup; raycasts have not been performance-tested in game.
9. In Keys, bind PiPZoomIn and PiPZoomOut with the normal Bind controls. Both must default None and retain saved choices. With PiP visible outside fullscreen, hold each key: zoom should change smoothly within 0.1–60 degrees; both held cancel. Native target camera must remain unchanged; an opted-in replacement cockpit pane shares the owned feed zoom. Try supported letter and function keys, native/known-mod conflicts, same-key duplicates and remapping while held.
10. PiP zoom must not act with PiP hidden, no live feed, during fullscreen entry/fullscreen, or aftermath. Enter fullscreen after using PiP zoom: native follow framing and wheel behavior remain as before. Return to PiP, change native target selection, then repeat. Configure/close the panel while holding the new keys: neither typed/captured/close keys may zoom until the neutral boundary completes. Test UI/focus/owner transitions and both keyboard sensor mode and mouse-only setup.



Use a backed-up offline mission. Test this DLL alone, then Observer 0.5.1, then the existing mod set. Capture logs and screenshots. Compilation and pure tests do not replace these checks.

- [ ] Revisit the reported helipad in COLOR and IR. Confirm no localized magenta surfaces; compare to vanilla. Capture the new Sensor render parity log if any remain. Compilation does not prove this fixed.
- [ ] Fullscreen hides native flight/radar/top-right panels while fresh own weapon advice remains. Fresh OUT OF ARC/RANGE transitions remain truthful; no stale or intentionally hidden SHOOT is invented. External Canvas ownership change exits without reacquiring. Menus/chat/expanded map stay usable.
- [ ] With FullscreenWheelZoom=true, entry waits for a neutral verified boundary; the first next notch zooms exactly once without native camera/weapon/flight response. Test split wheel-as-button mappings, XY/buttons and alternate keyboard/joystick bindings, exit while scrolling, fast reentry, remaps and focus/map loss.
- [ ] Unsupported digital-smoothed wheel bindings refuse entry precisely. Explicit FullscreenWheelZoom=false permits prior fullscreen without pod scroll consumption; native wheel bindings stay live. Config changes invalidate the session.
- [ ] Check third-party raw-wheel readers separately. Native Rewired isolation does not prove unknown-mod raw-input isolation.
- [ ] Disabled defaults leave camera/input/weapons unchanged. Existing config survives DLL-only update and receives new PiP/aftermath keys.
- [ ] Native camera initialized by ordinary selection; unique cockpit target RawImage found through registered intact parts even after normal physics unparenting. Missing/ambiguous/damaged displays stay native.
- [ ] Separate landing image sharing native texture stays unchanged. Target/landing overlap, registry removal, detachment and another mod's replacement release only owned values.
- [ ] Actual compact green legends, white TGP / selected-AGM green split reticles and transparent background are upright, readable and not doubled with vanilla targeting-camera text. Test square cockpit and wide fullscreen. Range matches native target distance; ARS follows aircraft, not sensor motion; UTC clock and LSR N/A remain honest.
- [ ] F6 (or configured unused key) enters real edge-to-edge direct camera view, without cockpit geometry. World resolution follows screen size. Exit repeatedly restores native camera and cockpit. Check any remaining screen-space HUD and report exact canvas/screenshot, rather than disabling shared UI blindly.
- [ ] Pause/map/chat/menu/focus loss, external view, death/ejection, damaged cockpit, origin shift, respawn and scene unload cannot leave a black screen or resurrect the cockpit in another camera state.
- [ ] Passive right-side PiP enables/disables by config and shares the cockpit feed. It intercepts no mouse/input. PiP/cockpit offscreen pass stops during fullscreen and resumes on exit.
- [ ] Manual entry requires distinct unused toggle/sensor keys and explicit other-mod key confirmation. A native binding collision refuses manual controls without disabling native input. Changing any key or confirmation while active releases and requires key-up before reentry.
- [ ] Slew/zoom/recenter/inertial direction hold work through origin shifts. Manual motion never changes native target selection or weapon acquisition. Aircraft steering/throttle/firing remain live; no autopilot assumed.
- [ ] A uniquely watched target's actual native kill report starts live AFTERMATH for configured seconds; moving smoke/debris/world proves it is live. Target name/lock/weapon hint disappears immediately. No destroyed Unity target object is retained by aftermath.
- [ ] Ordinary deselection, target cleanup/despawn, another unit's kill, multiple selections and replacement IDs do not start aftermath. Same-frame selection removal before kill report is handled without a frozen image. New designation, manual entry and context loss cancel; duration 0 disables, 10 caps.
- [ ] Native COLOR/IR settings compare with vanilla; manual stays COLOR. No claim of true thermal/night. Switch weapon roles: surface missile with live selected target gets green long arms and three lower ticks; deselection/destruction removes them immediately, ambiguous/air roles stay generic, no fabricated lock/laser/launch values.
- [ ] Observer absent/idle/hold can coexist; fullscreen/drain/modal or unknown identity blocks/releases interactive pod view. Native flight controls remain untouched.
- [ ] Measure frame time, allocation and memory over prolonged use, repeated mode changes and resolution changes. No doubled offscreen world pass during direct fullscreen, orphan cameras or persistent fog changes.

On unsafe behavior disable this DLL and retain vanilla presentation. Report aircraft, plugin/game versions, log and screenshot; do not claim broad aircraft compatibility before testing.

## General cockpit screen option (runtime required)
1. In the installed ConfigurationManager panel, open Targeting Pod Display → Presentation. With the mod enabled and PiP off, turn `DisableCockpitScreen` on and off, closing the panel and resuming cockpit gameplay after each change. Only the target pane should hide and restore; native camera mode, targeting, radar, clock and landing view must still work. No new Observer menu should appear.
2. With both cockpit-disable options false, the native/replacement pane should remain normal. With only `DisableCockpitScreenWhenPiPEnabled` true, it should hide only while a current PiP frame is available. With `DisableCockpitScreen` true, stopping PiP or losing the pod feed must not restore it while the same valid cockpit context remains.
3. Initialize the native target display normally, then deselect all targets and leave PiP/fullscreen/manual scanning off. Turn the general option on: the initialized proven pane should hide without requiring a pod presentation or starting a native sensor camera. Before native initialization or on an unsupported/ambiguous pane, leave the native display untouched and retry when proof becomes available.
4. Change either option repeatedly in the panel and enter/exit fullscreen. The pane must restore when neither setting applies. Check pause/map/chat, focus loss, landing mode, external view, cockpit damage/ejection, aircraft/scene change and mod disable. Surviving captured graphics restore their previous enabled state; no landing/radar/time component or sensor camera should be disabled.
5. With the pane suppressed, let another owner enable it or replace its texture/owner. The plugin should release and not repeatedly take the successor over. Re-entering a new valid cockpit/config context may retry normally. Keep this as a rendering-only check; no frame-rate gain is established.


## Retained no-target mouse scan checks (runtime required)
1. Keep your existing config and F6 (or configured key). Leave ManualSensor=None and confirmation=false. Ensure FullscreenMouseSlew=true. Enter an offline cockpit without selecting any target, stop mouse/wheel briefly, then open fullscreen. Expect live COLOR view, TARGET NONE, and no native cockpit behind it. This must also work before the first native target camera render.
2. Move the mouse in each direction, then scroll. Expect sensor aim and zoom only; no mouse steering or cockpit-head movement. Keyboard/joystick control and fire buttons remain live. The aircraft is not held steady automatically.
3. Exit while moving the mouse, stop movement, and verify normal mouse flight/view controls return with no stored virtual-stick turn. Repeat with a nonzero virtual-stick offset before entry. Repeat F6, Escape, pause/map/chat, focus loss, aircraft exit/death and scene changes.
4. With a selected contact behind the aircraft, enter fullscreen and move the mouse. Expect continued native centering, with no manual detachment or aircraft mouse steering. Try the optional manual key, slew, recenter and inertial keys: none may break follow. Repeat below 1-degree FOV and with aircraft roll. Native wheel zoom remains available.
5. While fullscreen is active, use native Cancel tap with multiple targets: only the newest target should clear and remaining targets must keep native group framing. Hold native Cancel to clear all: expect manual viewing to remain available from the current camera view. A real watched kill may first show the configured aftermath; moving the mouse cancels it immediately. Exit/reenter with a valid selected target to resume native following.
6. Compare friendly, neutral and hostile contacts. Known hostiles may have hollow red diamonds; friendlies/neutral/unknown units must not. Move a known hostile behind terrain/buildings/another vehicle: its native known-position marker may remain through cover. Lose fresh tracking: expect the native last-known location with steady muted intensity, not flashing or secretly updated hidden coordinates. Move it outside or behind the camera: marker disappears. Repeat cockpit/PiP/fullscreen at multiple aspect ratios.
7. Change mouse mapping modes or switch input context during fullscreen. Expect release and original native mouse mappings restored, or a clear refusal before entry for unsupported modes. No stuck steering/view mappings may remain. Third-party raw mouse handlers require separate compatibility checking.
8. Confirm native weapon advice/range retains its original meaning even while manually looking away. Mouse scanning/diamonds alone must not create weapon selection or lock. Only the explicit Select action described below adds targets.

Build and tests alone do not establish any of these in-game outcomes. Capture a screenshot and fresh BepInEx log for any failure.

## 0.1.6 selection, group following and PiP suppression
1. Compare the same radar/network-known hostile in vanilla and in cockpit/PiP/fullscreen. Terrain/buildings must not toggle its diamond on and off. No unknown, friendly or neutral contact may gain a diamond. Check stable intensity for both current and last-known contacts, origin shifts, square/wide views and multiple clustered contacts.
2. In manual fullscreen, point the center crosshair near a known hostile and tap the existing native Select control. Expect native target-list/map selection and sound, with the same target exclusions, no duplicate and no firing. When explicit Scan is not active, the camera must return to native centering on the next normal native tick, with matching target range/advice. Explicit Scan instead retains its view. Try a clustered set with different ranges and weapon priorities: tap should use native priority rather than simply the closest pixel. PiP does not accept clicks.
3. Aim at empty space or an excluded contact: no hidden cockpit target may be selected. Test a remapped Select control, tap versus native timed hold, existing selections, weapon exclusions and no weapon station. A hold only adds native weapon-eligible targets; it must not clear the list. Expect one selection sound and list update for the group, native marker order, group-bounds centering and native group FOV. Selection changes reset pod wheel override. Verify more than 32 eligible contacts; the deliberate safety bound is 128 additions per hold event.
4. Hold Select before entering: release it, then make a fresh gesture before TGP selection can occur. Press Select in fullscreen and exit with F6 before releasing: release must not select a hidden/native cockpit target. Repeat hold-paint, Escape, no-target/no-feed return and rapid exit/reentry. After neutral, a fresh normal cockpit click must work.
5. Change aircraft/HUD/input owner, open native UI or lose focus during a held gesture. The old drain must not suppress input for a new owner. Selection-hook conflict/failure must release fullscreen and restore normal native interaction. Runtime Harmony ordering remains unverified by authored-fixture tests.
6. With PiPEnabled=true, set DisableCockpitScreenWhenPiPEnabled=true. Only the native cockpit target pane should disappear; PiP, radar, clock, landing mode and native targeting must continue. Disable PiP or the option: the original pane must return. Repeat fullscreen, native landing-camera toggle, camera switch, focus loss, damaged cockpit, scene change and disabling the plugin.
7. Enable the option before the native texture/consumer has initialized, then initialize it normally. Suppression should begin after a later valid current PiP frame. Replace or enable the leased pane externally: the plugin should release without repeatedly overriding the successor. Compare frame time before/after; do not assume a second sensor render was removed.


## 0.1.7 Scan/Follow, view memory and PiP keys
1. Keep the old config. Confirm ScanFollow and PiPToggle appear under Keys in ConfigurationManager and default None. Configure distinct unused keys. Check each against native input, Fullscreen, ManualSensor, the other optional key and any active sensor shortcut. A conflict must disable only that optional action, not normal fullscreen. Test a remap while held, release both old/new keys and re-enter.
2. With ManualSensor=None and keyboard-sensor confirmation=false, select one target and open fullscreen. Toggle Scan, move away and add several separated contacts. Existing selections remain; every addition keeps the manual view. Toggle Follow: the native group is framed and mouse motion no longer pans or steers. Native wheel zoom remains available. Check native Cancel tap/hold in both modes.
3. Hold native Select while requesting either mode change. Expect RELEASE SELECT and the current mode to remain. Release Select: any queued tap/paint uses the old view, then mode changes. Press the mode key twice while waiting to cancel the pending change. Test first selection and mode change on the same frame, empty aim and all targets removed.
4. Verify SCAN/FOLLOW and valid selected count in square cockpit, PiP and wide fullscreen. Scan shows selected-target data with SEL labels and no misleading range at the reticle. Pending notice, native advice and FLIGHT LIVE must remain readable. AFTERMATH must not display a false target count or Scan/Follow notice.
5. Scan to a rearward/rolled view and narrow zoom, close with F6 and reopen without targets. Repeat Escape, including when Escape opens native pause UI. View and zoom should resume, not reset forward. Repeat with explicit Scan plus selected targets and after a no-feed teardown. Move/roll the aircraft while closed: the saved relative aim follows the aircraft; an explicit inertial hold should remain inertial. Verify normal mouse controls restore while closed.
6. Close in Follow with wheel zoom, reopen with the same group: native target motion stays live and owned zoom resumes. Change target order/group while closed or while waiting for neutral entry: native new-group framing must win over old zoom. Clear targets while closed: the last actual camera aim seeds manual scanning, not an old manual default.
7. Switch aircraft/TargetCam or unload the owning scene, and disable/re-enable the plugin. The old view must not transfer. Config changes, focus loss, death and unsupported ownership still restore native cameras/input safely. Saved view contains no old world camera position and does not survive a game restart.
8. Toggle PiP by its key in ordinary cockpit and during Follow, Scan and a pending Select gesture. PiPEnabled persists in the saved config; fullscreen/mode/isolated mouse ownership must stay intact. PiP remains hidden in fullscreen and uses the new setting on exit. Check the general and PiP-only cockpit suppression options still restore correctly.


## 0.1.8 contact identity and top-center native advice
1. Compare selected and unselected known enemies at several zoom levels. Both remain red diamonds; only native-selected hostiles gain bright brackets. Select several, remove newest with native Cancel, then clear all. Brackets/count must agree with native selection and disappear without stale marks. Scanning alone must not select anything or claim seeker lock.
2. Compare actual same-faction units with hostile, neutral/no-faction and unknown units. Friendly cyan squares must come from the native faction inventory even when absent from enemy trackingDatabase. The own aircraft is not marked. Aim Select/paint at a friendly: the mod must never add it to the selected list. Test a contact changing faction, disappearing, losing identity or being replaced under a reused ID.
3. Crowd the viewport with friendlies and hostiles. Each layer has its own bounded nearest-center budget; adding friendlies must not remove/reorder the previous hostile candidates. Check square cockpit, wide fullscreen and small PiP. Terrain cover and last-known enemy positions retain their native information semantics, without hidden current-position substitution.
4. Observe real native OUT OF ARC, OUT OF RANGE, TOO CLOSE, TOO SLOW and permitted SHOOT transitions. The text must appear top center, below the header, and blink at a slow1Hz without overlapping mode/count, sensor/FOV or the reticle. Other text/markers must stay steady. A cropped or vanished native hint must never turn into fabricated fire readiness.
5. Change weapon station, target list, camera owner and ammunition while a status is blinking. Old status must clear immediately, including during the next blink-on phase. Hidden native SHOOT must remain hidden. AFTERMATH and no-selection states suppress weapon status. While Scan is active, SEL advice remains explicitly about selected targets.
6. Repeat the 0.1.7 Scan/Follow, held Select, remembered-view and PiP shortcut checks to verify this presentation change has not changed camera/input/selection behavior. Capture the screenshot and log if status timing or marker identity differs from vanilla.

## 0.1.9 IR and key-capture acceptance
1. Keep your config and previous DLL for rollback. In ConfigurationManager, confirm Keys entries show Bind/Clear instead of the unrestricted dropdown. Existing F7/F10 values should show rejection reasons without changing themselves. Bind distinct accepted keys; Escape/cancel/rejected keys must keep the prior setting.
2. Capture the same existing key, cancel capture, close/filter the row, and lose focus while capturing. No Fullscreen/Scan/PiP/IR action may trigger until capture ends and held keys are released. Native game input is not suppressed by this mod's capture UI.
3. Open fullscreen without targets. Toggle InfraredToggle: COLOR and IR (GAME) should alternate while the view/zoom stays fixed. Select/add targets and switch Scan/Follow; IR choice must persist without altering native target selection or fire controls.
4. Close/reopen fullscreen and enable PiP/cockpit replacement. IR must apply to those owned views while ordinary world/cockpit/other cameras keep their appearance. Return to COLOR, leave cockpit, change aircraft/scene and disable the plugin; verify no fog/color spill or sticky postprocessing.
5. Try day/night conditions and IR failure/ownership diagnostics if available. This is native-style IR grading, not per-object heat sensing. Mode labels must describe the actual view, never claim a seeker lock or fabricated fire readiness.

## 0.1.11 paired Observer smoke test

Use the delivered Observer 0.5.2 DLL and TGP 0.1.12 DLL without duplicates. Confirm
TGP works both without Observer and with Observer idle, yields while Observer's
paused menu/fullscreen/release drain owns input, and recovers on return. Verify a
cross-mod main-key collision is refused without changing either config. Preserve
all Scan/AREA/Follow, IR, PiP zoom and selection checks above. Unknown Observer
binaries must remain blocked; do not bypass the fingerprint guard. This paired
runtime behavior has not been validated in game by cloud tests.

## 0.1.11 ground acquisition retest

Aim Scan at ordinary nearby terrain from the native cockpit sensor mount, including
mounts embedded in the aircraft hull. Verify AREA while terrain is clear and MASKED
or NO GROUND behind a foreign object, water, a building or sky. Own-aircraft geometry
must no longer falsely block acquisition, but no foreign unit is skipped. Check the
same aircraft after floating-origin movement and close/reopen; no sensor-origin
offset, target selection, world-collider or native terrain mutation is permitted.
Dense collider queries may conservatively refuse at the bounded capacity. Hollow
nonconvex geometry containment is not proven by this test or the overlap/raycast API.

## 0.1.12 aircraft-relative gimbal retest

- Follow a selected target behind the aircraft, enter Scan, then slew toward forward
  in either direction. A forbidden initial rear view moves to the nearest edge.
  The stop must be 135 degrees from the current nose, never from the previous target.
- At each rear edge, outward input stops; reversing moves away immediately. A large
  mouse movement must not jump across the blocked rear sector to the other edge.
- Repeat with Scan ground stabilization on/off, tilted/rolled aircraft, simultaneous
  pitch input, near-vertical directions and rapid aircraft motion between frames.
  Existing pitch bounds and complete orientation must remain finite and stable.
- Turn the aircraft so a held AREA point or DIRECTION lies behind the permitted
  sector. GIMBAL LIMIT appears; the original desired reference remains stored.
  Clipped AREA must not keep its active stabilizer icon or acquire a substitute spot.
  Turn back and verify original-point recovery when reachable.
- Ground range loss alone must not invent a gimbal warning. An actual point exactly
  on the allowed boundary can show AREA and the stop warning together.
- Close/reopen at a boundary, then with the aircraft rotated while closed. Revalidate
  against the current aircraft and do not restore stale status or hidden input.
- Native Follow/aftermath remain unchanged with no manual gimbal warning. Check the
  warning at fullscreen and small PiP sizes, separate from weapon advice and reticle.

These runtime checks remain unperformed here. No extra-pod extension is claimed
until actual equipped payload identity is verified.

## 0.1.13 keyboard and paired Observer checks

- Pause in the cockpit, click Bind, release held inputs, then try a free digit-row
  key, base punctuation, keypad, editing key and extended function key supported by
  your keyboard. Confirm the panel saves the actual key and the action works after
  closing the panel and releasing keys. Test both mods and Observer modifier chords.
- Try an enabled native key, another action's main key, a known other-mod key and
  an unsupported input. The original binding must remain; inspect the exact reason.
- F7-F11 must become usable if their actual conflicting settings are cleared, not
  while Observer still owns the same key. Native raw conflicts must track context.
- Hold a key before Bind, press Escape or click Cancel, close/filter the row, switch
  focus and change a saved key externally. No stale press may activate either mod.
- Repair an undefined numeric legacy key. It must not throw or strand all inputs;
  a valid replacement still waits for old/new valid held keys and a neutral frame.
- Test NumLock/layout changes, normal ConfigurationManager search typing, and
  same-main-key different-modifier Observer conflicts. Do not infer Fn/media support.
- Reproduce a Flight Hold preparation refusal over repeated updates. The first
  reason must remain readable without repeated “Blocked:” prefixes. A readable
  error is not evidence that the underlying preparation failure has been fixed.
