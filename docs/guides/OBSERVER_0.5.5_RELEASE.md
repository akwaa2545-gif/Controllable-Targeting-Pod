# Observer 0.5.5 and Targeting Pod Display 0.1.15

## Install and open settings

Close the game. Back up the old DLLs and both configs. Replace each DLL under BepInEx/plugins with exactly one copy of this pair. Keep existing configs; examples are not upgrade files. Check the startup log for both versions. Older TGP builds do not recognize this Observer binary.

Enter a supported local offline cockpit, pause with Esc, then press the configured Observer Panel shortcut (default F8). The independent menu is hosted by Observer and remains accessible when Observer viewing is disabled. It offers separate Observer and TGP sections, scrollable settings and bindings. A missing or unsupported TGP is explained rather than edited. The menu does not require ConfigurationManager. TGP installed alone retains its config/ConfigurationManager controls.

Defaults remain Observer F8 panel, F9 PiP, F10 next missile, F11 fullscreen, F7 reset orbit and Ctrl+left-click MapWatch. Your configured values take precedence. Automatic own-launch viewing and Flight Hold remain separate opt-ins. The TGP fullscreen/optional shortcuts remain opt-in rather than taking over new keys.

If the Panel shortcut is cleared, open ConfigurationManager if installed, or close the game and restore `Panel = F8` in the `[Keys]` section of `BepInEx/config/io.github.nuclearoption.observer.cfg`. No hidden fallback hotkey is installed. The menu shows this recovery path before rebinding.

## Binding workflow

The controls list uses ACTION and ASSIGNED KEYS columns. Select an action, then Bind. The editor lets you choose Key only or a special input: a detected mouse button, Left/Right Ctrl, Left/Right Shift or Left/Right Alt. Choose Alone or Combine. Combine waits for an ordinary keyboard key; Alone uses the selected special. Clear unbinds, and Cancel leaves the existing binding unchanged. Details explains the action. Each accepted change is saved without a separate global Apply step.

The selected-action editor, category organization and conflict presentation are Arma-inspired. These are original controls for these two mods, not copied game assets, multiple alternate binding slots, double-tap presets or a full Arma input system.

Mouse0 is left, Mouse1 right, Mouse2 middle, and Mouse3–6 extra buttons if the hardware and Unity report them. Wheel/axes/controller bindings are not added. Physical Minus, Shift+Equals, KeypadPlus and KeypadMinus remain supported. Keyboard layout, NumLock, Fn/media keys and OS shortcuts affect what reaches Unity. Escape cancels; unsupported Windows/Command/AltGr and legacy shifted-character aliases remain explained refusals.

Older keyboard-only, modifier-chord and MapWatch settings remain valid. Observer preserves its existing combined Ctrl/Shift/Alt family matching: either physical side satisfies that modifier in a chord. Alone uses the selected physical side. TGP modifier companions remain exact-sided. The selected side is preserved in saved settings; the editor explains this runtime distinction. TGP retains each original KeyCode entry and stores its modifiers separately in `[KeyModifiers]`, using `Section.Action` names such as `Keys.Fullscreen`. Empty means no modifiers. Existing raw TGP configuration is backed up once to the same path with `.pre-mouse-chords.bak` appended before binding entries. An existing backup is not overwritten. BepInEx can normalize invalid enum text while loading; this backup preserves the original. Invalid numeric/companion values are retained and diagnosed instead of silently remapped.

## Activation and input ownership

Discrete special-alone actions use a fresh clean press/release, not the initial down edge. Another key/button, lost focus, missing eligible context or interrupted polling cancels that tap. This prevents a standalone modifier action also firing when that modifier starts a chord. Special-alone continuous sensor/zoom controls use a fresh eligible press and stop/cancel when another input joins. Holding that special before entering the view must not start a new action. Existing ordinary keyboard-held controls keep their prior held behavior.

Observer mouse-alone actions and mouse-related Panel requests wait for their gesture and neutral boundary. Observer mouse-plus-keyboard view shortcuts still activate on the keyboard edge while the selected mouse button is held. TGP mouse-related toggles defer through mouse/native Select release and neutral boundaries. A mouse-only Panel binding does not close the menu when clicking its controls; use Close. Capture's opening, picker and save clicks cannot replay into an action, even when saving the same value. ConfigurationManager visibility and the dedicated menu suspend affected gameplay actions and drain inputs after closing.

For MapWatch, bind a keyboard key/chord and hold it while left-clicking a missile in the native map. A standalone Ctrl/Shift/Alt or Mouse1–6 special can likewise be held with the actual left-click trigger. Z alone never Watches. Plain Mouse0 alone is refused because it cannot be separated from ordinary native map selection. Existing Ctrl+Mouse0 remains supported. Readiness, top-icon ownership, cancellation and paired release checks remain in place.

These safeguards are not exclusive global input ownership. Native click, keyboard and other-mod actions remain live; a shared mouse button can fire, free-look, select or open a map command menu. Existing TGP fullscreen X/Y and wheel leases do not suppress all mouse buttons. Use the persistent overlap details before choosing a binding.

## Conflict feedback

Both mods allow recognized overlaps with known configured actions/native mappings/handlers and supported mod inventories, with a visible warning and named details. The Observer scanner also reads the paired TGP's exact modifier-companion schema rather than guessing at arbitrary string settings. They do not silently choose another key. Different chords sharing an input can be warned conservatively. Unknown/unreadable inventory, unsupported binding shape and unsafe camera/input context still refuse. An absence of a detected overlap is not proof that another mod has no undeclared raw input handler.

## Retained features and validation boundary

Observer's main-display fullscreen continues to remove its old 1280×720/20 Hz fullscreen cap while following the game's URP render scale, AA and display settings. PiP retains 480×270/20 Hz. Flight Hold's native part/engine checks, precise refusal messages, damage/ownership checks and opt-in behavior remain. A Hold refusal is not silently disabled or bypassed. See the 0.5.4 guide for those unchanged corrections.

TGP retains native selection/group Follow, manual Scan, ground AREA, rear-sector stop, IR, remembered view, friendly/hostile indicators and cockpit/PiP behavior. Its input adapter now supports the shared binding workflow. Native Select and Cancel still own designation/deselection; view changes must not redirect a held Select into a different camera aim.

TGP 0.1.15 accepts this exact Observer 0.5.5 artifact plus the previous delivered 0.5.1–0.5.4 exact version/hash pairs. Unknown rebuilds and crossed version/hash pairs remain refused. The Observer-hosted settings bridge independently verifies the installed TGP identity and expected config definitions before editing them.

Authored policy/adapter/UI tests, exact-reference builds, loader persistence checks and independent review do not establish live Unity/GPU/hardware behavior. Run the smoke checklist in a safe offline mission. No live game validation is claimed, and the original user-specific Flight Hold refusal still needs an actual retest.
