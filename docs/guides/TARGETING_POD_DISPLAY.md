# Targeting Pod Display 0.1.17 — paired Observer fullscreen/Hold release

> **Current public distribution: TGP-only.** Download only TargetingPodDisplay.dll. Observer, paired ZIP bundles and example configs are not included. References to supplied packages/configs in historical sections below describe earlier development packages. Let the mod generate its config or preserve your existing one; follow the repository README for current installation.

**Compile/test verified; live game/hardware/GPU validation remains required.** Separate DLL; Observer is optional for TGP operation. The shared independent menu requires paired Observer 0.5.7. Exact game0.34.6 references and supported BepInEx5.4.23.5/5.4.23.6 remain required. Offline local cockpit only.

TGP 0.1.17 adds a verified same-camera contract for Observer Flight Hold in TGP fullscreen. With Auto Hold enabled, supported virtual-stick mouse movement is excluded from aircraft steering; keyboard/controller steering cancels Hold but leaves the TGP view open. TGP sensor slew/mouse capture remains unchanged. Auto Hold off preserves native map/TGP flight behavior. Direct Mouse Pitch/Roll/Yaw bindings remain unsupported and refuse/close safely. See the paired release guide.

## Current settings and binding behavior

See [paired release guide](OBSERVER_0.5.7_RELEASE.md) for the complete workflow. With paired Observer installed, pause in a supported cockpit and press its Panel key (default F8), select TGP, then Settings or Bindings. The menu remains accessible while Observer viewing is disabled. TGP alone uses its existing config or optional ConfigurationManager.

Select an action in ACTION / ASSIGNED KEYS, then Bind. Choose Key only or a special mouse/Ctrl/Shift/Alt input, followed by Alone or Combine. Combine captures an ordinary keyboard key. Clear unbinds; Cancel preserves. Native input may also act: recognized overlaps show warnings, while unsupported/unreadable inventory and unsafe contexts still refuse. No global suppression of native mouse buttons is added.

TGP retains its original main KeyCode entries and adds modifier companions under `[KeyModifiers]`, for example `Keys.Fullscreen`. Empty companions preserve the old single-key behavior. An existing raw config is backed up once as `.pre-mouse-chords.bak` before entry binding. Keep existing settings rather than copying the example over them. BepInEx may normalize invalid enum text; the raw backup is retained for recovery.

Discrete special-alone actions use clean release and cancel when another input or a context interruption joins. Special-alone continuous controls need a fresh eligible press; ordinary keyboard-held controls keep their prior behavior. Mouse-related changes wait for release/neutral boundaries so an in-progress native Select is not redirected to a new camera aim. This does not prevent native firing, panning or map orders from a shared button. ConfigurationManager and shared-menu capture block the mods' actions, not every game/OS action.

Mouse0–6, keyboard punctuation/keypad/function keys and supported Ctrl/Shift/Alt combinations depend on what Unity receives. Escape remains cancellation. Wheel/controller axes, Windows/Command/AltGr, legacy shifted-character aliases and OS-only keys are not added. Use physical Shift+Equals for plus or KeypadPlus. Hardware/NumLock/layout may differ.

This pair supports exact Observer 0.5.7 plus the delivered 0.5.1–0.5.6 version/hash pairs. Unknown rebuilds remain refused. The existing camera, Scan/Follow, AREA, IR, gimbal, markers and PiP/cockpit features below remain; input descriptions in the historical sections are superseded by this current section.

## 0.1.12 rear-only Scan limit

Normal Scan looks up to **135 degrees left or right from the aircraft nose**. The
remaining **90-degree sector directly behind** is blocked. The boundary follows
the current aircraft, not the target that was selected before Scan. Forward remains
reachable when leaving a rearward native target view. If that initial view is inside
the blocked sector, entering Scan moves the camera to the nearest allowed edge.
This replaces 0.1.11's unrestricted manual yaw continuation.

A separate steady **GIMBAL LIMIT** warning appears at an actual viewing stop or when
a retained ground/direction reference cannot be reached. It does not replace the
SCAN/FOLLOW label, selection count or native weapon advice. Generic AREA **LIMIT**
can also mean a range limit and is not automatically a gimbal warning. A ground
point remains stored when blocked, but cannot show active AREA while the displayed
ray points elsewhere. It can resume when the aircraft brings it back into reach.
Reopening checks the current aircraft-relative boundary again rather than trusting
an old saved status.

Near-vertical or near-boundary large input is checked with a bounded calculation.
It may conservatively shorten a movement rather than jump across an unresolved rear
sector. Exactly vertical aim has no meaningful aircraft-relative azimuth.

Existing pitch bounds, zoom and selection controls remain. Native selected-target
**Follow** and aftermath continue their native behavior; the rear stop applies to
the mod's manual Scan/AREA/direction paths. These are mod viewing limits, not claims
about real sensor hardware. An extra targeting pod's wider range is not enabled
from generic radar, laser hardware or built-in EOTS. Its exact payload identity
still needs verification; unknown equipment keeps the normal limit.

## 0.1.11 ground acquisition and paired Observer compatibility

A camera mount inside its own aircraft hull no longer automatically rejects ground
acquisition. Read-only overlap/raycast queries skip only colliders on the current
aircraft transform or its children, and exclude the game's avoidance-only
ExclusionZones layer. The actual camera/ray origin is unchanged. Foreign overlaps
and the closest non-self obstruction still block ground acquisition. Both bounded
queries fail closed at 64 results rather than guessing from a truncated hit list.
This corrects a reproducible source/fixture failure; it does not establish which
branch caused the user's screenshot or constitute live game validation.

The 0.1.11 rear-target correction removed an unreachable forward sector caused by
initial-target-relative yaw limits. Version 0.1.12 replaces its unrestricted yaw
continuation with the confirmed aircraft-relative rear boundary described above.

This release adds the reviewed exact Observer 0.5.2 binary to the input-ownership
allowlist, while preserving support for the delivered Observer 0.5.1 binary. Unknown,
modified or cross-paired versions/hashes still fail closed. Keep both configs and
replace each DLL only once. Observer remains a separate optional mod; TGP works without it.

Observer now stores typed shortcut settings, so both mods can check their main-key
conflicts live. A conflict is refused, not silently remapped. Different modifier chords
sharing a main key remain conflicts. TGP shortcuts still use single keyboard keys,
not modifier chords. Version 0.1.13 replaces the former F7–F11 reservation with live conflict checks. ConfigurationManager
still blocks both mods' actions while visible. Neither capture UI suppresses every
native game action; pause while rebinding. Native controls and undeclared raw-key
handlers in other mods need in-game checking.

## 0.1.10 ground stabilization in Scan
- **Use the existing Scan mode and controls. There is no additional mode key.** With **Presentation → ScanGroundStabilization = true** (default), aiming at supported terrain establishes a fixed ground spot. As the aircraft moves, the owned camera turns to keep that same point centered. Move the mouse or configured sensor slew keys to search a different area; the new terrain aim becomes the held spot. Scroll zoom remains unchanged. Uncheck the option in ConfigurationManager to restore the old Scan behavior.
- A bracketed ground-point **stabilizer icon + AREA** appears on the left only while the held ground point is valid and the conservative physics checks pass. The header remains **SCAN / N SELECTED**. **NO GROUND** means the ray did not establish supported ground, **MASKED** means the remembered point is obstructed, **LIMIT** means its viewing/range limit is exceeded, **DIRECTION** means the optional legacy inertial-direction hold is active, and **UNAVAILABLE** means the physics compatibility check did not pass. Loss states do not show the active stabilizer icon. On very small output, NO GROUND and DIRECTION abbreviate to NO GND and DIR HOLD.
- This is a geometric fixed-ground reference, not image-feature tracking, moving-object POINT track, thermal detection, seeker lock or autopilot. Aiming at the sky, water, a vehicle or unsupported building/scenery does not create a ground point. The normal selected-target **Follow** mode remains separate and uses native target/group framing. Native Select adds targets exactly as before; explicit Scan keeps selections while searching, and ScanFollow returns to native Follow. Native Cancel remains unchanged.
- Ground coordinates use the game's global-position conversion so map-origin shifts do not move the reference. A conservative 1 cm overlap probe at the actual camera mount refuses foreign solid overlap. Only the verified current aircraft transform/hierarchy and native avoidance-only ExclusionZones are skipped; no origin offset is used. The nearest remaining hit must be the exact native terrain material on eligible static geometry in the current scene. Water, buildings, vehicles and other nearer objects remain blockers. The overlap/raycast checks do not prove containment or optical visibility for every hollow/nonconvex mesh. The point is bounded by the live sensor far clip and a 60 km cap, the near plane and existing manual slew limits. Obstruction or loss never silently substitutes a foreground point. Move the sensor to acquire a fresh patch. Any selected-target **SEL RNG / SEL GRID / SEL** weapon advice still describes the native selected targets, not the ground spot.
- Normal same-aircraft fullscreen close/reopen retains the ground point and zoom when valid. It is revalidated before showing AREA, never replayed as an image. Follow ignores stored Scan coordinates. Aircraft/TargetCam/scene or world-datum replacement, reset, invalid coordinates and plugin disable invalidate ownership. State is session-only. The optional InertialHold key deliberately selects direction hold; slew or recenter returns to normal Scan ground acquisition.
- The implementation is compiled and tested against authored native boundaries; **live game terrain capture, motion, origin shifts and rendering still require the smoke test**. Existing IR/key capture, red hostile diamonds with white selected-target brackets, friendly symbols, native weapon status, cockpit/PiP options and input restoration are retained.

## PiP Zoom In / Zoom Out keys
- Open **Targeting Pod Display → Keys → PiPZoomIn / PiPZoomOut**, click **Bind**, release any held key, then press distinct unused supported keyboard keys. Both default to None and persist in your config. Capture, native-map and known-mod conflict checks are the same as other optional TGP shortcuts; no ManualSensor binding or sensor-key confirmation is required.
- Hold Zoom In to narrow the visible PiP field of view, or Zoom Out to widen it. Holding both cancels. These keys work **outside fullscreen while PiPEnabled is true and a current live feed is available**. They do not change fullscreen wheel zoom, operate during aftermath, or force a hidden/no-target native feed to open.
- The owned PiP and optional replacement cockpit pane share one camera, so both share this zoom. Native target-camera FOV and native cockpit output when replacement is off are untouched. Follow zoom is reset on target/group changes and explicit Follow reset; it is session-only. Scan uses its existing manual FOV and normal view-memory behavior.
- Inputs are ignored while ConfigurationManager/native UI is open or keys are passing their release boundary. An unavailable/conflicting zoom key reports the reason and does not take over native input. Unknown raw-key handlers in other mods still cannot be proven absent.

## 0.1.9 IR and click-to-bind keys
- In ConfigurationManager, open **Targeting Pod Display → Keys → InfraredToggle**, click **Bind**, release held keys, then press a supported unused keyboard key. Escape cancels and **Clear** unbinds. The key setting persists; default remains **None**. All TGP keyboard settings now use this capture control rather than an unrestricted KeyCode dropdown.
- The first IR press switches the currently displayed sensor mode. Further presses toggle **COLOR** and **IR (GAME)** in fullscreen, PiP and supported cockpit replacement. IR also works during no-target manual Scan. The choice stays with the same aircraft/TargetCam/scene across Scan/Follow and normal close/reopen; changing owner/scene or disabling the mod clears it. It is not saved across game restarts. Until the first press, old behavior remains: Scan uses color and Follow inherits the native camera mode.
- This is the game's IR presentation: native saturation calibration, ambient-dependent IR exposure/contrast and camera-scoped fog behavior. It is **not temperature-based thermal imagery**, a heat-signature detector, or proof of visibility. Explicit COLOR uses the mod's existing unprocessed color view. Only the owned sensor camera changes; native IR preferences, shared profiles, flight controls, target selections and weapon advice remain untouched. Unsupported calibration falls back to COLOR with a log diagnostic; render-state takeover fails closed until restart, matching the existing plugin safety boundary.
- Capture accepts the keyboard families listed above. Enabled native mappings, active native raw handlers, TGP action conflicts and known installed-mod KeyCode/KeyboardShortcut settings are checked. Conflicting or unsupported input explains the reason and keeps the old binding. Unknown raw-key handlers in other mods still require checking.
- F7-F11 can be used when their live conflict checks pass. Existing invalid saved keys are not silently changed. F1 may belong to ConfigurationManager. A newly captured, rejected or window-close key cannot trigger a TGP action until the panel closes and keys pass a neutral boundary.
- The installed ConfigurationManager 19.1 custom hotkey interface is used without packaging its DLL. Capture does not disable native game controls; pause the game while configuring controls if needed. Live game rendering and panel execution still require the smoke test below.

## 0.1.8 selected enemies, friendly symbols and native weapon status
- Known hostiles remain red hollow diamonds. A hostile already in the native selected-target list gains bright corner brackets, so selection is visible on the contact itself rather than only in the total. The brackets are a designation indicator, not weapon-seeker lock. They disappear when the native selection clears.
- Known friendly units use distinct cyan hollow squares. These come from the current HQ's declared faction-unit inventory and native known-position API. The own aircraft, neutral/no-faction, invalid, destroyed and offscreen units are excluded. Friendly symbols are display-only and never enter this mod's hostile Select/paint path.
- Friendly and hostile display budgets are independent, up to 128 of each nearest the view center. Adding friendlies does not change the previous hostile selection aperture, native priority ranking or 128-hostile candidate budget. Contact positions remain native radar/network knowledge, including last-known enemy locations; symbols are not proof of optical visibility.
- The existing native weapon advice now appears in a dedicated **top-center** row and blinks slowly at one cycle per second. Only this text blinks. SCAN/FOLLOW, selected count, contact markers and flight-control warning remain steady. Native OUT OF RANGE, TOO CLOSE, OUT OF ARC, TOO SLOW and permitted SHOOT keep their original wording and meaning. Unavailable/stale/hidden readiness is omitted, never converted to READY, FIRE or LOCK. The text mirrors native advice and its native calculation cadence, not an independent launch-readiness or hit guarantee.
- The header continues to show **SCAN / N SELECTED** or **FOLLOW / N SELECTED**. FOLLOW means the camera follows selected targets; it is not a seeker-lock claim. While scanning, **SEL** status/range/grid still refer to selected targets rather than the new reticle point. All 0.1.7 controls, view memory, PiP shortcuts and cockpit-screen options remain.

## 0.1.7 Scan/Follow, remembered view and PiP shortcut
- In ConfigurationManager, open **Targeting Pod Display → Keys**. Set **ScanFollow** and **PiPToggle** to distinct unused keys. Both default to **None**. Preserve your existing Fullscreen key (often F6). All supported keyboard families use the same live conflict checks. F1 may open ConfigurationManager and Observer may own F7-F11; neither is silently overridden.
- ScanFollow works in fullscreen with FullscreenMouseSlew=true. It does not require ManualSensor or the eight keyboard-sensor bindings/confirmation. Select a target normally, press ScanFollow to move the camera without removing it, add more with ordinary native Select, then press ScanFollow again to follow the group. Explicit Scan stays active after every addition, including when starting with no targets. Ordinary no-target fullscreen entry still follows the first selected target unless explicit Scan was chosen.
- The display reads **SCAN / N SELECTED** or **FOLLOW / N SELECTED**. In Follow, mouse movement is consumed without moving the sensor or steering the aircraft. A mode change waits for a held Select gesture to finish, displays **RELEASE SELECT**, and resolves the final selection in the current view before switching. Pressing the mode key again cancels the pending change. With no selected targets, returning to Follow is unavailable and Scan stays active.
- Native Cancel is unchanged: tap removes the newest target, hold clears all. Explicit Scan does not clear selections. Scanning range/grid and advice are labeled **SEL** and kept separate from the reticle: they describe native selected targets, not the point now under the crosshair. Selecting/following is not seeker lock. Aircraft controls and firing remain live.
- Normal fullscreen close/reopen remembers the last same-aircraft camera direction, zoom and explicit Scan state, even when the no-target presentation was torn down. With ScanGroundStabilization off, manual direction is relative to the aircraft or keeps optional inertial direction hold. With it on, 0.1.10 also preserves the value-only ground reference described above. Follow resumes current native target/group motion; its wheel override is restored only if selected identities/order are unchanged, including after the entry-neutral wait. If targets cleared while closed, the last actual view can seed manual scan. New aircraft/TargetCam, the owning scene unloading, or disabling the plugin clears the saved view. Memory is session-only, not written to the config or carried across game restarts.
- PiPToggle changes and saves **Presentation → PiPEnabled**. It does not close fullscreen or reset Scan/Follow. PiP stays hidden during direct fullscreen and uses the chosen setting when you exit. External configuration edits retain the normal session-release safety boundary.

## Cockpit screen option
- In the existing BepInEx ConfigurationManager panel, open **Targeting Pod Display → Presentation → DisableCockpitScreen**. This new setting defaults to **false** and hides only the proven cockpit target pane while this mod is enabled in a valid local cockpit context. Close the panel and resume cockpit gameplay to apply it under the normal UI guard. No separate menu or Observer change is required.
- Unlike `DisableCockpitScreenWhenPiPEnabled`, it works with PiP off and without an available pod presentation, once the native target texture and unique pane owner have initialized. It takes precedence over cockpit replacement. It does not initialize an unsupported native display or force a target-camera render.
- Turning it off restores the captured pane state unless the PiP-only option still applies. Landing mode, external view, UI/focus/context/scene loss and mod disable release suppression. A valid returning context may hide the pane again while the setting remains on. An external takeover of a held pane is respected instead of repeatedly overwritten.
- Radar, landing and clock screens and native targeting-camera logic stay active. This suppresses a pane draw, not the native sensor pass; no FPS improvement is claimed. Runtime verification is still required.

## 0.1.6 native target following and selection
- Selecting a target now returns the owned camera to the native target view and keeps it there. Mouse movement and legacy manual controls cannot detach Follow. The new explicit ScanFollow key temporarily allows scanning while preserving selections. Captured mouse motion is consumed rather than steering the aircraft or accumulating for later.
- Multiple targets follow the game's own group framing: the midpoint of their known-position bounds and native framing/FOV, not a new first-target-only camera. Existing target-list ordering and selections remain native. A changed selection resets only the pod's wheel-zoom override so the game can frame the new group; wheel zoom remains available afterward.
- Use the game's existing remapped **Cancel** control to unlock, just as in vanilla. A tap removes the newest selected target. Holding Cancel clears all selected targets. If any remain, native following continues. Once none remain, fullscreen returns to manual scanning; an explicit Scan session stays in Scan throughout. F6/your configured key or Escape still exits.
- Native target following and selection are not evidence that a weapon seeker has locked. Native weapon advice remains authoritative.

## Retained known-contact markers and native selection
- Red diamonds now use the game's faction tracking database and native known-position query. Contacts can appear through terrain/buildings when already known to the native radar/network, matching that information model. Unknown contacts are never discovered by a world scan. Old/uncertain contacts use their native last-known position and a steady muted marker, not a flashing optical visibility test. No current hidden position is substituted.
- In fullscreen, aim the center crosshair near a red diamond and use your ordinary remapped **Select** control. A tap adds the highest-priority eligible known hostile within 100 fullscreen camera pixels of the center, using native weapon opportunity/threat and tracked range in the priority calculation. A native timed hold paints eligible contacts in that aperture using native weapon-opportunity filtering and native marker order. One selection sound and target-list update is emitted for a group. Existing targets are retained; exclusions and duplicate checks apply. Ordinary selection returns to native target/group following on the next normal camera tick; explicit Scan keeps its camera view until you toggle back. This is designation, not seeker lock or firing.
- Only fullscreen redirects Select. PiP remains passive. Mouse buttons other than this native selection dispatch and firing remain live. Entry waits for Select neutral before accepting a new gesture. On a normal exit, an in-progress Select gesture is suppressed only for the same aircraft/HUD/input owner until release; UI/focus/owner loss cancels the capture. Hook ownership failures exit fullscreen instead of selecting at hidden cockpit aim.
- `[Presentation] DisableCockpitScreenWhenPiPEnabled = true` optionally hides only the proven cockpit target pane while a current PiP frame is displayed. Default is **false**. PiP disable, fullscreen, landing/camera transitions, context loss and mod disable restore the pane. Uninitialized native displays retry; an actual takeover of a held pane is not repeatedly overridden.
- This option saves the cockpit target-pane draw and avoids replacement binding. Cockpit and PiP already share one owned render, so it does **not** eliminate a second sensor camera pass. Native targeting, radar/landing displays and targeting-camera logic remain active. No measured FPS improvement is claimed.

## Retained 0.1.4 manual scanning
- Press your existing fullscreen key (for example F6) without selecting a target. The initialized native camera/mount supplies rendering settings, while an independent COLOR camera provides the view. A rendered native target texture is no longer required for manual fullscreen.
- Move the mouse to scan while no target is selected. If targets are already selected, fullscreen follows the native target/group view and ignores manual camera movement until you explicitly choose Scan or native Cancel clears the selection. The existing optional ManualSensor key applies only with no selected targets.
- The mouse wheel still zooms. Manual FOV supports 0.1 to 60 degrees; normal horizontal Scan is bounded to ±135° from the current aircraft nose. The existing ±85° vertical slew bounds remain relative to the entry view (or boresight after recenter). These are viewing limits, not claims about real pod hardware.
- F6/your configured fullscreen key or Escape exits. Ordinary fullscreen exit briefly waits for neutral mouse movement before restoring its native mappings; focus/UI/ownership loss restores immediately. Keyboard/joystick flight control and firing remain live. The ordinary Select action has the fullscreen routing described above; other mouse buttons retain their native behavior. This is not autopilot.
- Shared input-behavior changes during capture now restore the unchanged owned mouse/wheel mapping flags before exiting. Actual element reassignment remains protected from stale restoration.
- Only exact physical Rewired mouse X/Y element mappings are leased. Entry waits for a neutral input boundary; unsupported processed-axis modes refuse entry with a log diagnostic. Stored virtual-stick steering is cleared once at capture/release so an old mouse turn is not replayed. Alternate device inputs are rebuilt by the native loop. No whole map/player/action is disabled.
- Hollow red diamonds project native known hostile positions into the current owned camera view. Friendly contacts use their separate cyan layer; neutral, unknown, destroyed, offscreen and stale-frame data are excluded. They clear during aftermath. They are radar/network information, not proof of optical visibility or a weapon lock.

## Previous 0.1.3 runtime corrections
- User screenshots confirmed cockpit replacement and direct fullscreen in 0.1.2. This update matches the owned camera to the exact native URP renderer, native culling mask minus UI-only exclusions, depth/color requirements, shadows, HDR/MSAA and clipping settings. It also matches native output format/sample count. These remove proven mismatches; the reported partial magenta helipad still needs a runtime retest, not a promise of a verified shader fix. One diagnostic per render-contract change records the actual native/owned settings.
- Fullscreen leases only Canvas rendering flags beneath the verified native FlightHud canvas, including the minimized map and weapon/target graphics. HUD scripts and targeting/firing logic remain active. Shared menu/chat/expanded-map roots are rejected. External canvas ownership changes exit fullscreen rather than suppressing the successor again.
- Fresh native OUT OF ARC/TOO SLOW and other inspected warnings remain visible even if the native hint Graphic has stayed disabled. SHOOT retains native visible intent and freshness/owner checks. No invented FIRE or lock permission.
- TGP and selected-AGM reticle lines are bolder and longer; text size/layout is unchanged.
- Fullscreen mouse-wheel zoom uses only the owned camera. With FullscreenWheelZoom=true (default), entry waits for neutral wheel/action state and a verified Rewired pre-source boundary. Only vertical-wheel element mappings are leased; steering, firing, other mouse axes/buttons and alternate keyboard/joystick bindings are not globally blocked. Exit drains the old wheel sample before restoring; hard UI/focus/owner loss restores immediately. Digital-smoothed/unknown bindings refuse entry with a diagnostic. Third-party raw wheel readers cannot be automatically isolated.

## Existing capabilities
- Fixes cockpit discovery when intact physics parts are normally unparented. Only current-aircraft registered, attached parts and a unique initialized cockpit presentation qualify. Ambiguous, damaged or unsupported surfaces remain native. Landing displays and shared materials are not modified.
- Clean owned camera follows native targeting-camera pose/FOV without copying its UI stack. Compact baked-green original symbology replaces oversized white labels. Aircraft attitude uses the aircraft cockpit frame, the clock is explicitly UTC, and RNG is the native selected-target distance, not a reticle ground scale or manual-camera measurement.
- Fullscreen enables an owned camera rendering directly to the main display, following the game renderer's render-scale/display settings. It temporarily disables only the captured native scene/cockpit Camera render components. Camera controllers and simulation continue. Exit/fault/context loss restore native rendering. The proven native aircraft HUD canvas is suppressed separately; unsupported/shared UI layouts remain untouched and diagnosed.
- Optional passive right-center PiP shares the one offscreen camera/presentation output with the cockpit. During direct fullscreen, the offscreen pass and cockpit/PiP presentation are suspended. The camera pose is retained across transitions; output aspect changes to the screen.
- Native kill notification for the uniquely watched target can trigger a live view of its last known native tracking position for 3 seconds. Duration is configurable from 0 to 10 seconds. No frozen screenshot, new designation or weapon command is used. Target/weapon hints clear and AFTERMATH is shown. Ordinary deselection, despawn and cleanup do not prove a kill. New target/manual control/context loss cancels it.
- Manual COLOR camera provides dedicated-key slew, zoom, recenter and inertial direction hold. Camera motion alone does not designate targets, stabilize a ground point or control the aircraft; only the explicit native Select action designates in fullscreen.

## Honest limits
- **Not autopilot. Aircraft controls and firing remain live.** No flight-axis writes or whole-map/player suppression. Only the requested fullscreen physical mouse X/Y and vertical-wheel mappings are temporarily leased. Captured native cached axes are neutralized once at each mouse-control handover; normal input processing then continues.
- **No physical heat-signature thermal.** The IR toggle copies read-only native grading and scoped fog behavior for owned views; visual equivalence needs runtime checking. It is labeled IR (GAME). Failure returns to truthful COLOR or releases the owned view rather than claiming IR.
- Selected target is not seeker lock. No invented acquisition, laser-active state, launch envelope or impact cue. Laser status is LSR N/A. Fresh native weapon hints retain their native meaning.
- The requested green long split crosshair and three lower ticks appear only for a live native selected target with a conservative surface-missile role. The label is TARGET SELECTED, not seeker lock. Clearing selection or entering aftermath removes it. The surface score must be positive and exceed air/missile scores; this is a presentation-role inference, not an AGM enum. Ambiguous roles use ordinary TGP presentation. Weapon names remain native; the ticks are decorative viewing references, not a launch/ground-range scale.
- Fullscreen selection intentionally uses only known hostile contacts projected into the pod camera, not hidden cockpit-screen coordinates, friendly/neutral contacts or a world scan. The displayed candidate set is bounded to the 128 known hostiles nearest the view center. Paint is bounded to 128 additions per native hold event (the native weapon-station target packet capacity); vanilla can retain a larger internal list. No existing selections are cleared to enforce this bound.
- The native targeting camera and mount must already be initialized by the aircraft. Manual fullscreen does not need a selected target or a previously rendered native output. Unsupported aircraft setup and expanded target search are not performed.
- Native-follow adds a scene render up to 1024 pixels on its long edge, preserving native texture aspect outside fullscreen. Fullscreen replaces main/cockpit geometry rendering but the native target-camera pass may continue. Performance and exact postprocessing/renderer feature equivalence are unmeasured.
- The original compact alphabet supports limited characters. The raster preview tests verify geometry/colors, not actual Unity blending.

## Install or update, preserving your config
1. Close the game. Replace only `BepInEx/plugins/TargetingPodDisplay/TargetingPodDisplay.dll`. Do not install reference DLLs or another Observer copy.
2. Keep your existing `BepInEx/config/local.nuclearoption.targetingpoddisplay.cfg`. Missing new settings are added when the plugin loads. The supplied config is an example, not a required replacement.
3. Set `[General] Enabled = true`; use `ReplaceCockpit = true` if desired. Defaults remain opt-in false.
4. Set `[Keys] Fullscreen` and optional `ManualSensor` through Bind in the shared menu or ConfigurationManager. Main keys and modifier companions are saved together. Inspect overlap warnings; F6/F5 are examples, not reserved assignments.
5. Optional keyboard-manual entry also requires `ConfirmNoOtherModUsesSensorKeys = true` after checking your other mods. Rewired keyboard-map collisions are checked automatically; other mods' raw key handlers cannot be proved absent.
6. Default manual keys: arrows slew, PageUp/PageDown zoom, Home recenter, End inertial direction hold. All eight can be rebound using the current binding editor. Inspect overlap warnings; unknown/unreadable inventories still refuse.
7. `[Presentation] FullscreenWheelZoom = true` enables isolated fullscreen scroll zoom and neutral-entry gating. Stop scrolling before entry. If unsupported bindings are reported, explicitly setting it false retains the prior fullscreen behavior **without pod scroll zoom; native scroll controls remain live**. There is no automatic fallback.
8. `[Presentation] FullscreenMouseSlew = true` (new default) enables isolated mouse scanning and no-target entry. Keep `ManualSensor = None` if you only want mouse control; no keyboard-sensor confirmation is needed. Stop moving/scrolling briefly when entering. False explicitly restores prior native mouse behavior and disables automatic no-target entry; no mouse-slew fallback is attempted. Other mods that read raw mouse movement outside Rewired cannot be automatically isolated.
9. `[Presentation] PiPEnabled = true` enables the passive right-side view. In the existing ConfigurationManager panel, set `DisableCockpitScreen = true` to hide the cockpit target pane independently of PiP, or `DisableCockpitScreenWhenPiPEnabled = true` to hide it only while PiP is active. Both default false and leave native targeting logic active. Editing the same saved config entries also works; keep the rest of your current config.
10. Aim at a known hostile diamond in fullscreen and use your existing game Select binding, not a new hardcoded mouse button. Tap uses native priority ranking; timed hold uses native paint filtering. Native Cancel tap removes the newest selection, and hold clears all so mouse scanning can resume. `AftermathSeconds = 3` is the default; 0 disables aftermath.

External configuration changes to keys/confirmation/general activation invalidate the session; release both old and new keys before reentry. Pause/map/chat/focus loss, external view, owner/scene change and landing mode release the view. Reentry is explicit. Observer 0.5.1 idle/hold can coexist; its fullscreen/drain/modal takes priority. Unknown Observer identity blocks interactive pod views, not unrelated plugins generally.

## Build and checks
Private references are compiler inputs only, never executed, committed or redistributed.

```sh
dotnet build src/TargetingPodDisplay -c Release -p:GameRefs=/absolute/private/refs -p:LoaderRefs=/absolute/BepInEx/core
dotnet run --project tests/TargetingPodDisplay.Tests
dotnet run --project tests/Aftermath.Tests
dotnet run --project tests/WheelLease.Tests
dotnet run --project tests/WheelAdapter.Tests
dotnet run --project tests/MouseAdapter.Tests
dotnet run --project tests/ManualScan.Tests
dotnet run --project tests/HostileIndicator.Tests
dotnet run --project tests/TargetSelection.Tests
dotnet run --project tests/TargetSelectionAdapter.Tests
dotnet run --project tests/TargetFollow.Tests
dotnet run --project tests/OptionalViewKeys.Tests
dotnet run --project tests/Presentation.Tests
dotnet run --project tests/NativeHint.Tests
dotnet run --project tests/SensorViewMemory.Tests
dotnet run --project tests/PipScreenLease.Tests
dotnet run --project tests/overlay-raster
dotnet run --project tests/Observer.Tests
python3 -m unittest discover -s tests -p 'test_*.py'
```

Read `TARGETING_POD_SMOKE_TEST.md` before describing a runtime feature as validated.
