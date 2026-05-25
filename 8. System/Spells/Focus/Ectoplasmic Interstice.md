---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "4"
traits: ["[[Cleric]]", "[[Concentrate]]", "[[Focus]]", "[[Manipulate]]"]
cast: "`pf2:2`"
range: "30 feet"
area: "15-foot burst"
duration: "1 minute (sustained)"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You force the mortal Universe and Ethereal Planes to partially merge, creating a zone that causes incorporeal and spiritual entities to take on many of the aspects of corporeal creatures. Within the area of effect, incorporeal creatures can't pass through solid objects or corporeal creatures, and they can manipulate and attempt Strength-based checks against physical creatures and objects. An incorporeal PC or other creature with a normal Strength modifier simply uses that modifier, but if the creature had a Strength modifier of –5, like most incorporeal monsters, it uses a +4 modifier instead, increasing its Athletics modifier by 9 accordingly. Attacks against creatures that are within the area overcome resistances as if they were by ghost touch weapons.

**Source:** `= this.source` (`= this.source-type`)
