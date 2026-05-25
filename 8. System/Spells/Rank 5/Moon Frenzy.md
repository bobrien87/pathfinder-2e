---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "5"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Morph]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "up to 5 willing creatures"
duration: "1 minute"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

A feral aspect overcomes the targets, filling them with strength and ferocity. Targets gain 5 temporary Hit Points, a +10-foot status bonus to their Speeds, and weakness 5 to silver. They also grow vicious fangs and claws, which are unarmed attacks. The fangs deal 2d8 piercing damage; the claws deal 2d6 slashing damage and have the agile and finesse traits. The targets use their highest weapon or unarmed attack proficiency with these attacks, and if they have weapon specialization or greater weapon specialization, they add this damage as well. On a critical hit with one of these unarmed attacks, the creature struck takes 1d4 persistent bleed damage.

The targets can't use concentrate actions unless those actions also have the rage trait, with the exception of [[Seek]]. A creature can attempt to end the spell's effect on itself by using a single action, which has the rage trait, to attempt a Will save against your spell DC; on a success, it ends the spell's effect on itself.

If a target is in the light of a full moon, it also grows by one size if it were Medium or smaller. This increases the reach of a Medium or Tiny creature by 5 feet.

**Heightened (6th)** The temporary Hit Points increase to 10, the silver weakness to 10, and the damage dealt by the attacks to three dice.

**Heightened (10th)** The temporary Hit Points increase to 20, the silver weakness to 20, and the damage dealt by the attacks to four dice.

> [!danger] Effect: Spell Effect: Moon Frenzy

**Source:** `= this.source` (`= this.source-type`)
