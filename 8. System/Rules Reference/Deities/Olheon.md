---
type: deity
source-type: "Remaster"
domains: "Confidence, Duty, Protection, Truth"
favored-weapon: "Halberd"
divine-font: "Heal"
divine-skill: "Diplomacy"
divine-spells: "Rank 1: [[Draw Ire]], Rank 4: [[Suggestion]], Rank 5: [[Glimmer Of Charm]]"
source: "Pathfinder Lost Omens Divine Mysteries"
---
### `= this.file.name`
`= choice(this.alignment != null and this.alignment != "", "**Alignment** " + this.alignment, "") + choice(this.sanctification != null and this.sanctification != "", choice(this.alignment != null and this.alignment != "", "; ", "") + "**Sanctification** " + this.sanctification, "")`
**Portfolio** `= this.portfolio`
**Domains** `= this.domains` | **Favored Weapon** `= this.favored-weapon`
`= choice(this.divine-font != null and this.divine-font != "", "**Divine Font** " + this.divine-font, "") + choice(this.divine-skill != null and this.divine-skill != "", choice(this.divine-font != null and this.divine-font != "", "; ", "") + "**Divine Skill** " + this.divine-skill, "")`
`= choice(this.divine-spells != null and this.divine-spells != "", "**Divine Spells** " + this.divine-spells, "")`

Whether it be the rule of a king or queen over their nation, or that of parents with their children, Olheon judges all who hold positions of power over others. The Just Arbiter is said to observe all legitimate power relationships as her purview, showing favor to those who commit their responsibilities with righteousness. To those seeking her aid who are deserved of such, she works subtly, teaching through subjects who have enjoyed her favor in the past and her divine servitors. Tyrants and others who misuse their legitimate authority to oppress or disenfranchise those under their auspices cause her to boil. Woe be to the one whose actions cause her to descend from Heaven, herself to address the issue.

**Title** The Just Arbiter

**Areas of Concern** Deservedness, nobility, rulership

**Edicts** Rule with honor, guard the weak and oppressed, obey righteous laws

**Anathema** Oppress others, fail to challenge tyrants or unjust laws, break a sworn promise

**Religious Symbol** figure framed by branches

**Sacred Animal** wolf

**Sacred Colors** blue, gold

**Source:** `= this.source` (`= this.source-type`)
