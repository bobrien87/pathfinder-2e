---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Bard]]", "[[Concentrate]]", "[[Focus]]", "[[Spellshape]]"]
cast: "`pf2:0`"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You call upon your muse to greatly increase the benefits you provide with your *courageous anthem*, *rallying anthem*, or *song of strength* composition. If your next action is to cast one of these compositions, attempt a Performance check. The DC is usually the highest Will DC of the composition's targets, but the GM can assign a different DC based on the circumstances. The effect of your composition depends on the result of your check.

> [!danger] Effect: Spell Effect: Fortissimo Composition
- **Critical Success** The status bonus from your composition increases to +3.
- **Success** The status bonus from your composition increases to +2.
- **Failure** Your composition provides only its normal bonus of +1, but you don't spend the Focus Point for casting this spell.

**Source:** `= this.source` (`= this.source-type`)
