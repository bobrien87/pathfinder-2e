---
type: deity
source-type: "Remaster"
domains: "Duty, Fate, Knowledge, Vigil"
favored-weapon: "War-flail"
divine-font: "Harm, Heal"
divine-skill: "Occultism"
divine-spells: "Rank 1: [[Share Lore]], Rank 3: [[Hypercognition]], Rank 6: [[Chromatic Image]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

When souls are judged in Pharasma's court, the psychopomp usher Vale serves as the Boneyard's chief prosecutor. They judge mortals on their actions and the impact their actions have on the world, disregarding their thoughts, beliefs, and even intentions. To Vale, a mortal only proves themselves good or evil through deeds enacted and choices made; there is no kernel of innate purity or corruption within a mortal soul, and no change wrought upon the multiverse from the privacy of the heart or mind.

**Title** The Court of Ancestors

**Areas of Concern** Consequences, superstition, tradition

**Edicts** Learn and share and stories of the dead, chronicle languages and cultural traditions, protect knowledge

**Anathema** Allow intent to sway your judgment of an action, disrespect the traditions of those around you

**Religious Symbol** three circles bisected by a horizontal line

**Sacred Animal** butterfly

**Sacred Colors** gold, silver

**Source:** `= this.source` (`= this.source-type`)
