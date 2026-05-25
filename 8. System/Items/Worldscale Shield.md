---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]", "[[Mythic]]"]
price: "{'gp': 500}"
bulk: "L"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

It's believed that four *worldscale shields* (Hardness 9, HP 60, BT 30) exist, each made from the scale of one of the four worldscale serpents rumored to burrow through the heart of the world. When a hero-god went to slay one of these serpents, they found that they first needed to tear a scale from the beast's body to reveal the vulnerable flesh beneath. These four scales removed became the four *worldscale shields*.

**Activate—Absorb Blow** `pf2:f`

**Trigger** You would take physical damage (bludgeoning, piercing, or slashing) from an attack and you have your *worldscale shield* Raised

**Effect** Spend 1 Mythic Point. The *worldscale shield* completely absorbs the blow, preventing all damage that you would have taken from the attack. The *worldscale shield* breaks. If it was already broken, it is destroyed.

**Source:** `= this.source` (`= this.source-type`)
