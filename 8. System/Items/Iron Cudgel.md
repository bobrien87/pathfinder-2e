---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 900}"
usage: "affixed-to-melee-weapon"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to a melee weapon

**Activate** A (manipulate)

This miniature club is typically affixed to a weapon by an iron chain. When you activate the cudgel, you use [[Brutal Finish]], as the fighter feat. You must meet the normal requirements, including those of the press trait.

If you have the Brutal Finish feat, add an additional weapon damage die on a success or a failure to the normal results.

**Source:** `= this.source` (`= this.source-type`)
