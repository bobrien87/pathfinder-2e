---
type: spell
sub-type: "Focus Spell"
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Druid]]", "[[Focus]]", "[[Manipulate]]", "[[Polymorph]]"]
cast: "`pf2:2`"
duration: "varies"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You reach within for a different part of yourself, and you set it free, transforming your body into another form. You can polymorph into any form listed in [[Pest Form]], which lasts 10 minutes. All other *untamed form* shapes last 1 minute. You can add more shapes to your *untamed form* list with druid feats; your feat might grant you some or all of the shapes from a given polymorph spell.

When you transform into a shape granted by a spell, you gain all the effects of the shape you chose from a version of the spell heightened to *untamed form*'s rank. *Untamed form* allows you to use your own shapeshifting training more easily than most polymorph spells. When you choose to use your own attack modifier while polymorphed instead of the form's default attack modifier, you gain a +2 status bonus to your attack rolls.

> [!danger] Effect: Spell Effect: Untamed Form

**Heightened (2nd)** You can transform into shapes listed in [[Animal Form]].

**Source:** `= this.source` (`= this.source-type`)
