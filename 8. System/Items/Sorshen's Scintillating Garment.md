---
type: item
source-type: "Remaster"
level: "20"
traits: ["[[Apex]]", "[[Artifact]]", "[[Comfort]]", "[[Mythic]]"]
price: "{'cp': 0, 'gp': 0, 'pp': 0}"
bulk: "L"
source: "Pathfinder #221: Into the Apocalypse Archive"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The traditional robes of Sorshen, Runelord of Lust, this garment combines a powerful artifact with a sign of office, as with many runelords' accoutrements. Woven of the finest silks and accented with precious stones, the garment is light and easy to move in. Sorshen created, then expanded on the artifact throughout her time as the runelord of lust, adding to it during much of the Age of Legend.

This ever-shifting garment of silk and gems subtly reshapes itself in response to its wearer, adopting an appearance most flattering to their form. It's a set of *+3 greater resilient explorer's clothing*. The garment's four pockets each function as separate *Spacious Pouches (Type IV)*. While wearing the garment, you're immune to mental effects unless you choose otherwise. When you invest *Sorshen's Scintillating Garment*, you increase your Charisma modifier by 1, or increase it to +4, whichever would give you a higher value.

**Activate—Scintillating Colors** `pf2:2` (arcane, aura, visual)

**Frequency** once per hour

**Effect** *Sorshen's Scintillating Garment* casts [[Dizzying Colors]] (DC 41), heightened to 10th rank, to your specifications. If you spend 1 Mythic Point as part of this activation, the spell's area changes to a @Template[type:emanation|distance:20], and you can designate any number of creatures in that area to be immune to the spell's effects, and the spell loses the incapacitation trait.

**Destruction** *Sorshen's Scintillating Garment* is destroyed if it's immersed in the waters of a destroyed *Runewell of Lust*.

**Source:** `= this.source` (`= this.source-type`)
