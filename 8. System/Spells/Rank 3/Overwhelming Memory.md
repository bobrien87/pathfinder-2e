---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Manipulate]]", "[[Mental]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You cause the target to recall a specific type of memory you choose from the list below, bringing it to the forefront of their mind with perfect clarity.

- **Gleeful** The memory makes the target laugh uncontrollably. They can't use reactions.
- **Romantic** The creature is consumed with their love for another. They are [[Fascinated]] by the memory.
- **Terrifying** The creature is filled with terror and is [[Frightened]] 1.
- **Tragic** The creature is overwhelmed with sorrow. They are [[Dazzled]] from the tears in their eyes.

The target must attempt a Will save.
- **Critical Success** The target is unaffected.
- **Success** The target is affected by the memory until the beginning of your next turn.
- **Failure** The target is affected by the memory until the beginning of your next turn and [[Stupefied 2]] for the spell's duration.
- **Critical Failure** As failure, but the target is [[Stupefied 3]] for the spell's duration.

**Source:** `= this.source` (`= this.source-type`)
