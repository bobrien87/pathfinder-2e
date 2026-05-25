---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Earth]]", "[[Magical]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

You can throw a *stalagmite seed*, use it as a sling stone, or pack it into firearm ammunition. When you use the seed, you aim it at a 5-foot square rather than a specific target. Stalagmites of assorted sizes erupt in the square the seed lands in, dealing 6d6 piercing damage to any creature within that space (DC 23 [[Reflex]] save). The stalagmites remain for 1 minute, creating difficult terrain in that space, before they crumble into dust.

**Source:** `= this.source` (`= this.source-type`)
