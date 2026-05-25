---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Necrologist|Necrologist]]"
source-type: "Remaster"
level: "6"
traits: ["[[Archetype]]", "[[Dedication]]"]
prerequisites: "ability to cast spells from spell slots, ability to cast summon undead"
source: "Pathfinder Battlecry!"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Your studies of the lists of the dead allow you to call forth a horde of undead with a brief incantation. You can summon your horde with the [[Raise the Horde]] activity, and you can use the [[Mobbing Assault]] action while your horde is raised to command it to attack. The eerie connection you have with your horde precludes you from also having an animal companion or any other companion (such as a follower; page 76), though if an ability allows you to have more than one follower (such as with the Additional Follower feat of the captain archetype), you can count your horde as one. You have enough control over your horde that it doesn't attack you or your allies.

When raised, your horde is Huge and has a speed of 20 feet. It has the mindless and undead traits. It can be attacked. Though it's made of several undead creatures, it can't share the same space as other creatures (unless you have certain feats). Due to your eldritch connection with your horde, it uses your AC, saves, and other defensive statistics like skill DCs, but is immune to the [[Grabbed]], [[Prone]], and [[Restrained]] conditions. The horde has resistance equal to your level to physical damage, but weakness equal to your level to area and splash damage. You share an animating force, so any damage that would be dealt to the horde is dealt to you instead, though you take damage only once from any ability that includes both you and the horde in the area of effect (though you take the greater amount of damage).

Necrologist

**Source:** `= this.source` (`= this.source-type`)
