---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Splinter Of Finality|Splinter Of Finality]]"
source-type: "Remaster"
level: "20"
traits: ["[[Archetype]]", "[[Concentrate]]", "[[Occult]]", "[[Unholy]]"]
prerequisites: "Spectral Dagger"
source: "Pathfinder Lost Omens Shining Kingdoms"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

**Trigger** You reduce a creature to 0 Hit Points with an attack from your spectral dagger.

**Requirements** Your splinter of finality doesn't contain a trapped soul.

Your mortal strike wrenches the soul from your victim's body and imprisons it in your splinter of finality, with the effects of seize soul. The splinter of finality can only hold one soul at a time, but you can release a trapped soul as a free action. If you don't free a soul willingly, it escapes automatically after 24 hours. However, if you touch the splinter of finality to an unbroken final blade while a soul is trapped within, the soul is transferred to the final blade and imprisoned indefinitely.

While your splinter of finality contains a trapped soul, you gain fast healing 15.

> [!danger] Effect: Soul Oubliette

**Source:** `= this.source` (`= this.source-type`)
