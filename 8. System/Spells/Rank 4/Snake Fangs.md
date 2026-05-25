---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Morph]]"]
cast: "`pf2:2`"
duration: "1 minute"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

Your jaw unhinges as your teeth extend into wicked fangs. For the spell's duration, you gain a fangs unarmed attack. They're a finesse, grapple, unarmed attack that deals 1d8 piercing damage and an extra 2d10 poison damage. If you have a creature at least one size smaller than you [[Grabbed]] with your fangs, you can use the [[Swallow Whole]] ability that deals 4d6 bludgeoning damage and has a Rupture value of 17. A swallowed creature is transported to an extraplanar space that resembles the inside of a snake's stomach, so when it gets free, it appears in a space adjacent to you. If you're killed or the spell ends, the swallowed creature is immediately freed.

> [!danger] Effect: Spell Effect: Snake Fangs

**Heightened (+3)** The extra poison damage of your fangs unarmed attack increases by 1d10, the damage dealt by the Swallow Whole ability increases by 6d6, and the Rupture value increases by 9.

**Source:** `= this.source` (`= this.source-type`)
