---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Fire]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 willing creature"
duration: "5 minutes"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

As long as you have magic, you're never unarmed. You materialize a flaming simulacrum of any common simple or martial weapon into the target's grasp. The target must have a free hand to hold the weapon, or else the weapon falls to the ground in the target's space. The blazing weapon functions as a *+1 striking weapon*, and its damage type changes to fire. The damage type can't be changed using the versatile trait, modular trait, or similar methods.

A thrown weapon rematerializes in the target's hand after the Strike is complete. If you choose a ranged weapon that uses ammunition, the wielder must still reload the weapon using the normal number of actions, though this generates ammunition automatically; this functions as normal ammunition, and the blazing weapon can't use other types of ammunition.

Any creature other than you or the target that attempts to touch, make a Strike with, or [[Disarm]] the weapon takes 1d6 fire damage each time.

**Heightened (4th)** You can target up to 5 willing creatures and can choose a different weapon for each target. The weapons function as *+1 striking flaming* weapons.

**Heightened (6th)** As 4th, but the weapons function as *+2 greater striking flaming* weapons.

**Heightened (8th)** As 4th, but the weapons function as *+3 greater striking greater flaming* weapons.

**Heightened (10th)** As 4th, but the weapons function as *+3 major striking greater flaming* weapons.

**Source:** `= this.source` (`= this.source-type`)
