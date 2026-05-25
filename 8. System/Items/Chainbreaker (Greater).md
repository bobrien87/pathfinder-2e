---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Fatal d10]]", "[[Magical]]"]
price: "{'gp': 1750}"
usage: "held-in-one-hand"
bulk: "1"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The head of this *+2 striking pick* is adorned with a detailed etching of an eagle with outstretched wings. When you use it to Strike an unattended object whose intended purpose is to restrain or confine, such as a pair of manacles or the bars of a prison cell, you ignore the first 10 points of the object's Hardness.

**Activate—Liberating Strike** `pf2:2`

**Frequency** once per day

**Effect** You Strike a creature with the *chainbreaker*. If you hit and deal damage, one [[Grabbed]] or [[Restrained]] ally within 60 feet of the target can use a reaction to attempt to [[Escape]].

**Source:** `= this.source` (`= this.source-type`)
