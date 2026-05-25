---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Living Vessel|Living Vessel]]"
source-type: "Remaster"
level: "16"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Polymorph]]"]
prerequisites: "Living Vessel Dedication"
frequency: "once per day"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You symbiotically combine your form with that of the entity within you, taking a powerful hybrid form to temporarily boost your abilities in combat while maintaining control. For 1 minute, you gain the following effects.

- If you were Medium or smaller, you become Large, and your reach increases to 10 feet.
- You gain a +2 status bonus to attack and damage rolls and a +1 status bonus on saving throws against spells. If you use [[Entity's Resurgence]], the status bonuses to attack and damage rolls increase to +3 during the time that the two effects overlap.
- If you have the [[Entity's Strike]] feat, the unarmed attack you gained from that feat increases its damage die from 1d6 to 1d8.
- You gain 40 temporary Hit Points.
- You gain a fly Speed equal to your Speed.

**Special** This action has the tradition trait appropriate to your entity, typically divine for a demon, occult for an aberration or outer entity, or primal for a fey.

**Source:** `= this.source` (`= this.source-type`)
