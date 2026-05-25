---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Magical]]"]
price: "{'gp': 900}"
usage: "etched-onto-metal-armor"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This rune alters the magnetic polarity of your armor, making other metal items drawn to it ever so slightly. You can amplify the magnetic power of the armor to keep another creature from getting away from you.

**Activate**`pf2:1` (concentrate)

**Frequency** once per hour

**Requirements** A creature adjacent to you is made of metal or wearing metal armor

**Effect** You magnetize your armor. If you or the target attempt to move away from one another, treat each square as difficult terrain. This doesn't affect movement that keeps you the same distance from one another, so you could still [[Step]] if you remained adjacent to the target. This effect ends once either of you is no longer adjacent to the other at the end of an action.

This Activation might work on some creatures partially made of metal, such as those with metal scales, as determined by the GM. Likewise, the GM might determine some metal creatures are non-magnetic, depending on the metal they're made of.

**Source:** `= this.source` (`= this.source-type`)
