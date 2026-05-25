---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "10"
traits: ["[[Concentrate]]", "[[Incarnate]]", "[[Manipulate]]"]
cast: "`pf2:3`"
range: "500 feet"
duration: "until the end of your next turn"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You bartered for this spell in some strange market or perhaps gained it while wandering the desert, hopelessly lost and surrounded by nothing but the remnants of time and fallen empires. With a gesture and words of a language not spoken since the fall of the Hanging City of Teskra, you summon Jassim the Wanderer. Jassim, a true Jistkan automaton, occupies the space of a Gargantuan creature and has a Speed of 60 feet.

**Arrive** (fire) *Eyes of Fire* Jassim emerges from the ground and glares at your enemies, a fearsome look forming on a face of ancient metal and glass. He shoots an energy beam in a 60-foot line, dealing 5d12 fire damage and 5d12 piercing damage (basic Reflex save). Enemies that critically fail are [[Drained]] 2.

**Depart** (metal) *Heart of Rust* Jassim takes a metal piece from his chest and holds it out, crushing it in his fist and allowing the powder to spread across a 60-foot emanation. These particles deal 10d6 slashing damage to all creatures and unattended objects within the area (basic Fortitude save). A metal creature that fails its save also takes @Damage[2d8[persistent,slashing]|traits:metal] damage. A non-metal creature that fails this save is also [[Sickened]] 2.

**Source:** `= this.source` (`= this.source-type`)
