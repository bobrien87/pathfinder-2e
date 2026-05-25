---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 40}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Lost Omens Tian Xia Character Guide"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** Tian Xia origin

**Activate** `pf2:1` (concentrate)

Symbols of good fortune and luck are carved on this thin, square wooden plaque. It smells of sandalwood from the blessings placed upon it. After activation, for the next minute, you can sense attacks from undead. You aren't [[Off Guard]] to [[Hidden]], [[Undetected]], or flanking undead of your level or lower, or undead of your level or lower using surprise attack. However, they can still help their allies flank.

**Source:** `= this.source` (`= this.source-type`)
