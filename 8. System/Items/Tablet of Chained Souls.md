---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Cursed]]", "[[Magical]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Half-formed, unreadable runes drift across this weathered stone tablet, which resembles a tombstone too eroded to be legible. Created by a long-dead order of scholars dedicated to Pharasma, the *tablet of chained souls* can be a powerful tool in laying uneasy spirits to rest, but its magic exacts a heavy cost.

**Activate—Spirit Carving** `pf2:3` (concentrate, manipulate)

**Effect** You present the tablet to a ghost or lay it on a haunted site. The tablet's words resolve into a cryptic but accurate clue about the spirit's unfinished business. Upon reading the tablet's words, you're subject to a [[Geas]] that requires you to right that wrong and lay the ghost to rest. If you die without completing the task, you become a ghost, cursed to remain until another recovers the tablet and discharges your duty.

**Source:** `= this.source` (`= this.source-type`)
