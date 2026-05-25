---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Wood]]"]
cast: "`pf2:2`"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Wood shapes itself according to your will readily, making staircases appear as you climb up the side of a tree, automatically weaving vines into ladders, or lowering branches to lift you up to the top. When you Cast this Spell, move up to your Speed in any direction or along any surface, so long as there are living plants or trees of size Large or larger within 15 feet of you. The wood allows you to move but doesn't protect you from hazardous terrain or other dangers. Each time you Sustain this spell, you can move again in the same way.

**Heightened (8th)** The duration of this spell becomes 10 minutes. You no longer need to Sustain the spell to extend its duration, but you can Sustain it to move as described.

**Source:** `= this.source` (`= this.source-type`)
