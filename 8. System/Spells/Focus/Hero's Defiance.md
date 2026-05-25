---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "10"
traits: ["[[Champion]]", "[[Concentrate]]", "[[Focus]]", "[[Healing]]", "[[Vitality]]"]
cast: "`pf2:0`"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** An attack would bring you to 0 Hit Points.

You shout in defiance and are filled with a burst of healing. Just before applying the attack's damage, you recover 6d8+20 Hit Points. If this is enough to prevent the attack from bringing you to 0 Hit Points, you don't become [[Unconscious]] or [[Dying]]. Either way, cheating death is difficult, and you can't use *hero's defiance* again until you Refocus or make your daily preparations. *Hero's defiance* can't be used against effects with the death trait or that would leave no remains, such as disintegrate.

**Source:** `= this.source` (`= this.source-type`)
