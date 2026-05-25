---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]", "[[Reach]]", "[[Versatile p]]"]
price: "{'gp': 60}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Adventure Path: Hellbreakers"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This *+1 asp coil* is used by many trained Sisters of the Golden Erinys. It has a deep-red hue on each segment of the blade complemented by a pitch-black pommel. Death isn't the worst outcome for someone on the receiving end of its lashes.

**Activate—Taste the Pain** `pf2:f` (manipulate, visual)

**Frequency** once per hour

**Trigger** Your last action was a Strike with the crimson thorn that dealt damage to a creature

**Effect** Attempt an Intimidation check to [[Demoralize]] the creature you dealt damage to with a +2 item bonus to the roll. You don't take any penalties to this check for not sharing a language.

**Source:** `= this.source` (`= this.source-type`)
