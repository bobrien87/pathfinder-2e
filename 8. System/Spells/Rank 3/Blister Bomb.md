---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Concentrate]]", "[[Disease]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "100 feet"
area: "5-foot burst"
defense: "Fortitude"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You launch a small bomb enchanted with a fast-acting skin disease at your foes, causing their skin to break out in horrible bleeding sores. All creatures in the area of the burst must attempt a Fortitude save.
- **Critical Success** The creature is unaffected and is immune to blister pox for 1 week.
- **Success** The creature is [[Sickened]] 2.
- **Failure** The creature is afflicted with blister pox at stage 1.
- **Critical Failure** The creature is afflicted with blister pox at stage 2.

**Blister Pox** (disease) Level 5; A creature can't reduce its sickened value below 1 while it's taking persistent bleed damage from blister pox

**Stage 1** sickened 2 (1 round)

**Stage 2** sickened 2 and 1d6 persistent bleed damage (1 round)

**Stage 3** sickened 2 and 2d6 persistent bleed damage (1 round)

**Stage 4** [[Sickened]] 3 and 2d6 persistent bleed damage (1 day)

**Source:** `= this.source` (`= this.source-type`)
