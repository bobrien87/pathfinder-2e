---
type: spell
sub-type: "Spell"
source-type: "Remaster"
level: "2"
traits: ["[[Concentrate]]", "[[Manipulate]]", "[[Plant]]", "[[Polymorph]]", "[[Wood]]"]
cast: "`pf2:2`"
duration: "10 minutes or 8 hours"
source: "Pathfinder Player Core"
---
### `= this.file.name`
`= "**Spell** " + this.level + choice(this.traditions != null and this.traditions != "", "<br>**Traditions** " + this.traditions, "")`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cast** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.range != null and this.range != "" or this.area != null and this.area != "" or this.targets != null and this.targets != "", "<br>" + choice(this.range != null and this.range != "", "**Range** " + this.range, "") + choice(this.area != null and this.area != "", choice(this.range != null and this.range != "", "; ", "") + "**Area** " + this.area, "") + choice(this.targets != null and this.targets != "", choice(this.range != null and this.range != "" or this.area != null and this.area != "", "; ", "") + "**Targets** " + this.targets, ""), "") + choice(this.defense != null and this.defense != "" or this.duration != null and this.duration != "", "<br>" + choice(this.defense != null and this.defense != "", "**Defense** " + this.defense, "") + choice(this.duration != null and this.duration != "", choice(this.defense != null and this.defense != "", "; ", "") + "**Duration** " + this.duration, ""), "")`

You can either transform into a plant or merge with plant matter. While transformed, you can't move or affect anything outside the plant, but you can cast spells as long as they don't require line of effect beyond the plant. You can Dismiss this spell.

- **Merge with Plants** The spell's duration is 10 minutes. While casting the spell, you must touch a plant with enough volume to fit you and your possessions or the spell is disrupted. While merged, you can hear, but not see, what's going on outside the plant. If the plant takes damage while you're inside it, you're expelled from the plant and take 10d6 damage. *Magic passage* expels you without dealing damage. The spell ends if you're ever outside the plant.

- **Turn into a Plant** The spell's duration is 8 hours. You become a Large plant—typically a tree. Perception checks don't reveal your true nature, but a successful Nature or Survival check against your spell DC reveals that you appear to be a plant that is strangely new to the area. While in this form, you can observe everything around you, using your normal senses. As a plant, your AC is 20, and only status bonuses, status penalties, circumstance bonuses, and circumstance penalties affect you. Any successes and critical successes you roll on Reflex saves are failures

**Source:** `= this.source` (`= this.source-type`)
