---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Consumable]]", "[[Magical]]"]
price: "{'gp': 2300}"
bulk: "—"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Ammunition** round

**Activate** `pf2:1` (manipulate)

These bullets are formed from a liquefied high-grade precious metal and enchanted to unlock that metal's true potential.

The shot is a high-grade cold iron bullet. The awakened cold iron attempts to disrupt magic influences the target placed on others' minds. You can name a creature you believe to be enchanted by your target or allow the shot to choose an enchanted creature randomly. On a hit, the shot attempts to counteract the spell or effect the target is using to manipulate that creature's mind. The counteract rank is 9, and the counteract modifier is +27. If you fail (but don't critically fail) the counteract check against a demon or fey, you get a success instead. If you hit a demon or fey with no active spell effects on other creatures, the target is [[Stupefied 1]] for 1 minute instead.

**Source:** `= this.source` (`= this.source-type`)
