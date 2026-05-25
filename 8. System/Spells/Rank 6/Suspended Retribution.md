---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "6"
traits: ["[[Concentrate]]", "[[Curse]]", "[[Manipulate]]", "[[Mental]]", "[[Prediction]]"]
cast: "`pf2:2`"
range: "60 feet"
targets: "1 creature"
defense: "basic Reflex"
duration: "1 minute"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

All life dances one step from the precipice, one heartbeat from disaster. You open your eyes wide and see doom waiting in the wings, then invite it to step forward. A spectral omen of disaster appears above the target's head—traditionally, this is a downward-pointing sword, but some spellcasters report seeing a hangman's noose or a grinning skull instead. When you Cast this Spell, pick one of the following triggers.

- The target moves more than its Speed in a single round.
- The target makes more than one Strike in a single round.
- The target Casts a Spell.
- The target uses a specific skill you name.
- The target uses a specific ability you name.

The target uses a specific ability you name. If the target takes the triggering action, the portent of doom activates—the sword strikes down, the noose loops around the target's neck, the skull bares its fangs—and the target takes 70 mental damage with a basic Reflex save. The target instinctively knows which action will trigger the omen and can ward off the omen by spending a total of 3 actions, which have the concentrate trait, to pray, make signs against doom, or similar apotropaic actions. These actions need not be consecutive. After the creature spends the actions, the spell ends.

**Heightened (+1)** The damage increases by 10.

**Source:** `= this.source` (`= this.source-type`)
