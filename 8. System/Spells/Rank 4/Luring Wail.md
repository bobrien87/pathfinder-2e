---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
area: "60-foot emanation"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You emit a plaintive cry to lure your enemies closer. Each creature in the emanation that can hear you must attempt a Will save. If you speak a creature's name as part of the casting of the spell, that creature takes a –2 circumstance penalty to its saving throw. Each creature that enters the area on its turn must attempt a save. If you attack or take a hostile action, the [[Fascinated]] condition ends only for the creature that's attacked.
- **Critical Success** The creature is unaffected.
- **Success** The creature is [[Slowed]] 1 for 1 round.
- **Failure** The creature becomes fascinated and compelled to move toward the sound of your cry on its turn. As long as it is in the emanation and can hear, it must spend at least one of its actions on each of its turns to move closer to you.
- **Critical Failure** As failure, but the creature must spend all its actions moving toward the sound. Additionally, the creature is [[Off Guard]].

**Source:** `= this.source` (`= this.source-type`)
