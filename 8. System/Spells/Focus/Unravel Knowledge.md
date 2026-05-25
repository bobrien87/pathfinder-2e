---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Hex]]", "[[Manipulate]]", "[[Mental]]", "[[Witch]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Will"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your patron reaches into the target's mind, plucking out their past training like pulling a thread from a cloth. Choose a single action, activity, or spell you know the target can use, such as from seeing it previously or identifying the creature's capabilities with a Recall Knowledge check. You could select, for example, the Strike action, the [[Disarm]] action, a dragon's breath, or the [[Haste]] spell if you were aware the target could use them. The target attempts a Will save.
- **Success** The target is unaffected.
- **Failure** The target's memories of their ability grow foggy. The first time they use the chosen ability each round, they take 3d8 mental damage. This ability is less effective if you choose an ability almost anyone can use; the target takes 3d4 mental damage instead if you choose a basic action (such as Strike, Stride, or Raise a Shield) or a skill action that can be used untrained (such as [[Demoralize]] or Hide).
- **Critical Failure** As failure, and the target takes a –2 status penalty to any check or DC for the ability the first time they use it each round.

> [!danger] Effect: Spell Effect: Unravel Knowledge

**Heightened (+1)** The damage increases by 1d8, or by 1d4 for a basic action or untrained skill action.

**Source:** `= this.source` (`= this.source-type`)
