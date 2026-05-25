---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Consumable]]", "[[Holy]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 2000}"
usage: "affixed-to-weapon"
bulk: "—"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Usage** affixed to a weapon

**Activate** `pf2:f` (concentrate)

**Trigger** You deal damage using the affixed weapon to a creature that has the unholy trait or that you witnessed harm an ally, an innocent, or a noncombatant within the last minute.

This long, fire-red feather smolders from the weapon it adorns. When you activate the feather, the creature you damaged burns with sacred light. The creature must succeed at a DC 35 [[Will]] save or take a –2 status penalty to AC and saving throws and reduce its resistances by 10. These effects last until the end of your next turn. This item has no effect on a creature with the holy trait.

**Source:** `= this.source` (`= this.source-type`)
