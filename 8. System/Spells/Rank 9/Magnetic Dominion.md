---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "9"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Metal]]"]
cast: "`pf2:3`"
area: "100-foot emanation"
targets: "any number of creatures wearing metal armor, creatures made of metal, creatures that have the metal trait, and unattended metal objects"
defense: "Reflex"
duration: "1 minute (sustained)"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The roiling magnetic fields of the Plane of Metal radiate from you as you channel and reshape them at your merest thought. When you Cast this Spell, you can relocate each affected target to any other unoccupied space within the emanation. You can't move yourself in this way. An unwilling target can resist being moved with a successful Reflex save.

The creatures move all at once—after you know the results of all the saves, you determine which target occupies each space in whatever order you choose. You can move a creature into a space that was previously occupied by another creature so long as you also relocate the first creature elsewhere as part of the movement. If you move a target into the air, it descends to the ground harmlessly after being moved unless it chooses not to.

You can choose to be affected by an 8th-rank [[Magnetic Repulsion]] spell that lasts for the duration of *magnetic dominion*. Each time you Sustain the spell, you can move one creature in the emanation, with the same targeting restrictions and stipulations as above.

**Source:** `= this.source` (`= this.source-type`)
