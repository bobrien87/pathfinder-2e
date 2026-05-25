---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Consumable]]", "[[Magical]]", "[[Oil]]"]
price: "{'gp': 30}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

A *restful salve* is a compound that can be applied to the skin to prevent undeath. If applied to a fresh corpse, the corpse doesn't decay, nor can it be transformed into an undead or otherwise controlled until the sun rises the next morning. If applied to a living creature, this salve lasts for only 1 hour due to the body's natural excretions. For that duration, the salve wards off effects that would cause undeath upon dying.

**Source:** `= this.source` (`= this.source-type`)
