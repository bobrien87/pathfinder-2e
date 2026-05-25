---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "6"
traits: ["[[Dream]]", "[[Illusion]]", "[[Mythic]]"]
cast: "1 day"
targets: "1 dead runelord who is not already active as a risen runelord"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

By drawing upon fragments of physical remains or treasured objects of a dead runelord and upon remnant energies of each runelord that live on after their deaths in the Dreamlands, this ritual creates a physical illusion of a long-dead runelord. There can only exist a limited number of risen runelords at a time, since each must be created from one of the finite number of dead runelords, although there's no limit as to how many times a risen runelord can be created to replace one who was destroyed. Risen runelords cannot be made from living or undead runelords. This leaves 32 potential risen runelords in the world at any one time as of the start of Revenge of the Runelords. This ritual creates an 11th-level risen runelord associated with the original runelord's sin, but the duration of that runelord's life depends on the ritual's result. As long as this ritual's inventor, Runelord Xanderghul, still lives, any attempt to cast this ritual by any other creature can never achieve a greater success than failure.
- **Critical Success** You create a risen runelord with a lifespan of decades, if not more.
- **Success** You create a risen runelord with a lifespan of 10 days.
- **Failure** You fail to create the risen runelord.
- **Critical Failure** You fail to create a risen runelord but also attract the attention of vengeful psychopomps who manifest in place of the risen runelord. This should be a severe encounter of a level equal to the primary caster against a mix of psychopomps, who attack at once and fight to the death.

**Heightened (7th)** You can create a 14th-level risen runelord, and the cost is 3,000 gp.

**Heightened (8th)** You can create a 16th-level risen runelord, and the cost is 5,000 gp.

**Heightened (9th)** You can create an 18th-level risen runelord, and the cost is 10,000 gp.

**Heightened (10th)** You can create a 20th-level risen runelord, and the cost is 20,000 gp.

**Source:** `= this.source` (`= this.source-type`)
