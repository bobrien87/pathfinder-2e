---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "3"
traits: ["[[Bard]]", "[[Cantrip]]", "[[Composition]]", "[[Concentrate]]", "[[Mental]]"]
cast: "`pf2:1`"
area: "60-foot emanation"
duration: "1 hour (sustained)"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You maintain a brisk performance that keeps allies on the move. You and your allies in the area can [[Hustle]] for the spell's duration, in addition to your other exploration activities (your exploration activity is Sustaining this spell). You and your allies then become temporarily immune for 1 day.

If you enter an encounter while performing this song, you can use your Performance modifier for the initiative roll. You and your affected allies also receive a +1 status bonus to that initiative roll.

**Heightened (6th)** You can Sustain the Spell for up to 2 hours.

**Heightened (9th)** You can Sustain the Spell for up to 4 hours.

**Source:** `= this.source` (`= this.source-type`)
