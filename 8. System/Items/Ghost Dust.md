---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Consumable]]", "[[Illusion]]", "[[Occult]]", "[[Talisman]]"]
price: "{'gp': 1800}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** A (concentrate)

**Requirements** You are trained in Stealth

This small vial is filled with a grayish-green dust rendered from dried ectoplasm. When you activate the dust, it casts a 4th-rank [[Invisibility]] spell on you. You may then Stride or Step. You can instead Burrow, Climb, Fly, or Swim if you have the corresponding Speed.

**Source:** `= this.source` (`= this.source-type`)
