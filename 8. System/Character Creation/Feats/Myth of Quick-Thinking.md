---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Godling|Godling]]"
source-type: "Remaster"
level: "14"
traits: ["[[Mythic]]"]
prerequisites: "Godling Dedication, hero-god accomplishment"
source: "Pathfinder #218: Titanbane"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your myth includes amusing parables of clever plans and sly maneuvers, often applied to small things in life such as disguising yourself as a sheep to ambush a wolf or tricking a snake into shedding its skin. You can Lie as a two-action activity, regardless of how elaborate your tale. When you attempt a Deception check, you can spend a Mythic Point to do so at mythic proficiency. If you succeed at a Deception check while in the presence of your hierophant, any of your worshippers that you can see automatically succeed at an attempt to Impersonate or Lie in such a way that supports your story (for example, the target of your Lie claiming you are a teacher sees all of your worshippers as students).

You also lay claim to one of the following domains of your choice: confidence, secrecy, or trickery.

**Source:** `= this.source` (`= this.source-type`)
