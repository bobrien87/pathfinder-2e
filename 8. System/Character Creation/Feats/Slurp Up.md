---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Thlipit Contestant|Thlipit Contestant]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Thlipit Contestant Dedication, unarmed attack with your tongue"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your tongue darts out in search of refreshment. Choose a liquid container of up to light Bulk within reach of your lash, such as a potion or elixir. The container must be held or in the open, not stowed in a pack or bandoleer. If the container is unattended or held by a willing ally, you Interact to drink the contents. If the container is held by an unwilling creature, you must succeed on a check using your unarmed attack modifier or Thievery modifier against the creature's Reflex DC to drink the contents; this adds the attack trait.

**Source:** `= this.source` (`= this.source-type`)
