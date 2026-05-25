---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Fortune]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 20}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` Interact

This potion holds a tiny, tightly wrapped scroll and tastes like paper. Upon drinking it, you gain a burst of insight into your immediate future—and how to potentially avoid it. When you attempt a saving throw, you can roll twice and use the better result. The potion's magic ends when you make use of this effect, or after 1 minute. You then become immune to *bottled omen* potions for 24 hours.

> [!danger] Effect: Bottled Omen

**Source:** `= this.source` (`= this.source-type`)
