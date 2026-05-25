---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Disease]]", "[[Focus]]", "[[Hex]]", "[[Manipulate]]", "[[Witch]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 creature"
defense: "Fortitude"
duration: "1 minute (sustained)"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You infect your target with fungal spores to hasten the cycle of decay. The target must attempt a Fortitude saving throw. Undead that aren't incorporeal, such as skeletons and zombies, don't have their normal immunity to this disease, as the spores can still colonize their remaining flesh and bone. This might also apply to other non-living creatures made of organic material at the GM's discretion.
- **Critical Success** The target is unaffected.
- **Success** The target sprouts mushrooms and is [[Enfeebled]] 2 for 1 round.
- **Failure** The target is afflicted with voidcap spores at stage 1.
- **Critical Failure** The target is afflicted with voidcap spores at stage 2.

**Voidcap Spores (disease)** This disease ends when the spell ends;

**Stage 1** enfeebled 2 (1 round)

**Stage 2** enfeebled 2 and [[Slowed]] 1 (1 round)

**Stage 3** enfeebled 2, slowed 1, and [[Stupefied 2]] (1 round)

**Source:** `= this.source` (`= this.source-type`)
