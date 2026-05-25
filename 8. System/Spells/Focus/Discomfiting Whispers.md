---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Animist]]", "[[Aura]]", "[[Focus]]", "[[Misfortune]]", "[[Void]]"]
cast: "`pf2:1`"
area: "5-foot emanation"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You are surrounded by an aura of spiteful murmurings that incite bad luck and punish failure. Each creature that starts their turn within the area of this spell must succeed at a Will save or roll twice on their first attack roll that round and take the lower result. If an attack roll modified in this way results in a failure, the creature that rolled the failed attack takes 1d6 void damage.

> [!danger] Effect: Spell Effect: Discomfiting Whispers

**Heightened (+2)** The void damage dealt on a failure increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
