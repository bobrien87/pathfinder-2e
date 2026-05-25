---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beast Lord|Beast Lord]]"
source-type: "Remaster"
level: "20"
traits: ["[[Mythic]]"]
prerequisites: "Beast Lord Dedication"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

The minds of you and your companion are so intertwined that, so long as one of you lives, the other continues to exist in the living one's mind. If your united companion ever dies or is destroyed and it is within 30 feet of you, its consciousness is drawn into your mind, where it can communicate with you normally and remains there until your next daily preparations. During your next daily preparations, you can call upon your union to restore your companion to life again in a ritual that takes 1 hour. Your restored united companion returns whole-bodied, at their maximum Hit Point total, and cured of any afflictions that may have been afflicting it when it died.

If you would ever die or be destroyed and you are within 30 feet of your united companion, you consciousness flows into your companion for 3 days. During this time, you can perform actions as if you are your united companion using its abilities and characteristics for any actions you perform. After spending 3 days in this state, you are returned to life with a number of Hit Points equal to @Damage[(2*@actor.level)[healing]]{twice your level} and regain a Mythic Point.

If you or your united companion die while sharing your body with the other's consciousness, you truly die, but if you are not returned to life within 1 year, you are both reincarnated as children (or in a similarly immature state) in a location near where you first became companions. Neither you nor your companion complete your journeys along the River of Souls, nor do you possess any knowledge of the other's reincarnated form. However, you both feel an inkling of your former connection, should you ever meet. If either of you are killed before you are together again as companions, the cycle of reincarnation is broken, and you can both die as normal.

**Source:** `= this.source` (`= this.source-type`)
