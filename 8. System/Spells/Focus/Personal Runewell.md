---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Focus]]", "[[Manipulate]]", "[[Wizard]]"]
cast: "`pf2:2`"
range: "30 feet"
area: "15-foot cylinder"
defense: "basic Reflex"
duration: "1 minute"
source: "Pathfinder Lost Omens Rival Academies"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

**Area** (continued) 15-foot radius, 30-foot-tall cylinder

The runelords of Thassilon pioneered the creation of *runewells*, magical artifacts that could extract and store the power of sin magic from mortal souls. A circle of light carves its way across the ground as you create your very own *runewell*, your personal rune flaring to life within it as you add your own sin to those seven revered in the past. Whenever any creature Casts a Spell within your *personal runewell*, the well resonates, with your choice of effects.

- The runewell amplifies the power of your spells, as well as those of your allies. If the spell deals damage and doesn't have a duration, the well adds a status bonus to damage equal to the spell's rank.

> [!danger] Effect: Spell Effect: Personal Runewell

- The runewell punishes enemies foolish enough to attempt magic in your seat of power, firing arcane bolts at the spell's caster that deal 4d6 force damage, with a basic Reflex save.

If you cast *personal runewell* a second time, your previous *personal runewell* vanishes. You can Dismiss the spell.

**Heightened (+1)** The amount of damage dealt by the *runewell*'s bolts increases by 1d6.

*PFS Note:* Within the area of a *personal runewell* spell, the caster chooses the effect each time a spell is cast. This can be a different effect for different spells.

**Source:** `= this.source` (`= this.source-type`)
