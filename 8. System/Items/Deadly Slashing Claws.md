---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Graft]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 320}"
usage: "implanted"
bulk: "—"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Sharp claws have been grafted to your hands or feet, perhaps extending from your knuckles or the tips of your toes. You gain a claw unarmed attack that deals 1d6 slashing damage. These claws are in the brawling group and have the agile, deadly d8, and finesse traits.

**Source:** `= this.source` (`= this.source-type`)
