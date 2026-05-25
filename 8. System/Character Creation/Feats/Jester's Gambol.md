---
type: feat
source-type: "Remaster"
level: "16"
traits: ["[[Animist]]", "[[Apparition]]", "[[Divine]]", "[[Stance]]", "[[Wandering]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** You are attuned to an apparition that grants Circus Lore or Fey Lore as one of its apparition skills.

You adopt a stance that makes your movements carefree and sublimely unpredictable, allowing you to move past impediments with ease and resist the attacks and importunateness of natural threats. You ignore difficult terrain, and you gain resistance equal to half your level against damage dealt to you by animals, beasts, fey, fungi, and plants.

**Source:** `= this.source` (`= this.source-type`)
