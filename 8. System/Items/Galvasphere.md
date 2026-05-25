---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 20}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (manipulate)

A galvasphere animates a corpse to motion via electricity, rather than dark magic. When you Activate the galvasphere by inserting it into an adjacent intact Medium or Small humanoid corpse, the corpse animates as a galvaheart zombie for 1 minute. The galvaheart zombie has the statistics of a zombie shambler except that it's a construct instead of an undead, isn't unholy, can't be harmed by vitality energy, and is the same size as the corpse (Medium or Small). The zombie is your minion and performs the actions you choose when you Command it. If you don't Command it, it takes no action, twitching in place as the electricity that animates it slowly expends itself.

**Source:** `= this.source` (`= this.source-type`)
