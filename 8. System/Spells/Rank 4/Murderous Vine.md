---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Attack]]", "[[Concentrate]]", "[[Manipulate]]", "[[Plant]]", "[[Wood]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature adjacent to a flat surface"
duration: "1 minute"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You summon a slithering, thorny vine that attempts to constrict and crush a foe against a wall or other surface. Make a spell attack roll against the target's Fortitude DC. On a success, the creature is grabbed and takes 3d6 bludgeoning damage and 2d8 piercing damage. At the end of that creature's turn, if it's still grabbed by the vine, it takes @Damage[(floor(@item.level/2))d6[bludgeoning]] damage.

The vine's Escape DC is equal to your spell DC. A creature can attack the vine in an attempt to break its grip. The vine's AC is equal to your spell DC, and the vine is destroyed if it takes 20 or more damage. Destroying or escaping from the vines ends the spell. You can Dismiss the spell.

**Heightened (+2)** The initial bludgeoning damage increases by 1d6, the initial piercing damage increases by 1d8, and the damage a creature takes for ending its turn grabbed by the vine increases by 1d6.

**Source:** `= this.source` (`= this.source-type`)
