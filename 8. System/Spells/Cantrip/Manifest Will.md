---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Aura]]", "[[Cantrip]]", "[[Concentrate]]", "[[Hex]]", "[[Witch]]"]
cast: "`pf2:1`"
area: "10-foot emanation"
duration: "1 minute (sustained)"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You unleash energy from the broken connection to your patron. You are [[Concealed]] from creatures beyond the edge of the emanation but can't use that concealment to [[Hide]]. Any creature that begins its turn in the emanation is affected based on your patron's tradition.

> [!danger] Effect: Aura: Manifest Will

- **Arcane** Raw energy and magical formulae circulate around you. A creature that begins its turn in the emanation gains weakness 1 to spell damage for 1 round.
- **Divine** Divine power crashes in a cycle of life and death. A living or undead creature that begins its turn in the emanation gains 2 temporary Hit Points for 1 round. This effect has the spirit trait.
- **Occult** Esoteric symbology etches the air. An allied creature that begins its turn in the emanation has 

> [!danger] Effect: Lesser Cover

 while inside the emanation, and for 1 round after it leaves.
- **Primal** Plants and fungus symbolic of your patron constantly grow and wither in the emanation. A creature that begins its turn in the emanation has a –10-foot status penalty to all its Speeds for 1 round or until it [[Escapes]]. This effect has the fungus, plant, and wood traits.

> [!danger] Effect: Spell Effect: Manifest Will

**Heightened (+1)** An arcane manifestation increases its weakness by 1 and a divine manifestation increases its temporary Hit Points by 2.

**Source:** `= this.source` (`= this.source-type`)
