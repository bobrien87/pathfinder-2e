---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Incapacitation]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "touch"
targets: "1 living creature that has a soul"
defense: "Fortitude"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your touch disrupts the connection between body and soul, possibly forcing the soul out of the body altogether. The target must attempt a Fortitude save. You can allow allies to choose the degree of success instead of rolling a saving throw.
- **Success** The target is unaffected.
- **Failure** The target is [[Stunned]] 1 as its soul briefly loses its connection to their body.
- **Critical Failure** The target's soul exits its body and the target's body becomes stunned for 1 round. While their body is stunned in this way, the target remains fully aware in soul form; they simply can't consciously move their body (though the body makes basic instinctual defensive movements). The target's soul has the incorporeal trait, is [[Invisible]], and has a fly Speed of 60 feet. It can't attack, cast spells, or attempt any skill checks that require a physical body, and it must always maintain line of effect to the target's body. When the target's body ceases being stunned, the target's soul instantly returns to their body as the target wakes.

**Heightened (+3)** If a willing ally chooses to critically fail, they can stay in soul form for 1 additional round.

**Source:** `= this.source` (`= this.source-type`)
