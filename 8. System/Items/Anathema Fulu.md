---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Consumable]]", "[[Fulu]]", "[[Magical]]"]
price: "{'gp': 250}"
usage: "affixed-to-an-object-or-structure"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Duration** 1 hour

First used by celestial-touched nephilim of Tianjing to weaken qlippoth, an anathema fulu comes in four pieces, one placed in each cardinal direction. Choose one of the following traits when activating the fulus: celestial, elemental, fey, fiend, monitor, or undead. If a creature with that trait starts its turn in the area, it must succeed at a DC 30 [[Fortitude]] save saving throw or become [[Sickened]] 2 until the start of its next turn. On a critical success, the creature becomes temporarily immune to any anathema fulus for 1 hour. Regardless of the save result, if you subsequently cast [[Banishment]] on such a creature in the area, the creature takes the –2 penalty described in that spell for adding a special cost of an object that's anathema to that creature. The fulu acts as that object; you don't need to add it. If a creature affected by this penalty rolls a saving throw against *banishment*, the caster can use a free action to force the result one step lower. Doing so burns the whole fulu out, ending the effect. If any of the fulu's pieces are moved or destroyed after activation, the effect ends.

**Source:** `= this.source` (`= this.source-type`)
