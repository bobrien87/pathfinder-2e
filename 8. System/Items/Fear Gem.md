---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Emotion]]", "[[Fear]]", "[[Magical]]", "[[Mental]]", "[[Talisman]]"]
price: "{'gp': 20}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate)

Dark smoke seems to writhe within this obsidian gem. When you activate the gem, make a melee Strike. If you hit and deal damage, the target is [[Frightened]] 1, or [[Frightened]] 2 on a critical hit.

If you have the [[Intimidating Strike]] feat, increase the frightened condition value caused by the Strike to [[Frightened]] 2, or [[Frightened]] 3 on a critical hit.

**Source:** `= this.source` (`= this.source-type`)
