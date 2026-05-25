---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Bloodrager|Bloodrager]]"
source-type: "Remaster"
level: "8"
traits: ["[[Archetype]]"]
prerequisites: "Rising Blood Magic"
frequency: "once per PT1H"
source: "Pathfinder War of Immortals"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Requirements** Your last action was to Harvest Blood.

**Frequency** once per hour

You temporarily add a 3rd-rank spell to your spell repertoire, as determined by the type of creature whose blood you just drank (see table below). If the creature has more than one of the listed traits, choose one and gain the appropriate spell. If the granted spell is not on your chosen tradition's list, you cast the spell as though it was from your chosen tradition. The spell is removed from your spell repertoire after 24 hours, the next time you use Spelldrinker, or when you next make your daily preparations, whichever comes first.

TraitSpellNotesAberration[[Vampiric Feast]]Animal, beast[[Summon Animal]]Summoned creatures appear as otherworldly versions of the creature whose blood you drank.Celestial[[Holy Light]]Dragon[[Blazing Bolt]]Instead of fire damage, this spell deals the same damage as the dragon breath of the dragon whose blood you drank (if applicable).Fey[[Wall of Thorns]]Fiend[[Chilling Darkness]]Giant[[Pummeling Rubble]]Humanoid[[Crisis of Faith]]Monitor[[Impending Doom]]**Special** If you have [[Surging Blood Magic]], you can add the spell at 4th rank. If you have [[Exultant Blood Magic]], you can add the spell at 7th rank.

**Source:** `= this.source` (`= this.source-type`)
