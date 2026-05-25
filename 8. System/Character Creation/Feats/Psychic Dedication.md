---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Psychic|Psychic]]"
source-type: "Remaster"
level: "2"
traits: ["[[Archetype]]", "[[Dedication]]", "[[Multiclass]]"]
prerequisites: "Intelligence +2 or Charisma +2"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

You feel something awaken within your mind. You become trained in Occultism; if you were already trained in Occultism, you become trained in a skill of your choice.

You cast spells like a psychic and gain the Cast a Spell activity; as you don't have a subconscious mind class feature, your thoughtforms are simple intentions. Choose a conscious mind. You gain a spell repertoire with one standard psi cantrip of your choice from your conscious mind, which you cast as a psi cantrip.

You gain the normal benefits for this psi cantrip, but not any other benefits from the conscious mind. You're trained in the spell attack modifier and spell DC statistics. Your key spellcasting attribute for psychic archetype spells is the attribute you used to qualify for the archetype, and they are occult psychic spells.

Psychic

**Source:** `= this.source` (`= this.source-type`)
