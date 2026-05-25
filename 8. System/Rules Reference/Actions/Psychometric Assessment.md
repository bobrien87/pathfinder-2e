---
type: action
source-type: "Remaster"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Exploration]]", "[[Mental]]", "[[Occult]]"]
cast: "Passive"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= "**Cost** " + this.cast + choice(this.trigger != null and this.trigger != "", "<br>**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", "<br>**Requirements** " + this.requirements, "") + choice(this.prerequisites != null and this.prerequisites != "", "<br>**Prerequisites** " + this.prerequisites, "")`

**Requirements** Your bare hands are touching an object in which you detected psychometric resonance

**Effect** You spend 1 minute concentrating on the object to get a vision of the face of the person who imbued the item with such emotion in the first place. If the associated emotion is painfully negative, you might take 1d6 mental damage, as determined by the GM.

**Source:** `= this.source` (`= this.source-type`)
