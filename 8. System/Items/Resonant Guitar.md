---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Magical]]", "[[Metal]]", "[[Sonic]]"]
price: "{'gp': 1850}"
usage: "held-in-two-hands"
bulk: "1"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Every part of this dark, shining guitar, from the strings to the soundboard, is constructed of metal. When the strings are strummed, the gilding on the guitar ripples like a liquid. A *resonant guitar* is a virtuoso handheld musical instrument that grants a +2 item bonus to Performance checks attempted while using it.

A *resonant guitar* is a planar key for [[Interplanar Teleport]] and similar magic to travel to the Plane of Metal. When using it in this way, you can play a tune inspired by your destination to make it more likely to arrive where you intend to be, appearing 1d6×25 miles from your intended destination instead of 1d10×25 miles away.

**Activate-Strum of Thunder** 1 minute (manipulate)

**Frequency** once per day

**Effect** You play a magnetic tune, enchanting one metallic weapon within 60 feet of you. This item gains the [[Thundering]] rune for 1 hour.

> [!danger] Effect: Strum of Thunder

**Activate-Chord of Protection** R (manipulate)

**Trigger** A creature within 30 feet of you targets you or an ally with a melee attack

**Frequency** once per day

**Effect** You strike a piercing chord, putting up an invisible sound barrier between the target and the attacker. The target gains a +2 status bonus to AC against the triggering attack. If the Strike still hits, the barrier breaks, dealing 3d10 sonic damage to the attacker.

**Source:** `= this.source` (`= this.source-type`)
