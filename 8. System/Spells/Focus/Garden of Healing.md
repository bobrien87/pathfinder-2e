---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Animist]]", "[[Aura]]", "[[Emotion]]", "[[Focus]]", "[[Healing]]", "[[Mental]]"]
cast: "`pf2:1`"
area: "10-foot emanation"
duration: "1 minute (sustained)"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Spirits of comfort and respite swirl around you, trailing visions of growing grass and blooming blossoms. When you cast this spell and the first time you Sustain it on each subsequent round, you generate a pulse of renewing energy that heals each creature within the emanation for 1d4 Hit Points. The calm of this effect lingers; once this spell ends, any creature that has been affected by its healing gains a +1 circumstance bonus to saves against emotion effects for 10 minutes but does not receive any healing from additional castings of the spell while the bonus persists.

> [!danger] Effect: Spell Effect: Garden of Healing

**Heightened (+1)** The healing granted by the spell's pulse increases by 1d4 Hit Points.

**Source:** `= this.source` (`= this.source-type`)
