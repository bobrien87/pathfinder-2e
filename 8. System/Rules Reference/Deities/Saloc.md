---
type: deity
source-type: "Remaster"
domains: "Change, Death, Freedom, Knowledge"
favored-weapon: "Guisarme"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Share Lore]], Rank 3: [[Hypercognition]], Rank 5: [[Dreaming Potential]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Ruler of the planar metropolis of Spire's Edge in the Boneyard, the psychopomp usher Saloc is humanoid, but their face is devoid of features save stag horns, and two golden rings lined with eyes constantly rotate about their body. As a defense counsel in Pharasma's court, the Minder of Immortals argues that a person's intentions should be considered in equal part to the consequences of their actions when deciding their soul's afterlife. Saloc has even been known to resurrect condemned souls to give them a second chance to prove themselves. Mortals revere Saloc as the patron of agency, bronze, and education. These followers are people who seek to improve themselves or others, including both students and teachers. Some seek to earn their freedom from earthly prisons, while others wish to change their ways to avoid punishment in the hereafter.

**Title** The Minder of Immortals

**Areas of Concern** Agency, bronze, education

**Edicts** Help creatures grow and find purpose, offer second chances to failures, study different perspectives on ethics

**Anathema** Manipulate or remove a creature's emotions with magic, spread nihilism or hopelessness

**Religious Symbol** equilateral triangle set inside a circle

**Sacred Animal** silkworm

**Sacred Colors** gold, gray

**Source:** `= this.source` (`= this.source-type`)
