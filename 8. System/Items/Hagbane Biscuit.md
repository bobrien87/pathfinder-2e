---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Alchemical]]", "[[Consumable]]", "[[Processed]]"]
price: "{'gp': 10}"
usage: "held-in-one-hand"
bulk: "—"
source: "Pathfinder Adventures: Troubles in Grayce"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

This gingerbread biscuit is stamped in the shape of a menacing witch, her features decorated with anise and fennel seeds. When you eat the biscuit, its sharp spices warm your body for 10 minutes, granting you a +1 status bonus Perception checks to pierce a hag's disguise, to skill checks to [[Recall Knowledge]] about hags, and to saving throws made against hags' abilities and spells. During this time, weapons you wield count as cold iron for any physical attacks made against hags.

The biscuit tastes especially bitter to hags, changelings, and other hag-related creatures (such as a sorcerer with the hag bloodline). If such a creature attempts to eat the biscuit, they must succeed at a DC 18 [[Fortitude]] save or it fails and wastes the action (and is [[Sickened]] 1 on a critical failure).

**Source:** `= this.source` (`= this.source-type`)
