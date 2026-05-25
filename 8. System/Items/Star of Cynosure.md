---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Magical]]", "[[Talisman]]"]
price: "{'gp': 175}"
usage: "affixed-to-armor"
bulk: "—"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:f` (concentrate)

**Trigger** You attempt a Will save against a mental spell, but you haven't rolled yet

**Requirements** You have master proficiency in Will saves.

Found throughout Golarion, these star-shaped talismans of whalebone scrimshaw are carved by the Erutaki people from the Crown of the World. They are popular with adherents to the cult of Desna, who believe the talismans protect their dreams.

When you activate this talisman, you gain a +2 status bonus to saves against spells with the mental trait for 1 minute. On the triggering save, if the outcome of the roll is a failure, you get a success instead, or if the outcome is a critical failure, you get a failure instead.

> [!danger] Effect: Star of Cynosure

**Source:** `= this.source` (`= this.source-type`)
