---
type: item
source-type: "Remaster"
level: "0"
traits: ["[[Kickback]]", "[[Repeating]]"]
price: "{'gp': 6}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Like the one-handed air repeater, this thin-barreled firearm uses a container of pressurized air instead of black powder to propel small metal pellets from an attached cartridge. The long air repeater has better range and ammo capacity than the one-handed variant, though it still lacks significant stopping power. A typical long air repeater magazine holds 8 pellets.

**Source:** `= this.source` (`= this.source-type`)
