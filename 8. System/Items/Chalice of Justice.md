---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Divine]]", "[[Holy]]", "[[Versatile p]]"]
price: "{'gp': 4500}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This gleaming golden sword is a *+2 greater striking holy cold iron longsword* given only to the worthiest heroes of a holy faith. It's made of a sacred, secret alloy that makes the blade both cold iron and silver. If you're unholy, you're [[Drained]] 2 while holding a *chalice of justice*. You can't recover from this condition while holding the weapon.

**Activate—Sip of Justice** `pf2:1` (manipulate)

**Frequency** once per day

**Effect** The pommel of the weapon transmutes into the shape of a miniature chalice. You drink deep from the chalice and regain @Damage[(@item.level)[healing]]{HP} equal to the chalice's level. If you're holy, you regain double the @Damage[(2*@item.level)[healing]]{HP}, and for 1 minute, whenever you critically hit an unholy creature with the *chalice of justice*, the creature takes 2d6 persistent,spirit damage, and it's [[Slowed]] 1 for 1 round. The persistent spirit damage has the holy trait.

> [!danger] Effect: Sip of Justice

**Craft Requirements** You're holy.

**Source:** `= this.source` (`= this.source-type`)
