---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Manipulate]]", "[[Morph]]", "[[Water]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 creature"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You temporarily transform one of your limbs into water, taking the form of ice, liquid water, or steam as you desire. Make a melee spell attack roll. On a hit, the target takes 2d6 damage; the type of damage dealt and any additional effect depends on the form you choose. On a critical hit, double the damage.

- **Ice** The limb deals cold damage, and the target takes a –10-foot status penalty to its Speeds until the start of your next turn. This spell gains the cold trait.

> [!danger] Effect: Spell Effect: Threefold Limb (Ice)

- **Liquid Water** The limb deals bludgeoning damage and you can [[Reposition]] the target up to 10 feet.
- **Steam** The limb deals fire damage and steam clings to the target, making all creatures [[Concealed]] to them until the start of your next turn or they perform an Interact action to wave the steam away. This spell gains the fire trait.

**Heightened (+1)** The damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
