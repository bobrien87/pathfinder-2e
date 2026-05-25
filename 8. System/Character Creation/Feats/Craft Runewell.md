---
type: feat
archetype: "[[8. System/Character Creation/Archetypes/Avenging Runelord|Avenging Runelord]]"
source-type: "Remaster"
level: "20"
traits: ["[[Mythic]]"]
prerequisites: "Avenging Runelord Dedication"
source: "Pathfinder #219: Lord of the Trinity Star"
---
### `= this.file.name`
**Feat** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.prerequisites != null and this.prerequisites != "", "**Prerequisites** " + this.prerequisites, "") + choice(this.access != null and this.access != "", choice(this.prerequisites != null and this.prerequisites != "", "<br>", "") + "**Access** " + this.access, "") + choice(this.frequency != null and this.frequency != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "", "<br>", "") + "**Frequency** " + this.frequency, "") + choice(this.trigger != null and this.trigger != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "", "<br>", "") + "**Trigger** " + this.trigger, "") + choice(this.requirements != null and this.requirements != "", choice(this.prerequisites != null and this.prerequisites != "" or this.access != null and this.access != "" or this.frequency != null and this.frequency != "" or this.trigger != null and this.trigger != "", "<br>", "") + "**Requirements** " + this.requirements, "")`

Even if the runelord whose soul influences you never did so themselves, you know how to create your own *runewell*—an artifact that grants you a measure of immortality. You learn the [[Create Demiplane]] ritual. To create your *runewell*, you must cast *create demiplane* heightened to 10th-rank. When you do so, you also create an anima focus (an immobile object like a statue or fortification with an appearance you design) at the location you cast the ritual, connecting your other-worldly home to this location. Once you create your *runewell*, you cannot create another unless the current one is destroyed.

While you are located on the same plane that your anima focus is located on, or while you are within your *runewell*, any doomed value you gain stops at [[Doomed]] 3. The only way an adversary can destroy your anima focus or *runewell* is to reduce you to 0 Hit Points and doomed 3 and then reduce your anima focus to 0 Hit Points using arcane magic (or an agent affected by arcane magic) from one of the schools in opposition to your specialized sin chosen when you took Avenging Runelord Dedication. Your anima focus has Hardness equal to twice your level and Hit Points equal to your own. Your anima focus has fast healing equal to twice your Intelligence modifier.

Your anima focus is associated with the same sin as your chosen avenging runelord sin. As long as at least one sizable settlement in which this sin is prevalent (subject to the GM's discretion) is within a hundred miles of it, your anima focus absorbs energy from these sins. As long as it does so and you are on the same plane as the anima focus, you do not age and are immune to effects that rob you of your mental abilities (such as the never mind spell or the [[Confused]] and stupefied conditions).

Other creatures cannot enter your *runewell* unless they possess a planar key you created and gave to them, or unless they're adjacent to your anima focus. Your *runewell* has an exit that allows adjacent creatures within to activate with an Interact action; when they do so, they exit the *runewell* and appear adjacent to your anima focus. You gain the [[Enter Runewell]] activity.

**Source:** `= this.source` (`= this.source-type`)
