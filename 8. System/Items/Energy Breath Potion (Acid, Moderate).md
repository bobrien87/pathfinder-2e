---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Acid]]", "[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 400}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

Distilled from the energy of dangerous spells, an energy breath potion grants you the Energy Breath action for 1 hour after you imbibe the concoction.

**Energy Breath** `pf2:1` You create a @Template[line|distance:30] of acid which deals @Damage[6d6[acid]|options:area-damage] damage. All creatures in the area must attempt a DC 29 [[Reflex]] save.

After you use Energy Breath, you can't do so again for 1d4 rounds.

**Source:** `= this.source` (`= this.source-type`)
