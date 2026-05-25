---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Fire]]", "[[Manipulate]]", "[[Move]]"]
cast: "`pf2:r`"
defense: "basic Reflex"
source: "Pathfinder #216: The Acropolis Pyre"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** A creature within 10 feet of you Strikes and deals damage to you.

Fiery wings briefly envelop your arms, and with a swift wingbeat, you flutter away from your attacker in a shower of searing sparks. You deal 1d6 fire damage to the triggering creature, with a basic Reflex save, and Fly up to 10 feet in a straight line directly away from it. If the creature critically fails its saving throw, your movement does not provoke reactions from it, and it's [[Dazzled]] until the end of its next turn.

**Heightened (+2)** The damage increases by 1d6, and the maximum distance you can Fly increases by 5 feet.

**Source:** `= this.source` (`= this.source-type`)
