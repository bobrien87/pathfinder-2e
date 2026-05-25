---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 55}"
usage: "worneyepiece"
bulk: "L"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

When you wear these green-tinted glasses, all the movement in the surrounding area seems to jump out at you. You gain a +1 item bonus to your Perception DC against Stealth checks to [[Hide]] or [[Sneak]], and anyone attempting to Sneak doesn't benefit from the circumstance bonus from cover against your Perception DC.

**Activate—Find the Hidden** `pf2:1` (detection, manipulate)

You twist the lenses of your glasses as you look for someone [[Hidden]]. You [[Seek]] with a +1 item bonus. If you find a hidden creature or object, you can Point Out as a free action.

**Source:** `= this.source` (`= this.source-type`)
