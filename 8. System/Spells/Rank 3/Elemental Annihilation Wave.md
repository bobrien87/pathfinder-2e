---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Air]]", "[[Concentrate]]", "[[Earth]]", "[[Fire]]", "[[Manipulate]]", "[[Water]]"]
cast: "2 to 2 rounds"
area: "30-foot cone"
defense: "basic Reflex"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You draw elemental power from your surroundings, and combining it with your own magical energy, unleash a wave of utter destruction and swirling colors that deals 1d6 fire damage and 3d6 bludgeoning damage with a basic Reflex save. You can replace the air trait with the metal and wood traits when you cast the spell. The number of actions you spend when Casting this Spell determines the area and other parameters.

`pf2:2` **(somatic, verbal)** The spell is a 30-foot cone.

`pf2:3` **(material, somatic, verbal)** The spell is a 30-foot cone. On a failed saving throw, creatures are pushed 5 feet away from you, and on a critical failure they are pushed 10 feet away and are knocked prone.

**Two Rounds** If you spend 3 actions Casting the Spell, you can avoid finishing the spell and spend another 3 actions on your next turn to empower the spell even further. If you do, the spell is as 3 actions, but the area is a @Template[cone|distance:60], and for 1 round, the elements linger in the cone, racing off into the distance and making approaching you difficult, with the effects of [[Gust of Wind]].

**Heightened (+2)** The damage increases by 3d6 bludgeoning and 1d6 fire, and the distance that enemies are pushed back if you spent 3 actions or 2 rounds increases by 5 feet on a failed save and 10 feet on a critical failure.

**Source:** `= this.source` (`= this.source-type`)
