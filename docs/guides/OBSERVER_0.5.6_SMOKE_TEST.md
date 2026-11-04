# Observer 0.5.6 / TGP 0.1.16 live smoke checklist

Not yet run in the game. Use a backed-up offline mission and existing configs.

1. Close the game, replace both DLLs once each, restart, and confirm 0.5.6 / 0.1.16 in the startup log. Keep your configs and backups. An already faulted 0.5.5 process cannot recover without restart.
2. In a supported cockpit, pause with Esc, close native Settings/ConfigurationManager, release mouse buttons and press Panel (default F8). The panel should appear after canvas readiness without the old immediate shield refusal. Try with Observer viewing enabled and disabled.
3. Confirm clicks, wheel and native keyboard submit cannot activate the game menu through the settings panel. Close/reopen repeatedly; confirm Observer and TGP tabs, key capture, Cancel/Clear and saved values still work. Changing settings must not change the native menu or fire a weapon. Keep menu weapon safety enabled.
4. Test focus loss, native-menu closure and scene/aircraft changes during opening and while open. The panel must disappear without leaving an invisible blocker. If initialization cannot complete, it must remain closed and report its depth/culling or top-hit reason rather than hanging indefinitely.
5. Enable Observer if desired, select a live missile using Next (F10) or the menu, and show PiP (F9). Auto-show own launch remains opt-in and applies only to future new missile registrations. Check that PiP updates rather than freezing.
6. Enter missile fullscreen (F11), orbit/reset, return to PiP and repeat. If automatic Flight Hold refuses because airspeed/stall/overspeed margins are unsafe, treat that as an unchanged safety guard, not a reason to bypass it.
7. During fullscreen, change window size/resolution and test ordinary focus/menu transitions. Confirm native view/HUD return correctly and no owned camera or input blocker remains. Test the installed mod set as well as a minimal setup.
8. If Observer disables again, retain the new full LogOutput.log. The new fullscreen diagnostic should name target texture, target display, viewport or aspect and include the relevant expected/actual values. Include the display/window mode, exact action and screenshot. The candidate is not confirmed until this live path works.
9. Confirm paired TGP settings and ordinary Scan/Follow, IR, PiP, cockpit options, native target selection and input restoration are unchanged. Use the retained [TGP smoke checklist](TARGETING_POD_SMOKE_TEST.md) for broader coverage.
