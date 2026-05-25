---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Scions Of Domora|Scions Of Domora]]"
source-type: "Remaster"
level: "14"
traits: ["[[Archetype]]", "[[Polymorph]]"]
prerequisites: "Scion of Domora Dedication"
frequency: "once per day"
source: "Pathfinder Adventure Path: Gatewalkers"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Frequency** once per day

You fuse with your spirit guide, becoming a hybrid being with enhanced physical and spiritual power. This effect lasts 1 minute; you can end it early as a free action. During this time, you can't use any other actions granted by this archetype.

You gain the following statistics and abilities, regardless of your type of spirit guide.

- You become incorporeal.
- You gain resistance 10 to all damage (except force, ghost touch, or spirit; double resistance vs. non-magical).
- Darkvision.
- An unarmed melee attack of the same type as your spirit guide (either claws or jaws), which is the only attack you can Strike with. You're trained with this attack. Your attack modifier is +29 or your normal unarmed attack modifier, whichever is higher. You use the listed statistics for the unarmed attack type:

- **Claws** (agile, backstabber, finesse) `pf2:1`, **Damage** 3d6+5 slashing plus 1d6 force;
- **Jaws** (forceful) `pf2:1` **Damage** 3d10+5 piercing plus 1d6 force.

**Source:** `= this.source` (`= this.source-type`)
