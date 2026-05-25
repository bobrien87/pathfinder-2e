---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]"]
cast: "`pf2:2`"
duration: "1 hour"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You continually and harmlessly slough off the top layer of your skin while new skin regenerates immediately, quickly moving damaging substances away from your body. The flat check to remove persistent damage from effects that coat your skin (such as most persistent acid damage) is reduced to 5, and you gain a +2 status bonus to your initial save against contact poison (but not to further saves since, by that point, the toxin has already entered your system).

If you're affected by an effect other than persistent damage that depends on continuous contact with your skin, and if that effect allows a saving throw, you receive a new saving throw against that effect at the end of each turn when you attempt your flat checks against persistent damage, and you also receive a +2 status bonus to those saving throws.

While affected by this spell, your continually shedding skin makes you much easier to [[Track]]. Anyone Tracking you gains a +2 circumstance bonus to do so, and you can't Hide Your Tracks.

**Source:** `= this.source` (`= this.source-type`)
