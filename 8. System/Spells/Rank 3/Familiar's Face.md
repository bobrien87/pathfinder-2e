---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Scrying]]"]
cast: "`pf2:2`"
range: "1 mile"
targets: "1 willing creature that's your animal companion or familiar"
duration: "sustained"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The target becomes a scrying sensor, allowing you to see through its eyes, smell what it smells, and similarly use its other senses. If you Cast a Spell with the revelation trait that affects your senses, such as [[See the Unseen]], while this spell is active, you gain the benefit of the spell through the target's senses instead of your own. You can also speak through the target with a voice much like yours, though it takes on some of the timbre and character of the target's growls or squawks. You can use Command an Animal on the target as part of Sustaining this spell. You don't need line of sight or line of effect to your target when you Cast this Spell.

**Source:** `= this.source` (`= this.source-type`)
