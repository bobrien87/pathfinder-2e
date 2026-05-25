---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 85}"
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

Quenching potion is a clear liquid that tastes like fresh, cool spring water. Drinking this potion or pouring it over yourself completely hydrates you and cleanses your system. Immediately attempt a flat check to end any persistent acid, fire, poison, or void damage affecting you, and attempt a new saving throw against any poison affecting you. Poison can't progress to a worse stage due to this saving throw. The potion counts as a particularly appropriate type of help against persistent acid, fire, poison, and void damage.

**Source:** `= this.source` (`= this.source-type`)
