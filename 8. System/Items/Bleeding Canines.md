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

Some of your teeth have been replaced with those of a larger meat-eating predator. You gain a jaws unarmed attack that deals 1d8 piercing damage. These jaws are in the brawling group. Whenever you score a critical hit with your jaws, your target takes 1 persistent bleed damage per weapon damage die.

**Source:** `= this.source` (`= this.source-type`)
