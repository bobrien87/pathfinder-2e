---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "5"
cast: "4 hours"
range: "20 feet"
source: "Pathfinder Player Core 2"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You craft a large quantity of restorative drink, such as an invigorating tea, a refreshing ale, or a stimulative alchemical tonic. The ritual speeds along any natural processes to make the brew, such as fermenting fruit to make a wine. At the conclusion of the first 3 hours of the ritual, you produce enough brew for up to 10 people to drink, any of whom can be the secondary caster of the ritual. The brew must then be consumed over the next hour. There is no danger of the drinkers becoming drunk if the brew is alcoholic. Once that hour is completed, you and the secondary caster attempt your checks as normal.
- **Critical Success** The brew is delicious and revitalizing. It casts a 4th-rank [[Cleanse Affliction]], a 4th-rank [[Clear Mind]], and a 4th-rank [[Sound Body]] on each drinker for each relevant affliction or condition, using your modifier for the primary skill check as the counteract modifier. Each drinker also gains 20 temporary Hit Points that last 12 hours and a +2 status bonus to saves against diseases and poisons for the next 12 hours.

> [!danger] Effect: Spell Effect: Fortifying Brew
- **Success** As critical success, except drinkers gain only 10 temporary Hit Points, and don't gain the status bonus to saves.
- **Failure** You and the other drinkers are left with a sour taste—something went wrong with the brewing process.
- **Critical Failure** Your attempt to craft the drink resulted in something more akin to a poison. You and the other drinkers become [[Sickened]] 4 and can't reduce the condition for 12 hours.

**Heightened (+1)** The temporary Hit Points increases by 2 (or 4 on a critical success).

**Source:** `= this.source` (`= this.source-type`)
