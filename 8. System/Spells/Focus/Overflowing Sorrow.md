---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Aura]]", "[[Cleric]]", "[[Concentrate]]", "[[Emotion]]", "[[Focus]]", "[[Incapacitation]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
area: "15-foot emanation"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Sadness flows out of you into nearby creatures, blotting out any other thoughts they had. The first time a creature begins its turn in the area or enters the area, it must attempt a Will save. If it later leaves and reenters the area, it uses the same effect as before.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes a –1 status penalty to skill checks and Perception checks as long as it remains in the area.
- **Failure** While the creature is in the area, any emotion effects of lower counteract rank than overflowing sorrow are suppressed, and whenever the creature attempts to use an emotion action or cast an emotion spell, it must succeed at a DC 11 flat check or the action or spell is disrupted.
- **Critical Failure** As failure, but the creature can't use emotion actions or spells.

**Heightened (+2)** When you Cast the Spell, you can choose to increase the area by 5 feet.

**Source:** `= this.source` (`= this.source-type`)
