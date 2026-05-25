---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Cantrip]]", "[[Concentrate]]", "[[Manipulate]]", "[[Psychic]]"]
cast: "`pf2:2`"
range: "60 feet"
area: "10-foot line"
duration: "until the start of your next turn"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You set up a transparent, rippling screen of telekinetic energy that seizes small, fast-moving projectiles. Creatures can pass through the screen, but ammunition from physical ranged attacks—such as arrows, bolts, sling bullets, and other objects of similar size—is automatically trapped in the screen, clattering to the ground once the spell ends. Attacks with bigger ranged weapons, such as javelins, take a –2 circumstance penalty to their attack rolls if their paths pass through the screen. Massive ranged weapons and spell effects that don't create physical objects pass through the screen with no penalty.

**Heightened (5th)** The screen is 20 feet long.

**Heightened (6th)** The screen is 20 feet long and can interfere even with massless attacks, like magical blasts or gouts of flame. The screen imposes a –2 circumstance penalty to the attack rolls of spell effects even if they don't create physical objects. It also protects against area effects that pass through the screen, granting standard cover to creatures on the opposite side of the screen from the center or origin point of an area.

**Source:** `= this.source` (`= this.source-type`)
