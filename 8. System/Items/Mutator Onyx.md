---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Earth]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A mutator onyx is a jet-black, alien mineral first found within the walls of the Onyx Citadel but is now used primarily as an alchemical teaching or experimentation tool within Oprak. Pressing the gem into a solid, unattended inanimate object with Hardness 5 or less transforms that object's surface into a curious syrupy, liquid-like state, reducing its Hardness to 0. One mutator onyx can transform up to a 5-foot cube. After 10 minutes, the matter reverts to its solid state, regaining its Hardness.

**Source:** `= this.source` (`= this.source-type`)
