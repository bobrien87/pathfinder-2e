---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "50 feet"
targets: "up to 50 feet of unattended rope or an inanimate rope-like object"
duration: "1 minute (sustained)"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cause a section of rope or a rope-like object to animate, slither to your square, and encircle you, wreathing you in twisting, lashing fibers.

When you Cast the Spell and each time you Sustain the Spell, you can make a melee Strike with the rope, which uses and contributes to your multiple attack penalty. These rope Strikes are melee spell attacks; have the magical, reach, and trip weapon traits; and deal 3d6 slashing damage.

If you critically fail a check to [[Trip]] using the rope, you can't make any more Strikes with it this turn, nor can you use it to make an Attack of Opportunity until the beginning of your next turn. This replaces the usual results of a critical failure to Trip.

**Heightened (+2)** The damage from your rope Strikes increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
