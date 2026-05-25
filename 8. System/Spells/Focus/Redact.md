---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
targets: "unattended written materials of up to 1 Bulk or less"
duration: "1 day"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You strike mention of a specific name from one or more documents. When you Cast the Spell, give one proper name, be it a creature, location, or object. Any mention of that name within the document becomes blurred, smudged, or otherwise completely illegible. Epithets and unambiguous references to the name are redacted as well; for instance, redacting the name of the goddess Sarenrae from a book would also remove references to her title "the Dawnflower." Attempts to use this reference material to Recall Knowledge about the given proper name automatically fail.

**Heightened (3rd)** Instead of striking out a given name, you can replace it with a different name you choose. Epithets and references are substituted with similar ones relating to the replacement name. Anyone reading the text can attempt a Perception or Society check against your spell DC to notice the altered text, though that doesn't tell them what the original said.

**Heightened (4th)** At your choice, the duration is unlimited.

**Source:** `= this.source` (`= this.source-type`)
