---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:3`"
range: "60 feet"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A Medium tree sprouts in an unoccupied square within range, its branches capable of striking out at your foes. This animated tree uses your spell attack modifier for its attack rolls and your spell DC for its AC. Its saving throw modifiers are equal to your spell DC – 10, and it has 20 Hit Points. Other creatures can't occupy its space, but allies can pass through its space. When you Cast the Spell and each time you Sustain it, you can have the tree make a branches Strike against a creature within 15 feet of it, dealing 2d8 bludgeoning, piercing, or slashing damage. You choose the damage type each time.

If the tree is in soil and survives to the end of the spell's duration, it remains as an ordinary, non-magical tree and continues to grow and thrive. The GM might determine that the tree disappears immediately in certain inhospitable situations.

**Heightened (+2)** The animated tree has 10 additional Hit Points, and its branches Strike deals 1d8 additional damage.

**Source:** `= this.source` (`= this.source-type`)
