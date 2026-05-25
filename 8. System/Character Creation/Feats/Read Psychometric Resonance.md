---
type: feat
source-type: "Remaster"
level: "1"
traits: ["[[Concentrate]]", "[[Emotion]]", "[[Exploration]]", "[[General]]", "[[Mental]]", "[[Occult]]", "[[Skill]]"]
prerequisites: "trained in Occultism"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

With a touch, you can read the psychic impressions left on objects by their previous owners. This exploration activity functions similarly to Detect Magic in that you move at half your travel speed or slower while looking for psychometric resonance. You must brush your bare hands over any objects you pass while you do this. This detects objects with significant emotional resonance attached to them, such as the joy from a child's beloved teddy bear, the sorrow from a widower's wedding ring, or the fear from a victim's murder weapon. If you're looking for a particular type of emotional resonance, you can choose to ignore other emotions. If you find an item with that resonance, you can explore that resonance with the [[Psychometric Assessment]] action.

**Source:** `= this.source` (`= this.source-type`)
