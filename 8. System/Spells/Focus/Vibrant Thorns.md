---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Focus]]", "[[Manipulate]]", "[[Morph]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:1`"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your body sprouts a coat of brambly thorns that thrive on life magic. Adjacent creatures that hit you with a melee attack, as well as creatures that hit you with unarmed attacks, take @Damage[(@item.rank)[piercing]] damage each time they do. Anytime you cast a vitality spell, the thorns' damage increases to @Damage[(@item.rank)d6[piercing]] until the start of your next turn.

**Heightened (+1)** The damage increases by 1, or 1d6 after you cast a vitality spell.

**Source:** `= this.source` (`= this.source-type`)
