---
type: spell
sub-type: "Ritual"
source-type: "Remaster"
level: "6"
cast: "8 hours"
duration: "1 week"
source: "Pathfinder #205: Singer, Stalker, Skinsaw Man"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

The majority of the *Song of Silver's* time needed to Cast it consists of preparations for the performance, which must take place on a stage in Kintargo. While the *Song of Silver* can be cast by a single primary caster, up to six secondary casters can assist by helping to decorate the stage with Crafting or by spreading word and gathering an audience with Society. At the end of this 8-hour period, the primary caster performs the song, which takes up the final minute of the casting time.

> [!danger] Effect: Spell Effect: Song of Silver
- **Critical Success** The stage and rooftop above any stage where the song was performed glows softly with silver radiance for 1 week. During this time, the ritual tries to counteract teleportation effects and planar travel into or out of Kintargo attempted by unholy creatures, and all weapons wielded within Kintargo are treated as if they were made of silver for the purposes of calculating damage against creatures who possess weakness to silver. The ritual also generates the Success effects below. The *Song of Silver* can't be attempted again for 1 month.
- **Success** For 1 week, the primary and secondary casters gain a +2 status bonus to all saving throws against mental effects; this bonus doubles to a +4 status bonus against all fear effects. Each caster gains the ability to cast [[Breath of Life]] as an innate occult spell at a rank equal to what the *Song of Silver* was cast at, once during the week. These benefits are suppressed as long as the character is outside of Kintargo. The *Song of Silver* can't be attempted again for 1 month.
- **Failure** The *Song of Silver* fails, and it can't be attempted again for 1 month.
- **Critical Failure** Not only does the ritual fail, but the primary caster is overwhelmed with shame at the failure and becomes [[Stupefied 2]] for 1 week (can't be removed by any means). The *Song of Silver* can't be attempted again for 6 months.

**Heightened (10th)** The effects of the *Song of Silver* expand to cover all of Ravounel.

**Source:** `= this.source` (`= this.source-type`)
