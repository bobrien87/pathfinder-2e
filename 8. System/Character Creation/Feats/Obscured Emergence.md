---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Ranger]]"]
prerequisites: "expert in Stealth"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You are, by nature, a thing of gloomy woods and barren wilds, and when you choose show yourself, a bit of this gloom clings to you, obscuring your form with strange distortions or mist. When you stop being hidden due to your own actions (not due to someone successfully finding you), you gain concealment until the start of your next turn as people's eyes find it oddly hard to focus on you. As usual for concealment involving an obvious visual manifestation, you can't use this concealment to hide.

**Source:** `= this.source` (`= this.source-type`)
