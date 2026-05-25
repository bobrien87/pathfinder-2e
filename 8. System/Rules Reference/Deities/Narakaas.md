---
type: deity
source-type: "Remaster"
domains: "Change, Death, Pain, Sorrow"
favored-weapon: "Greataxe"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Endure]], Rank 2: [[Slough Skin]], Rank 4: [[Rewrite Memory]]"
source: "Pathfinder Lost Omens Divine Mysteries Web Supplement"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

**Title** The Cleansing Sentence

**Areas of Concern** Atonement, difficult choices, pain

**Edicts** Help others through painful changes, offer harsh punishments to the penitent, seek and allow redemption

**Anathema** Torture an unwilling creature, take joy in suffering

**Religious Symbol** vertical line intersected by two diagonal lines and capped with a circle

**Sacred Animal** caecilian

**Sacred Colors** silver, white

**Source:** `= this.source` (`= this.source-type`)
