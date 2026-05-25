---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Beast Lord|Beast Lord]]"
source-type: "Remaster"
level: "18"
traits: ["[[Mythic]]"]
prerequisites: "Beast Lord Dedication, you have a united companion with a specialization"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your specialized united companion grows with unparalleled power and strength, becoming a creature of myth. It gains one of the following effects.

- **Baleful Body** Your united companion's blood is boiling, its mechanical fluid is acidic, or its insides are otherwise destructive to the touch. Choose acid, fire, or poison. If your united companion would take damage from a melee attack, it deals half your level in damage of the chosen type to the creature that made the melee attack. By spending a Mythic Point when you Command your united companion, your united companion can spew its corrosive power as a 2-action activity to deal 14d6 damage of the chosen type in a 15-foot cone or 30-foot line (basic Reflex save against your class DC or spell DC, whichever is higher).

- **Chimeric Heads** Your united companion sprouts an extra head which gives it extra eyes and allows it to make additional attacks with related unarmed attacks. Your united companion gains all-around vision. By spending a Mythic Point when you Command your united companion, your united companion can make two Strikes with its unarmed attacks as a single action, each using its current multiple attack penalty. Both Strikes must have the same target. If both attacks hit, combine their damage, and then add any other applicable effects. This counts as one attack when calculating your united companion's multiple attack penalty. Your united companion must have a head and at least one unarmed attack that uses its mouth or head (such as a beak, jaws, or mandible attack) to select this.

- **Energy Aegis** Your united companion is protected from hazardous energy. Your united companion becomes immune to your choice of acid, cold, electricity, or fire. Your companion gains a +1 status bonus to AC and saves that originate from creatures with the listed trait and to effects and spells with the listed trait. By spending a Mythic Point when you Command your united companion, your united companion can take a single action with the concentrate trait to extend these same benefits to all creatures who are adjacent to it until the beginning of your next turn.

- **Magnificent Flight** Your united companion grows wings or learns some other method of flight. Your united companion gains a Fly speed equal to its Speed and it gains the mount special ability. If your united companion already had the mount special ability or a Fly speed equal to its Speed, it instead increases its Speed by 10 feet. By spending a Mythic Point when you Command your united companion, your united companion can, as a two-action activity, Fly up to twice its speed and make a single unarmed melee attack at any point along the way.

- **Protective Skin** Your united companion is hardened by the infused magic of otherworldly powers. Its maximum Hit Points increase by 30 but it gains a weakness of 10 to either cold iron or silver. By spending a Mythic Point when you Command your united companion, your united companion gains fast healing equal to your level for 1 minute.

**Source:** `= this.source` (`= this.source-type`)
