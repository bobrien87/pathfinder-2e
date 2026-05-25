---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Focus]]", "[[Manipulate]]", "[[Polymorph]]", "[[Sorcerer]]"]
cast: "`pf2:1`"
duration: "1 minute"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You transform your flesh and organs into a bizarre amalgam of glistening skin, rough scales, tufts of hair, and tumorous protuberances. This has three effects:

- You gain resistance 10 to precision damage and resistance 10 to extra damage from critical hits. If the resistance is greater than the extra damage, it reduces the extra damage to 0 but doesn't reduce the attack's normal damage.

- You gain darkvision.

- Acid oozes from your skin. Any creature that hits you with an unarmed attack or with a non-reach melee weapon takes 2d6 acid damage.

**Heightened (+2)** The resistances increase by 5, and the acid damage increases by 1d6.

> [!danger] Effect: Spell Effect: Unusual Anatomy

**Source:** `= this.source` (`= this.source-type`)
