---
type: deity
source-type: "Remaster"
domains: "Decay, Dust, Earth, Nightmares"
favored-weapon: "Spiked-gauntlet"
divine-font: "Harm"
divine-skill: "Nature"
divine-spells: "Rank 1: [[Grease]], Rank 2: [[Feast Of Ashes]], Rank 5: [[Acid Storm]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Before his mortal death, Trelmarixian had already destroyed an entire world. Born a daemonic-blooded tiefling, his hatred of those around him was an all-consuming hunger, and he never knew peace. During an eclipse, he performed a ritual so powerful it mummified every living creature on his world, and his heart was finally full. Dying from starvation but elated by his success, Trelmarixian heard a voice call out to him. The voice mocked him, exclaiming all he'd accomplished was insignificant compared to what awaited him next. Trelmarixian's last mortal memory was of staring into an eclipse.

Lyutheria, the original Horseman of Famine, was impressed by Trelmarixian's conquest and took him on as her apprentice, fatally underestimating his ambitions. After Trelmarixian learned all he could from his master, he devoured her and assumed her title.

**Title** The Lysogenic Prince

**Areas of Concern** Famine

**Edicts** End all mortal life through wasting consumption and starvation, violently consume matter and souls

**Anathema** Kill or remove a parasite or tumor, grow food

**Religious Symbol** jackal skull and eclipse

**Sacred Animal** horse, jackal

**Sacred Colors** black

**Source:** `= this.source` (`= this.source-type`)
