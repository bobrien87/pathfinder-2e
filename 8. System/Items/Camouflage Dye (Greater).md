---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Alchemical]]", "[[Consumable]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Camouflage dye uses a variety of alchemically treated paints and crushed crystals to make the user particularly hard to distinguish from their surroundings. When you Activate the dye by sprinkling it on yourself or a creature within reach, the target and its clothing change colors, blending into their surroundings until the target makes a sudden movement. The target can [[Hide]] or [[Sneak]] without cover or concealment for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
