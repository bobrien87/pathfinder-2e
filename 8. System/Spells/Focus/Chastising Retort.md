---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Mental]]"]
cast: "`pf2:r`"
range: "30 feet"
targets: "the triggering creature"
defense: "Will"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Trigger** A creature within range attempts a Deception check to [[Lie]] or [[Feint]].

You unleash some choice words empowered with divine might. The creature takes 2d6 mental damage and must attempt a Will save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes half damage.
- **Failure** The creature takes full damage and is [[Stupefied 1]] for 1d4 rounds.
- **Critical Failure** As failure, but the creature takes double damage and is [[Stupefied 2]] for 1d4 rounds.

The creature can immediately choose to reveal the truth about its deception as a free action to immediately recover Hit Points equal to the mental damage it took and lose the stupefied condition from the spell. If it does, it quickly notes that its words and actions were lies, though it might need more time to explain the proper truth. If the creature used Deception to successfully Feint and it reveals the truth in this way, the target of the creature's Feint is no longer [[Off Guard]] due to the successful Feint.

**Heightened (+1)** The damage increases by 2d6.

**Source:** `= this.source` (`= this.source-type`)
