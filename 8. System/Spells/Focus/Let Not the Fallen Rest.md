---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Healing]]", "[[Manipulate]]", "[[Sorcerer]]"]
cast: "`pf2:3`"
area: "30-foot emanation"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You exhort your fallen comrades to return to the battle. Each allied creature within the emanation whose [[Dying]] value is 2 or less regains 4d10 Hit Points and can Stand as a free action, which doesn't provoke reactions.

**Heightened (+1)** The amount of healing increases by 1d10.

*PFS Note:* This spell affects unconscious allies with a dying value of 2 or less, in addition conscious allies with the dying 1 or 2 condition. Conscious characters are not considered to have the dying 0 condition and are unaffected.

**Source:** `= this.source` (`= this.source-type`)
