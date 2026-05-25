---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Death]]", "[[Focus]]", "[[Hex]]", "[[Manipulate]]", "[[Void]]", "[[Witch]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "1 creature"
defense: "Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your patron wraps a hand around your target's heart. The target must attempt a Fortitude saving throw. Regardless of the result, the target is temporarily immune to all *curses of death* for 1 day.
- **Critical Success** The target is unaffected.
- **Success** The target is afflicted with the *curse of death* at stage 1, and the stage of the curse can't increase beyond stage 1.
- **Failure** The target is afflicted with the *curse of death* at stage 1.
- **Critical Failure** The target is afflicted with the *curse of death* at stage 2

**Curse of Death** (curse, death, void) This curse ends when the spell ends

**Stage 1** @Damage[(max(4,(@item.rank)-1))d6[void]] damage and [[Fatigued]] (1 round)

**Stage 2** @Damage[(max(8,@item.rank+3))d6[void]] damage and fatigued (1 round)

**Stage 3** @Damage[(max(12,@item.rank+7))d6[void]] damage and fatigued (1 round)

**Stage 4** death

**Heightened (+1)** Increase the void damage taken on a success and during the first three stages of the curse by 1d6.

**Source:** `= this.source` (`= this.source-type`)
