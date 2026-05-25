---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]", "[[Vitality]]"]
price: "{'gp': 75}"
usage: "applied-to-armor"
bulk: "—"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You Cast a Spell that restores Hit Points to another creature.

This simple religious symbol bolsters you when you help others. When you activate it, you gain a number of temporary Hit Points equal to your level plus the rank of the spell you cast. These temporary Hit Points last for 1 minute.

> [!danger] Effect: Impelling Symbol

**Source:** `= this.source` (`= this.source-type`)
