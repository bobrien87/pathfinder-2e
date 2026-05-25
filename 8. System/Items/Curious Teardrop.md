---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Divine]]", "[[Intelligent]]", "[[Invested]]", "[[Metal]]"]
price: "{'value': {}}"
usage: "worn"
bulk: "—"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Perception** +26; precise vision 60 feet, imprecise hearing 30 feet

**Communication** telepathy (Common, Talican)

**Skills** Diplomacy +24, Alchemy Lore +26, Metal Lore +26, Society +24

**Int** +6, **Wis** +2, **Cha** +4

**Will** +26

A *curious teardrop*, despite being a sphere of liquid metal, hangs like an earring on a golden finding. The intelligent droplet is a spirited chatterbox, always observing and taking mental notes; however, it's easily overwhelmed by new sights, which often reduce it to a sobbing mess. Occasionally, the *curious teardrop* enters a stage of melancholy over the fragility of all matter, requiring immense reassurance to pull it out of its nihilism.

The tear prefers not to talk about its past, though it claims to be an actual tear separated from its "parent." Clerics of Laudinmio maintain that the elemental lord is the only being capable of shedding a perfect, sapient tear of metal.

**Activate—Request a Spell** `pf2:2` (concentrate, manipulate)

**Frequency** once per day

**Effect** You ask for the *curious teardrop*'s assistance. It casts [[Curse of Lost Time]], [[Ferrous Form]], or 7th-rank [[Elemental Form]] (metal elemental only), depending on your request.

**Activate—Reflect Emotions** R (concentrate)

**Trigger** You're targeted by an emotion or metal effect

**Effect** You receive a +4 status bonus to your saving throw against the triggering effect. Whether or not your save is successful, the teardrop attempts a counteract check at +36 to immediately reflect a copy of the effect back at the originator, targeting it using the creature's own relevant statistics but controlling the effect as if the teardrop had cast it.

**Source:** `= this.source` (`= this.source-type`)
