---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'gp': 900}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Season of Ghosts Hardcover Compilation"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This folding handheld paper fan appears blank when first found, but if the wielder unfolds its leaves as an Interact action, they display an ink-brush painting of the wielder's choice. The fan must be closed and opened again to display a different painting. While held, the *fan of falling words* grants you a +2 item bonus to Performance checks to act or perform comedy, orate, or sing.

**Activate—Whispered World** `pf2:3` (concentrate, manipulate)

**Frequency** once per day

**Effect** You manifest the tapestry of your words, causing the image you depict on the fan to leap off its leaves. The fan casts illusory scene to your specifications (DC 27 [[Will]] save). While this only takes 3 actions to perform (as opposed to the spell's normal 10 minutes of casting), the effect has no range, and the @Template[type:burst|distance:50] it creates is centered on you.

**Source:** `= this.source` (`= this.source-type`)
