---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Poison]]"]
cast: "`pf2:2`"
range: "100 feet"
area: "30-foot burst"
defense: "Fortitude"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You conjure an exploding glass container filled with a sight-stealing poison and hurl it across enemy lines. Upon impact, the bottle bursts and exposes all creatures in the area to the toxin within. Each creature in the area must attempt a Fortitude save.
- **Critical Success** The creature is unaffected.
- **Success** The creature takes 3d6 poison damage.
- **Failure** The creature is afflicted with blinding poison at stage 1.
- **Critical Failure** The creature is afflicted with blinding poison at stage 2.

**Blinding Poison** (incapacitation, poison) Level 9

**Maximum Duration** 4 rounds

**Stage 1** @Damage[3d6[poison]|traits:incapacitation,poison] damage and [[Blinded]] for 1 round (1 round)

**Stage 2** @Damage[4d6[poison]|traits:incapacitation,poison] damage and blinded for 1 round (1 round)

**Stage 3** @Damage[5d6[poison]|traits:incapacitation,poison] poison damage and blinded for 1 round (1 round)

**Stage 4** @Damage[6d6[poison]|traits:incapacitation,poison] poison damage and blinded for 1 minute (1 round)

*PFS Note:* The poison inflicted by this spell has the incapacitation trait, but the spell itself does not. This means that a creature which fails the save against the spell begins at stage 1 for the poison.

**Source:** `= this.source` (`= this.source-type`)
