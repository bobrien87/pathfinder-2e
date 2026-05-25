---
type: feat
source-type: "Remaster"
level: "12"
traits: ["[[Auditory]]", "[[Concentrate]]", "[[Exemplar]]"]
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You entice or threaten a weapon, making it swear not to harm you. Attempt a Diplomacy check to [[Request]] or an Intimidation check to [[Demoralize]] against one weapon within 60 feet—even though most weapons are inanimate and mindless, your words somehow still can affect it as if it were living and you shared a language. The DC for this check is the Will DC of the creature wielding the weapon or a moderate DC for the weapon's level if it's unattended. If the weapon is an intelligent item, use its Will DC. Regardless of the result of the save, the weapon is then temporarily immune to Extract Vow of Nonviolence for 1 day.
- **Critical Success** The object swears not to hurt you. You gain resistance to all damage dealt by that specific weapon as the weapon attempts to mitigate harm to you. The resistance is equal to half your level and lasts for 10 minutes.
- **Success** As critical success, but the remaining duration decreases by 1 minute each time the weapon hits you (even if it deals no damage).

**Special** When you gain this feat, choose cold iron, duskwood, dawnsilver, or silver. For some reason—perhaps because you underestimate this material, or because you think it a friend—you are forever unable to use Extract Vow of Nonviolence on objects composed of the chosen material.

**Source:** `= this.source` (`= this.source-type`)
