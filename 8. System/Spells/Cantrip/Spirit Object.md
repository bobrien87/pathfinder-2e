---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cantrip]]", "[[Hex]]", "[[Manipulate]]", "[[Witch]]"]
cast: "`pf2:1`"
range: "30 feet"
targets: "1 unattended object up to 1 bulk"
duration: "1 minute"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Using a sliver of Baba Yaga's power, you briefly bring a nearby object to life. The object gains a means of locomotion if it does not already have one, such as sprouting chicken legs, and Strides up to 25 feet to a space you decide within range. Once per round, you can Sustain the spell to command the object further, either prompting it to move again or to Strike. If prompted to move, the object Strides up to 25 feet again to a space within 30 feet of you. If prompted to Strike, the object attacks one creature of your choice adjacent to its space. Make a melee spell attack roll against the creature. On a success, the creature takes 2d4 damage. The damage is either bludgeoning, piercing, or slashing damage, as appropriate for the object. The object doesn't do anything if it doesn't receive further commands from you. If you cast spirit object again, any previously affected object reverts back to normal. You can Dismiss the spell.

**Heightened (+1)** Increase the maximum Bulk of the target by 1 and the damage by 2d4.

**Source:** `= this.source` (`= this.source-type`)
