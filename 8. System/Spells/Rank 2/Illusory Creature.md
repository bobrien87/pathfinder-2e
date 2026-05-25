---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Illusion]]", "[[Manipulate]]", "[[Olfactory]]", "[[Visual]]"]
cast: "`pf2:2`"
range: "500 feet"
duration: "sustained"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You create an illusory image of a Large or smaller creature. It generates the appropriate sounds, smells, and feels believable to the touch. If you and the image are ever farther than 500 feet apart, the spell ends.

The image can't speak, but you can use your actions to speak through the creature, with the spell disguising your voice as appropriate. You might need to attempt a Deception or Performance check to mimic the creature, as determined by the GM. This is especially likely if you're trying to imitate a specific person and engage with someone that person knows.

In combat, the illusion can use 2 actions per turn, which it uses when you Sustain the spell. It uses your spell attack modifier for attack rolls and your spell DC for its AC. Its saving throw modifiers are equal to your spell DC – 10. It is substantial enough that it can flank other creatures. If the image is hit by an attack or fails a save, the spell ends.

The illusion can cause damage by making the target believe the illusion's attacks are real, but it cannot otherwise directly affect the physical world. If the illusory creature hits with a Strike, the target takes 3d4 mental damage. The illusion's Strikes are nonlethal. If the damage doesn't correspond to the image of the monster—for example, if an illusory Large dragon deals only 5 damage—the GM might allow the target to attempt an immediate Perception check to disbelieve the spell. Any relevant resistances and weaknesses apply if the target thinks they do, as judged by the GM. For example, if the illusion wields a warhammer and attacks a creature resistant to bludgeoning damage, the creature would take less mental damage. However, illusory damage does not deactivate regeneration or trigger other effects that require a certain damage type. The GM should track illusory damage dealt by the illusion.

Any creature that touches the image or uses the [[Seek]] action to examine it can attempt to disbelieve your illusion. When a creature disbelieves the illusion, it recovers from half the damage it had taken from it (if any) and doesn't take any further damage from it.

**Heightened (+1)** The damage of the image's Strikes increases by 1d4, and the maximum size of creature you can create increases by one (to a maximum of Gargantuan).

**Source:** `= this.source` (`= this.source-type`)
