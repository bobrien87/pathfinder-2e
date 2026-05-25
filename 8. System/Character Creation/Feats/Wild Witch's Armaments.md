---
type: feat
source-type: "Remaster"
level: "6"
traits: ["[[Witch]]"]
prerequisites: "Witch's Armaments"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your patron's power continues to enhance your natural offensive capabilities. You gain additional effects for any of the unarmed Strikes you chose from Witch's Armaments. If you took that feat multiple times to gain multiple attacks, you gain the appropriate additional effects.

- **Eldritch Nails** Your nails can tear and rend with the force of a beast. If you hit the same enemy with two consecutive nails Strikes, that enemy takes additional slashing damage equal to half your level on the second Strike.
- **Iron Teeth** Like a true predator, your teeth can crunch bone. A creature that you critically hit with a jaws Strike must succeed at a [[Fortitude]] save against the higher of your class DC or spell DC or become [[Sickened]] 1.
- **Living Hair** Part of your hair hardens into sharp quills that you can eject with force. You gain a quills ranged unarmed strike that deals 1d4 piercing damage with a range of 15 feet. Your quills are in the dart group.

**Source:** `= this.source` (`= this.source-type`)
