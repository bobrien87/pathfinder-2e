---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Magical]]"]
price: "{'gp': 600}"
usage: "attached-to-crossbow-or-firearm-firing-mechanism"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This device replaces the attached firearm's normal firing mechanism (normally, most guns use a flintlock or matchlock firing mechanism). When the firearm's wielder fires the weapon, a small rune etched on a piece of stone affixed inside the mechanism releases a magical spark that's propelled through the firing mechanism and into the firearm, launching its bullet. An *underwater firing mechanism* allows the attached firearm to be fired underwater or in other conditions that would normally prevent the ignition of black powder. Attaching an *underwater firing mechanism* to a firearm takes 1 hour, though this time can overlap with the standard time required to maintain and clean your firearm to prevent misfires.

**Source:** `= this.source` (`= this.source-type`)
