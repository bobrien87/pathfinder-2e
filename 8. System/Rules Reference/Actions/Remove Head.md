---
type: action
source-type: "Remaster"
traits: ["[[Manipulate]]"]
cast: "`pf2:1`"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Effect** You Interact to remove your head from your ghostly body and hold it in a free hand. While your head is detached, you can use it to look around and over obstacles while remaining behind cover, although you don't have line of effect to target creatures unless the effect originates from your head. You can leave your head behind and move your body around independently, but your head gains the [[Paralyzed]] condition and your body becomes [[blind]], [[deaf]], and unable to take any action that has the auditory trait that requires speech or vocalization. You can cause your head to dematerialize and reappear atop your neck as a free action, which occurs automatically if it takes damage while detached or is separated from your body by more than 50 feet.

**Source:** `= this.source` (`= this.source-type`)
